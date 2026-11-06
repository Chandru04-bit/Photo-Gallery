import glob, re

files = sorted(glob.glob("*.html") + glob.glob("pages/**/*.html", recursive=True))

print("Checking inline style backgrounds in HTML files:")
inline_bg_pattern = re.compile(r'style=["\'][^"\']*(?:background|bgcolor)[^"\']*["\']', re.IGNORECASE)

found_inline_bgs = []
for f in files:
    with open(f, "r", encoding="utf-8") as fp:
        c = fp.read()
    for m in inline_bg_pattern.finditer(c):
        style_val = m.group(0)
        # Check if it specifies white, cream, or light backgrounds
        if any(color in style_val.lower() for color in ['#fff', 'white', 'var(--color-cream)', 'rgb(255']):
            found_inline_bgs.append((f, style_val))

print(f"Total potential light inline backgrounds: {len(found_inline_bgs)}")
for f, s in found_inline_bgs[:15]:
    print(f"  In {f}: {s}")
