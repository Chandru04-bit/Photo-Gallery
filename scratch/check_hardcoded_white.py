import glob, re

files = sorted(glob.glob("*.html") + glob.glob("pages/**/*.html", recursive=True))

hardcoded_white_inline = []
pattern = re.compile(r'style=["\'][^"\']*(?:background|background-color):\s*(?:#fff|white)[^"\']*["\']', re.IGNORECASE)

for f in files:
    with open(f, "r", encoding="utf-8") as fp:
        c = fp.read()
    for m in pattern.finditer(c):
        hardcoded_white_inline.append((f, m.group(0)))

print(f"Hardcoded white inline backgrounds: {len(hardcoded_white_inline)}")
for f, s in hardcoded_white_inline:
    print(f"  In {f}: {s}")
