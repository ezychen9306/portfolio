# coding: utf-8
from html.parser import HTMLParser
from pathlib import Path
import sys, json, re

ROOT = Path(r"d:\AI_agents\21_Report_Projects\05_portfolio")
PAGES = [ROOT/'index.html', ROOT/'cv.html']
DEMOS = [p for p in (ROOT/'demos').rglob('index.html')]
JS = ROOT/'assets/js/script.js'
ROBOTS = ROOT/'robots.txt'
SITEMAP = ROOT/'sitemap.xml'
MANIFEST = ROOT/'assets/icons/site.webmanifest'
PROJECTS = ROOT/'assets/data/projects.json'

issues = []

class Collector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.metas=[]; self.links=[]; self.anchors=[]; self.images=[]; self.titles=[]
    def handle_starttag(self, tag, attrs):
        d=dict(attrs)
        if tag=='meta': self.metas.append(d)
        elif tag=='link': self.links.append(d)
        elif tag=='a': self.anchors.append(d)
        elif tag=='img': self.images.append(d)
        elif tag=='title': self.titles.append('')
    def handle_data(self, data):
        if self.titles and self.titles[-1]=='' and data.strip():
            self.titles[-1]=data.strip()

def check_html(path:Path):
    c=Collector()
    try:
        c.feed(path.read_text(encoding='utf-8'))
    except Exception as e:
        issues.append((str(path),'parse',f'html parse error: {e}'))
        return
    has_charset=any('charset' in m for m in c.metas)
    has_vp=any(m.get('name','').lower()=='viewport' for m in c.metas)
    has_desc=any(m.get('name','').lower()=='description' for m in c.metas)
    if not has_charset: issues.append((str(path),'meta','missing charset'))
    if not has_vp: issues.append((str(path),'meta','missing viewport'))
    if not has_desc: issues.append((str(path),'meta','missing description'))
    og_reqs={'og:title','og:description','og:image','og:url'}
    og_present={m.get('property') for m in c.metas if 'property' in m}
    for k in og_reqs:
        if k not in og_present: issues.append((str(path),'og',f'missing {k}'))
    # icons/manifest
    icons_ok = any(l.get('rel')=='icon' and 'favicon-32' in (l.get('href') or '') for l in c.links)
    manifest_ok = any(l.get('rel')=='manifest' for l in c.links)
    if not icons_ok: issues.append((str(path),'icons','missing favicon link'))
    if not manifest_ok: issues.append((str(path),'icons','missing manifest link'))
    # anchors target=_blank need rel noopener
    for a in c.anchors:
        if a.get('target')=='_blank' and ('noopener' not in (a.get('rel') or '')):
            issues.append((str(path),'a11y','target=_blank without rel=noopener'))
    # images need alt
    for img in c.images:
        if 'alt' not in img:
            issues.append((str(path),'img','missing alt on <img>'))

def check_js():
    txt=JS.read_text(encoding='utf-8', errors='ignore')
    if 'prefers-reduced-motion' not in txt:
        issues.append((str(JS),'motion','missing prefers-reduced-motion guard'))
    for marker in [
        'getElementById("particleCanvas");',
        'getElementById("waveCanvas");'
    ]:
        if marker in txt and 'reduceMotion' not in txt:
            issues.append((str(JS),'motion','canvas guards may be missing'))

def check_robots_sitemap():
    r=ROBOTS.read_text(encoding='utf-8') if ROBOTS.exists() else ''
    if 'Sitemap:' not in r: issues.append((str(ROBOTS),'seo','robots.txt missing Sitemap'))
    x=SITEMAP.read_text(encoding='utf-8') if SITEMAP.exists() else ''
    # every demo index should be present in sitemap
    for d in DEMOS:
        rel = d.relative_to(ROOT).as_posix()
        if rel not in x:
            issues.append((str(SITEMAP),'seo',f'sitemap missing {rel}'))

def check_projects():
    try:
        data = json.loads(PROJECTS.read_text(encoding='utf-8-sig'))
    except Exception as e:
        issues.append((str(PROJECTS),'json',f'parse error: {e}'))
        return
    allowed={'risk','data','ai'}
    for p in data:
        if p.get('category') not in allowed:
            issues.append((str(PROJECTS),'json',f'invalid category for {p.get("id")}'))
        # local existence
        href = ROOT / p.get('href','')
        cover = ROOT / p.get('cover','')
        if not href.exists(): issues.append((str(PROJECTS),'json',f'missing href target for {p.get("id")}'))
        if not cover.exists(): issues.append((str(PROJECTS),'json',f'missing cover for {p.get("id")}'))

# run checks
for p in PAGES: check_html(p)
for d in DEMOS: check_html(d)
check_js(); check_robots_sitemap(); check_projects()

# portfolio structure sanity
idx = ROOT/'index.html'
html = idx.read_text(encoding='utf-8', errors='ignore')
for tab in ['all','webdevelop','webdesign','appdevelop']:
    if f'id="{tab}"' not in html:
        issues.append((str(idx),'structure',f'missing tab-content #{tab}'))
if 'cv.html' not in html:
    issues.append((str(idx),'nav','missing CV link in nav'))

# report
if issues:
    print('Preflight FAILED:')
    for f,cat,msg in issues:
        print(f' - [{cat}] {f}: {msg}')
    sys.exit(1)
else:
    print('Preflight OK: pages/meta/og/icons/links/images/js/seo all good; demos:', len(DEMOS))
