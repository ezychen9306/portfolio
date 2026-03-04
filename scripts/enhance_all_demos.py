# coding: utf-8
from pathlib import Path
import json

ROOT = Path(r'd:\AI_agents\21_Report_Projects\05_portfolio')
DEMOS = ROOT/'demos'

MARK = '<!-- ralph-mini-start -->'

CSS_BLOCK = '''\n<!-- ralph-mini-start -->\n<style>\n.mini{max-width:1180px;margin:12px auto 16px;background:#fff;border:1px solid #eee;border-radius:10px;padding:12px}\n.mini-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}\n.mini-card{background:linear-gradient(135deg,#6b8e9f 0%,#5a7a8a 100%);color:#fff;border-radius:8px;padding:12px}\n.mini-k{font-size:.8rem;opacity:.85;margin-bottom:.25rem}\n.mini-v{font-size:1.6rem;font-weight:700}\n.mini-spark{grid-column:1/-1;height:40px}\n.mini-bars{display:flex;gap:10px;margin-top:6px;flex-wrap:wrap}\n.mini-bar{flex:1 1 180px;background:#eee;height:10px;border-radius:6px;overflow:hidden}\n.mini-bar div{height:100%;background:#c9a227}\n.mini-title{font-weight:600;margin:8px 0 6px;color:#2d2d2d}\n.mini-list{margin:6px 0 0;padding-left:18px;color:#555;font-size:.9rem}\n.mini-list li{margin:3px 0}\n</style>\n'''

# Per-demo injection builders ------------------------------------------------

def inject_04_ai_deep_strategy(html_path: Path):
    data = {
        "summary": {"uplift": 0.128, "coverage": 0.72, "tests": 8},
        "cohorts": [{"name": "新客", "uplift": 0.15}, {"name": "复贷", "uplift": 0.12}, {"name": "高价值", "uplift": 0.18}],
        "tactics": [{"name": "提前结清", "cov": 0.35}, {"name": "借新还旧", "cov": 0.28}, {"name": "额度曲线", "cov": 0.22}, {"name": "经营贷", "cov": 0.15}],
        "trend": [98,101,104,103,108,111,115,117,119,121,123,126]
    }
    (html_path.parent/'data.json').write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
    script = '''\n<script src="../../assets/js/ralph.js"></script>\n<script>(function(){\n  function el(t,c){const e=document.createElement(t); if(c) e.className=c; return e;}\n  function pct(x){return (x*100).toFixed(1)+'%'}\n  async function init(){\n    try{ const d = await RALPH.loadJSON('./data.json');\n      const box=el('div','mini'); const grid=el('div','mini-grid');\n      grid.append(el('div','mini-card'),el('div','mini-card'),el('div','mini-card'),el('div','mini-card'));\n      const [c1,c2,c3,c4]=grid.children;\n      c1.innerHTML='<div class="mini-k">整体 Uplift</div><div class="mini-v">'+pct(d.summary.uplift)+'</div>';\n      c2.innerHTML='<div class="mini-k">覆盖率</div><div class="mini-v">'+pct(d.summary.coverage)+'</div>';\n      c3.innerHTML='<div class="mini-k">在测策略</div><div class="mini-v">'+d.summary.tests+'</div>';\n      c4.innerHTML='<div class="mini-k">高价值 Cohort</div><div class="mini-v">'+pct(d.cohorts[2].uplift)+'</div>';\n      const spark=el('div','mini-spark'); grid.append(spark); box.append(grid);\n      const barsT=el('div'); barsT.className='mini-title'; barsT.textContent='策略覆盖'; box.append(barsT);\n      const bars=el('div','mini-bars'); d.tactics.forEach(t=>{const w=el('div','mini-bar');const f=el('div'); f.style.width=(t.cov*100)+'%'; w.appendChild(f); const lb=el('div');lb.style.fontSize='.85rem';lb.style.marginTop='4px';lb.textContent=t.name+' '+Math.round(t.cov*100)+'%'; const wrap=el('div'); wrap.style.flex='1 1 220px'; wrap.append(w,lb); bars.appendChild(wrap);}); box.append(bars);\n      document.body.insertBefore(box, document.body.firstElementChild);\n      RALPH.sparkline(spark, d.trend, '#c9a227');\n    }catch(e){ console.warn('ai_deep init fail', e);} }\n  document.addEventListener('DOMContentLoaded', init);\n})();</script>\n<!-- ralph-mini-end -->\n'''
    return CSS_BLOCK, script


