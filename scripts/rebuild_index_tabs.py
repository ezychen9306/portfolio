# coding: utf-8
import re
from pathlib import Path
import json

ROOT = Path(r"d:\AI_agents\21_Report_Projects\05_portfolio")
INDEX = ROOT/'index.html'
DATA = ROOT/'assets/data/projects.json'

html = INDEX.read_text(encoding='utf-8')
projects = json.loads(DATA.read_text(encoding='utf-8-sig'))

# prepare new fragments

def card_html(p):
    url=p['href']; cover=p['cover']; title=p['name']; desc=p['desc']
    return f"""<a class="image" href="{url}" target="_blank" rel="noopener">
  <div class="portfolio-card__media">
    <img src="{cover}" alt="{title}" loading="lazy" width="480" height="300" onerror="this.style.display='none';this.nextElementSibling.classList.add('is-fallback');">
    <div class="portfolio-card__placeholder"><span class="portfolio-card__placeholder-title">{title}</span></div>
  </div>
  <div class="portfolio-card__caption">
    <h4>{title}</h4>
    <p>{desc}</p>
  </div>
</a>"""

all_html='\n'.join(card_html(p) for p in projects)
map_cat={'risk':'webdevelop','data':'webdesign','ai':'appdevelop'}
cat_html={'webdevelop':[], 'webdesign':[], 'appdevelop':[]}
for p in projects:
    cat_html[ map_cat.get(p['category'],'webdevelop') ].append(card_html(p))
for k in list(cat_html):
    cat_html[k]='\n'.join(cat_html[k])

# utility: find the end position of the div starting at given index by counting nested <div ...> ... </div>

div_open_re=re.compile(r'<div\b', re.I)
div_close_re=re.compile(r'</div\s*>', re.I)

def replace_tab(html_text, tab_id, new_inner):
    # find the start of the specific tab-content div
    start = re.search(r'<div[^>]*\bid\s*=\s*"'+re.escape(tab_id)+r'"[^>]*>', html_text)
    if not start:
        return html_text
    i = start.start()
    j = start.end()
    depth = 1
    pos = j
    # scan forward counting divs
    while depth>0 and pos < len(html_text):
        m_open = div_open_re.search(html_text, pos)
        m_close = div_close_re.search(html_text, pos)
        if not m_close:
            break
        if m_open and m_open.start() < m_close.start():
            depth += 1
            pos = m_open.end()
        else:
            depth -= 1
            pos = m_close.end()
    end = pos
    # rebuild html: keep opening tag, inject new_inner, then closing </div>
    opening = html_text[i:j]
    new_block = opening + '\n' + new_inner + '\n</div>'
    return html_text[:i] + new_block + html_text[end:]

html = replace_tab(html, 'all', all_html)
html = replace_tab(html, 'webdevelop', cat_html['webdevelop'])
html = replace_tab(html, 'webdesign', cat_html['webdesign'])
html = replace_tab(html, 'appdevelop', cat_html['appdevelop'])

INDEX.write_text(html, encoding='utf-8')
print('index tabs rebuilt with balanced div matching')
