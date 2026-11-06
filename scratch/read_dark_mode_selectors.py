with open("assets/css/dark-mode.css", "r", encoding="utf-8") as f:
    css = f.read()

import re
selectors = re.findall(r'([^{}]+)\s*\{', css)
print(f"Total CSS rules in dark-mode.css: {len(selectors)}")
unique_roots = set()
for s in selectors:
    parts = s.strip().split()
    if parts:
        unique_roots.add(parts[0])

print("Unique selector root elements in dark-mode.css:")
for r in sorted(unique_roots)[:25]:
    print("  ", r)
