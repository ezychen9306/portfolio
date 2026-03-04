# Portfolio Refactor Plan (Desktop-First)

Created: 2026-03-04  
Project root: `21_Report_Projects/05_portfolio`  
Scope: content fixes + visual/interaction upgrades. Mobile-specific adaptation is out of scope for this round.

## Rules

- Single source of truth: this file.
- Each task must track:
  - `status`: `pending` | `in_progress` | `completed`
  - `completed_at`
  - `acceptance`: `pass` | `fail` | `n/a`
  - `evidence`
- Gate: no next task before current task record is updated.

## Execution Scope (Converged Spec)

- Target directory: `21_Report_Projects/05_portfolio` only.
- Desktop-first: mobile-specific adaptation is deferred to a later round.
- This round must include:
  - Content cleanup (no placeholder testimonial text, no empty `alt`, favicon data URI).
  - Contact form + JS validation + success toast.
  - Portfolio card redesign (category strip, tech tags, hover overlay, stagger animation).
  - Script/API updates: `tabOpen(x, el)`, theme persistence (`portfolio_theme`), scrollspy nav highlight.
  - CDN switch: ScrollReveal + Typed.js from unpkg to jsdelivr.
  - About/skills visualization: remove old SVG progress-ring path and use ApexCharts (`#skills-chart`) directly.
- Redundant step removed: no standalone “fix GradientColor duplicate IDs” task; replaced by direct chart replacement.

## Task Tracker

| id | task | status | completed_at | acceptance | evidence |
|---|---|---|---|---|---|
| P0-1 | Full snapshot commit (`git add -A` + checkpoint commit) | completed | 2026-03-04 14:44:35 +08:00 | pass | commit: `69ae2c2`, msg: `chore: checkpoint before portfolio refactor (full snapshot)` |
| P0-2 | Record checkpoint hash + repo state + current scope | completed | 2026-03-04 14:45:11 +08:00 | pass | `git rev-parse --short HEAD`=`69ae2c2`; `git status --short --branch`=`## main...origin/main [ahead 16]` |
| P1-1 | Converge plan in this repo and mark desktop-first scope | completed | 2026-03-04 14:45:30 +08:00 | pass | Added `Execution Scope (Converged Spec)` in this file |
| P1-2 | Add nav-highlight as explicit requirement and acceptance | completed | 2026-03-04 14:45:30 +08:00 | pass | Requirement now explicit in converged scope + acceptance checklist |
| P1-3 | Remove duplicate SVG-id fix step and keep direct chart replacement path | completed | 2026-03-04 14:45:30 +08:00 | pass | Converged scope states direct ApexCharts replacement path |
| P2-1 | Replace placeholder testimonial content with achievements section | completed | 2026-03-04 14:46:46 +08:00 | pass | Added `section#testimonial` with 4 metric cards in `index.html` |
| P2-2 | Ensure empty `alt` count is zero in `index.html` | completed | 2026-03-04 14:46:56 +08:00 | pass | check: `empty_alt 0` from python verification |
| P2-3 | Add favicon data URI in `<head>` | completed | 2026-03-04 14:46:56 +08:00 | pass | check: `favicon_data_uri True` from python verification |
| P2-4 | Add contact form (`action="#"`) for JS validation flow | completed | 2026-03-04 14:46:56 +08:00 | pass | added `form#contact-form action=\"#\"` in contact section |
| P3-1 | Add skills chart container and ApexCharts radial chart init | completed | 2026-03-04 14:48:03 +08:00 | pass | `index.html` has `id=\"skills-chart\"` + ApexCharts CDN; `script.js` contains `new ApexCharts(...)`; legacy `GradientColor`/`outer-circle` CSS removed |
| P3-2 | Redesign project cards (category strip, tags, overlay, stagger) | completed | 2026-03-04 14:49:40 +08:00 | pass | Added dynamic card metadata/tags/overlay in `script.js`; added strip/tag/overlay/stagger styles in `style.css` |
| P3-3 | Switch ScrollReveal/Typed.js CDN from unpkg to jsdelivr | completed | 2026-03-04 14:50:14 +08:00 | pass | `index.html` now uses jsdelivr URLs for ScrollReveal + Typed.js |
| P3-4 | Change `tabOpen(x)` -> `tabOpen(x, el)` and update onclick | completed | 2026-03-04 14:50:42 +08:00 | pass | `script.js` uses `function tabOpen(x, el)` and no `event.currentTarget`; all tab buttons pass `this` |
| P3-5 | Persist theme in `localStorage` (`portfolio_theme`) | completed | 2026-03-04 14:51:21 +08:00 | pass | `script.js` now uses `THEME_KEY=\"portfolio_theme\"`, applies saved theme on load, writes on toggle |
| P3-6 | Add contact form validation and success toast | completed | 2026-03-04 14:52:54 +08:00 | pass | Added `wireContactForm()` + `showToast()` in `script.js`; added `.toast` styles in `style.css`; form added as `#contact-form` |
| P3-7 | Add scrollspy nav highlight | completed | 2026-03-04 14:53:50 +08:00 | pass | Added `wireScrollSpy()` for hash sections and `.navlist li a.active` style |
| P4-1 | Add executable validation script (HTML/JS/structure checks) | completed | 2026-03-04 14:55:18 +08:00 | pass | Added `scripts/check_refactor_acceptance.py` + `package.json` script `refactor:check` |
| P4-2 | Run validation + desktop smoke checks, fill final acceptance | completed | 2026-03-04 14:56:23 +08:00 | pass | `check_refactor_acceptance.py`: all pass; `validate_links.py`: pass; Playwright smoke: `themePersisted=true`, `activeTab=webdesign`, `emptyToast=请先填写所有必填项。`, `successToast=消息已收到...`, `consoleErrors=0` |
| P5-1 | Feature commit (`feat: portfolio refactor (desktop-first)`) | in_progress |  | n/a | start: 2026-03-04 14:56:23 +08:00 |
| P5-2 | Close documentation (all statuses + final/open issues) | pending |  | n/a |  |

