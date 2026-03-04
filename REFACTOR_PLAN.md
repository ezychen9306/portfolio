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

## Task Tracker

| id | task | status | completed_at | acceptance | evidence |
|---|---|---|---|---|---|
| P0-1 | Full snapshot commit (`git add -A` + checkpoint commit) | in_progress |  | n/a | start: 2026-03-04 14:43:20 +08:00 |
| P0-2 | Record checkpoint hash + repo state + current scope | pending |  | n/a |  |
| P1-1 | Converge plan in this repo and mark desktop-first scope | pending |  | n/a |  |
| P1-2 | Add nav-highlight as explicit requirement and acceptance | pending |  | n/a |  |
| P1-3 | Remove duplicate SVG-id fix step and keep direct chart replacement path | pending |  | n/a |  |
| P2-1 | Replace placeholder testimonial content with achievements section | pending |  | n/a |  |
| P2-2 | Ensure empty `alt` count is zero in `index.html` | pending |  | n/a |  |
| P2-3 | Add favicon data URI in `<head>` | pending |  | n/a |  |
| P2-4 | Add contact form (`action="#"`) for JS validation flow | pending |  | n/a |  |
| P3-1 | Add skills chart container and ApexCharts radial chart init | pending |  | n/a |  |
| P3-2 | Redesign project cards (category strip, tags, overlay, stagger) | pending |  | n/a |  |
| P3-3 | Switch ScrollReveal/Typed.js CDN from unpkg to jsdelivr | pending |  | n/a |  |
| P3-4 | Change `tabOpen(x)` -> `tabOpen(x, el)` and update onclick | pending |  | n/a |  |
| P3-5 | Persist theme in `localStorage` (`portfolio_theme`) | pending |  | n/a |  |
| P3-6 | Add contact form validation and success toast | pending |  | n/a |  |
| P3-7 | Add scrollspy nav highlight | pending |  | n/a |  |
| P4-1 | Add executable validation script (HTML/JS/structure checks) | pending |  | n/a |  |
| P4-2 | Run validation + desktop smoke checks, fill final acceptance | pending |  | n/a |  |
| P5-1 | Feature commit (`feat: portfolio refactor (desktop-first)`) | pending |  | n/a |  |
| P5-2 | Close documentation (all statuses + final/open issues) | pending |  | n/a |  |

## Final Acceptance Checklist

- [ ] No Lorem placeholder text in `index.html`.
- [ ] Empty `alt` count in `index.html` is 0.
- [ ] Favicon data URI exists in `<head>`.
- [ ] Skills chart (`#skills-chart`) renders via ApexCharts.
- [ ] Portfolio cards show category strip + tech tags + hover overlay + stagger animation.
- [ ] ScrollReveal and Typed.js use jsdelivr URLs.
- [ ] Theme persists after refresh (`portfolio_theme`).
- [ ] Tab switching works with `tabOpen(x, el)`.
- [ ] Contact form validation + toast works.
- [ ] Nav highlight updates by scroll position.

## Daily Updates

### 2026-03-04

- Completed:
- Failed:
- Blockers:
- Next:

## Open Issues

- None yet.
