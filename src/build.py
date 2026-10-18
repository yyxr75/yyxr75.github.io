"""Static site generator for yyxr75.github.io.

    python3 src/build.py

Reads src/content.py, src/figures/*.svg, src/style.css, src/site.js and writes
the HTML pages into the repo root (served as-is by GitHub Pages; .nojekyll).
"""
import os
import shutil

import content as C

SRC = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(SRC)
SITE = "https://yyxr75.github.io"

NAV = [("Research", "/research/"), ("Projects", "/projects/"), ("About", "/about/"), ("CV", "/cv/")]
CAT = {"research": "Research", "industry": "Industry", "public": "Public"}


def fig(name, cls=""):
    svg = open(os.path.join(SRC, "figures", name + ".svg")).read().strip()
    return svg.replace('class="fig"', f'class="fig {cls}"'.strip(), 1)


def webp_size(path):
    # width/height from the WebP header, so <img> reserves its box without Pillow
    b = open(path, "rb").read(30)
    if b[12:16] == b"VP8X":
        return 1 + int.from_bytes(b[24:27], "little"), 1 + int.from_bytes(b[27:30], "little")
    if b[12:16] == b"VP8L":
        v = int.from_bytes(b[21:25], "little")
        return (v & 0x3FFF) + 1, ((v >> 14) & 0x3FFF) + 1
    return int.from_bytes(b[26:28], "little") & 0x3FFF, int.from_bytes(b[28:30], "little") & 0x3FFF


def shot(slug, n, cap, src, cls="", eager=False):
    url = f"/images/projects/{slug}/{n}.webp"
    w, h = webp_size(os.path.join(OUT, url.lstrip("/")))
    classes = " ".join(c for c in ("shot", "wide" if w / h > 2.2 else "", cls) if c)
    load = "" if eager else ' loading="lazy"'
    return (f'<figure class="{classes}"><a href="{url}" aria-label="Open full-size image">'
            f'<img src="{url}" width="{w}" height="{h}" alt="{cap}"{load} decoding="async"></a>'
            f'<figcaption>{cap} <span class="mono src">{src}</span></figcaption></figure>')


def authors(p):
    out = []
    for i, a in enumerate(p["authors"]):
        out.append(f"<strong>{a}</strong>" if i == p["me"] else a)
    return ", ".join(out)


def links(items, cls="lk"):
    if not items:
        return ""
    return '<span class="links">' + "".join(
        f'<a class="{cls}" href="{u}"{"" if u.startswith("/") else " rel=noopener"}>{t}</a>' for t, u in items) + "</span>"


def page(path, title, desc, body, active=""):
    nav = "".join(
        f'<a href="{u}"{" aria-current=page" if u == active else ""}>{t}</a>' for t, u in NAV)
    full_title = C.NAME if title == C.NAME else f"{title} · {C.NAME}"
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}/{path}">
<meta property="og:title" content="{full_title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<link rel="icon" href="/images/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/images/favicon-32x32.png" sizes="32x32">
<link rel="apple-touch-icon" href="/images/apple-touch-icon-180x180.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css">
<script>try{{var t=localStorage.getItem("theme");if(t)document.documentElement.dataset.theme=t}}catch(e){{}}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="top">
  <div class="wrap top-in">
    <a class="brand" href="/"><span class="mark" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M2 12c2.5-6 5-6 7.5 0s5 6 7.5 0 3.5-4 5-3"/></svg></span>Yanlong Yang</a>
    <nav class="nav" aria-label="Main">{nav}<a class="mail" href="mailto:{C.EMAIL}">Email</a></nav>
    <button class="theme" type="button" aria-label="Toggle dark mode"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M21 13A9 9 0 1 1 11 3a7 7 0 0 0 10 10z"/></svg></button>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="foot">
  <div class="wrap foot-in">
    <span>© 2026 Yanlong Yang · Cairns, Australia</span>
    <span class="foot-l"><a href="mailto:{C.EMAIL}">Email</a><a href="{C.SCHOLAR}" rel="noopener">Google Scholar</a><a href="{C.GITHUB}" rel="noopener">GitHub</a><a href="{C.ORCID}" rel="noopener">ORCID</a></span>
  </div>
