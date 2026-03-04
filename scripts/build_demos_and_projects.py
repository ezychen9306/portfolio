# coding: utf-8
import os, re, json
from pathlib import Path
from string import Template

ROOT = Path(r"d:\AI_agents\21_Report_Projects\05_portfolio")
DEMOS = ROOT / 'demos'
JSON_PATH = ROOT / 'assets' / 'data' / 'projects.json'

# Minimal markdown -> html fallback
def md_to_html(md: str) -> str:
    html_lines = []
    in_code = False
    list_open = False
    for line in md.splitlines():
        if line.strip().startswith('```'):
            if not in_code:
                html_lines.append('<pre><code>')
                in_code = True
            else:
                html_lines.append('</code></pre>')
                in_code = False
            continue
        if in_code:
            html_lines.append( (line
                .replace('&','&amp;')
                .replace('<','&lt;')
                .replace('>','&gt;')) )
            continue
        m = re.match(r'^(#{1,6})\s+(.*)$', line)
        if m:
            if list_open:
                html_lines.append('</ul>'); list_open=False
            level = len(m.group(1))
            html_lines.append(f'<h{level}>{m.group(2)}</h{level}>')
            continue
        if line.strip().startswith('- '):
            if not list_open:
                html_lines.append('<ul>'); list_open=True
            html_lines.append('<li>' + line.strip()[2:] + '</li>')
            continue
        else:
            if list_open:
                html_lines.append('</ul>'); list_open=False
        if line.strip():
            text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2" target="_blank" rel="noopener">\1</a>', line.strip())
            html_lines.append('<p>' + text + '</p>')
    if in_code:
        html_lines.append('</code></pre>')
    if list_open:
        html_lines.append('</ul>')
    return '\n'.join(html_lines)

HEADER_TPL = Template('''<!doctype html>
<html lang="zh-CN"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${title} · 演示</title>
<meta name="description" content="${desc}">
<link rel="apple-touch-icon" sizes="180x180" href="../../assets/icons/apple-touch-icon.png">
<link rel="icon" type="image/png" sizes="32x32" href="../../assets/icons/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="../../assets/icons/favicon-16x16.png">
<link rel="manifest" href="../../assets/icons/site.webmanifest">
<meta property="og:title" content="${title} · 演示" />
<meta property="og:description" content="${desc}" />
<meta property="og:type" content="website" />
<meta property="og:image" content="../../screenshot.png" />
<meta property="og:url" content="https://ezychen9306.github.io/portfolio/" />
<link href="https://cdn.jsdelivr.net/npm/remixicon@4.1.0/fonts/remixicon.css" rel="stylesheet">
<style>
:root{--primary:#6b8e9f;--accent:#c9a227;--text:#2d2d2d;--muted:#666}
body{font-family:system-ui,-apple-system,Segoe UI,Roboto,Ubuntu,"Microsoft Yahei",sans-serif;margin:0;background:#fafafa;color:var(--text)}
.topbar{display:flex;gap:.75rem;align-items:center;justify-content:space-between;padding:.6rem .9rem;border-bottom:1px solid #eee;background:#fff;position:sticky;top:0}
.topbar a{color:var(--primary);text-decoration:none;font-weight:600}
.topbar a.btn{display:inline-flex;align-items:center;gap:.35rem;background:var(--primary);color:#fff;padding:.35rem .6rem;border-radius:6px}
.container{max-width:1040px;margin:0 auto;padding:1rem}
footer{padding:2rem 1rem;color:#888;text-align:center}
article{background:#fff;border:1px solid #eee;border-radius:10px;padding:1.2rem}
article h1,article h2{border-bottom:1px solid #eee;padding-bottom:.25rem}
article img{max-width:100%;height:auto}
</style>
</head><body>
<div class="topbar">
  <div><a href="../../index.html"><i class="ri-arrow-left-line"></i> 返回作品集</a></div>
  <div style="color:#999;font-size:.9rem">${title}</div>
  <div><a class="btn" href="#" onclick="history.back();return false;"><i class="ri-history-line"></i> 返回</a></div>
</div>
<div class="container">
''')
FOOTER = '''</div>
<footer>© 2026 Portfolio Demos</footer>
</body></html>'''

# Ensure index.html exists for each demo, generating from README.md or copying demo.html

def ensure_demo_index(demo_dir: Path, title: str, desc: str):
    demo_dir.mkdir(parents=True, exist_ok=True)
    idx = demo_dir / 'index.html'
    if idx.exists():
        return False
    demo_html = demo_dir / 'demo.html'
    if demo_html.exists():
        idx.write_bytes(demo_html.read_bytes())
        return True
    md = demo_dir / 'README.md'
    if md.exists():
        md_html = md_to_html(md.read_text(encoding='utf-8', errors='ignore'))
        content = HEADER_TPL.substitute(title=title, desc=desc or title) + f'<article>\n{md_html}\n</article>' + FOOTER
        idx.write_text(content, encoding='utf-8')
        return True
    return False

# load projects
projects = json.loads(JSON_PATH.read_text(encoding='utf-8-sig'))

created = []
for p in projects:
    href = p.get('href','')
    if not href.startswith('demos/'):
        continue
    demo_rel = Path(href).parent
    demo_dir = ROOT / demo_rel
    if ensure_demo_index(demo_dir, p.get('name','Demo'), p.get('desc','')):
        created.append(str(demo_rel))
print('created/updated index.html for demos:', len(created))

# Build index.html sections
index_path = ROOT / 'index.html'
html = index_path.read_text(encoding='utf-8')

def card_html(p):
    url = p['href']
    cover = p['cover']
    title = p['name']
    desc = p['desc']
    return f"""<a class="image" href="{url}">
  <div class="portfolio-card__media">
    <img src="{cover}" alt="{title}" loading="lazy" width="480" height="300" onerror="this.style.display='none';this.nextElementSibling.classList.add('is-fallback');">
    <div class="portfolio-card__placeholder"><span class="portfolio-card__placeholder-title">{title}</span></div>
  </div>
  <div class="portfolio-card__caption">
    <h4>{title}</h4>
    <p>{desc}</p>
  </div>
</a>"""

all_html = '\n'.join(card_html(p) for p in projects)
map_cat_to_tab = {'risk':'webdevelop','data':'webdesign','ai':'appdevelop'}
cat_html = {k: [] for k in map_cat_to_tab.values()}
for p in projects:
    tab = map_cat_to_tab.get(p['category'],'webdevelop')
    cat_html[tab].append(card_html(p))
for k in cat_html:
    cat_html[k] = '\n'.join(cat_html[k])

def replace_tab(html_text, tab_id, new_inner):
    pattern = re.compile(r'(\<div class="tab-content[^\"]*" id="'+re.escape(tab_id)+r'"[^>]*\>)([\s\S]*?)(\</div\>)', re.M)
    return pattern.sub(r"\1\n"+new_inner+"\n\3", html_text, count=1)

html = replace_tab(html, 'all', all_html)
html = replace_tab(html, 'webdevelop', cat_html['webdevelop'])
html = replace_tab(html, 'webdesign', cat_html['webdesign'])
html = replace_tab(html, 'appdevelop', cat_html['appdevelop'])

index_path.write_text(html, encoding='utf-8')
print('index.html grids refreshed from assets/data/projects.json')

