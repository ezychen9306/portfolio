# coding: utf-8
from pathlib import Path
import json, re
ROOT=Path(r'd:\AI_agents\21_Report_Projects\05_portfolio')
DATA=ROOT/'assets/data/projects.json'
proj=json.loads(DATA.read_text(encoding='utf-8-sig'))

def card_html(p):
    url=p['href']; cover=p['cover']; title=p['name']; desc=p['desc']
    return f'''<a class="image" href="{url}">
  <div class="portfolio-card__media">
    <img src="{cover}" alt="{title}" loading="lazy" width="480" height="300" onerror="this.style.display='none';this.nextElementSibling.classList.add('is-fallback');">
    <div class="portfolio-card__placeholder"><span class="portfolio-card__placeholder-title">{title}</span></div>
  </div>
  <div class="portfolio-card__caption">
    <h4>{title}</h4>
    <p>{desc}</p>
  </div>
</a>'''

all_html='\n'.join(card_html(p) for p in proj)
map_cat={'risk':'webdevelop','data':'webdesign','ai':'appdevelop'}
cat={'webdevelop':[], 'webdesign':[], 'appdevelop':[]}
for p in proj:
    cat[ map_cat.get(p['category'],'webdevelop') ].append(card_html(p))
for k in list(cat):
    cat[k]='\n'.join(cat[k])

HTML=f'''<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="description" content="贷中风控策略负责人 · AI 策略专家 · AI Agent 开发者" />
    <link rel="apple-touch-icon" sizes="180x180" href="assets/icons/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="assets/icons/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="assets/icons/favicon-16x16.png">
    <link rel="manifest" href="assets/icons/site.webmanifest">
    <meta name="theme-color" content="#6b8e9f" />
    <meta property="og:title" content="Ezy Chen · Portfolio" />
    <meta property="og:description" content="贷中风控策略 · AI 策略 · Agent 开发" />
    <meta property="og:type" content="website" />
    <meta property="og:image" content="screenshot.png" />
    <meta property="og:url" content="https://ezychen9306.github.io/portfolio/" />
    <link rel="stylesheet" href="assets/css/style.css" />
    <link href="https://cdn.jsdelivr.net/npm/remixicon@4.1.0/fonts/remixicon.css" rel="stylesheet" />
    <title>Ezy Chen · Portfolio — 贷中风控策略 · AI 策略 · Agent 开发</title>
  </head>
  <body>
    <nav>
      <div class="container nav-container">
        <a href="index.html" class="logo">Ezy<span>Portfolio</span></a>
        <ul class="navlist">
          <li><a href="#home">首页</a></li>
          <li><a href="#services">能力</a></li>
          <li><a href="#portfolio">项目</a></li>
          <li><a href="cv.html" class="nav-link-resume">简历</a></li>
          <li><a href="#contact">联系</a></li>
        </ul>
        <div class="nav-icons">
          <div id="theme-btn" class="ri-moon-line"></div>
          <div id="menu-btn" class="ri-menu-line"></div>
        </div>
      </div>
    </nav>
    <section class="home" id="home">
      <div class="section-placeholder" aria-hidden="true"><span class="section-placeholder__num">01</span><span class="section-placeholder__dots">···</span></div>
      <div class="container home-container">
        <div class="left">
          <h1 class="home-name"><span class="home-name-inner">Ezy Chen</span></h1>
          <p class="home-typed">我是 <span class="multiple-text"></span></p>
          <p class="home-intro home-summary">7 年贷中风控 · <span class="home-key">4 年团队管理</span>；服务国内外，覆盖多类金融产品；在贷余额超 <b class="home-key home-key-accent">500 亿</b>；多项 <span class="home-key">0→1</span> 项目，持续交付可衡量业务价值。</p>
        </div>
      </div>
    </section>
    <section class="portfolio" id="portfolio">
      <div class="section-placeholder" aria-hidden="true"><span class="section-placeholder__num">03</span><span class="section-placeholder__dots">···</span></div>
      <div class="title"><h2>精选 <span>项目</span></h2></div>
      <div class="container portfolio-container">
        <div class="portfolio-buttons">
          <button class="btn portfolio-tab" onclick="tabOpen('all')">全部</button>
          <button class="btn portfolio-tab active" onclick="tabOpen('webdevelop')">风控/经营</button>
          <button class="btn portfolio-tab" onclick="tabOpen('webdesign')">数据/报表</button>
          <button class="btn portfolio-tab" onclick="tabOpen('appdevelop')">AI Agent</button>
        </div>
        <div class="tab-content" id="all">\n{all_html}\n</div>
        <div class="tab-content active-content" id="webdevelop">\n{cat['webdevelop']}\n</div>
        <div class="tab-content" id="webdesign">\n{cat['webdesign']}\n</div>
        <div class="tab-content" id="appdevelop">\n{cat['appdevelop']}\n</div>
      </div>
    </section>
    <script src="assets/js/script.js"></script>
  </body>
</html>
'''
(ROOT/'index.html').write_text(HTML, encoding='utf-8')
print('index.html regenerated cleanly')
