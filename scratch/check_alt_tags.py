import glob, os, re

root = os.path.abspath(".")
html_files = glob.glob(os.path.join(root, "*.html")) + glob.glob(os.path.join(root, "pages", "**", "*.html"), recursive=True)

missing_alt = []
img_tag_pattern = re.compile(r'<img\s+([^>]+)>', re.IGNORECASE)

for f in html_files:
    rel = os.path.relpath(f, root).replace("\\", "/")
    with open(f, "r", encoding="utf-8", errors="ignore") as fp:
        content = fp.read()
    
    for tag in img_tag_pattern.findall(content):
        src_m = re.search(r'src=["\']([^"\']+)["\']', tag, re.IGNORECASE)
        alt_m = re.search(r'alt=["\']([^"\']*)["\']', tag, re.IGNORECASE)
        src = src_m.group(1) if src_m else "NO_SRC"
        alt = alt_m.group(1) if alt_m else None
        
        if alt is None or alt.strip() == "":
            missing_alt.append((rel, src))

print(f"Total HTML files checked: {len(html_files)}")
print(f"Images with missing or empty alt tags: {len(missing_alt)}")
for rel, src in missing_alt[:10]:
    print(f"  In {rel}: {src}")
