with open("assets/js/navigation.js", "r", encoding="utf-8") as f:
    nav_js = f.read()

import re
matches = re.findall(r'.{0,100}(?:theme|dark|toggle).{0,200}', nav_js, re.IGNORECASE | re.DOTALL)
print(f"Matches in navigation.js: {len(matches)}")
for m in matches:
    print("--- MATCH ---")
    print(m.strip().replace("\n", " "))
