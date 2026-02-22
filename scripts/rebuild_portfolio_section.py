# coding: utf-8
import re, json
from pathlib import Path

ROOT = Path(r"d:\AI_agents\21_Report_Agent\05_portfolio")
INDEX = ROOT/'index.html'
DATA = ROOT/'assets/data/projects.json'

def card_html(p):
    url=p['href']; cover=p['cover']; title=p['name']; desc=p['desc']
    return f"""<a class=\"image\" href=\"{url}\">\n  <div class=\"portfolio-card__media\">\n    <img src=\"{cover}\" alt=\"{title}\" loading=\"lazy\" width=\"480\" height=\"300\" onerror=\"this.style.display='none';this.nextElementSibling.classList.add('is-fallback');\">\n    <div class=\"portfolio-card__placeholder\"><span class=\"portfolio-card__placeholder-title\">{title}</span></div>\n  </div>\n  <div class=\"portfolio-card__caption\">\n    <h4>{title}</h4>\n    <p>{desc}</p>\n  </div>\n</a>"""

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

container_html = '<div class="container portfolio-container">\n' + buttons + '\n' + \
  f"<div class=\"tab-content active-content\" id=\"all\">\n{all_html}\n</div>\n" + \
  f"<div class=\"tab-content\" id=\"webdevelop\">\n{cat['webdevelop']}\n</div>\n" + \
  f"<div class=\"tab-content\" id=\"webdesign\">\n{cat['webdesign']}\n</div>\n" + \
  f"<div class=\"tab-content\" id=\"appdevelop\">\n{cat['appdevelop']}\n</div>\n" + '</div>'

html = INDEX.read_text(encoding='utf-8')
# locate portfolio section range
sec_m = re.search(r'<section[^>]*\bclass=\"[^\"]*\bportfolio\b[^\"]*\"[^>]*>', html)
if not sec_m:
    print('portfolio <section> not found'); raise SystemExit(1)
sec_start = sec_m.start()
# find closing </section> after start
end_m = re.search(r'</section\s*>', html[sec_m.end():])
if not end_m:
    print('portfolio </section> not found'); raise SystemExit(1)
sec_end = sec_m.end() + end_m.end()
section = html[sec_start:sec_end]
# split section into head(before container) + body(after container)
cont_m = re.search(r'<div\s+class=\"container\s+portfolio-container\"\s*>', section)
if not cont_m:
    print('container not found inside section'); raise SystemExit(1)
head = section[:cont_m.start()]
# replace entire container to end-of-section with clean container + closing </section>
new_section = head + container_html + '</section>'
new_html = html[:sec_start] + new_section + html[sec_end:]
INDEX.write_text(new_html, encoding='utf-8')
print('portfolio section rebuilt (container + purge trailing leftovers)')

