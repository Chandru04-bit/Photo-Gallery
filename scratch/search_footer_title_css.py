import glob, re

for f in glob.glob("assets/css/*.css"):
    with open(f, "r", encoding="utf-8") as fp:
        c = fp.read()
    matches = re.findall(r'([^{}]*footer-title[^{]*)\{([^}]+)\}', c)
    if matches:
        print(f"=== {f} ===")
        for sel, body in matches:
            print(sel.strip())
            print("  ", body.strip().replace("\n", " "))
