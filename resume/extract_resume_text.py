#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
从本目录的简历 PDF 提取全文，输出为 简历_提取文本.txt，便于合并到 cv 或给 AI 读取。
使用项目内 15_skills_library/local/pdf_processor。
"""
import sys
from pathlib import Path

# 项目根：resume 在 21_Report_Agent/05_portfolio/resume → 回退 3 级到 AI_agents
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent.parent.parent
LOCAL_SKILLS = REPO_ROOT / "15_skills_library" / "local"
sys.path.insert(0, str(LOCAL_SKILLS))

def main():
    pdf_dir = SCRIPT_DIR
    pdf_name = "风险策略_陈恩昭.pdf"
    pdf_path = pdf_dir / pdf_name
    if not pdf_path.exists():
        # 尝试本目录下任意 PDF
        pdfs = list(pdf_dir.glob("*.pdf"))
        if not pdfs:
            print(f"未找到 {pdf_name}，也未找到其他 PDF。请将简历 PDF 放入：{pdf_dir}")
            return 1
        pdf_path = pdfs[0]
        print(f"使用 PDF：{pdf_path.name}")

    try:
        from pdf_processor import process_pdf
    except ImportError:
        print("请先安装 PyPDF2：pip install PyPDF2")
        print("并在项目根目录执行本脚本，或确保 15_skills_library/local 可被导入。")
        return 1

    out_path = pdf_dir / "简历_提取文本.txt"
    result = process_pdf("extract_text", {"file_path": str(pdf_path)})

    if not result.get("success"):
        print("提取失败：", result.get("error", result))
        return 1

    text = result.get("result", {}).get("full_text", "")
    if not text or not text.strip():
        print("提取结果为空，可能是扫描版 PDF 或需 OCR。")
        return 1

    out_path.write_text(text, encoding="utf-8")
    print(f"已写入：{out_path}（{len(text)} 字）")
    return 0

if __name__ == "__main__":
    sys.exit(main())