</footer>
<script src="/assets/site.js" defer></script>
</body>
</html>
"""
    dest = os.path.join(OUT, path, "index.html") if path.endswith("/") or path == "" else os.path.join(OUT, path)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    open(dest, "w").write(html)


def pub_row(p, with_fig=False):
    kind = {"conference": "Conference", "journal": "Journal", "preprint": "Preprint"}[p["kind"]]
    detail = f' <span class="dim">· {p["detail"]}</span>' if p.get("detail") else ""
    figure = f'<div class="pub-fig">{fig(p["fig"])}</div>' if with_fig else ""
    star = '<span class="star" title="First or co-first author">★</span>' if p.get("star") else ""
    return f"""<article class="pub{' pub-feat' if with_fig else ''}" id="{p['id']}" data-kind="{p['kind']}">
  <div class="pub-meta"><span class="yr">{p['year']}</span><span class="tag tag-{p['kind']}">{kind}</span></div>
  {figure}
  <div class="pub-body">
    <h3>{star}{p['title']}</h3>
    <p class="au">{authors(p)}</p>
    <p class="ven"><em>{p['venue']}</em>{detail}</p>
    <p class="blurb">{p['blurb']}</p>
    {links(p['links'])}
  </div>
</article>"""


def proj_card(pr, big=False):
    return f"""<a class="card{' card-big' if big else ''}" href="/projects/{pr['slug']}/" data-cat="{pr['cat']}">
  <div class="card-fig">{fig(pr['fig'])}</div>
  <div class="card-body">
    <p class="card-meta"><span class="tag tag-{pr['cat']}">{CAT[pr['cat']]}</span><span class="mono">{pr['period']}</span></p>
    <h3>{pr['title']}</h3>
    <p>{pr['short']}</p>
  </div>
</a>"""


def section_head(title, link=None, kicker=None):
    k = f'<p class="kicker">{kicker}</p>' if kicker else ""
    l = f'<a class="more" href="{link[1]}">{link[0]} →</a>' if link else ""
    return f'<div class="sec-h">{k}<h2>{title}</h2>{l}</div>'


# ------------------------------------------------------------------ pages
def home():
    stats = "".join(f'<div class="stat"><b>{a}</b><span>{b}</span></div>' for a, b in C.STATS)
    feat_pubs = "".join(pub_row(p, with_fig=True) for p in C.PUBS if p["id"] in ("deblursdi", "radarinv", "ralibev"))
    news = "".join(f'<li><span class="mono">{d}</span><span>{t}</span></li>' for d, t in C.NEWS)
    feat = [p for p in C.PROJECTS if p.get("feat")]
    title = {"ralibev": "RaLiBEV", "data-closed-loop": "Data closed-loop", "world-models": "World models",
             "deblursdi": "DeblurSDI", "radarinv": "RadarINV", "self-diffusion": "Self-Diffusion",
             "crocodile-detection": "Crocodile detection", "ausimmitool": "ausimmitool.com",
             "mimo-radar": "MIMO radar chain", "thermal-reconstruction": "3D thermal body", "smart-car": "Smart car"}
    pillars = "".join(
        f'<div class="pillar"><h3>{t}</h3><p>{d}</p><ul class="skl">{"".join(f"<li>{k}</li>" for k in sk)}</ul>'
        f'<p class="pl-links">{" · ".join(f'<a href="/projects/{s}/">{title[s]}</a>' for s in ps)}</p></div>'
        for t, d, sk, ps in C.PILLARS)
    cards = "".join(proj_card(p) for p in feat)
    body = f"""
<section class="hero">
  <div class="wrap hero-in">
    <div class="hero-txt">
      <p class="kicker">PhD candidate · James Cook University</p>
      <h1>From sensors to <span class="acc">deployed AI.</span></h1>
      <p class="lede">{C.TAGLINE}</p>
      <p class="hero-meta mono">Cairns, Australia · Advisor Dr Tao Huang · Expected Oct 2027</p>
      <div class="cta"><a class="btn btn-p" href="/research/">View research</a><a class="btn" href="{C.CV_PDF}">Download CV</a><button class="btn btn-g copy" type="button" data-copy="{C.EMAIL}">Copy email</button></div>
    </div>
    <div class="hero-fig">{fig("hero", "hero-svg")}<p class="cap">Four sides of my work: perception for autonomous driving, generative models, applied AI systems, and the signals and hardware underneath.</p></div>
  </div>
  <div class="wrap"><div class="stats">{stats}</div></div>
