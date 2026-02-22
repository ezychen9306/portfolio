// generate_icons.js
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const outDir = path.join(__dirname);

function iconHtml(size){
  const bg = '#6b8e9f', accent = '#c9a227', txt = '#ffffff';
  const r = Math.round(size*0.16);
  const fontSize = Math.round(size*0.48);
  return `<!doctype html><meta charset=utf-8>
  <style>
  html,body{margin:0;padding:0;background:transparent}
  .icon{position:relative;width:${size}px;height:${size}px;display:flex;align-items:center;justify-content:center;
        background:${bg};border-radius:${r}px;box-shadow:0 0 0 ${Math.max(2,Math.round(size*0.04))}px ${accent} inset}
  .txt{font: ${fontSize}px/1.0 system-ui,-apple-system,Segoe UI,Roboto,Ubuntu,'Microsoft Yahei',sans-serif; 
       color:${txt};font-weight:900;letter-spacing:.02em}
  </style>
  <div class=icon><div class=txt>EZ</div></div>`;
}

(async()=>{
  const browser = await chromium.launch();
  const page = await browser.newPage();
  const sizes = [16,32,180,192,512];
  for (const s of sizes){
    await page.setViewportSize({ width:s, height:s });
    await page.setContent(iconHtml(s), { waitUntil:'load' });
    const file = s===180? 'apple-touch-icon.png' : (s===16? 'favicon-16x16.png' : (s===32? 'favicon-32x32.png' : `android-chrome-${s}x${s}.png`));
    await page.screenshot({ path: path.join(outDir, file) });
    console.log('wrote', file);
  }
  await browser.close();
  // manifest
  const manifest = {
    name: "Ezy Portfolio",
    short_name: "Portfolio",
    icons: [
      { src: "android-chrome-192x192.png", sizes: "192x192", type: "image/png" },
      { src: "android-chrome-512x512.png", sizes: "512x512", type: "image/png" }
    ],
    theme_color: "#6b8e9f",
    background_color: "#f7f4ef",
    display: "standalone"
  };
  fs.writeFileSync(path.join(outDir,'site.webmanifest'), JSON.stringify(manifest,null,2));
})();
