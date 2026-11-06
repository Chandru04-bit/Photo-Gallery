import glob, re

files = sorted(glob.glob("*.html") + glob.glob("pages/**/*.html", recursive=True) + glob.glob("assets/js/*.js"))

print("Searching localStorage across all files:")
for f in files:
    with open(f, "r", encoding="utf-8", errors="ignore") as fp:
        c = fp.read()
    matches = re.findall(r'localStorage\.[a-zA-Z0-9_]+\([^)]*\)', c)
    if matches:
        print(f"=== {f} ===")
        for m in set(matches):
            print("  ", m)
