// ============== MENU NAVBAR ================
const navlist = document.querySelector(".navlist");
// Respect user motion preference
const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
const menuBtn = document.querySelector(".ri-menu-line");

menuBtn.onclick = function () {
  navlist.classList.toggle("active");
  menuBtn.classList.toggle("ri-arrow-up-double-line");
};

// ============== STICKY NAVBAR ================
window.addEventListener("scroll", () => {
  document.querySelector("nav").classList.toggle("scrolling", scrollY > 50);
});

function wireScrollSpy() {
  const navAnchors = [...document.querySelectorAll(".navlist a[href^='#']")];
  const sectionPairs = navAnchors
    .map((link) => ({ link, section: document.querySelector(link.getAttribute("href")) }))
    .filter((pair) => pair.section);
  if (!sectionPairs.length) return;

  function updateActiveNav() {
    const marker = window.scrollY + 140;
    let active = sectionPairs[0];
    for (const pair of sectionPairs) {
      if (pair.section.offsetTop <= marker) {
        active = pair;
      }
    }
    sectionPairs.forEach((pair) => pair.link.classList.remove("active"));
    active.link.classList.add("active");
  }

  window.addEventListener("scroll", updateActiveNav, { passive: true });
  updateActiveNav();
}

// ============== 社交图标：悬停展开后不收回，点击文案区域才收起 ================
document.querySelectorAll(".home .social-icon-item").forEach((item) => {
  item.addEventListener("mouseenter", () => item.classList.add("is-expanded"));
  item.querySelectorAll(".social-icon-label").forEach((label) => {
    label.addEventListener("click", (e) => {
      e.preventDefault();
      item.classList.remove("is-expanded");
    });
  });
});

// ============== PORTFOLIO TABS ================
let portfolioTabs = document.getElementsByClassName("portfolio-tab");
let tabContents = document.getElementsByClassName("tab-content");

const PROJECT_META = {
  "demos/01_disaster_management/index.html": { category: "risk", tags: ["策略", "应急", "风控"], summary: "T+1 响应机制，灾难场景风险快速收敛。" },
  "demos/02_quota_strategy_v5/index.html": { category: "risk", tags: ["额度", "模型", "策略"], summary: "弹性曲线与安全边界结合，规模增长与风险平衡。" },
  "demos/03_rm_system/summary.html": { category: "risk", tags: ["经营", "监控", "报表"], summary: "统一经营与风险视图，支持审计与财报汇总。" },
  "demos/04_ai_deep_strategy/index.html": { category: "risk", tags: ["AI", "分群", "实验"], summary: "以 AI 策略缩短迭代周期并提升效果可解释性。" },
  "demos/05_kyc_platform/index.html": { category: "risk", tags: ["KYC", "分配", "转化"], summary: "客群与座席协同分发，提升经营效率与转化率。" },
  "demos/06_telesales_system/index.html": { category: "risk", tags: ["电销", "推荐", "转化"], summary: "策略驱动的电销推荐，提升触达质量与转化。" },
  "../02_2025end_report/2025_year_end_report_package/outputs/2025_year_end_report.html": { category: "data", tags: ["复盘", "汇报", "指标"], summary: "年度成果与策略演进全景复盘。" },
  "../03_ai_internal_sharing/old_customer_weekly_report/202601_W5/outputs/【菲律宾老客】周报_20260130_v1_在线版.html": { category: "data", tags: ["周报", "监控", "自动化"], summary: "目标追踪、异常识别与图表自动生成闭环。" },
  "demos/13_knowledge_base_agent/index.html": { category: "ai", tags: ["RAG", "检索", "知识库"], summary: "结构化知识检索与回答，支撑高频问答场景。" },
  "demos/14_skills_development/index.html": { category: "ai", tags: ["Skills", "规范", "效率"], summary: "能力模板化沉淀，提升团队复用效率。" },
  "../03_ai_internal_sharing/03_analysis_reports/01_overview/ai_internal_sharing_ezy_creative.html": { category: "ai", tags: ["分享", "赋能", "协同"], summary: "AI 能力传播与组织协同实践沉淀。" },
  "demos/10_fof_system/index.html": { category: "ai", tags: ["投顾", "配置", "资产"], summary: "智能配置策略在投顾场景中的业务落地。" },
};

function applyCardStagger(tabId) {
  const active = document.getElementById(tabId);
  if (!active) return;
  [...active.querySelectorAll("a.image")].forEach((card, idx) => {
    card.style.setProperty("--stagger-index", idx);
  });
}

