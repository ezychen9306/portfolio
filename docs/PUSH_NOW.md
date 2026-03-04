# 🚀 Portfolio 推送指南 - 立即执行

## 步骤 1: 创建 GitHub 仓库（2 分钟）

1. **访问 GitHub 创建页面**
   - 打开：https://github.com/new

2. **填写仓库信息**
   - Repository name: `portfolio`（必须完全一致）
   - Description: `Personal portfolio website`
   - **选择 Public**（必须，才能使用 GitHub Pages）
   - **不要勾选** "Initialize this repository with a README"
   - **不要勾选** "Add .gitignore"
   - **不要勾选** "Choose a license"

3. **创建仓库**
   - 点击绿色的 `Create repository` 按钮

## 步骤 2: 推送代码（1 分钟）

在 PowerShell 中执行以下命令：

```powershell
cd d:\AI_agents\21_Report_Projects\05_portfolio

# 如果之前添加过远程仓库，先删除（没有可忽略报错）
git remote remove origin

# 添加远程仓库
git remote add origin https://github.com/ezychen9306/portfolio.git

# 确保分支是 main
git branch -M main

# 推送到 GitHub
git push -u origin main
```

### 🔐 如果要求输入用户名和密码

**用户名**：`ezychen9306`

**密码**：使用 Personal Access Token（不是 GitHub 密码）

#### 如何获取 Token：

1. 访问：https://github.com/settings/tokens
2. 点击 `Generate new token` → `Generate new token (classic)`
3. 填写：
   - Note: `Portfolio Push`
   - Expiration: `90 days` 或 `No expiration`
   - 勾选 `repo` 权限（会自动勾选所有子权限）
4. 点击 `Generate token`
5. **复制 token**（只显示一次！类似：`ghp_xxxxxxxxxxxxx`）
6. 在推送时，密码处粘贴这个 token

## 步骤 3: 启用 GitHub Pages（1 分钟）

推送成功后：

1. **进入仓库页面**
   - 访问：https://github.com/ezychen9306/portfolio

2. **打开 Settings**
   - 点击仓库页面顶部的 `Settings` 标签

3. **找到 Pages 选项**
   - 左侧菜单向下滚动，找到 `Pages`

4. **配置 Pages**
   - Source: 选择 `Deploy from a branch`
   - Branch: 选择 `main`
   - Folder: 选择 `/ (root)`
   - 点击 `Save`

5. **等待部署**
   - 等待 1-2 分钟
   - 页面会显示：`Your site is live at https://ezychen9306.github.io/portfolio/`

## 🌐 你的网站地址

推送并启用 Pages 后，你的网站将在：

**https://ezychen9306.github.io/portfolio/**

## ✅ 验证

1. 推送成功后，访问：https://github.com/ezychen9306/portfolio
2. 应该能看到你的文件（index.html, README.md 等）
3. 启用 Pages 后，访问上面的网址，应该能看到你的作品集网站

## 🆘 遇到问题？

### 推送失败：仓库不存在
- 确保已创建 `portfolio` 仓库
- 仓库名必须完全一致：`portfolio`

### 推送失败：认证错误
- 使用 Personal Access Token 代替密码
- 确保 token 有 `repo` 权限

### Pages 显示 404
- 等待 2-3 分钟让 GitHub 完成构建
- 检查仓库是否为 Public
- 检查 Pages 设置是否正确

### 网站显示但样式丢失
- 检查文件路径是否正确
- 确保所有文件都已推送

## 📝 后续更新

更新网站内容后：

```powershell
cd d:\AI_agents\21_Report_Projects\05_portfolio

git add .
git commit -m "Update: 描述你的更改"
git push
```

GitHub Pages 会自动更新（通常 1-2 分钟）。