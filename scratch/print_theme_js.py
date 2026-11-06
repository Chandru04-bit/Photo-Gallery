with open("assets/js/main.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'Dark Mode Toggle' in l:
        print("".join(lines[max(0, i-2):min(len(lines), i+35)]))
