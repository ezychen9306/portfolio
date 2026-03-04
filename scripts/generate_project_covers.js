const fs = require("fs");
const path = require("path");

const OUT_DIR = path.resolve(__dirname, "../assets/images/projects");
const WIDTH = 960;
const HEIGHT = 600;

function xmur3(str) {
  let h = 1779033703 ^ str.length;
  for (let i = 0; i < str.length; i += 1) {
    h = Math.imul(h ^ str.charCodeAt(i), 3432918353);
    h = (h << 13) | (h >>> 19);
  }
  return function next() {
    h = Math.imul(h ^ (h >>> 16), 2246822507);
    h = Math.imul(h ^ (h >>> 13), 3266489909);
    h ^= h >>> 16;
    return h >>> 0;
  };
}

function mulberry32(seed) {
  return function rand() {
    let t = (seed += 0x6d2b79f5);
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

function rndFactory(seedText) {
  const seedFn = xmur3(seedText);
  return mulberry32(seedFn());
}

function clamp(x, min, max) {
  return Math.max(min, Math.min(max, x));
}

function pointPath(points) {
  if (!points.length) return "";
  let d = `M ${points[0][0].toFixed(2)} ${points[0][1].toFixed(2)}`;
  for (let i = 1; i < points.length; i += 1) {
    d += ` L ${points[i][0].toFixed(2)} ${points[i][1].toFixed(2)}`;
  }
  return d;
}

function makeContour(cx, cy, baseR, wobble, steps, f1, f2, phase = 0) {
  const pts = [];
  for (let i = 0; i <= steps; i += 1) {
    const t = (Math.PI * 2 * i) / steps;
    const r = baseR + wobble * Math.sin(f1 * t + phase) + wobble * 0.45 * Math.cos(f2 * t - phase);
    pts.push([cx + r * Math.cos(t), cy + r * Math.sin(t)]);
  }
  return pointPath(pts) + " Z";
}

function bg(svg, c1, c2, accent) {
  return `
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="${c1}" />
      <stop offset="100%" stop-color="${c2}" />
    </linearGradient>
    <radialGradient id="spot" cx="20%" cy="15%">
      <stop offset="0%" stop-color="rgba(255,255,255,0.22)" />
      <stop offset="100%" stop-color="rgba(255,255,255,0)" />
    </radialGradient>
    <linearGradient id="accent" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="${accent}" stop-opacity="0.95" />
      <stop offset="100%" stop-color="${accent}" stop-opacity="0.45" />
    </linearGradient>
    <filter id="grain" x="-10%" y="-10%" width="120%" height="120%">
      <feTurbulence type="fractalNoise" baseFrequency="0.7" numOctaves="2" seed="7" />
      <feColorMatrix type="saturate" values="0" />
      <feComponentTransfer>
        <feFuncA type="table" tableValues="0 0 0.055" />
      </feComponentTransfer>
    </filter>
  </defs>
  <rect width="${WIDTH}" height="${HEIGHT}" fill="url(#bg)" />
  <rect width="${WIDTH}" height="${HEIGHT}" fill="url(#spot)" />
  <rect width="${WIDTH}" height="${HEIGHT}" filter="url(#grain)" />
  <rect x="18" y="18" width="${WIDTH - 36}" height="${HEIGHT - 36}" rx="26" fill="none" stroke="rgba(255,255,255,0.24)" />
  <rect x="18" y="18" width="${WIDTH - 36}" height="8" rx="4" fill="url(#accent)" />
  `;
}

function titleBlock(title, subtitle) {
  return `
  <text x="46" y="74" fill="rgba(255,255,255,0.95)" font-size="30" font-family="Montserrat, Segoe UI, sans-serif" font-weight="700" letter-spacing="1.2">${title}</text>
  <text x="46" y="106" fill="rgba(255,255,255,0.72)" font-size="16" font-family="Segoe UI, sans-serif" letter-spacing="1">${subtitle}</text>
  `;
}

function motifDisaster() {
  const cx = 320;
  const cy = 336;
  const contours = [150, 118, 88, 62].map((r, i) => `<path d="${makeContour(cx, cy, r, 8 + i * 2, 80, 4 + i, 7 + i, i)}" fill="none" stroke="rgba(180,220,255,${0.34 - i * 0.05})" stroke-width="${2 - i * 0.2}" />`).join("");
  return `
  <g>
    ${contours}
    <path d="${makeContour(cx, cy, 98, 18, 12, 3, 5, 0.6)}" fill="rgba(245,158,11,0.2)" stroke="rgba(245,158,11,0.95)" stroke-width="2.6" />
    <line x1="${cx}" y1="${cy - 162}" x2="${cx}" y2="${cy + 164}" stroke="rgba(255,255,255,0.18)" />
    <line x1="${cx - 160}" y1="${cy}" x2="${cx + 160}" y2="${cy}" stroke="rgba(255,255,255,0.18)" />
  </g>`;
}

function motifQuota() {
  const curves = [];
  for (let i = 0; i < 4; i += 1) {
    const y = 200 + i * 72;
    const len = 520 - i * 78;
    curves.push(`<path d="M 120 ${y} C ${240 + i * 24} ${y - 34}, ${360 + i * 18} ${y + 38}, ${120 + len} ${y - 6}" fill="none" stroke="rgba(255,255,255,${0.24 + i * 0.08})" stroke-width="${4 - i * 0.2}" stroke-linecap="round" />`);
    curves.push(`<circle cx="${120 + len}" cy="${y - 6}" r="${8 - i}" fill="rgba(245,179,35,0.95)" />`);
  }
  return `<g>${curves.join("")}</g>`;
}

function motifRM(rand) {
  let cells = "";
  const ox = 146;
  const oy = 176;
  const w = 124;
  const h = 78;
  for (let r = 0; r < 3; r += 1) {
    for (let c = 0; c < 5; c += 1) {
      const x = ox + c * (w + 12);
      const y = oy + r * (h + 12);
      const heat = clamp(rand() * 0.9 + 0.1, 0, 1);
      const a = 0.16 + heat * 0.5;
      cells += `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="8" fill="rgba(255,255,255,${a.toFixed(3)})" stroke="rgba(255,255,255,0.22)" />`;
    }
  }
  return `<g>${cells}</g>`;
}

function motifAIDeep(rand) {
  const layers = [4, 5, 4, 2];
  const x0 = 160;
  const gapX = 176;
  const yTop = 180;
  const yBottom = 448;
  const nodes = [];
  layers.forEach((n, li) => {
    for (let i = 0; i < n; i += 1) {
      const y = yTop + ((yBottom - yTop) * (i + 1)) / (n + 1) + (rand() - 0.5) * 10;
      nodes.push({ li, x: x0 + li * gapX, y, accent: li === layers.length - 1 });
    }
  });
  let lines = "";
  for (let li = 0; li < layers.length - 1; li += 1) {
    const left = nodes.filter((n) => n.li === li);
    const right = nodes.filter((n) => n.li === li + 1);
    left.forEach((a) => {
      right.forEach((b) => {
        lines += `<line x1="${a.x}" y1="${a.y.toFixed(1)}" x2="${b.x}" y2="${b.y.toFixed(1)}" stroke="rgba(255,255,255,0.18)" stroke-width="1.6" />`;
      });
    });
  }
  const circles = nodes.map((n) => `<circle cx="${n.x}" cy="${n.y.toFixed(1)}" r="${n.accent ? 11 : 9}" fill="${n.accent ? "rgba(245,179,35,0.95)" : "rgba(189,228,255,0.82)"}" />`).join("");
  return `<g>${lines}${circles}</g>`;
}

function motifKYC() {
  return `
  <g>
    <path d="M140 188 H820 L752 246 H208 Z" fill="rgba(255,255,255,0.18)" />
    <path d="M188 272 H772 L720 326 H240 Z" fill="rgba(255,255,255,0.15)" />
    <path d="M242 352 H718 L684 402 H276 Z" fill="rgba(255,255,255,0.12)" />
    <path d="M306 430 H654 L632 476 H328 Z" fill="rgba(20,184,166,0.75)" />
    <line x1="480" y1="476" x2="480" y2="520" stroke="rgba(20,184,166,0.95)" stroke-width="6" stroke-linecap="round" />
  </g>`;
}

function motifTeleSales() {
  return `
  <g>
    <circle cx="200" cy="304" r="22" fill="rgba(190,228,255,0.8)" />
    <circle cx="338" cy="248" r="22" fill="rgba(190,228,255,0.8)" />
    <circle cx="338" cy="360" r="22" fill="rgba(190,228,255,0.8)" />
    <circle cx="524" cy="304" r="24" fill="rgba(250,204,21,0.96)" />
    <path d="M222 304 C 260 292, 292 272, 316 250" fill="none" stroke="rgba(255,255,255,0.45)" stroke-width="2.4"/>
    <path d="M222 304 C 262 318, 292 338, 316 360" fill="none" stroke="rgba(255,255,255,0.45)" stroke-width="2.4"/>
    <path d="M360 248 C 418 248, 456 276, 500 304" fill="none" stroke="rgba(250,204,21,0.9)" stroke-width="2.6"/>
    <path d="M360 360 C 418 352, 456 330, 500 304" fill="none" stroke="rgba(250,204,21,0.9)" stroke-width="2.6"/>
  </g>`;
}

function motifTimeline() {
  return `
  <g>
    <line x1="118" y1="442" x2="842" y2="442" stroke="rgba(255,255,255,0.26)" stroke-width="3" />
    <path d="M118 442 C 212 364, 286 392, 362 334 S 538 256, 642 218 S 760 170, 842 154" fill="none" stroke="rgba(245,179,35,0.92)" stroke-width="4" />
    <circle cx="118" cy="442" r="11" fill="rgba(245,179,35,0.95)" />
    <circle cx="362" cy="334" r="9" fill="rgba(255,255,255,0.8)" />
    <circle cx="642" cy="218" r="9" fill="rgba(255,255,255,0.8)" />
    <circle cx="842" cy="154" r="11" fill="rgba(245,179,35,0.95)" />
  </g>`;
}

function motifDashboard() {
  return `
  <g>
    <rect x="136" y="176" width="260" height="130" rx="12" fill="rgba(255,255,255,0.16)" />
    <rect x="414" y="176" width="410" height="130" rx="12" fill="rgba(255,255,255,0.12)" />
    <rect x="136" y="322" width="340" height="154" rx="12" fill="rgba(255,255,255,0.12)" />
    <rect x="494" y="322" width="330" height="154" rx="12" fill="rgba(255,255,255,0.17)" />
    <polyline points="170,434 220,398 270,412 320,362 370,376 430,340" fill="none" stroke="rgba(250,204,21,0.92)" stroke-width="3" />
    <polyline points="448,260 518,238 592,268 666,226 744,248 806,214" fill="none" stroke="rgba(154,230,255,0.9)" stroke-width="3" />
  </g>`;
}

function motifKnowledge() {
  return `
  <g>
    <rect x="144" y="192" width="250" height="210" rx="14" fill="rgba(255,255,255,0.16)" />
    <rect x="204" y="222" width="250" height="210" rx="14" fill="rgba(255,255,255,0.14)" />
    <rect x="264" y="252" width="250" height="210" rx="14" fill="rgba(255,255,255,0.12)" />
    <path d="M548 300 C 634 254, 694 236, 814 228" fill="none" stroke="rgba(34,211,238,0.95)" stroke-width="4" />
    <path d="M548 348 C 644 336, 724 356, 814 410" fill="none" stroke="rgba(34,211,238,0.7)" stroke-width="3" />
    <circle cx="830" cy="224" r="12" fill="rgba(34,211,238,0.95)" />
    <circle cx="830" cy="420" r="12" fill="rgba(34,211,238,0.82)" />
  </g>`;
}

function motifSkills(rand) {
  let block = "";
  const cols = 6;
  const rows = 4;
  const ox = 164;
  const oy = 190;
  const s = 96;
  for (let r = 0; r < rows; r += 1) {
    for (let c = 0; c < cols; c += 1) {
      const alpha = 0.08 + rand() * 0.28;
      const x = ox + c * (s + 10);
      const y = oy + r * (s * 0.62 + 10);
      block += `<rect x="${x}" y="${y}" width="${s}" height="${(s * 0.62).toFixed(1)}" rx="10" fill="rgba(255,255,255,${alpha.toFixed(3)})" />`;
    }
  }
  return `<g>${block}<path d="M164 452 C 322 392, 500 508, 744 430" fill="none" stroke="rgba(251,113,133,0.95)" stroke-width="4" /></g>`;
}

function motifSharing() {
  return `
  <g>
    <circle cx="486" cy="316" r="42" fill="rgba(167,139,250,0.85)" />
    <circle cx="486" cy="316" r="92" fill="none" stroke="rgba(167,139,250,0.55)" stroke-width="3" />
    <circle cx="486" cy="316" r="146" fill="none" stroke="rgba(167,139,250,0.35)" stroke-width="3" />
    <circle cx="486" cy="316" r="196" fill="none" stroke="rgba(167,139,250,0.22)" stroke-width="3" />
    <path d="M192 314 H782" stroke="rgba(255,255,255,0.25)" stroke-width="2" />
    <path d="M486 122 V512" stroke="rgba(255,255,255,0.2)" stroke-width="2" />
  </g>`;
}

function motifFOF(rand) {
  const points = [];
  for (let i = 0; i < 16; i += 1) {
    const x = 180 + i * 40;
    const y = 450 - Math.pow(i / 15, 1.38) * 250 + (rand() - 0.5) * 16;
    points.push([x, y]);
  }
  const pLine = pointPath(points);
  const dots = points.map((p, i) => `<circle cx="${p[0].toFixed(1)}" cy="${p[1].toFixed(1)}" r="${i % 4 === 0 ? 7 : 5}" fill="${i % 4 === 0 ? "rgba(250,204,21,0.95)" : "rgba(255,255,255,0.72)"}" />`).join("");
  return `<g><path d="${pLine}" fill="none" stroke="rgba(250,204,21,0.95)" stroke-width="3.2" />${dots}</g>`;
}

const covers = [
  { file: "disaster-management.svg", title: "DISASTER CONTROL", subtitle: "topological response", c1: "#0f172a", c2: "#1d4ed8", accent: "#f59e0b", mode: "disaster" },
  { file: "quota-strategy-v5.svg", title: "QUOTA STRATEGY V5", subtitle: "elastic boundary", c1: "#0b2239", c2: "#245b74", accent: "#fbbf24", mode: "quota" },
  { file: "rm-system.svg", title: "RM RISK MANAGEMENT", subtitle: "matrix intelligence", c1: "#111827", c2: "#1f2937", accent: "#f6ad2b", mode: "rm" },
  { file: "ai-deep-strategy.svg", title: "AI DEEP STRATEGY", subtitle: "decision mesh", c1: "#182234", c2: "#334155", accent: "#f59e0b", mode: "aideep" },
  { file: "kyc-platform.svg", title: "KYC PLATFORM", subtitle: "segment funnel", c1: "#0f172a", c2: "#155e75", accent: "#14b8a6", mode: "kyc" },
  { file: "telesales-system.svg", title: "TELESALES SYSTEM", subtitle: "call flow graph", c1: "#172554", c2: "#1e3a8a", accent: "#facc15", mode: "telesales" },
  { file: "year-end-report.svg", title: "YEAR END REVIEW", subtitle: "strategic timeline", c1: "#312e81", c2: "#1d4ed8", accent: "#f59e0b", mode: "timeline" },
  { file: "weekly-monitoring.svg", title: "WEEKLY MONITORING", subtitle: "automation cockpit", c1: "#0c4a6e", c2: "#0369a1", accent: "#fbbf24", mode: "dashboard" },
  { file: "knowledge-base-agent.svg", title: "KNOWLEDGE BASE AGENT", subtitle: "rag retrieval graph", c1: "#111827", c2: "#0f766e", accent: "#22d3ee", mode: "knowledge" },
  { file: "skills-dev.svg", title: "SKILLS DEVELOPMENT", subtitle: "modular acceleration", c1: "#3f1d2e", c2: "#7c2d12", accent: "#fb7185", mode: "skills" },
  { file: "ai-sharing.svg", title: "AI INTERNAL SHARING", subtitle: "team resonance", c1: "#312e81", c2: "#4338ca", accent: "#a78bfa", mode: "sharing" },
  { file: "fof-system.svg", title: "FOF INVESTMENT", subtitle: "efficient frontier", c1: "#14532d", c2: "#166534", accent: "#facc15", mode: "fof" },
];

function composeCover(c) {
  const rand = rndFactory(c.file);
  let motif = "";
  switch (c.mode) {
    case "disaster": motif = motifDisaster(); break;
    case "quota": motif = motifQuota(); break;
    case "rm": motif = motifRM(rand); break;
    case "aideep": motif = motifAIDeep(rand); break;
    case "kyc": motif = motifKYC(); break;
    case "telesales": motif = motifTeleSales(); break;
    case "timeline": motif = motifTimeline(); break;
    case "dashboard": motif = motifDashboard(); break;
    case "knowledge": motif = motifKnowledge(); break;
    case "skills": motif = motifSkills(rand); break;
    case "sharing": motif = motifSharing(); break;
    case "fof": motif = motifFOF(rand); break;
    default: motif = "";
  }
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${WIDTH} ${HEIGHT}" role="img" aria-label="${c.title}">
${bg("", c.c1, c.c2, c.accent)}
${titleBlock(c.title, c.subtitle)}
${motif}
</svg>
`;
}

fs.mkdirSync(OUT_DIR, { recursive: true });
covers.forEach((c) => {
  const out = path.join(OUT_DIR, c.file);
  fs.writeFileSync(out, composeCover(c), "utf8");
});

console.log(`Generated ${covers.length} project cover SVG files in ${OUT_DIR}`);
