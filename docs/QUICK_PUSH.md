# ⚡ 快速推送指南

## 方法一：使用 GitHub CLI（如果已安装）

```powershell
cd d:\AI_agents\portfolio
gh repo create portfolio --public --source=. --remote=origin --push
```

## 方法二：手动推送（推荐）

### 1. 确保仓库已创建

访问：https://github.com/new
- 仓库名：`portfolio`
- Public
- 不要初始化任何文件

### 2. 推送代码

```powershell
cd d:\AI_agents\portfolio
git push -u origin main
```

如果要求认证：
- Username: `ezychen9306`
- Password: 使用 Personal Access Token

### 3. 启用 Pages

访问：https://github.com/ezychen9306/portfolio/settings/pages
- Source: `main` branch, `/ (root)`
- Save

### 4. 访问网站

等待 1-2 分钟后访问：
**https://ezychen9306.github.io/portfolio/**

## 方法三：使用 GitHub Desktop（图形界面）

1. 下载：https://desktop.github.com/
2. 登录 GitHub
3. File → Add Local Repository → 选择 `d:\AI_agents\portfolio`
4. Publish repository
5. 在 GitHub 上启用 Pages
