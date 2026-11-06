with open("about.html", "r", encoding="utf-8") as f:
    c = f.read()

import re
m = re.search(r'(<footer[^>]*>.*?</footer>)', c, re.DOTALL)
if m:
    print(m.group(1)[1000:2500])
