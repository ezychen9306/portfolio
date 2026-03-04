#!/usr/bin/env python3
"""
portfolio 项目卡片生成器
========================
维护 CARDS / TABS 数据，运行后自动更新 index.html 中的 portfolio section。

用法:
  python scripts/build_portfolio.py

新增项目:
  1. 在 CARDS 里加一条记录
  2. 在 TABS 里把 id 加到对应分类
  3. 运行脚本
"""

import re, sys
from pathlib import Path

# ─────────────────────────────────────────
#  1. 数据层 — 只需维护这里
# ─────────────────────────────────────────

CARDS = {
    "01": {
        "href":  "demos/01_disaster_management/index.html",
        "img":   "disaster-management.png",
        "alt":   "灾难管控策略",
        "title": "灾难管控策略",
        "desc":  "T+1 响应 · 风险降幅 10%+",
    },
    "02": {
        "href":  "demos/02_quota_strategy_v5/index.html",
        "img":   "quota-strategy-v5.png",
        "alt":   "额度策略 V5",
        "title": "额度策略 V5",
        "desc":  "规模 2× · 风险持平",
    },
    "03": {
        "href":  "demos/03_rm_system/summary.html",
        "img":   "rm-system.png",
        "alt":   "全面风险管理系统",
        "title": "全面风险管理系统",
        "desc":  "9 条业务线 · 风险预估 · 财报与审计支持",
    },
    "04": {
        "href":  "demos/04_ai_deep_strategy/index.html",
        "img":   "ai-deep-strategy.png",
        "alt":   "AI 风控策略",
        "title": "AI 风控策略",
        "desc":  "借新还旧 · 提前结清 · 额度曲线",
    },
    "05": {
        "href":  "demos/05_kyc_platform/index.html",
        "img":   "kyc-platform.png",
        "alt":   "KYC 策略中台",
        "title": "KYC 策略中台",
        "desc":  "转化率 +15.6% · 月增 2.7 亿",
    },
    "06": {
        "href":  "demos/06_telesales_system/index.html",
        "img":   "telesales-system.png",
        "alt":   "智能电销系统",
        "title": "智能电销系统",
        "desc":  "转化率 +9.8% · 月增 1.1 亿",
    },
    "07": {
        "href":  "../02_2025end_report/2025_year_end_report_package/outputs/2025_year_end_report.html",
        "img":   "year-end-report.png",
        "alt":   "25年年度总结",
        "title": "25年年度总结",
        "desc":  "策略体系 · 时间线 · 核心成果",
    },
    "08": {
        "href":  "../03_ai_internal_sharing/old_customer_weekly_report/202601_W5/outputs/【菲律宾老客】周报_20260130_v1_在线版.html",
        "img":   "weekly-monitoring.png",
        "alt":   "目标达成体系",
        "title": "目标达成体系",
        "desc":  "目标追踪 · 周度监控 · 一键出图",
    },
    "09": {
        "href":  "../03_ai_internal_sharing/03_analysis_reports/01_overview/ai_internal_sharing_ezy_creative.html",
        "img":   "ai-sharing.png",
        "alt":   "AI 内部分享",
        "title": "AI 内部分享",
        "desc":  "团队赋能 · 效率 +30%+",
    },
    "10": {
        "href":  "demos/10_fof_system/index.html",
        "img":   "fof-system.png",
        "alt":   "智能投顾系统（FOF）",
        "title": "智能投顾系统（FOF）",
        "desc":  "AUM 8 亿+ · 年化 12.5%",
    },
    "13": {
        "href":  "demos/13_knowledge_base_agent/index.html",
        "img":   "knowledge-base-agent.png",
        "alt":   "知识库 Agent",
        "title": "知识库 Agent",
        "desc":  "RAG 检索 · 准确率 92.5%",
    },
    "14": {
        "href":  "demos/14_skills_development/index.html",
        "img":   "skills-dev.png",
        "alt":   "Skills 技能开发",
        "title": "Skills 技能开发",
        "desc":  "效率 +50% · 规范遵守 95%+",
    },
}

