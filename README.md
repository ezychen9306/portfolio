# Portfolio - 个人作品集

**归属**：本仓库中为 Report Agent 子项目，路径 `21_Report_Agent/05_portfolio`。

数据分析师 & AI Agent 开发者的个人作品集网站。

## 功能特点

- ✨ 现代化响应式设计
- 🎨 平滑滚动与动画效果
- 📱 移动端完美适配
- 🚀 纯静态 HTML，无需后端
- ⚡ 快速加载，性能优化

## 项目结构

```
portfolio/
├── index.html          # 主页面
├── README.md          # 项目说明
└── .gitignore         # Git 忽略文件
```

## 本地预览

直接在浏览器中打开 `index.html` 文件即可预览。

或者使用 Python 简单服务器：

```bash
# Python 3
python -m http.server 8000

# Python 2
python -m SimpleHTTPServer 8000
```

然后在浏览器访问：http://localhost:8000

## 部署到 GitHub Pages

### 方法一：使用 GitHub Pages（推荐）

1. **创建 GitHub 仓库**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Portfolio website"
   git branch -M main
   git remote add origin https://github.com/ezychen9306/portfolio.git
   git push -u origin main
   ```

2. **启用 GitHub Pages**
   - 进入仓库 Settings
   - 找到 Pages 选项
   - Source 选择 `main` 分支
   - 选择 `/ (root)` 目录
   - 点击 Save

3. **访问网站**
   - 几分钟后，你的网站将在以下地址可用：
   - `https://ezychen9306.github.io/portfolio/`

### 方法二：使用 gh-pages 分支

```bash
# 创建 gh-pages 分支
git checkout -b gh-pages
git push origin gh-pages

# 在仓库 Settings > Pages 中选择 gh-pages 分支
```

### 方法三：使用 GitHub Actions 自动部署

创建 `.github/workflows/deploy.yml`：

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Deploy
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./portfolio
```

## 自定义内容

### 更新联系信息

编辑 `index.html`，找到联系部分（约第 400 行）：

```html
<a href="mailto:your.email@example.com" class="contact-link">
<a href="https://github.com/ezychen9306" class="contact-link">
<a href="https://linkedin.com/in/yourprofile" class="contact-link">
```

### 添加/修改项目

在 Projects Section 中添加新的项目卡片：

```html
<div class="project-card">
  <span class="project-category">分类</span>
  <h3 class="project-title">项目名称</h3>
  <p class="project-desc">项目描述</p>
  <div class="project-tech">
    <span class="tech-tag">技术1</span>
    <span class="tech-tag">技术2</span>
  </div>
  <div class="project-impact">📊 项目影响</div>
</div>
```

### 修改配色方案

编辑 `index.html` 的 CSS 变量（约第 15 行）：

```css
:root {
  --bg: #FAFAFA;           /* 背景色 */
  --ink: #09090B;          /* 文字色 */
  --accent: #EC4899;       /* 强调色 */
  --accent-hover: #DB2777; /* 悬停色 */
}
```

## 技术栈

- HTML5
- CSS3 (CSS Variables, Flexbox, Grid)
- Vanilla JavaScript
- Iconify Icons
- Google Fonts (Inter, Libre Baskerville)

## 浏览器支持

- Chrome (最新版)
- Firefox (最新版)
- Safari (最新版)
- Edge (最新版)

## 性能优化

- ✅ 使用 CSS 变量，易于主题切换
- ✅ 内联关键 CSS
- ✅ 使用 CDN 加载字体和图标
- ✅ 响应式图片（如需要）
- ✅ 平滑滚动优化

## 许可证

MIT License - 可自由使用和修改

## 更新日志

### v1.0.0 (2026-02-10)
- ✨ 初始版本
- ✨ 9 个精选项目展示
- ✨ 响应式设计
- ✨ 平滑滚动与动画效果

## 本地命令

- 构建（生成 demos/index.html 与项目卡片，刷新首页截图）：
  ```bash
  npm run build
  ```
- 校验（检查 projects.json 的链接与配图是否存在、分类是否合法）：
  ```bash
  npm run validate
  ```
- 本地预览：直接双击 `index.html` 即可。

## 数据驱动

- 项目清单：`assets/data/projects.json`
- 封面图片：`assets/images/projects/`
- Demo 目录：`demos/<项目目录>/`（支持 `README.md` 或 `demo.html`，构建时生成 `index.html`）