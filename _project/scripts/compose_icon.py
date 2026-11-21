import json, re, sys, os
src, out = sys.argv[1], sys.argv[2]
cfg = json.load(open(os.path.join(src, "icon.json")))
def col(s):
    _, v = s.split(":")
    r, g, b, a = [float(x) for x in v.split(",")]
    return "#%02x%02x%02x" % (round(r*255), round(g*255), round(b*255))
defs, body = [], []
for gi, grp in enumerate(cfg["groups"]):
    for li, L in enumerate(grp["layers"]):
        svg = open(os.path.join(src, "Assets", L["image-name"])).read()
        paths = re.findall(r'<path d="([^"]+)"[^>]*?(?:fill-rule="([^"]+)")?[^>]*/>', svg)
        orig = re.search(r'fill="(#[0-9a-fA-F]{6})"', svg).group(1)
        f = L.get("fill")
        if f and "solid" in f:
            fill = col(f["solid"])
        elif f and "linear-gradient" in f:
            gid = "g%d_%d" % (gi, li)
            o = f["orientation"]
            c1, c2 = [col(c) for c in f["linear-gradient"]]
            defs.append('<linearGradient id="%s" gradientUnits="userSpaceOnUse" x1="%g" y1="%g" x2="%g" y2="%g"><stop offset="0" stop-color="%s"/><stop offset="1" stop-color="%s"/></linearGradient>' % (gid, o["start"]["x"]*1024, o["start"]["y"]*1024, o["stop"]["x"]*1024, o["stop"]["y"]*1024, c1, c2))
            fill = "url(#%s)" % gid
        else:
            fill = orig
        for d, rule in paths:
            body.append('<path d="%s" fill="%s" fill-rule="%s"/>' % (d, fill, rule or "nonzero"))
bg = col(cfg["fill"]["solid"])
svg = ('<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024" viewBox="0 0 1024 1024">'
       '<defs><clipPath id="sq"><rect width="1024" height="1024" rx="230"/></clipPath>%s</defs>'
       '<g clip-path="url(#sq)"><rect width="1024" height="1024" fill="%s"/>%s</g></svg>') % ("".join(defs), bg, "".join(body))
open(out, "w").write(svg)
print("ok", len(body), "paths")