</section>

<section class="wrap blk">
  {section_head("What I do", None, "Experience &amp; skills")}
  <div class="pillars">{pillars}</div>
</section>

<section class="wrap blk">
  {section_head("Selected research", ("All publications", "/research/"), "Papers")}
  <div class="pubs">{feat_pubs}</div>
</section>

<section class="wrap blk two">
  <div>
    {section_head("News", None, "Recent")}
    <ul class="news">{news}</ul>
  </div>
  <div class="about-mini">
    {section_head("About", ("More about me", "/about/"), "Bio")}
    <img class="avatar" src="/images/profile.jpg" alt="Portrait of Yanlong Yang" width="96" height="96">
    <p>{C.BIO[1]}</p>
  </div>
</section>

<section class="wrap blk">
  {section_head("Selected projects", ("All 11 projects", "/projects/"), "Projects")}
  <div class="grid">{cards}</div>
</section>
"""
    page("", C.NAME, "Yanlong Yang — PhD candidate at James Cook University: deep learning for autonomous-driving perception, generative models for inverse problems, and applied AI systems.", body)


def research():
    chips = '<div class="chips" role="group" aria-label="Filter publications"><button class="chip on" data-f="all" aria-pressed="true">All</button><button class="chip" data-f="conference" aria-pressed="false">Conference</button><button class="chip" data-f="journal" aria-pressed="false">Journal</button><button class="chip" data-f="preprint" aria-pressed="false">Preprint</button></div>'
    rows = "".join(pub_row(p) for p in C.PUBS)
    pats = "".join(
        f'<li><span class="yr">{y}</span><div><h3>{t}</h3><p class="au">{", ".join("<strong>%s</strong>" % a if a == "Y. Yang" else a for a in inv)}</p><p class="ven mono">{n} · granted</p></div></li>'
        for t, n, y, inv in C.PATENTS)
    interests = "".join(f"<li>{i}</li>" for i in C.INTERESTS)
    body = f"""
<section class="wrap page-h">
  <p class="kicker">Research</p>
  <h1>Publications &amp; patents</h1>
  <p class="lede">Papers on autonomous-driving perception, generative models for inverse problems and multi-sensor sensing, plus patents from four years in industry. ★ marks first or co-first authorship; full list on <a href="{C.SCHOLAR}" rel="noopener">Google Scholar</a>.</p>
  <ul class="themes">{interests}</ul>
</section>
<section class="wrap blk">
  <div class="sec-h"><h2>Publications</h2>{chips}</div>
  <div class="pubs list" data-list>{rows}</div>
</section>
<section class="wrap blk" id="patents">
  <div class="sec-h"><h2>Patents</h2><span class="count mono">9 granted · first inventor on 4</span></div>
  <p class="note">{C.PATENTS_NOTE}</p>
  <ol class="patents">{pats}</ol>
</section>
"""
    page("research/", "Research", "Publications and granted patents of Yanlong Yang: CVPR 2026, IEEE TCSVT, radar point-cloud enhancement, and nine Chinese invention patents.", body, "/research/")


def projects():
    chips = '<div class="chips" role="group" aria-label="Filter projects"><button class="chip on" data-f="all" aria-pressed="true">All</button><button class="chip" data-f="research" aria-pressed="false">Research</button><button class="chip" data-f="industry" aria-pressed="false">Industry</button><button class="chip" data-f="public" aria-pressed="false">Public</button></div>'
    cards = "".join(proj_card(p) for p in C.PROJECTS)
    body = f"""
<section class="wrap page-h">
  <p class="kicker">Projects</p>
  <h1>Things I have built</h1>
  <p class="lede">From a smart-car circuit board to a CVPR paper: eleven projects across research, industry and public tools, newest first.</p>