def inject_06_telesales_system(html_path: Path):
    data = {
        "funnel": [
            {"name":"外呼", "value": 260000}, {"name":"接通", "value": 97000}, {"name":"有效通话", "value": 52000},
            {"name":"意向", "value": 21000}, {"name":"转化", "value": 9800}
        ],
        "segments": [
            {"name":"老客", "conv": 0.082}, {"name":"白金", "conv": 0.116}, {"name":"银卡", "conv": 0.064}
        ],
        "trend": [8.1,8.3,8.0,8.5,8.7,8.9,9.0,9.4]
    }
    (html_path.parent/'data.json').write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
    script = '''\n<script src="../../assets/js/ralph.js"></script>\n<script>(function(){\n  function el(t,c){const e=document.createElement(t); if(c) e.className=c; return e;}\n  async function init(){ try{ const d= await RALPH.loadJSON('./data.json');\n    const box=el('div','mini'); const grid=el('div','mini-grid');\n    const c1=el('div','mini-card'); c1.innerHTML='<div class="mini-k">本日外呼</div><div class="mini-v">'+(d.funnel[0].value).toLocaleString()+'</div>';\n    const c2=el('div','mini-card'); c2.innerHTML='<div class="mini-k">接通率</div><div class="mini-v">'+(d.funnel[1].value/d.funnel[0].value*100).toFixed(1)+'%</div>';\n    const c3=el('div','mini-card'); c3.innerHTML='<div class="mini-k">转化率</div><div class="mini-v">'+(d.funnel[4].value/d.funnel[0].value*100).toFixed(2)+'%</div>';\n    const c4=el('div','mini-card'); c4.innerHTML='<div class="mini-k">有效通话</div><div class="mini-v">'+(d.funnel[2].value).toLocaleString()+'</div>';\n    grid.append(c1,c2,c3,c4); const spark=el('div','mini-spark'); grid.append(spark); box.append(grid);\n    const barsT=el('div'); barsT.className='mini-title'; barsT.textContent='分群转化'; box.append(barsT); const bars=el('div','mini-bars');\n    d.segments.forEach(s=>{ const bar=el('div','mini-bar'); const fill=el('div'); fill.style.width=(s.conv*100)+'%'; bar.appendChild(fill); const lb=el('div'); lb.style.fontSize='.85rem'; lb.style.marginTop='4px'; lb.textContent=s.name+' '+(s.conv*100).toFixed(1)+'%'; const wrap=el('div'); wrap.style.flex='1 1 220px'; wrap.append(bar,lb); bars.appendChild(wrap); }); box.append(bars);\n    document.body.insertBefore(box, document.body.firstElementChild); RALPH.sparkline(spark, d.trend, '#c9a227');\n  }catch(e){console.warn('telesales init fail',e);} } document.addEventListener('DOMContentLoaded', init);})();</script>\n<!-- ralph-mini-end -->\n'''
    return CSS_BLOCK, script


def inject_07_year_end_report(html_path: Path):
    data = {"trend": [62,65,70,74,78,83,88,92,97,103,110,118],
            "milestones": [
                {"m":"03-15","t":"策略 V4 上线"}, {"m":"07-02","t":"额度曲线灰度"}, {"m":"11-20","t":"AI 中台发布"}
            ]}
    (html_path.parent/'data.json').write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
    script = '''\n<script src="../../assets/js/ralph.js"></script>\n<script>(function(){ function el(t,c){const e=document.createElement(t); if(c) e.className=c; return e;}\nasync function init(){ try{ const d= await RALPH.loadJSON('./data.json'); const box=el('div','mini'); const grid=el('div','mini-grid');\nconst c1=el('div','mini-card'); c1.innerHTML='<div class="mini-k">年度规模(亿)</div><div class="mini-v">'+(d.trend[d.trend.length-1])+'</div>';\nconst c2=el('div','mini-card'); c2.innerHTML='<div class="mini-k">里程碑</div><div class="mini-v">'+d.milestones.length+'</div>';\nconst c3=el('div','mini-card'); c3.innerHTML='<div class="mini-k">同比增长</div><div class="mini-v">'+(((d.trend[-1] if false else d.trend[-1]) if false else 18).toFixed? '': '')+'</div>';\nconst c4=el('div','mini-card'); c4.innerHTML='<div class="mini-k">月均增量</div><div class="mini-v">'+((d.trend[d.trend.length-1]-d.trend[0])/ (d.trend.length-1)).toFixed(1)+'</div>';\ngrid.append(c1,c2,c3,c4); const spark=el('div','mini-spark'); grid.append(spark); box.append(grid);\nconst title=el('div','mini-title'); title.textContent='关键里程碑'; box.append(title); const ul=el('ul','mini-list'); d.milestones.forEach(mi=>{ const li=el('li'); li.textContent=mi.m+' · '+mi.t; ul.appendChild(li); }); box.append(ul);\nRALPH.sparkline(spark, d.trend, '#c9a227'); document.body.insertBefore(box, document.body.firstElementChild);}catch(e){console.warn('year end init fail',e);} } document.addEventListener('DOMContentLoaded', init);})();</script>\n<!-- ralph-mini-end -->\n'''
    # Fix the odd expression in c3 by setting a static yoy; keep simple in client
    script = script.replace("(((d.trend[-1] if false else d.trend[-1]) if false else 18).toFixed? '': '')","""'+((d.trend[d.trend.length-1]/max(1,d.trend[0])-1)*100).toFixed(1)+'%'""")
    return CSS_BLOCK, script


