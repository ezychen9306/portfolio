# coding: utf-8
import re, json
from pathlib import Path

ROOT = Path(r"d:\AI_agents\21_Report_Projects\05_portfolio")
INDEX = ROOT/'index.html'
DATA = ROOT/'assets/data/projects.json'

def card_html(p):
    url=p['href']; cover=p['cover']; title=p['name']; desc=p['desc']
    return f"""<a class=\"image\" href=\"{url}\" target=\"_blank\" rel=\"noopener\">\n  <div class=\"portfolio-card__media\">\n    <img src=\"{cover}\" alt=\"{title}\" loading=\"lazy\" width=\"480\" height=\"300\" onerror=\"this.style.display='none';this.nextElementSibling.classList.add('is-fallback');\">\n    <div class=\"portfolio-card__placeholder\"><span class=\"portfolio-card__placeholder-title\">{title}</span></div>\n  </div>\n  <div class=\"portfolio-card__caption\">\n    <h4>{title}</h4>\n    <p>{desc}</p>\n  </div>\n</a>"""

projects = json.loads(DATA.read_text(encoding='utf-8-sig'))
all_html='\n'.join(card_html(p) for p in projects)
map_cat={'risk':'webdevelop','data':'webdesign','ai':'appdevelop'}
cat={'webdevelop':[], 'webdesign':[], 'appdevelop':[]}
for p in projects:
    cat[ map_cat.get(p['category'],'webdevelop') ].append(card_html(p))
for k in list(cat):
    cat[k]='\n'.join(cat[k])

buttons = '''<div class="portfolio-buttons" >
  <button class="btn portfolio-tab active" onclick="tabOpen('all')">全部</button>
  <button class="btn portfolio-tab " onclick="tabOpen('webdevelop')">风控/经营</button>
  <button class="btn portfolio-tab " onclick="tabOpen('webdesign')">数据/报表</button>
  <button class="btn portfolio-tab " onclick="tabOpen('appdevelop')">AI Agent</button>
</div>'''

new_container = buttons + '\n' + \
  f"<div class=\"tab-content active-content\" id=\"all\">\n{all_html}\n</div>\n" + \
  f"<div class=\"tab-content\" id=\"webdevelop\">\n{cat['webdevelop']}\n</div>\n" + \
  f"<div class=\"tab-content\" id=\"webdesign\">\n{cat['webdesign']}\n</div>\n" + \
  f"<div class=\"tab-content\" id=\"appdevelop\">\n{cat['appdevelop']}\n</div>\n"

html = INDEX.read_text(encoding='utf-8')
# find the portfolio container div
m = re.search(r'<div\s+class=\"container\s+portfolio-container\"\s*>', html)
if not m:
    print('portfolio container not found')
    raise SystemExit(1)
start = m.start(); j = m.end()
# find matching closing </div> for this container
open_re=re.compile(r'<div\b', re.I); close_re=re.compile(r'</div\s*>', re.I)
pos=j; depth=1
while depth>0 and pos < len(html):
    mo = open_re.search(html, pos)
    mc = close_re.search(html, pos)
    if not mc:
        break
    if mo and mo.start() < mc.start():
        depth += 1; pos = mo.end()
    else:
        depth -= 1; pos = mc.end()
end = pos
# build replacement
opening = html[start:j]
new_html = html[:start] + opening + "\n" + new_container + html[end:]
INDEX.write_text(new_html, encoding='utf-8')
print('portfolio container rebuilt cleanly')