</section>
<section class="wrap blk">
  <div class="sec-h"><h2>All projects</h2>{chips}</div>
  <div class="grid" data-list>{cards}</div>
</section>
"""
    page("projects/", "Projects", "Eleven projects by Yanlong Yang across generative models, radar and LiDAR perception, industry systems and public data tools.", body, "/projects/")
    for i, pr in enumerate(C.PROJECTS):
        prev = C.PROJECTS[i - 1] if i > 0 else None
        nxt = C.PROJECTS[i + 1] if i + 1 < len(C.PROJECTS) else None
        paras = "".join(f"<p>{t}</p>" for t in pr["body"])
        pts = "".join(f"<li>{t}</li>" for t in pr["points"])
        pub = next((p for p in C.PUBS if p["id"] == pr.get("pub")), None)
        pubhtml = f'<h2 class="h3">Publication</h2><div class="pubs">{pub_row(pub)}</div>' if pub else ""
        lk = f'<div class="proj-links">{links(pr["links"], "btn")}</div>' if pr["links"] else ""
        pager = '<nav class="pager" aria-label="More projects">'
        pager += f'<a href="/projects/{prev["slug"]}/"><span class="mono">← Newer</span>{prev["title"]}</a>' if prev else "<span></span>"
        pager += f'<a class="r" href="/projects/{nxt["slug"]}/"><span class="mono">Older →</span>{nxt["title"]}</a>' if nxt else "<span></span>"
        pager += "</nav>"
        shots = pr.get("shots", [])
        if shots:
            # real project images: lead image up top, the sketch becomes a small schematic beside the text
            lead = shot(pr["slug"], *shots[0], cls="lead", eager=True)
            side = f'<figure class="proj-fig sm">{fig(pr["fig"])}<figcaption class="mono">Schematic</figcaption></figure>'
            more = "".join(shot(pr["slug"], *s) for s in shots[1:])
            gallery = f'<h2 class="h3">From the project</h2><div class="gallery">{more}</div>' if more else ""
        else:
            lead, gallery = "", ""
            side = f'<figure class="proj-fig">{fig(pr["fig"])}</figure>'
        body = f"""
<article class="wrap proj">
  <a class="back mono" href="/projects/">← All projects</a>
  <header class="proj-h">
    <p class="card-meta"><span class="tag tag-{pr['cat']}">{CAT[pr['cat']]}</span><span class="mono">{pr['period']}</span></p>
    <h1>{pr['title']}</h1>
    <p class="lede">{pr['sub']}</p>
  </header>
  {lead}
  <div class="proj-grid{' has-shots' if shots else ''}">
    {side}
    <div class="proj-txt">
      {paras}
      <h2 class="h3">Highlights</h2>
      <ul class="ticks">{pts}</ul>
      {lk}
    </div>
  </div>
  {gallery}
  {pubhtml}
  {pager}
</article>
"""
        plain = pr["short"].replace("&amp;", "&")
        page(f"projects/{pr['slug']}/", pr["title"].replace("&amp;", "&"), plain, body, "/projects/")


def about():
    def tl(items):
        return "".join(
            f'<li><span class="mono when">{w}</span><div><h3>{a}</h3><p class="dim">{b}</p>{f"<p>{d}</p>" if d else ""}</div></li>'
            for a, b, w, d in items)
    edu = tl(C.EDUCATION)
    exp = tl(C.EXPERIENCE)
    hon = tl([(a, b, w, "") for a, b, w in C.HONOURS])
    srv = tl([(a, b, w, "") for a, b, w in C.SERVICE])
    bio = "".join(f"<p>{t}</p>" for t in C.BIO)
    skills = "".join(f"<dt>{a}</dt><dd>{b}</dd>" for a, b in C.SKILLS)
    body = f"""
