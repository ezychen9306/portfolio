# Git 设置指南

## 前提条件

确保已安装 Git：
- Windows: 下载并安装 [Git for Windows](https://git-scm.com/download/win)
- 安装后重启终端或 IDE

## 1. 初始化 Portfolio 项目

```bash
# 进入 portfolio 目录
cd portfolio

# 初始化 Git
git init

# 添加所有文件
git add .

# 提交
git commit -m "Initial commit: Portfolio website"

# 创建 GitHub 仓库后，添加远程仓库（替换 yourusername）
git remote add origin https://github.com/yourusername/portfolio.git

# 推送到 GitHub
git branch -M main
git push -u origin main
```

## 2. 初始化整个 AI_agents 项目

```bash
# 返回项目根目录
cd ..

# 初始化 Git（如果还没有）
git init

# 添加所有文件
git add .

# 提交
git commit -m "Initial commit: AI Agents workspace"

# 创建 GitHub 仓库后，添加远程仓库（替换 yourusername）
git remote add origin https://github.com/yourusername/AI_agents.git

# 推送到 GitHub
git branch -M main
git push -u origin main
```

## 注意事项

1. **大文件处理**：如果项目中有大文件（>100MB），考虑使用 Git LFS：
   ```bash
   git lfs install
   git lfs track "*.xlsx"
   git lfs track "*.mp4"
   ```

2. **敏感信息**：确保 `.gitignore` 已排除敏感文件（API keys、密码等）

3. **GitHub 仓库设置**：
   - Portfolio: 设置为 Public 以启用 GitHub Pages
   - AI_agents: 可根据需要设置为 Public 或 Private

## 快速检查 Git 是否安装

```bash
git --version
```

如果显示版本号，说明 Git 已安装。
