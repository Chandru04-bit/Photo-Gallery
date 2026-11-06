with open("assets/js/main.js", "r", encoding="utf-8") as f:
    js = f.read()

import re
matches = re.findall(r'.{0,100}(?:theme|dark-mode|themeToggleBtn|data-theme).{0,200}', js, re.IGNORECASE | re.DOTALL)
print(f"Found {len(matches)} matches in main.js:")
for m in matches[:10]:
    print("--- MATCH ---")
    print(m.strip().replace("\n", " "))