def inject_08_weekly_monitoring(html_path: Path):
    data = {"summary": {"kpi": [
                {"n":"新批放款(亿)","v": 3.6}, {"n":"转化率","v": 0.214}, {"n":"30+ 逾期","v": 0.071}, {"n":"ROI","v": 0.176}
            ]},
            "trend": [3.1,3.3,3.0,3.4,3.5,3.7,3.6],
            "alerts": ["A 渠道转化下滑 3.2%","成长客群逾期率上升 0.6pp","模型服务 P95 延迟升高"]}
    (html_path.parent/'data.json').write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
    script = '''\n<script src="../../assets/js/ralph.js"></script>\n<script>(function(){ function el(t,c){const e=document.createElement(t); if(c) e.className=c; return e;}\nasync function init(){ try{ const d= await RALPH.loadJSON('./data.json'); const box=el('div','mini'); const grid=el('div','mini-grid');\n d.summary.kpi.forEach(k=>{ const c=el('div','mini-card'); c.innerHTML='<div class="mini-k">'+k.n+'</div><div class="mini-v">'+(typeof k.v==='number'?(k.n.includes('逾期')||k.n.includes('转化')||k.n==='ROI'?(k.v*100).toFixed(1)+'%':k.v):k.v)+'</div>'; grid.append(c);});\n const spark=el('div','mini-spark'); grid.append(spark); box.append(grid); const t=el('div','mini-title'); t.textContent='告警'; box.append(t); const ul=el('ul','mini-list'); d.alerts.forEach(a=>{ const li=el('li'); li.textContent=a; ul.appendChild(li);}); box.append(ul); document.body.insertBefore(box, document.body.firstElementChild); RALPH.sparkline(spark, d.trend, '#c9a227'); }catch(e){console.warn('weekly init fail',e);} } document.addEventListener('DOMContentLoaded', init);})();</script>\n<!-- ralph-mini-end -->\n'''
    return CSS_BLOCK, script


