# coding: utf-8
import json, sys
from pathlib import Path

ROOT = Path(r"d:\AI_agents\21_Report_Agent\05_portfolio")
DATA = ROOT / 'assets' / 'data' / 'projects.json'
ALLOWED = {'risk','data','ai'}

problems = []
projects = json.loads(DATA.read_text(encoding='utf-8-sig'))
for i,p in enumerate(projects,1):
    pid = p.get('id') or f'#{i}'
    href = ROOT / p.get('href','')
    cover = ROOT / p.get('cover','')
    cat = p.get('category','')
    if cat not in ALLOWED:
        problems.append((pid, f"invalid category: {cat}"))
    if not href.exists():
        problems.append((pid, f"missing href target: {p.get('href')}"))
    if not cover.exists():
        problems.append((pid, f"missing cover image: {p.get('cover')}"))
    if not p.get('name'):
        problems.append((pid, "missing name"))
    if not p.get('desc'):
        problems.append((pid, "missing desc"))

if problems:
    print('Validation FAILED:')
    for pid,msg in problems:
        print(f' - {pid}: {msg}')
    sys.exit(1)
else:
    print('Validation OK: all project links and images found, categories valid.')
