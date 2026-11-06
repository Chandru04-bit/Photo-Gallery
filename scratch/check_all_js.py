import glob, os

for f in sorted(glob.glob("assets/js/*.js")):
    print(f"=== {f} ({os.path.getsize(f)} bytes) ===")
    with open(f, "r", encoding="utf-8") as fp:
        lines = fp.readlines()
    print("  Lines:", len(lines))
