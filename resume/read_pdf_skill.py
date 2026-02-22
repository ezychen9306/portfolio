#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""用 OpenSkills pdf skill 方式（pypdf）提取本目录下 PDF 全文，并写入 resume_text.txt（UTF-8）。"""
import sys
from pathlib import Path
from pypdf import PdfReader

dir_path = Path(__file__).resolve().parent
pdfs = list(dir_path.glob("*.pdf"))
if not pdfs:
    print("NO_PDF_FOUND", file=sys.stderr)
    exit(1)
reader = PdfReader(str(pdfs[0]))
text = []
for page in reader.pages:
    text.append(page.extract_text() or "")
out_path = dir_path / "resume_text.txt"
out_path.write_text("\n\n".join(text), encoding="utf-8")
print("OK", out_path)
