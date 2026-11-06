import glob, re

files = sorted(glob.glob("*.html") + glob.glob("pages/**/*.html", recursive=True))

for f in files:
    with open(f, "r", encoding="utf-8") as fp:
        c = fp.read()
    btns = re.findall(r'<button[^>]+(?:themeToggleBtn|theme-toggle-btn)[^>]*>.*?</button>', c, re.DOTALL)
    print(f"=== {f} ({len(btns)} buttons) ===")
    for b in btns:
        print("  ", b.strip().replace("\n", " "))
