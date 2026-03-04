/** ralph.js - tiny helpers (no deps) */
(function(){
  const R = {};
  R.$ = (sel, root=document)=>root.querySelector(sel);
  R.$$ = (sel, root=document)=>Array.from(root.querySelectorAll(sel));
  R.fmt = (n)=>n.toLocaleString('en-US');
  R.sparkline = function(el, arr, color='#6b8e9f'){
    const w = el.clientWidth||160, h = el.clientHeight||40;
    const min = Math.min(...arr), max = Math.max(...arr);
    const norm = v => h - ((v-min)/(max-min||1))* (h-4) - 2;
    const step = (w-4)/Math.max(1,arr.length-1);
    const pts = arr.map((v,i)=>`${2+i*step},${norm(v)}`).join(' ');
    el.innerHTML = `<svg width="${w}" height="${h}"><polyline fill="none" stroke="${color}" stroke-width="2" points="${pts}"/></svg>`;
  };
  R.hbar = function(el, value, max=100, color='#6b8e9f'){
    el.style.position='relative'; el.style.background='#eee'; el.style.height='10px'; el.style.borderRadius='6px';
    const fill = document.createElement('div');
    fill.style.width = Math.max(0, Math.min(100, value/max*100))+'%';
    fill.style.height='100%'; fill.style.background=color; fill.style.borderRadius='6px';
    el.innerHTML=''; el.appendChild(fill);
  };
  R.loadJSON = async (path)=> (await fetch(path)).json();
  window.RALPH = R;
})();