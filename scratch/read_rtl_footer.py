with open('assets/css/rtl.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'footer' in l:
        print("".join(lines[max(0, i-2):min(len(lines), i+15)]))