def inject_09_ai_sharing(html_path: Path):
    data={"trend":[12,18,20,25,21,28,34], "topics":[{"name":"RAG","v":34},{"name":"Agent","v":28},{"name":"Prompt","v":22},{"name":"MCP","v":16}]}
    (html_path.parent/'data.json').write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
    script='''\n<script src="../../assets/js/ralph.js"></script>\n<script>(function(){ function el(t,c){const e=document.createElement(t); if(c) e.className=c; return e;} async function init(){ try{ const d=await RALPH.loadJSON('./data.json'); const box=el('div','mini'); const grid=el('div','mini-grid'); const c1=el('div','mini-card'); c1.innerHTML='<div class="mini-k">近7次分享</div><div class="mini-v">'+d.trend.reduce((a,b)=>a+(b||0),0)+'</div>'; const c2=el('div','mini-card'); c2.innerHTML='<div class="mini-k">最高出席</div><div class="mini-v">'+Math.max(...d.trend)+'</div>'; const c3=el('div','mini-card'); c3.innerHTML='<div class="mini-k">主题数</div><div class="mini-v">'+d.topics.length+'</div>'; const c4=el('div','mini-card'); c4.innerHTML='<div class="mini-k">均值</div><div class="mini-v">'+(d.trend.reduce((a,b)=>a+b,0)/d.trend.length).toFixed(1)+'</div>'; grid.append(c1,c2,c3,c4); const spark=el('div','mini-spark'); grid.append(spark); box.append(grid); const t=el('div','mini-title'); t.textContent='主题分布'; box.append(t); const bars=el('div','mini-bars'); d.topics.forEach(x=>{ const bar=el('div','mini-bar'); const fill=el('div'); fill.style.width=(x.v/Math.max(...d.topics.map(t=>t.v))*100)+'%'; bar.appendChild(fill); const lb=el('div'); lb.style.fontSize='.85rem'; lb.style.marginTop='4px'; lb.textContent=x.name+' '+x.v; const wrap=el('div'); wrap.style.flex='1 1 220px'; wrap.append(bar,lb); bars.appendChild(wrap);}); box.append(bars); document.body.insertBefore(box, document.body.firstElementChild); RALPH.sparkline(spark, d.trend, '#c9a227'); }catch(e){console.warn('ai sharing init fail',e);} } document.addEventListener('DOMContentLoaded', init); })();</script>\n<!-- ralph-mini-end -->\n'''
    return CSS_BLOCK, script


def inject_10_fof_system(html_path: Path):
    data={"aum":[3.1,3.4,3.8,4.2,4.6,5.1,5.5,5.9,6.3,6.8,7.2,7.8], "risk":[{"name":"低","v":0.42},{"name":"中","v":0.38},{"name":"高","v":0.20}]}
    (html_path.parent/'data.json').write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
    script='''\n<script src="../../assets/js/ralph.js"></script>\n<script>(function(){ function el(t,c){const e=document.createElement(t); if(c) e.className=c; return e;} async function init(){ try{ const d=await RALPH.loadJSON('./data.json'); const box=el('div','mini'); const grid=el('div','mini-grid'); const c1=el('div','mini-card'); c1.innerHTML='<div class="mini-k">AUM(亿)</div><div class="mini-v">'+d.aum[d.aum.length-1].toFixed(1)+'</div>'; const c2=el('div','mini-card'); c2.innerHTML='<div class="mini-k">年增长</div><div class="mini-v">'+((d.aum[d.aum.length-1]/d.aum[0]-1)*100).toFixed(1)+'%</div>'; const c3=el('div','mini-card'); c3.innerHTML='<div class="mini-k">产品数</div><div class="mini-v">12</div>'; const c4=el('div','mini-card'); c4.innerHTML='<div class="mini-k">客户数(万)</div><div class="mini-v">7.4</div>'; grid.append(c1,c2,c3,c4); const spark=el('div','mini-spark'); grid.append(spark); box.append(grid); const t=el('div','mini-title'); t.textContent='风险带分布'; box.append(t); const bars=el('div','mini-bars'); const max=1.0; d.risk.forEach(x=>{ const bar=el('div','mini-bar'); const fill=el('div'); fill.style.width=(x.v/max*100)+'%'; bar.appendChild(fill); const lb=el('div'); lb.style.fontSize='.85rem'; lb.style.marginTop='4px'; lb.textContent=x.name+' '+Math.round(x.v*100)+'%'; const wrap=el('div'); wrap.style.flex='1 1 220px'; wrap.append(bar,lb); bars.appendChild(wrap);}); box.append(bars); document.body.insertBefore(box, document.body.firstElementChild); RALPH.sparkline(spark, d.aum, '#c9a227'); }catch(e){console.warn('fof init fail',e);} } document.addEventListener('DOMContentLoaded', init); })();</script>\n<!-- ralph-mini-end -->\n'''
    return CSS_BLOCK, script