## Final Acceptance Checklist

- [x] No Lorem placeholder text in `index.html`.
- [x] Empty `alt` count in `index.html` is 0.
- [x] Favicon data URI exists in `<head>`.
- [x] Skills chart (`#skills-chart`) renders via ApexCharts.
- [x] Portfolio cards show category strip + tech tags + hover overlay + stagger animation.
- [x] ScrollReveal and Typed.js use jsdelivr URLs.
- [x] Theme persists after refresh (`portfolio_theme`).
- [x] Tab switching works with `tabOpen(x, el)`.
- [x] Contact form validation + toast works.
- [x] Nav highlight updates by scroll position.

## Daily Updates

### 2026-03-04

- Completed:
  - P0-1 checkpoint commit completed (`69ae2c2`).
  - P0-2 checkpoint metadata recorded (scope: desktop-first, mobile deferred).
  - P1-1~P1-3 converged scope finalized (added nav highlight + removed duplicate SVG-id step).
  - P2-1 achievements section added to `index.html`.
  - P2-2/P2-3/P2-4 passed content checks (`empty_alt=0`, no Lorem, favicon present, form action set).
  - P3-1 skills chart migrated to ApexCharts and legacy progress-ring CSS removed.
  - P3-2 portfolio cards upgraded with category strip, tags, hover overlay, stagger animation.
  - P3-3 CDN switched to jsdelivr for ScrollReveal and Typed.js.
  - P3-4 tab API updated to `tabOpen(x, el)` and button onclick synchronized.
  - P3-5 dark theme persistence implemented via `portfolio_theme`.
  - P3-6 contact form validation and toast feedback implemented.
  - P3-7 scrollspy nav highlight implemented.
  - P4-1 executable check script added (`scripts/check_refactor_acceptance.py`).
  - P4-2 validation and desktop smoke checks passed.
- Failed:
- Blockers:
- Next:
  - Create feature commit and close documentation.

## Open Issues

- None yet.