# Tab 定义: (tab_id, label, card_ids, default_active)
TABS = [
    ("all",         "全部",      ["01","02","03","04","05","06","07","08","13","14","09","10"], False),
    ("webdevelop",  "风控/经营", ["01","02","03","04","05","06"],                                       True),
    ("webdesign",   "数据/报表", ["07","08"],                                                             False),
    ("appdevelop",  "AI Agent",  ["13","14","09","10"],                                                  False),
]

# ─────────────────────────────────────────
#  2. 模板层 — 卡片 HTML
# ─────────────────────────────────────────

CARD_TMPL = """\
          <a class="image" href="{href}">
            <div class="portfolio-card__media">
              <img src="assets/images/projects/{img}" alt="{alt}" loading="lazy" width="480" height="300" onerror="this.style.display='none';this.nextElementSibling.classList.add('is-fallback');">
              <div class="portfolio-card__placeholder"><span class="portfolio-card__placeholder-title">{alt}</span></div>
            </div>
            <div class="portfolio-card__caption">
              <h4>{title}</h4>
              <p>{desc}</p>
            </div>
          </a>"""

# ─────────────────────────────────────────
#  3. 渲染层
# ─────────────────────────────────────────

def render_card(card_id):
    d = CARDS[card_id]
    return CARD_TMPL.format(**d)


def render_tab(tab_id, card_ids, active=False):
    cls = "tab-content active-content" if active else "tab-content"
    cards_html = "\n".join(render_card(cid) for cid in card_ids)
    return (
        f'        <div class="{cls}" id="{tab_id}">\n'
        f'{cards_html}\n'
        f'        </div>'
    )


def render_buttons():
    lines = []
    for tab_id, label, _, active in TABS:
        active_cls = " active" if active else ""
        lines.append(
            f'          <button class="btn portfolio-tab{active_cls}" '
            f'onclick="tabOpen(\'{tab_id}\')">{label}</button>'
        )
    return "\n".join(lines)


def render_section():
    buttons = render_buttons()
    tabs_html = "\n\n".join(
        render_tab(tid, cids, active)
        for tid, _, cids, active in TABS
    )
    return f"""\
    <!-- ==================================
                PORTFOLIO SECTION
    ==================================== -->
    <section class="portfolio" id="portfolio">
      <div class="section-placeholder" aria-hidden="true">
        <span class="section-placeholder__num">03</span>
        <span class="section-placeholder__dots">···</span>
      </div>
      <div class="title">
        <h2>精选 <span>项目</span></h2>
      </div>
      <div class="container portfolio-container">
        <div class="portfolio-buttons">
{buttons}
        </div>

{tabs_html}

      </div>
    </section>"""


# ─────────────────────────────────────────
#  4. 注入 index.html
# ─────────────────────────────────────────

PORTFOLIO_RE = re.compile(
    r'    <!-- ={10,}\s+PORTFOLIO SECTION.*?</section>',
    re.DOTALL,
)

def inject(index_path: Path):
    original = index_path.read_text(encoding="utf-8")
    new_section = render_section()

    if not PORTFOLIO_RE.search(original):
        print("ERROR: 找不到 portfolio section 标记，请检查 index.html 注释格式")
        sys.exit(1)

    updated = PORTFOLIO_RE.sub(new_section, original, count=1)
    index_path.write_text(updated, encoding="utf-8")

    # 验证
    wdev = updated.count('id="webdevelop"')
    total_cards = updated.count('class="image"')
    print("OK: portfolio section updated")
    print(f"  tabs    : {len(TABS)}")
    print(f"  cards   : {total_cards}  (expected 28 = 14+7+3+4)")
    print(f"  webdevelop occurrences: {wdev}  (expected 1)")
    if wdev != 1 or total_cards != 28:
        print("WARNING: count mismatch, please check")


if __name__ == "__main__":
    root = Path(__file__).parent.parent          # portfolio 根目录
    index = root / "index.html"
    inject(index)
