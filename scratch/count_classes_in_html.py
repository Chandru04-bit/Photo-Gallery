import glob, re

files = sorted(glob.glob("*.html") + glob.glob("pages/**/*.html", recursive=True))

counts = {
    "bg-white": 0,
    "bg-light": 0,
    "text-dark": 0,
    "card": 0,
    "table": 0,
    "breadcrumb": 0
}

for f in files:
    with open(f, "r", encoding="utf-8") as fp:
        c = fp.read()
    for k in counts:
        counts[k] += len(re.findall(r'\b' + k + r'\b', c))

print("Occurrences across all 28 HTML files:")
for k, v in counts.items():
    print(f"  {k:15}: {v}")
