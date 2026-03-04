# coding: utf-8
from pathlib import Path
import re
import sys

ROOT = Path(r"d:\AI_agents\21_Report_Projects\05_portfolio")
INDEX = ROOT / "index.html"
JS = ROOT / "assets" / "js" / "script.js"
CSS = ROOT / "assets" / "css" / "style.css"


def check(name, condition, detail):
    return {"name": name, "ok": bool(condition), "detail": detail}


def main():
    idx = INDEX.read_text(encoding="utf-8", errors="ignore")
    js = JS.read_text(encoding="utf-8", errors="ignore")
    css = CSS.read_text(encoding="utf-8", errors="ignore")

    results = []
    results.append(check("no_lorem", "lorem" not in idx.lower(), "index.html must not contain Lorem placeholder text"))
    results.append(check("empty_alt_zero", 'alt=""' not in idx, 'index.html must not contain empty alt=""'))
    results.append(check("favicon_data_uri", "data:image/svg+xml" in idx, "favicon data URI must exist in <head>"))
    results.append(check("achievements_section", 'id="testimonial"' in idx and "经验与" in idx and "成就" in idx, "achievements section should exist"))
    results.append(check("skills_chart_container", 'id="skills-chart"' in idx, "#skills-chart container should exist"))
    results.append(check("apexcharts_cdn", "cdn.jsdelivr.net/npm/apexcharts" in idx, "ApexCharts CDN should be present"))
    results.append(check("cdn_scrollreveal_jsdelivr", "cdn.jsdelivr.net/npm/scrollreveal@4/dist/scrollreveal.min.js" in idx, "ScrollReveal should use jsdelivr"))
    results.append(check("cdn_typed_jsdelivr", "cdn.jsdelivr.net/npm/typed.js@2.1.0/dist/typed.umd.js" in idx, "Typed.js should use jsdelivr"))
    results.append(check("tab_open_signature", "function tabOpen(x, el)" in js, "tabOpen should accept (x, el)"))
    results.append(check("tab_open_no_global_event", "event.currentTarget" not in js, "tabOpen should not rely on global event"))
    results.append(check("theme_persistence", 'THEME_KEY = "portfolio_theme"' in js and "localStorage.setItem(THEME_KEY" in js, "theme should persist in localStorage"))
    results.append(check("contact_toast_flow", "wireContactForm" in js and "showToast" in js, "contact form validation + toast should exist"))
    results.append(check("scrollspy_nav", "wireScrollSpy" in js and ".navlist a[href^='#']" in js, "scrollspy nav highlight should exist"))
    results.append(check("card_style_core", ".portfolio-card::before" in css and ".portfolio-card__tags" in css and ".portfolio-card__overlay" in css, "card redesign CSS should exist"))
    results.append(check("toast_style", ".toast--success" in css and ".toast--error" in css, "toast style should exist"))

    failed = [r for r in results if not r["ok"]]
    if failed:
        print("Refactor acceptance FAILED:")
        for row in failed:
            print(f" - {row['name']}: {row['detail']}")
        sys.exit(1)

    print("Refactor acceptance OK:")
    for row in results:
        print(f" - {row['name']}: pass")
    sys.exit(0)


if __name__ == "__main__":
    main()
