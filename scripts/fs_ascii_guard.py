# coding: utf-8
"""
Filesystem ASCII Guard (served folders only)
"""
import argparse, hashlib, os, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ALLOW = set("abcdefghijklmnopqrstuvwxyz0123456789-_.//")
TEXT_EXT = {'.html','.htm','.css','.js','.json','.md','.xml','.txt'}
SERVED_DIRS = {'', 'assets','demos','resume'}
IGNORE_DIRS = {'.git','node_modules','docs','constitution','apm_daily'}

slug_cache={}

def slugify(name:str)->str:
    base, ext = os.path.splitext(name)
    keep = []
    for ch in base.lower():
        if ch in ALLOW: keep.append(ch)
        elif ch.isalnum(): keep.append(ch.lower())
        elif ch in (' ','\t','\n'): keep.append('-')
        else: keep.append('-')
    s = re.sub(r'-+','-', ''.join(keep)).strip('-')
    if not s:
        s='f'
    return s + ext

def ascii_ok(p:Path)->bool:
    try:
        p.as_posix().encode('ascii')
        return all(ch in ALLOW or ch.isalnum() for ch in p.name)
    except UnicodeEncodeError:
        return False


def scan():
    bad=[]
    for root,dirs,files in os.walk(ROOT):
        rel=os.path.relpath(root, ROOT)
        top = '' if rel=='.' else rel.split(os.sep,1)[0]
        if top in IGNORE_DIRS: continue
        if top not in SERVED_DIRS: continue
        for name in dirs+files:
            path=Path(root)/name
            if not ascii_ok(path) or any(c for c in name if c.isupper() or c==' '):
                bad.append(path)
    return bad


def fix(paths):
    rename={}
    for p in paths:
        new = slugify(p.name)
        if new==p.name: continue
        if new in slug_cache:
            new = slugify(os.path.splitext(p.name)[0]+'-'+hashlib.md5(p.name.encode()).hexdigest()[:6]+os.path.splitext(p.name)[1])
        slug_cache[new]=1
        rename[p]=p.with_name(new)
    for src,dst in rename.items():
        print('rename:', src, '->', dst)
        os.rename(src,dst)
    repl=[(s.name, d.name) for s,d in rename.items()]
    for path in ROOT.rglob('*'):
        if path.suffix.lower() in TEXT_EXT and path.is_file():
            # limit updates to served folders
            rel=os.path.relpath(path, ROOT)
            top = '' if rel=='.' else rel.split(os.sep,1)[0]
            if top not in SERVED_DIRS: continue
            txt = path.read_text(encoding='utf-8', errors='ignore')
            orig=txt
            for a,b in repl:
                txt = txt.replace(a,b)
            if txt!=orig:
                path.write_text(txt, encoding='utf-8')
                print('updated refs:', path)

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--fix', action='store_true')
    args=ap.parse_args()
    bad=scan()
    if not bad:
        print('ASCII Guard: OK (no problematic paths)'); sys.exit(0)
    print('ASCII Guard: found', len(bad), 'paths with potential issues:')
    for p in bad: print(' -', p)
    if args.fix:
        fix(bad)
        print('ASCII Guard: fix complete')
        sys.exit(0)
    else:
        sys.exit(1)
