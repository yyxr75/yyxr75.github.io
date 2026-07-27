# Job hunt — API-first crawler + Claude ranking

Finds CV/ML research & internship roles from public job APIs, ranks them against Yanlong's
profile, and writes a daily digest. **No fragile HTML scraping / no ToS-restricted sites**
(LinkedIn, Seek, Indeed) — only public JSON boards.

## Pipeline
```
fetch.py      → pull all sources, normalize, dedup vs data/seen.json → data/raw-YYYY-MM-DD.json (new only)
shortlist.py  → keyword/seniority prefilter + prescore                → data/shortlist.json (top ~80)
[Claude]      → score shortlist vs profile.yml, write a ranked digest → digests/YYYY-MM-DD.md
```
Run the first two, then have Claude Code read `data/shortlist.json` + `profile.yml` and write the digest.

```bash
cd ~/Documents/yyl/job-hunt
python3 fetch.py && python3 shortlist.py
```

## Files
- `profile.yml`  — who you are / what you want (drives scoring). Edit as your focus shifts.
- `sources.yml`  — which APIs/boards to pull. **Grow this over time** (see below).
- `data/seen.json` — every posting id ever seen, so digests only show *new* ones.
- `digests/`     — dated ranked digests (the output you read).

## Broadening coverage
- **Adzuna** (free key, best Australian coverage): register at https://developer.adzuna.com,
  put `app_id`/`app_key` in `sources.yml`, set `enabled: true`.
- **Company boards**: find a company's ATS from its careers page URL and add the token:
  - `boards.greenhouse.io/{token}` → add to `greenhouse.tokens`
  - `jobs.lever.co/{token}`        → add to `lever.tokens`
  - `jobs.ashbyhq.com/{token}`     → add to `ashby.tokens`
  Good ones to hunt for CV/ML research: NVIDIA, Meta, Google/DeepMind, Microsoft, Apple,
  Adobe, Snap, Cohere, plus CSIRO/university boards for Australia.

## Automation (daily digest)
- **Local cron**: run `fetch.py && shortlist.py` daily, then invoke Claude to score.
- **Claude Code scheduled agent** (`/schedule`): a cloud routine that runs the fetch, scores,
  and writes the digest without a separate API key. Ask resume-maker to set it up.

## Integration
High-scoring roles feed the targeted-CV workflow in `../targeted-CVs/` — pick a job and
resume-maker drafts a tailored CV + PDF for it.
