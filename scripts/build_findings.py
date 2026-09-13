#!/usr/bin/env python3
"""Build docs/findings/0N-*.html from drafts/0N-*.md, inserting figures and animations after named headings."""
import re, html, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT/'docs/findings/_figures'   # saved svg/animation snippets

STYLE = '''<style>
  :root { --ink:#1b1b1f; --muted:#5a5f6a; --bg:#fbfbf8; --card:#fff; --line:#e3e2dc; --accent:#b4432c; --accent2:#2a6f97; --good:#2f7d4a; --warn:#b07a12; --purple:#6a4c93; }
  body { margin:0; background:var(--bg); color:var(--ink); font:16px/1.6 -apple-system,"Segoe UI",Helvetica,Arial,sans-serif; }
  main { max-width:780px; margin:0 auto; padding:36px 22px 60px; }
  h1 { font-size:27px; line-height:1.2; margin:0 0 14px; }
  h2 { font-size:19px; margin:32px 0 8px; padding-top:12px; border-top:1px solid var(--line); }
  p { margin:0 0 14px; } p.summary { font-size:17px; background:#f3f7fa; border-left:4px solid var(--accent2); padding:10px 14px; }
  table { border-collapse:collapse; width:100%; font-size:14.5px; margin:8px 0 16px; } th,td { text-align:left; padding:6px 8px; border-bottom:1px solid var(--line); vertical-align:top; } th { color:var(--muted); font-weight:600; } td.n, th.n { text-align:right; font-variant-numeric:tabular-nums; }
  ul, ol { margin:6px 0 14px; padding-left:22px; } li { margin:4px 0; }
  code { font-size:13px; background:#f1f0eb; padding:1px 4px; border-radius:3px; }
  figure { margin:16px 0 20px; } figcaption { color:var(--muted); font-size:13px; margin-top:6px; }
  svg text { font:13px -apple-system,Helvetica,Arial,sans-serif; }
  .anim { border:1px solid var(--line); border-radius:10px; background:var(--card); padding:12px 14px; margin:16px 0 20px; }
  .anim .ctl { display:flex; gap:10px; align-items:center; font-size:13px; color:var(--muted); margin-top:6px; flex-wrap:wrap; }
  .anim button { font:13px inherit; padding:3px 10px; border:1px solid var(--line); border-radius:6px; background:#fff; cursor:pointer; }
  .anim input[type=range] { width:160px; }
  .nav { display:flex; gap:14px; font-size:13px; margin:0 0 18px; } .nav a { color:var(--muted); text-decoration:none; }
  .kicker { color:var(--accent); font-weight:600; letter-spacing:.04em; text-transform:uppercase; font-size:12px; margin-bottom:6px; }
  .methods { color:var(--muted); font-size:14px; } .methods h2 { color:var(--ink); }
  a { color:var(--accent2); }
</style>'''

def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s = re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'(?<![\w*])\*([^*]+)\*(?!\w)', r'<i>\1</i>', s)
    s = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', s)
    return s

def table(lines):
    rows = [[c.strip() for c in l.strip().strip('|').split('|')] for l in lines if not re.match(r'^\s*\|?\s*-', l)]
    head, body = rows[0], rows[1:]
    def num(c): return bool(re.match(r'^[\d,.%°–<≤>~+\- /×]+$', c)) and any(ch.isdigit() for ch in c)
    numcol = [all(num(r[i]) for r in body if i < len(r) and r[i] not in ('–','')) for i in range(len(head))]
    out = ['<table>', '<tr>' + ''.join(f'<th class="{"n" if numcol[i] else ""}">{inline(c)}</th>' for i, c in enumerate(head)) + '</tr>']
    for r in body: out.append('<tr>' + ''.join(f'<td class="{"n" if numcol[i] else ""}">{inline(c)}</td>' for i, c in enumerate(r)) + '</tr>')
    return '\n'.join(out) + '</table>'

def md_to_html(md, inserts, kicker):
    lines = md.split('\n'); out = []; i = 0; in_methods = False
    while i < len(lines):
        l = lines[i]
        if l.startswith('# '):
            out.append(f'<div class="kicker">{kicker}</div><h1>{inline(l[2:])}</h1>'); i += 1; continue
        if l.startswith('## '):
            t = l[3:].strip()
            if t == 'Methods' and not in_methods: out.append('<div class="methods">'); in_methods = True
            out.append(f'<h2>{inline(t)}</h2>')
            if t in inserts: out.append(inserts[t])
            i += 1; continue
        if l.startswith('|'):
            j = i
            while j < len(lines) and lines[j].startswith('|'): j += 1
            out.append(table(lines[i:j])); i = j; continue
        if re.match(r'^(- |\d+\. )', l):
            ordered = l[0].isdigit(); items = []
            while i < len(lines) and re.match(r'^(- |\d+\. )', lines[i]):
                items.append(re.sub(r'^(- |\d+\. )', '', lines[i])); i += 1
            tag = 'ol' if ordered else 'ul'
            out.append(f'<{tag}>' + ''.join(f'<li>{inline(x)}</li>' for x in items) + f'</{tag}>'); continue
        if l.strip() == '': i += 1; continue
        j = i; para = []
        while j < len(lines) and lines[j].strip() != '' and not lines[j].startswith(('#', '|', '- ')) and not re.match(r'^\d+\. ', lines[j]):
            para.append(lines[j]); j += 1
        text = ' '.join(para)
        cls = ' class="summary"' if text.startswith('**Summary.**') else ''
        out.append(f'<p{cls}>{inline(text)}</p>')
        if text.startswith('**Summary.**') and '__after_summary__' in inserts: out.append(inserts['__after_summary__'])
        i = j
    if in_methods: out.append('</div>')
    return '\n'.join(out)

def build(n, slug, kicker, inserts):
    md = (ROOT/'drafts'/f'{n}-{slug}.md').read_text()
    title = re.search(r'^# (.*)$', md, re.M).group(1)
    body = md_to_html(md, inserts, kicker)
    page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Finding {int(n)}: {html.escape(title)}</title>
{STYLE}
</head>
<body>
<main>
  <nav class="nav"><a href="../circuit.html">Circuit view</a><a href="index.html">List view</a><a href="../index.html">Home</a></nav>
{body}
</main>
</body>
</html>
'''
    (ROOT/'docs/findings'/f'{n}-{slug}.html').write_text(page)
    print('built', f'{n}-{slug}.html')

def snip(name): return (FIG/f'{name}.html').read_text()

if __name__ == '__main__':
    build('01', 'synaptic-store', 'Finding 1 of 4 · the missing middle of the circuit', {
        '__after_summary__': snip('store-anim'),
        'Two ways to hold a running sum': snip('two-ways'),
        'What the wiring points to': snip('worked-example') + snip('convergence'),
    })
    build('02', 'return-inverter', 'Finding 2 of 4 · the sign problem', {
        '__after_summary__': snip('sign-question'),
        'Why that is wrong': snip('arbor-cases'),
        'Where the rotation actually happens': snip('two-routes'),
        'The simulation check': snip('return-anim'),
    })
    build('03', 'velocity-sources', 'Finding 3 of 4 · unnamed inputs to a solved circuit', {
        '__after_summary__': snip('velocity-fig'),
    })
    build('04', 'compass-brake', 'Finding 4 of 4 · most against the models', {
        '__after_summary__': snip('brake-fig'),
        'What the model shows': snip('brake-anim'),
    })
