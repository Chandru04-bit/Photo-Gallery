import glob, os, re

files = sorted(glob.glob("*.html") + glob.glob("pages/**/*.html", recursive=True))

for f in files:
    with open(f, "r", encoding="utf-8") as fp:
        c = fp.read()
    m = re.search(r'<link[^>]+href=["\']([^"\']*dark-mode\.css)["\']', c)
    if m:
        href = m.group(1)
        # resolve relative path
        d = os.path.dirname(f)
        target = os.path.normpath(os.path.join(d, href))
        exists = os.path.exists(target)
        if not exists:
            print(f"BROKEN CSS in {f}: {href} -> {target}")
    else:
        print(f"MISSING dark-mode.css link in {f}!")

print("All dark-mode.css paths checked.")
