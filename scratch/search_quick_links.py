import glob, re

root = "."
for f in sorted(glob.glob("*.html") + glob.glob("pages/**/*.html", recursive=True)):
    with open(f, "r", encoding="utf-8", errors="ignore") as fp:
        c = fp.read()
    m = re.search(r'Quick Links', c)
    if m:
        pos = m.start()
        print(f"=== {f} ===")
        print(c[max(0, pos-100):min(len(c), pos+150)])
        break
