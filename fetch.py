#!/usr/bin/env python3
"""Fetch jobs from API/feed sources, normalize, dedup, and record only new postings.

Usage:  python3 fetch.py
Output: data/raw-YYYY-MM-DD.json  (new jobs this run)  +  updates data/seen.json
No scraping of ToS-restricted sites; only public JSON APIs / boards.
"""
import json, os, sys, time, hashlib, datetime, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
UA = "Mozilla/5.0 (job-hunt personal aggregator; contact: yanlong.yang@my.jcu.edu.au)"


def load_yaml(path):
    import yaml
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def get_json(url, timeout=25):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8", "replace"))


def norm(source, company, title, location, url, posted="", desc=""):
    return {"source": source, "company": company, "title": (title or "").strip(),
            "location": (location or "").strip(), "url": url,
            "posted": posted or "", "desc": (desc or "").strip()[:1200]}


# ---------- source fetchers (each returns a list of normalized records) ----------
def fetch_amazon(cfg):
    out = []
    for q in cfg.get("queries", []):
        params = {"base_query": q, "loc_query": cfg.get("location", ""),
                  "result_limit": cfg.get("result_limit", 100), "sort": "recent"}
        url = "https://www.amazon.jobs/en/search.json?" + urllib.parse.urlencode(params)
        try:
            data = get_json(url)
        except Exception as e:
            print(f"  [amazon] '{q}' failed: {e}", file=sys.stderr); continue
        for j in data.get("jobs", []):
            out.append(norm("amazon.jobs", "Amazon", j.get("title"),
                            j.get("location") or j.get("city"),
                            "https://www.amazon.jobs" + (j.get("job_path") or ""),
                            j.get("posted_date", ""),
                            (j.get("description_short") or j.get("description") or "")))
        time.sleep(1)
    return out


def fetch_greenhouse(tokens):
    out = []
    for t in tokens or []:
        url = f"https://boards-api.greenhouse.io/v1/boards/{t}/jobs?content=true"
        try:
            data = get_json(url)
        except Exception as e:
            print(f"  [greenhouse] {t} failed: {e}", file=sys.stderr); continue
        for j in data.get("jobs", []):
            loc = (j.get("location") or {}).get("name", "")
            out.append(norm("greenhouse", t, j.get("title"), loc,
                            j.get("absolute_url", ""), j.get("updated_at", ""),
                            (j.get("content") or "")))
        time.sleep(0.6)
    return out


def fetch_lever(tokens):
    out = []
    for t in tokens or []:
        url = f"https://api.lever.co/v0/postings/{t}?mode=json"
        try:
            data = get_json(url)
        except Exception as e:
            print(f"  [lever] {t} failed: {e}", file=sys.stderr); continue
        for j in data:
            cat = j.get("categories", {}) or {}
            out.append(norm("lever", t, j.get("text"), cat.get("location", ""),
                            j.get("hostedUrl", ""), "", (j.get("descriptionPlain") or "")))
        time.sleep(0.6)
    return out


def fetch_ashby(tokens):
    out = []
    for t in tokens or []:
        url = f"https://api.ashbyhq.com/posting-api/job-board/{t}?includeCompensation=false"
        try:
            data = get_json(url)
        except Exception as e:
            print(f"  [ashby] {t} failed: {e}", file=sys.stderr); continue
        for j in data.get("jobs", []):
            out.append(norm("ashby", t, j.get("title"), j.get("location", ""),
                            j.get("jobUrl", ""), j.get("publishedAt", ""),
                            (j.get("descriptionPlain") or "")))
        time.sleep(0.6)
    return out


def fetch_adzuna(cfg):
    out = []
    if not cfg.get("enabled") or not cfg.get("app_id") or not cfg.get("app_key"):
        return out
    country = cfg.get("country", "au")
    for q in cfg.get("queries", []):
        params = {"app_id": cfg["app_id"], "app_key": cfg["app_key"],
                  "results_per_page": 50, "what": q, "content-type": "application/json"}
        url = f"https://api.adzuna.com/v1/api/jobs/{country}/search/1?" + urllib.parse.urlencode(params)
        try:
            data = get_json(url)
        except Exception as e:
            print(f"  [adzuna] '{q}' failed: {e}", file=sys.stderr); continue
        for j in data.get("results", []):
            out.append(norm("adzuna", (j.get("company") or {}).get("display_name", ""),
                            j.get("title"), (j.get("location") or {}).get("display_name", ""),
                            j.get("redirect_url", ""), j.get("created", ""), (j.get("description") or "")))
        time.sleep(1)
    return out


def main():
    src = load_yaml(os.path.join(HERE, "sources.yml"))
    records = []
    if src.get("amazon_jobs", {}).get("enabled"):
        print("fetching amazon.jobs ...", file=sys.stderr)
        records += fetch_amazon(src["amazon_jobs"])
    print("fetching greenhouse ...", file=sys.stderr)
    records += fetch_greenhouse(src.get("greenhouse", {}).get("tokens"))
    print("fetching lever ...", file=sys.stderr)
    records += fetch_lever(src.get("lever", {}).get("tokens"))
    print("fetching ashby ...", file=sys.stderr)
    records += fetch_ashby(src.get("ashby", {}).get("tokens"))
    print("fetching adzuna ...", file=sys.stderr)
    records += fetch_adzuna(src.get("adzuna", {}))

    # dedup within this run by URL (fall back to company+title)
    uniq = {}
    for r in records:
        key = r["url"] or (r["company"] + "|" + r["title"])
        uniq.setdefault(key, r)
    records = list(uniq.values())

    # compare against seen.json -> keep only NEW
    seen_path = os.path.join(HERE, "data", "seen.json")
    seen = set()
    if os.path.exists(seen_path):
        seen = set(json.load(open(seen_path)))

    def kid(r):
        return hashlib.sha1((r["url"] or r["company"] + r["title"]).encode()).hexdigest()[:16]

    new = [r for r in records if kid(r) not in seen]
    for r in new:
        r["id"] = kid(r)

    today = datetime.date.today().isoformat()  # crawler runs live, real date is fine here
    raw_path = os.path.join(HERE, "data", f"raw-{today}.json")
    json.dump(new, open(raw_path, "w"), ensure_ascii=False, indent=2)
    seen |= {kid(r) for r in records}
    json.dump(sorted(seen), open(seen_path, "w"))

    print(f"\nfetched {len(records)} unique postings, {len(new)} new -> {raw_path}")


if __name__ == "__main__":
    main()