function enhancePortfolioCards() {
  const cards = document.querySelectorAll(".portfolio .tab-content a.image");
  cards.forEach((card) => {
    const href = card.getAttribute("href") || "";
    const meta = PROJECT_META[href];
    const category = (meta && meta.category) || "risk";
    const tags = (meta && meta.tags) || ["项目", "策略"];
    const summary = (meta && meta.summary) || "项目详情可在演示页查看。";
    const iconMap = { risk: "ri-line-chart-line", data: "ri-database-2-line", ai: "ri-robot-2-line" };
    const labelMap = { risk: "风控/经营", data: "数据/报表", ai: "AI Agent" };

    card.classList.add("portfolio-card");
    card.dataset.category = category;

    const media = card.querySelector(".portfolio-card__media");
    if (media && !media.querySelector(".portfolio-card__overlay")) {
      const overlay = document.createElement("div");
      overlay.className = "portfolio-card__overlay";
      overlay.innerHTML = `<p>${summary}</p>`;
      media.appendChild(overlay);
    }

    const caption = card.querySelector(".portfolio-card__caption");
    if (caption && !caption.querySelector(".portfolio-card__tags")) {
      const tagsEl = document.createElement("div");
      tagsEl.className = "portfolio-card__tags";
      tagsEl.innerHTML = tags.map((tag) => `<span class="portfolio-card__tag">${tag}</span>`).join("");
      const metaEl = document.createElement("div");
      metaEl.className = "portfolio-card__meta";
      metaEl.innerHTML = `<span><i class="${iconMap[category]}"></i> ${labelMap[category]}</span><i class="ri-arrow-right-up-line"></i>`;
      caption.appendChild(tagsEl);
      caption.appendChild(metaEl);
    }
  });
}

function showToast(message, tone = "success") {
  const oldToast = document.querySelector(".toast");
  if (oldToast) oldToast.remove();
  const toast = document.createElement("div");
  toast.className = `toast toast--${tone}`;
  toast.textContent = message;
  document.body.appendChild(toast);
  requestAnimationFrame(() => toast.classList.add("is-visible"));
  setTimeout(() => {
    toast.classList.remove("is-visible");
    setTimeout(() => toast.remove(), 220);
  }, 3000);
}

function wireContactForm() {
  const form = document.getElementById("contact-form");
  if (!form) return;
  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const required = [...form.querySelectorAll("[required]")];
    const missing = required.find((el) => !String(el.value || "").trim());
    if (missing) {
      showToast("请先填写所有必填项。", "error");
      missing.focus();
      return;
    }

    const emailInput = form.querySelector("input[type='email']");
    const email = String(emailInput?.value || "").trim();
    const emailOk = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
    if (!emailOk) {
      showToast("邮箱格式不正确，请检查后重试。", "error");
      emailInput?.focus();
      return;
    }

    showToast("消息已收到，我会尽快与你联系。", "success");
    form.reset();
  });
}

function tabOpen(x, el) {
  for (const portfolioTab of portfolioTabs) {
    portfolioTab.classList.remove("active");
  }
  for (const tabContent of tabContents) {
    tabContent.classList.remove("active-content");
  }
  if (el) {
    el.classList.add("active");
  }
  document.getElementById(x).classList.add("active-content");
  applyCardStagger(x);
}

// ============== DARK THEME================
let themeBtn = document.querySelector("#theme-btn");
const THEME_KEY = "portfolio_theme";

function applyTheme(mode) {
  const dark = mode === "dark";
  document.body.classList.toggle("active", dark);
  themeBtn.classList.toggle("ri-sun-line", dark);
  themeBtn.classList.toggle("ri-moon-line", !dark);
}

if (themeBtn) {
  const savedTheme = localStorage.getItem(THEME_KEY) || "light";
  applyTheme(savedTheme);
  themeBtn.onclick = function () {
    const nextMode = document.body.classList.contains("active") ? "light" : "dark";
    applyTheme(nextMode);
    localStorage.setItem(THEME_KEY, nextMode);
  };
}

// ============== TYPED JS（首页已改为与简历一致，无打字元素时跳过）==============
const multipleTextEl = document.querySelector(".multiple-text");
if (multipleTextEl) {
  const typed = new Typed(".multiple-text", {
    strings: ['贷中风控策略负责人', 'AI 策略专家', 'AI Agent 开发者'],
    typeSpeed: 100,
    backSpeed: 100,
    backDelay: 1000,
    loop: true,
  });
}