def inject_11_customer_segmentation(html_path: Path):
    data={"segments":[{"name":"高价值","cnt":120000,"risk":0.021,"util":0.78},{"name":"标准","cnt":280000,"risk":0.056,"util":0.71},{"name":"成长","cnt":190000,"risk":0.089,"util":0.65},{"name":"高风险","cnt":42000,"risk":0.125,"util":0.45}], "trend":[68,70,73,74,76,78,80]}
    (html_path.parent/'data.json').write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
    script='''\n<script src="../../assets/js/ralph.js"></script>\n<script>(function(){ function el(t,c){const e=document.createElement(t); if(c) e.className=c; return e;} async function init(){ try{ const d=await RALPH.loadJSON('./data.json'); const box=el('div','mini'); const grid=el('div','mini-grid'); const c1=el('div','mini-card'); c1.innerHTML='<div class="mini-k">客户总数</div><div class="mini-v">'+(d.segments.reduce((a,b)=>a+b.cnt,0)).toLocaleString()+'</div>'; const c2=el('div','mini-card'); c2.innerHTML='<div class="mini-k">高价值 Util</div><div class="mini-v">'+Math.round(d.segments[0].util*100)+'%</div>'; const c3=el('div','mini-card'); c3.innerHTML='<div class="mini-k">总体风险</div><div class="mini-v">'+(d.segments.reduce((a,b)=>a+b.risk*b.cnt,0)/d.segments.reduce((a,b)=>a+b.cnt,0)*100).toFixed(1)+'%</div>'; const c4=el('div','mini-card'); c4.innerHTML='<div class="mini-k">月度规模(亿)</div><div class="mini-v">'+d.trend[d.trend.length-1]+'</div>'; grid.append(c1,c2,c3,c4); const spark=el('div','mini-spark'); grid.append(spark); box.append(grid); const t=el('div','mini-title'); t.textContent='分层 Util/风险'; box.append(t); const bars=el('div','mini-bars'); d.segments.forEach(x=>{ const bar=el('div','mini-bar'); const fill=el('div'); fill.style.width=(x.util*100)+'%'; bar.appendChild(fill); const lb=el('div'); lb.style.fontSize='.85rem'; lb.style.marginTop='4px'; lb.textContent=x.name+' Util '+Math.round(x.util*100)+'% · 风险 '+Math.round(x.risk*100)+'%'; const wrap=el('div'); wrap.style.flex='1 1 260px'; wrap.append(bar,lb); bars.appendChild(wrap);}); box.append(bars); document.body.insertBefore(box, document.body.firstElementChild); RALPH.sparkline(spark, d.trend, '#c9a227'); }catch(e){console.warn('seg init fail',e);} } document.addEventListener('DOMContentLoaded', init); })();</script>\n<!-- ralph-mini-end -->\n'''
    return CSS_BLOCK, script


def inject_12_apm(html_path: Path):
    """APM 日报 demo 无 mini 组件注入，返回空以跳过。"""
    return "", ""


def inject_13_knowledge_base_agent(html_path: Path):
    data={"trend":[0.72,0.75,0.78,0.80,0.83,0.86,0.88], "latency":[{"name":"P50","v":0.45},{"name":"P95","v":1.20},{"name":"P99","v":2.40}], "docs": 12600}
    (html_path.parent/'data.json').write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
    script='''\n<script src="../../assets/js/ralph.js"></script>\n<script>(function(){ function el(t,c){const e=document.createElement(t); if(c) e.className=c; return e;} async function init(){ try{ const d=await RALPH.loadJSON('./data.json'); const box=el('div','mini'); const grid=el('div','mini-grid'); const c1=el('div','mini-card'); c1.innerHTML='<div class="mini-k">库文档</div><div class="mini-v">'+d.docs.toLocaleString()+'</div>'; const c2=el('div','mini-card'); c2.innerHTML='<div class="mini-k">命中率</div><div class="mini-v">'+Math.round(d.trend[d.trend.length-1]*100)+'%</div>'; const c3=el('div','mini-card'); c3.innerHTML='<div class="mini-k">P95</div><div class="mini-v">'+d.latency[1].v.toFixed(2)+'s</div>'; const c4=el('div','mini-card'); c4.innerHTML='<div class="mini-k">P99</div><div class="mini-v">'+d.latency[2].v.toFixed(2)+'s</div>'; grid.append(c1,c2,c3,c4); const spark=el('div','mini-spark'); grid.append(spark); box.append(grid); const t=el('div','mini-title'); t.textContent='延迟分布'; box.append(t); const bars=el('div','mini-bars'); const max=Math.max(...d.latency.map(x=>x.v)); d.latency.forEach(x=>{ const bar=el('div','mini-bar'); const fill=el('div'); fill.style.width=(x.v/max*100)+'%'; bar.appendChild(fill); const lb=el('div'); lb.style.fontSize='.85rem'; lb.style.marginTop='4px'; lb.textContent=x.name+' '+x.v.toFixed(2)+'s'; const wrap=el('div'); wrap.style.flex='1 1 220px'; wrap.append(bar,lb); bars.appendChild(wrap);}); box.append(bars); document.body.insertBefore(box, document.body.firstElementChild); RALPH.sparkline(spark, d.trend.map(x=>x*100), '#c9a227'); }catch(e){console.warn('kb init fail',e);} } document.addEventListener('DOMContentLoaded', init); })();</script>\n<!-- ralph-mini-end -->\n'''
    return CSS_BLOCK, script


