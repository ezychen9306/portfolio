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

function tabOpen(x) {
  for (portfolioTab of portfolioTabs) {
    portfolioTab.classList.remove("active");
  }
  for (tabContent of tabContents) {
    tabContent.classList.remove("active-content");
  }
  event.currentTarget.classList.add("active");
  document.getElementById(x).classList.add("active-content");
}

// ============== DARK THEME================
let themeBtn = document.querySelector("#theme-btn");

themeBtn.onclick = function () {
  themeBtn.classList.toggle("ri-sun-line");
  if (themeBtn.classList.contains("ri-sun-line")) {
    document.body.classList.add("active");
  } else {
    document.body.classList.remove("active");
  }
};

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
sr.reveal(".services .title", { origin: "top" });
sr.reveal(".services .content-1", { origin: "left" });
sr.reveal(".services .content-2", { origin: "right" });
sr.reveal(".portfolio-container", { origin: "bottom" });
sr.reveal(".portfolio .title", { origin: "top" });
sr.reveal(".portfolio-buttons", { origin: "left" });
sr.reveal(".testimonial .title", { origin: "right" });
sr.reveal(".testimonial .testimonial-container", { origin: "left" });
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
    const btns = document.querySelectorAll('.portfolio-buttons .btn');
    const contentAll = document.getElementById('all');
    const contentWD = document.getElementById('webdevelop');
    if(btns.length>=2 && contentAll && contentWD){
      btns.forEach(b=>b.classList.remove('active'));
      document.querySelector('.portfolio-buttons .btn:nth-child(2)').classList.add('active');
      document.querySelectorAll('.tab-content').forEach(c=>c.classList.remove('active-content'));
      contentWD.classList.add('active-content');
    }
  }catch(e){}
});