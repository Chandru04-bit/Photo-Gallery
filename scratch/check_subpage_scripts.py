with open("pages/services/wedding-stage.html", "r", encoding="utf-8") as f:
    c = f.read()

import re
scripts = re.findall(r'<script[^>]*src=["\']([^"\']+)["\']', c)
print("Scripts in pages/services/wedding-stage.html:")
for s in scripts:
    print("  ", s)
