/**
 * 本地打开 portfolio 并截图为 screenshot.png
 * 使用：先 npm install playwright，再 node screenshot.js
 * 首次运行若提示安装浏览器：npx playwright install chromium
 */
const path = require("path");
const { chromium } = require("playwright");

const indexUrl = "file://" + path.join(__dirname, "index.html").replace(/\\/g, "/");
const outPath = path.join(__dirname, "screenshot.png");

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  await page.setViewportSize({ width: 1280, height: 900 });
  await page.goto(indexUrl, { waitUntil: "networkidle" });
  await page.screenshot({ path: outPath, fullPage: true });
  await browser.close();
  console.log("截图已保存: " + outPath);
})().catch((err) => {
  console.error(err);
  process.exit(1);
});
