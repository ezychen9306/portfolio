# Filesystem Constitution (Portfolio)

Purpose: ensure web-served paths are ASCII-only and URL-safe to avoid 404/encoding issues across platforms.

Rules
- Charset: ASCII only in file and directory names (a–z, 0–9, `-`, `_`, `.`).
- Case: lowercase only.
- Spaces/parentheses: not allowed. Use hyphens (`-`).
- Extensions: keep original (e.g. `.png`, `.html`).
- Served scope: only applies to `assets/`, `demos/`, `resume/`, and root files `index.html`, `cv.html`.
- Non-served folders (`.git`, `node_modules`, `docs`, etc.) are exempt.

Automation
- Check: `python scripts/fs_ascii_guard.py` (non‑zero exit on violations)
- Fix: `python scripts/fs_ascii_guard.py --fix` (renames + updates references in HTML/CSS/JS)

Notes
- For non‑ASCII originals (e.g. 中文文件名), the fix will slugify and ensure uniqueness.
- After a fix, always run: `npm run preflight`.
