#!/usr/bin/env python3
"""Prefilter + prescore the latest raw fetch into a focused shortlist for LLM scoring.

Cuts hundreds of raw postings down to the CV/ML-relevant, right-seniority ones so the
expensive Claude-scoring step only sees good candidates.
Usage: python3 shortlist.py   ->   data/shortlist.json
"""
import json, glob, os, yaml
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
prof = yaml.safe_load(open(os.path.join(HERE, "profile.yml"), encoding="utf-8"))
raw = sorted(glob.glob(os.path.join(HERE, "data", "raw-*.json")))[-1]
jobs = json.load(open(raw, encoding="utf-8"))

strong = [k.lower() for k in prof["keywords_strong"]]
nice = [k.lower() for k in prof.get("keywords_nice", [])]
role_signals = ["applied scientist", "research scientist", "research engineer",
                "computer vision", "machine learning", "deep learning", "phd",
                "intern", "postdoc", "research assistant", "perception", "vision",
                "ml scientist", "generative", "diffusion"]
excl = [e.lower() for e in prof.get("exclude_titles", [])] + [
    "software development engineer", "sde", " tpm", "program manager", "product manager",
    "data operations", "business", "account", "sales", "marketing", "recruit",
    "warehouse", "operations manager", "support engineer", "solutions architect",
    "business intelligence", "bie", "finance", "hr ", "legal"]


def prescore(j):
    t = j["title"].lower(); blob = (j["title"] + " " + j["desc"]).lower()
    if any(x in t for x in excl):
        return None
    if not any(s in blob for s in role_signals):
        return None
    s = 3 * sum(k in blob for k in strong) + sum(k in blob for k in nice)
    if "intern" in t or "phd" in blob:
        s += 4
    if "applied scientist" in t or "research scientist" in t or "research intern" in t:
        s += 4
    if "computer vision" in blob or "generative" in blob or "diffusion" in blob:
        s += 3
    loc = j["location"].lower()
    if any(x in loc for x in ["australia", "melbourne", "sydney", "brisbane", "canberra", "perth"]):
        s += 4
    if "remote" in loc:
        s += 1
    return s


cand = []
for j in jobs:
    s = prescore(j)
    if s and s > 0:
        j["prescore"] = s
        cand.append(j)
cand.sort(key=lambda x: -x["prescore"])
cand = cand[:80]

out = os.path.join(HERE, "data", "shortlist.json")
json.dump(cand, open(out, "w"), ensure_ascii=False, indent=2)
print(f"{len(jobs)} raw -> {len(cand)} shortlisted -> {out}")
print("by source:", dict(Counter(c["source"] for c in cand)))
au = [c for c in cand if any(x in c["location"].lower() for x in ["australia", "melbourne", "sydney", "brisbane"])]
print(f"Australia-based in shortlist: {len(au)}")
for c in cand[:30]:
    print(f"  {c['prescore']:>2} [{c['source'][:9]:9}] {c['title'][:52]:52} | {c['location'][:26]}")
