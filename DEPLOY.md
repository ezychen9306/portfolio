# 部署指南 - GitHub Pages

## 快速部署步骤

### 1. 准备 Git 仓库

```bash
# 在 portfolio 目录下初始化 Git
cd portfolio
git init

# 添加所有文件
git add .

# 提交
git commit -m "Initial commit: Portfolio website"
```

### 2. 创建 GitHub 仓库并推送

1. 在 GitHub 上创建一个新仓库（例如：`portfolio`）
2. 不要初始化 README、.gitignore 或 license（我们已经有了）

3. 连接本地仓库到 GitHub：

```bash
# 添加远程仓库（替换 yourusername 为你的 GitHub 用户名）
git remote add origin https://github.com/yourusername/portfolio.git

# 重命名分支为 main（如果还没有）
git branch -M main

# 推送代码
git push -u origin main
```

### 3. 启用 GitHub Pages

1. 进入你的 GitHub 仓库页面
2. 点击 **Settings**（设置）
3. 在左侧菜单找到 **Pages**
4. 在 **Source** 部分：
   - 选择 **Deploy from a branch**
   - Branch 选择 **main**
   - Folder 选择 **/ (root)**
   - 点击 **Save**

5. 等待几分钟，GitHub 会构建你的网站
6. 访问：`https://yourusername.github.io/portfolio/`

## 更新网站

每次修改后，只需：

```bash
git add .
git commit -m "Update portfolio content"
git push
```

GitHub Pages 会自动重新部署（通常需要 1-2 分钟）。

## 自定义域名（可选）

如果你想使用自己的域名（例如：`portfolio.yourname.com`）：

1. 在仓库 Settings > Pages 中，找到 **Custom domain**
2. 输入你的域名
3. 在你的域名 DNS 设置中添加 CNAME 记录：
   ```
   Type: CNAME
   Name: portfolio (或 @)
   Value: yourusername.github.io
   ```

## 常见问题

### Q: 网站显示 404？
A: 检查：
- 仓库是否设置为 Public（免费账户）
- Pages 设置是否正确
- 等待几分钟让 GitHub 完成构建

### Q: 样式丢失？
A: 确保所有资源路径都是相对路径（已正确设置）

### Q: 如何查看构建日志？
A: 在仓库页面点击 **Actions** 标签，可以看到 Pages 的构建状态

## 其他部署选项

### Vercel（推荐，更快的部署）

1. 访问 [vercel.com](https://vercel.com)
2. 使用 GitHub 账号登录
3. 导入你的 `portfolio` 仓库
4. 点击 Deploy（无需配置）
5. 几分钟后即可访问

### Netlify

1. 访问 [netlify.com](https://netlify.com)
2. 拖拽 `portfolio` 文件夹到 Netlify
3. 或连接 GitHub 仓库自动部署

### Cloudflare Pages

1. 访问 Cloudflare Dashboard
2. 选择 Pages > Create a project
3. 连接 GitHub 仓库
4. 构建命令留空，输出目录：`/`
5. 部署

## 性能优化建议

部署后可以：

1. **添加 favicon**：在 `<head>` 中添加：
   ```html
   <link rel="icon" type="image/x-icon" href="/favicon.ico">
   ```

2. **启用 HTTPS**：GitHub Pages 自动提供 HTTPS

3. **添加 meta 标签**：已在 HTML 中包含基本 SEO 标签

4. **压缩图片**：如果添加图片，使用 WebP 格式并压缩