// ============== SCROLL REVEAL ANIMATION ================
// 初始半透明 + 提前触发，避免滚动时出现大片空白
if(!reduceMotion){
const sr = ScrollReveal({
  distance: "60px",
  duration: 1000,
  delay: 80,
  reset: true,
  opacity: 0.2,
  viewOffset: { top: -120, right: 0, bottom: 0, left: 0 },
});

sr.reveal(".home-container h3", { origin: "top" });
sr.reveal(".home-container h1", { origin: "left" });
sr.reveal(".home-container p", { origin: "left" });
sr.reveal(".home-container .right", { origin: "right" });
sr.reveal(".social-icons-container", { origin: "right" });
sr.reveal(".about-container .title", { origin: "right" });
sr.reveal(".about-container h3", { origin: "bottom" });
sr.reveal(".about-container p", { origin: "bottom" });
sr.reveal(".about-container .left", { origin: "left" });
sr.reveal(".about-container .right", { origin: "right" });
sr.reveal(".portfolio-container", { origin: "bottom" });
sr.reveal(".portfolio .title", { origin: "top" });
sr.reveal(".portfolio-buttons", { origin: "left" });
sr.reveal(".testimonial .title", { origin: "right" });
sr.reveal(".achievements-intro", { origin: "bottom" });
sr.reveal(".achievements-grid", { origin: "bottom" });
sr.reveal(".achievements-evidence", { origin: "bottom" });
sr.reveal(".contact .title", { origin: "top" });
sr.reveal(".contact .row .box", { origin: "right" });
sr.reveal(".contact .row .contact-form", { origin: "left" });
}

// ============== 首页粒子网络动画（增强版）================
(function () {
  const canvas = document.getElementById("particleCanvas");
  if (!canvas) return;
  const ctx = canvas.getContext("2d");
  let w, h, particles, mouse, t = 0;
  const PARTICLE_COUNT = 150;
  const CONNECT_DIST = 120;
  const MOUSE_DIST = 150;

  function resize() {
    const rect = canvas.parentElement.getBoundingClientRect();
    w = canvas.width = rect.width;
    h = canvas.height = rect.height;
  }

  function createParticles() {
    particles = [];
    for (let i = 0; i < PARTICLE_COUNT; i++) {
      particles.push({
        x: Math.random() * w,
        y: Math.random() * h,
        vx: (Math.random() - 0.5) * 0.6,
        vy: (Math.random() - 0.5) * 0.6,
        r: Math.random() * 2 + 1,
        phase: Math.random() * Math.PI * 2,
      });
    }
  }

  mouse = { x: -999, y: -999 };
  canvas.addEventListener("mousemove", function (e) {
    const rect = canvas.getBoundingClientRect();
    mouse.x = e.clientX - rect.left;
    mouse.y = e.clientY - rect.top;
  });
  canvas.addEventListener("mouseleave", function () {
    mouse.x = -999;
    mouse.y = -999;
  });

  function draw() {
    ctx.clearRect(0, 0, w, h);

    // 全局缓慢旋转流场
    const flowAngle = t * 0.002;
    const flowStrength = 0.08;

    // 更新 & 绘制粒子
    for (let i = 0; i < particles.length; i++) {
      const p = particles[i];

      // 添加轻微的环形流动
      const centerX = w * 0.5;
      const centerY = h * 0.5;
      const dx = p.x - centerX;
      const dy = p.y - centerY;
      const dist = Math.sqrt(dx * dx + dy * dy);
      const angle = Math.atan2(dy, dx);

      // 缓慢旋转力
      p.vx += Math.cos(angle + Math.PI * 0.5 + flowAngle) * flowStrength;
      p.vy += Math.sin(angle + Math.PI * 0.5 + flowAngle) * flowStrength;

      // 轻微的向心/离心波动
      const pulse = Math.sin(t * 0.01 + p.phase) * 0.05;
      if (dist > 10) {
        p.vx += (dx / dist) * pulse;
        p.vy += (dy / dist) * pulse;
      }

      p.x += p.vx;
      p.y += p.vy;

      // 边界反弹
      if (p.x < 0 || p.x > w) p.vx *= -0.8;
      if (p.y < 0 || p.y > h) p.vy *= -0.8;
      p.x = Math.max(0, Math.min(w, p.x));
      p.y = Math.max(0, Math.min(h, p.y));

      // 摩擦力
      p.vx *= 0.98;
      p.vy *= 0.98;

      // 鼠标排斥
      const mdx = p.x - mouse.x;
      const mdy = p.y - mouse.y;
      const mdist = Math.sqrt(mdx * mdx + mdy * mdy);
      if (mdist < MOUSE_DIST && mdist > 0) {
        p.x += (mdx / mdist) * 1.5;
        p.y += (mdy / mdist) * 1.5;
      }

      // 粒子大小呼吸
      const breathe = p.r + Math.sin(t * 0.02 + p.phase) * 0.4;

      ctx.beginPath();
      ctx.arc(p.x, p.y, breathe, 0, Math.PI * 2);
      ctx.fillStyle = "rgba(107,142,159,0.7)";
      ctx.fill();
    }

    // 连线（颜色随时间渐变）
    const colorShift = Math.sin(t * 0.005) * 0.1 + 0.35;
    for (let i = 0; i < particles.length; i++) {
      for (let j = i + 1; j < particles.length; j++) {
        const dx = particles[i].x - particles[j].x;
        const dy = particles[i].y - particles[j].y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < CONNECT_DIST) {
          ctx.beginPath();
          ctx.moveTo(particles[i].x, particles[i].y);
          ctx.lineTo(particles[j].x, particles[j].y);
          const alpha = (1 - dist / CONNECT_DIST) * colorShift;
          ctx.strokeStyle = "rgba(107,142,159," + alpha + ")";
          ctx.lineWidth = 0.6;
          ctx.stroke();
        }
      }
    }

    // 鼠标金色连线
    if (mouse.x > 0) {
      for (let i = 0; i < particles.length; i++) {
        const dx = particles[i].x - mouse.x;
        const dy = particles[i].y - mouse.y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < MOUSE_DIST) {
          ctx.beginPath();
          ctx.moveTo(particles[i].x, particles[i].y);
          ctx.lineTo(mouse.x, mouse.y);
          ctx.strokeStyle = "rgba(201,162,39," + (1 - dist / MOUSE_DIST) * 0.5 + ")";
          ctx.lineWidth = 0.8;
          ctx.stroke();
        }
      }
    }    t++;
    requestAnimationFrame(draw);
  }

  resize();
  createParticles();
  draw();
  window.addEventListener("resize", function () {
    resize();
    createParticles();
  });
})();

