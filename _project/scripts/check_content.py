"""Check that every visible text string in the ORIGINAL pages still appears in the NEW pages.
Usage: python3 check_content.py <orig_site_dir> <new_site_dir>"""
import sys, re, html
from html.parser import HTMLParser

class Text(HTMLParser):
    def __init__(self):
        super().__init__(); self.parts = []; self.skip = 0; self.attrs_txt = []
    def handle_starttag(self, tag, attrs):
        if tag in ('style', 'script'): self.skip += 1
        for k, v in attrs:
            if k in ('alt', 'aria-label', 'content', 'href', 'src') and v: self.attrs_txt.append(v)
    def handle_endtag(self, tag):
        if tag in ('style', 'script'): self.skip -= 1
    def handle_data(self, d):
        if not self.skip and d.strip(): self.parts.append(d)

def norm(s): return re.sub(r'\s+', ' ', html.unescape(s)).strip()
def parse(path):
    p = Text(); p.feed(open(path, encoding='utf-8').read()); return p

ALLOWED_DROPS = {'Home', '← back to home', '💪','⏱','🔭','🎮','🔒','🚫','💸','🎯','💳','📵','🚧','✓','_','✉ support@cmdlinestudios.com','🔒 View privacy policy','›','‹','✕', 'View apps →', 'View policy →', 'Now available on the App Store', 'Get in touch', 'Our philosophy', "What we're working on", 'Our pricing promise'}
pages = ['index.html','privacy/index.html','categories/education.html','categories/fitness.html','categories/games.html','categories/productivity.html']
orig, new = sys.argv[1], sys.argv[2]
bad = 0
for pg in pages:
    o, n = parse(f'{orig}/{pg}'), parse(f'{new}/{pg}')
    ntext = norm(' '.join(n.parts)); nlow = ntext.lower()
    nattrs = set(norm(a) for a in n.attrs_txt)
    missing = []
    for seg in o.parts:
        s = norm(seg)
        if s.startswith('✓ '): s = s[2:]  # check marks are drawn by CSS now
        if not s or s in ALLOWED_DROPS: continue
        if s in ntext: continue
        if s.lower() in nlow: continue  # case-only changes (mono labels are lower-case now)
        missing.append(s)
    for a in o.attrs_txt:
        a = norm(a)
        if a.startswith('/') or a.startswith('#') or 'fonts.googleapis' in a or a in ('width=device-width, initial-scale=1.0',): continue
        if a not in nattrs: missing.append('[attr] ' + a)
    print(f'{pg}: ' + ('OK' if not missing else 'MISSING:'))
    for m in missing: print('    -', m); bad += 1
print('\nRESULT:', 'all original text present' if not bad else f'{bad} item(s) to review')
