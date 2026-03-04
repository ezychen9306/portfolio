#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
浠庢湰鐩綍鐨勭畝鍘?PDF 鎻愬彇鍏ㄦ枃锛岃緭鍑轰负 绠€鍘哶鎻愬彇鏂囨湰.txt锛屼究浜庡悎骞跺埌 cv 鎴栫粰 AI 璇诲彇銆?
浣跨敤椤圭洰鍐?15_skills_library/local/pdf_processor銆?
"""
import sys
from pathlib import Path

# 椤圭洰鏍癸細resume 鍦?21_Report_Projects/05_portfolio/resume 鈫?鍥為€€ 3 绾у埌 AI_agents
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent.parent.parent
LOCAL_SKILLS = REPO_ROOT / "15_skills_library" / "local"
sys.path.insert(0, str(LOCAL_SKILLS))

def main():
    pdf_dir = SCRIPT_DIR
    pdf_name = "椋庨櫓绛栫暐_闄堟仼鏄?pdf"
    pdf_path = pdf_dir / pdf_name
    if not pdf_path.exists():
        # 灏濊瘯鏈洰褰曚笅浠绘剰 PDF
        pdfs = list(pdf_dir.glob("*.pdf"))
        if not pdfs:
            print(f"鏈壘鍒?{pdf_name}锛屼篃鏈壘鍒板叾浠?PDF銆傝灏嗙畝鍘?PDF 鏀惧叆锛歿pdf_dir}")
            return 1
        pdf_path = pdfs[0]
        print(f"浣跨敤 PDF锛歿pdf_path.name}")

    try:
        from pdf_processor import process_pdf
    except ImportError:
        print("璇峰厛瀹夎 PyPDF2锛歱ip install PyPDF2")
        print("骞跺湪椤圭洰鏍圭洰褰曟墽琛屾湰鑴氭湰锛屾垨纭繚 15_skills_library/local 鍙瀵煎叆銆?)
        return 1

    out_path = pdf_dir / "绠€鍘哶鎻愬彇鏂囨湰.txt"
    result = process_pdf("extract_text", {"file_path": str(pdf_path)})

    if not result.get("success"):
        print("鎻愬彇澶辫触锛?, result.get("error", result))
        return 1

    text = result.get("result", {}).get("full_text", "")
    if not text or not text.strip():
        print("鎻愬彇缁撴灉涓虹┖锛屽彲鑳芥槸鎵弿鐗?PDF 鎴栭渶 OCR銆?)
        return 1

    out_path.write_text(text, encoding="utf-8")
    print(f"宸插啓鍏ワ細{out_path}锛坽len(text)} 瀛楋級")
    return 0

if __name__ == "__main__":
    sys.exit(main())

