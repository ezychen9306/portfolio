# 简历

- **在线简历**：作品集导航中「简历」指向独立 CV 页 `cv.html`。
- **PDF**：请将 **风险策略_陈恩昭.pdf** 放入本目录。放入后，可在 cv 页或首页增加「下载简历」链接指向：`resume/风险策略_陈恩昭.pdf`。

## 让 AI 读你简历（提取 PDF 文字）

- **优先用 OpenSkills 的 pdf skill**：已安装（`npx openskills install anthropics/skills`），AI 会按该 skill 用 pypdf/pdfplumber 提取 PDF 文本。把简历 PDF 放到本目录（如 `风险策略_陈恩昭.pdf`），再说「读我简历 / 把简历内容合并到 cv」即可。
- **备用**：本目录下有 **`extract_resume_text.py`**，使用项目内 `15_skills_library/local/pdf_processor`，运行后会生成 **`简历_提取文本.txt`**，AI 也可读该 txt 做合并。
