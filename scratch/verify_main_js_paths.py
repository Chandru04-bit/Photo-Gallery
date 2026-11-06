import glob, os, re

files = sorted(glob.glob("*.html") + glob.glob("pages/**/*.html", recursive=True))

for f in files:
    with open(f, "r", encoding="utf-8") as fp:
        c = fp.read()
    m = re.search(r'<script[^>]+src=["\']([^"\']*main\.js)["\']', c)
    if m:
        src = m.group(1)
        d = os.path.dirname(f)
        target = os.path.normpath(os.path.join(d, src))
        exists = os.path.exists(target)
        if not exists:
            print(f"BROKEN main.js in {f}: {src} -> {target}")
    else:
        print(f"MISSING main.js script in {f}!")

print("All main.js paths checked.")
