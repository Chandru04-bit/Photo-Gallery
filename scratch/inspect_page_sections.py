import glob, re

for page in ["about.html", "services.html", "pricing.html", "contact.html", "gallery.html", "pages/services/wedding-stage.html"]:
    with open(page, "r", encoding="utf-8") as f:
        c = f.read()
    sections = re.findall(r'<section[^>]*class=["\']([^"\']+)["\']', c)
    print(f"\n=== {page} Sections ===")
    for s in sections:
        print("  <section class=\"" + s + "\">")