def inject_14_skills_development(html_path: Path):
    data={"trend":[12,14,18,20,23,26,30], "compliance":0.95, "teams":[{"name":"风控","v":0.34},{"name":"运营","v":0.28},{"name":"产品","v":0.22},{"name":"研发","v":0.16}]}
    (html_path.parent/'data.json').write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
    script='''\n<script src="../../assets/js/ralph.js"></script>\n<script>(function(){ function el(t,c){const e=document.createElement(t); if(c) e.className=c; return e;} async function init(){ try{ const d=await RALPH.loadJSON('./data.json'); const box=el('div','mini'); const grid=el('div','mini-grid'); const c1=el('div','mini-card'); c1.innerHTML='<div class="mini-k">近7日使用</div><div class="mini-v">'+d.trend.reduce((a,b)=>a+b,0)+'</div>'; const c2=el('div','mini-card'); c2.innerHTML='<div class="mini-k">合规率</div><div class="mini-v">'+Math.round(d.compliance*100)+'%</div>'; const c3=el('div','mini-card'); c3.innerHTML='<div class="mini-k">活跃团队</div><div class="mini-v">'+d.teams.length+'</div>'; const c4=el('div','mini-card'); c4.innerHTML='<div class="mini-k">单日峰值</div><div class="mini-v">'+Math.max(...d.trend)+'</div>'; grid.append(c1,c2,c3,c4); const spark=el('div','mini-spark'); grid.append(spark); box.append(grid); const t=el('div','mini-title'); t.textContent='团队分布'; box.append(t); const bars=el('div','mini-bars'); d.teams.forEach(x=>{ const bar=el('div','mini-bar'); const fill=el('div'); fill.style.width=(x.v*100)+'%'; bar.appendChild(fill); const lb=el('div'); lb.style.fontSize='.85rem'; lb.style.marginTop='4px'; lb.textContent=x.name+' '+Math.round(x.v*100)+'%'; const wrap=el('div'); wrap.style.flex='1 1 220px'; wrap.append(bar,lb); bars.appendChild(wrap);}); box.append(bars); document.body.insertBefore(box, document.body.firstElementChild); RALPH.sparkline(spark, d.trend, '#c9a227'); }catch(e){console.warn('skills init fail',e);} } document.addEventListener('DOMContentLoaded', init); })();</script>\n<!-- ralph-mini-end -->\n'''
    return CSS_BLOCK, script

BUILDERS = {
  '04_ai_deep_strategy': inject_04_ai_deep_strategy,
  '06_telesales_system': inject_06_telesales_system,
  '07_year_end_report': inject_07_year_end_report,
  '08_weekly_monitoring': inject_08_weekly_monitoring,
  '09_ai_sharing': inject_09_ai_sharing,
  '10_fof_system': inject_10_fof_system,
  '11_customer_segmentation': inject_11_customer_segmentation,
  '13_knowledge_base_agent': inject_13_knowledge_base_agent,
  '14_skills_development': inject_14_skills_development,
}

# helpers ---------------------------------------------------------

def inject_into_html(html_path: Path, css: str, script: str):
    html = html_path.read_text(encoding='utf-8', errors='ignore')
    if MARK in html:
        return False
    # add CSS before </head>
    if '</head>' in html:
        html = html.replace('</head>', css + '\n</head>')
    else:
        html = css + html
    # add script before </body>
    if '</body>' in html:
        html = html.replace('</body>', script + '\n</body>')
    else:
        html = html + script
    html_path.write_text(html, encoding='utf-8')
    return True


def main():
    changed=0
    for slug, builder in BUILDERS.items():
        html_path = DEMOS/slug/'index.html'
        if not html_path.exists():
            print('skip (no index):', slug); continue
        css, script = builder(html_path)
        if inject_into_html(html_path, CSS_BLOCK, script):
            changed+=1; print('enhanced:', slug)
        else:
            print('already enhanced:', slug)
    print('done, enhanced pages:', changed)

if __name__=='__main__':
    main()
