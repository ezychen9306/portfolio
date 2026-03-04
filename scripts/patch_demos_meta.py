# coding: utf-8
from pathlib import Path
import json, re

ROOT = Path(r"d:\AI_agents\21_Report_Projects\05_portfolio")
DEMOS = ROOT/'demos'
DATA = ROOT/'assets/data/projects.json'

projects = { Path(p['href']).parent.as_posix(): p for p in json.loads(DATA.read_text(encoding='utf-8-sig')) }

for idx in DEMOS.rglob('index.html'):
    rel = idx.parent.relative_to(ROOT).as_posix()  # demos/xx
    p = projects.get(rel)
    desc = (p or {}).get('desc','Demo')
    html = idx.read_text(encoding='utf-8')
    head_end = html.find('</head>')
    if head_end==-1:
        continue
    # inject description if missing
    injects = []
    if 'name="description"' not in html:
        injects.append(f'<meta name="description" content="{desc}">')
    if 'og:title' not in html:
        title = re.search(r'<title>(.*?)</title>', html)
        og_title = (title.group(1) if title else 'Demo') + ' · 演示'
        injects += [
            f'<meta property="og:title" content="{og_title}" />',
            f'<meta property="og:description" content="{desc}" />',
            f'<meta property="og:type" content="website" />',
            f'<meta property="og:image" content="../../screenshot.png" />',
            f'<meta property="og:url" content="https://ezychen9306.github.io/portfolio/" />'
        ]
    if 'rel="icon"' not in html or 'rel="manifest"' not in html:
        injects += [
            '<link rel="apple-touch-icon" sizes="180x180" href="../../assets/icons/apple-touch-icon.png">',
            '<link rel="icon" type="image/png" sizes="32x32" href="../../assets/icons/favicon-32x32.png">',
            '<link rel="icon" type="image/png" sizes="16x16" href="../../assets/icons/favicon-16x16.png">',
            '<link rel="manifest" href="../../assets/icons/site.webmanifest">'
        ]
    if injects:
        html = html.replace('</head>', '\n'.join(injects) + '\n</head>')
        idx.write_text(html, encoding='utf-8')
        print('patched', rel)
print('done')
