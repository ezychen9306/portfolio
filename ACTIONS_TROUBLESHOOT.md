# 🔧 Actions 问题排查

## 常见情况

### 情况 1: Actions 页面为空（没有任务）

**原因**：Pages 还没配置，或者配置后没有触发构建

**解决**：
1. 进入 Pages 设置：https://github.com/Enzhao-Chen/portfolio/settings/pages
2. 确保配置：
   - Source: `Deploy from a branch`
   - Branch: `main`
   - Folder: `/ (root)`
3. 点击 Save
4. 如果已经配置，尝试重新保存：
   - 先改成 `None`，Save
   - 再改回 `main` + `/ (root)`，Save

### 情况 2: 有任务但显示 "No workflow runs"

**原因**：GitHub Actions 可能被禁用

**解决**：
1. 进入仓库 Settings
2. 找到 "Actions" → "General"
3. 确保 "Allow all actions and reusable workflows" 已启用
4. 保存后重新配置 Pages

### 情况 3: 任务运行中但很久没完成

**原因**：构建需要时间，或者卡住了

**解决**：
- 正常构建需要 1-3 分钟
- 如果超过 5 分钟，可以取消并重新触发

### 情况 4: 任务失败

**原因**：配置错误或文件问题

**解决**：
1. 点击失败的任务查看错误信息
2. 常见错误：
   - 文件路径不对 → 确保 `index.html` 在根目录
   - 仓库不是 Public → 改为 Public
   - 构建超时 → 重新触发

## 📋 快速检查

请告诉我 Actions 页面显示什么：

- [ ] 完全空白（没有任何任务）
- [ ] 显示 "No workflow runs"
- [ ] 有任务但状态是运行中
- [ ] 有任务但状态是失败
- [ ] 有任务且状态是成功

## 🎯 最可能的情况

如果 Actions 页面是空的，说明 Pages 还没正确配置。

**立即执行**：
1. 访问：https://github.com/Enzhao-Chen/portfolio/settings/pages
2. 配置 Source = `Deploy from a branch`, Branch = `main`, Folder = `/ (root)`
3. 点击 Save
4. 等待 1-2 分钟
5. 刷新 Actions 页面，应该能看到构建任务