// ============== Contact 底部流动波浪动画 ================
(function () {
  const canvas = document.getElementById("waveCanvas");
  if (!canvas) return;
  const ctx = canvas.getContext("2d");
  let w, h, t = 0;

  function resize() {
    const rect = canvas.parentElement.getBoundingClientRect();
    w = canvas.width = rect.width;
    h = canvas.height = rect.height;
  }

  function drawWave(offset, color, amp, freq, speed) {
    ctx.beginPath();
    ctx.moveTo(0, h);
    for (let x = 0; x <= w; x += 2) {
      const y =
        h * 0.5 +
        Math.sin(x * freq + t * speed + offset) * amp +
        Math.sin(x * freq * 0.5 + t * speed * 0.7 + offset * 2) * amp * 0.5;
      ctx.lineTo(x, y);
    }
    ctx.lineTo(w, h);
    ctx.closePath();
    ctx.fillStyle = color;
    ctx.fill();
  }

  function draw() {
    ctx.clearRect(0, 0, w, h);
    drawWave(0, "rgba(107,142,159,0.12)", 20, 0.008, 0.02);
    drawWave(2, "rgba(107,142,159,0.08)", 15, 0.012, 0.015);
    drawWave(4, "rgba(201,162,39,0.06)", 12, 0.01, 0.025);
    // 顶部漂浮小圆点
    for (let i = 0; i < 8; i++) {
      const x = (w / 8) * i + Math.sin(t * 0.02 + i) * 30 + w / 16;
      const y = h * 0.3 + Math.cos(t * 0.015 + i * 1.5) * 20;
      const r = 2 + Math.sin(t * 0.03 + i) * 1;
      ctx.beginPath();
      ctx.arc(x, y, r, 0, Math.PI * 2);
      ctx.fillStyle = "rgba(107,142,159,0.25)";
      ctx.fill();
    }
    t++;
    requestAnimationFrame(draw);
  }

  resize();
  draw();
  window.addEventListener("resize", resize);
})();


// 默认打开“风控/经营”Tab（避免首页一次性展示全部卡片过长）
document.addEventListener('DOMContentLoaded', function(){
  try{
    enhancePortfolioCards();
    wireContactForm();
    wireScrollSpy();
    const btns = document.querySelectorAll('.portfolio-buttons .btn');
    const contentWD = document.getElementById('webdevelop');
    if(btns.length>=2 && contentWD){
      btns.forEach(b=>b.classList.remove('active'));
      document.querySelector('.portfolio-buttons .btn:nth-child(2)').classList.add('active');
      document.querySelectorAll('.tab-content').forEach(c=>c.classList.remove('active-content'));
      contentWD.classList.add('active-content');
      applyCardStagger('webdevelop');
    }
  }catch(e){}
});
