with open("assets/js/main.js", "r", encoding="utf-8") as f:
    js = f.read()

print(f"Total lines in main.js: {len(js.splitlines())}")
print(js[:1500])