<section class="wrap page-h about-h">
  <img class="avatar lg" src="/images/profile.jpg" alt="Portrait of Yanlong Yang" width="140" height="140">
  <div>
    <p class="kicker">About</p>
    <h1>Yanlong Yang</h1>
    <p class="lede">PhD candidate · James Cook University · Cairns, Australia</p>
    <p class="hero-links">{links([("Email", "mailto:" + C.EMAIL), ("Google Scholar", C.SCHOLAR), ("GitHub", C.GITHUB), ("ORCID", C.ORCID), ("CV (PDF)", C.CV_PDF)])}</p>
  </div>
</section>
<section class="wrap blk prose">{bio}<p>If your group works on generative modelling, computational imaging, radar or sensor fusion, I would be glad to connect — <a href="mailto:{C.EMAIL}">email me</a>.</p></section>
<section class="wrap blk two">
  <div><div class="sec-h"><h2>Experience</h2></div><ol class="tl">{exp}</ol></div>
  <div><div class="sec-h"><h2>Education</h2></div><ol class="tl">{edu}</ol></div>
</section>
<section class="wrap blk two">
  <div><div class="sec-h"><h2>Honours &amp; awards</h2></div><ol class="tl">{hon}</ol></div>
  <div><div class="sec-h"><h2>Leadership &amp; service</h2></div><ol class="tl">{srv}</ol>
  <p class="note">At the JCU Student Association I helped deliver campus services and student-engagement initiatives, and represented JCU at the Australian University Student Voice Conference on the Gold Coast (2025).</p></div>
</section>
<section class="wrap blk"><div class="sec-h"><h2>Skills</h2></div><dl class="skills">{skills}</dl></section>
"""
    page("about/", "About", "About Yanlong Yang: education, experience, honours and service.", body, "/about/")


def cv():
    body = f"""
<section class="wrap page-h">
  <p class="kicker">Curriculum vitae</p>
  <h1>CV</h1>
  <p class="lede">The full CV as a PDF. Everything in it is also on this site: <a href="/research/">research</a>, <a href="/projects/">projects</a> and <a href="/about/">about</a>.</p>
  <div class="cta"><a class="btn btn-p" href="{C.CV_PDF}">Download PDF</a><a class="btn" href="{C.CV_PDF}" target="_blank" rel="noopener">Open in new tab</a></div>
</section>
<section class="wrap blk"><object class="pdf" data="{C.CV_PDF}#view=FitH" type="application/pdf" aria-label="CV of Yanlong Yang"><p>Your browser cannot show the PDF here. <a href="{C.CV_PDF}">Download it instead.</a></p></object></section>
"""
    page("cv/", "CV", "Curriculum vitae of Yanlong Yang (PDF).", body, "/cv/")


def notfound():
    body = """<section class="wrap page-h"><p class="kicker">404</p><h1>Signal lost.</h1><p class="lede">That page does not exist. Try the <a href="/">home page</a>, <a href="/research/">research</a> or <a href="/projects/">projects</a>.</p></section>"""
    page("404.html", "Not found", "Page not found.", body)


def redirects():
    for src, dst in C.REDIRECTS.items():
        if src in ("about/",):
            continue
        dest = os.path.join(OUT, src, "index.html")
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        open(dest, "w").write(
            f'<!doctype html><meta charset="utf-8"><title>Moved</title><link rel="canonical" href="{SITE}{dst}">'
            f'<meta http-equiv="refresh" content="0; url={dst}"><p>Moved to <a href="{dst}">{dst}</a>.</p>\n')


def sitemap():
    urls = ["", "research/", "projects/", "about/", "cv/"] + [f"projects/{p['slug']}/" for p in C.PROJECTS]
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    xml += "".join(f"  <url><loc>{SITE}/{u}</loc></url>\n" for u in urls) + "</urlset>\n"
    open(os.path.join(OUT, "sitemap.xml"), "w").write(xml)
    open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")


if __name__ == "__main__":
    os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)
    shutil.copy(os.path.join(SRC, "style.css"), os.path.join(OUT, "assets", "site.css"))
    shutil.copy(os.path.join(SRC, "site.js"), os.path.join(OUT, "assets", "site.js"))
    open(os.path.join(OUT, ".nojekyll"), "w").close()
    home(); research(); projects(); about(); cv(); notfound(); redirects(); sitemap()
    print("built", OUT)
