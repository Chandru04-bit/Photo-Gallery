import glob, re

root = "."
files = sorted(glob.glob("*.html") + glob.glob("pages/**/*.html", recursive=True))

title_types = {"footer-title": 0, "footer-widget-title": 0}

for f in files:
    with open(f, "r", encoding="utf-8") as fp:
        c = fp.read()
    t1 = len(re.findall(r'footer-title\b', c))
    t2 = len(re.findall(r'footer-widget-title\b', c))
    title_types["footer-title"] += t1
    title_types["footer-widget-title"] += t2
    if t1 > 0 or t2 > 0:
        print(f"{f:35} | footer-title: {t1} | footer-widget-title: {t2}")

print("\nTotals:", title_types)
