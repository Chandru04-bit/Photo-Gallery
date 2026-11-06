import os
import glob
import re

root_dir = os.path.abspath(".")
html_files = glob.glob(os.path.join(root_dir, "*.html")) + \
             glob.glob(os.path.join(root_dir, "pages", "**", "*.html"), recursive=True)

img_regex = re.compile(r'(<img[^>]+src=["\']([^"\']+)["\'][^>]*>)', re.IGNORECASE)

results = []
for h in html_files:
    rel_h = os.path.relpath(h, root_dir).replace("\\", "/")
    with open(h, "r", encoding="utf-8", errors="ignore") as fp:
        txt = fp.read()
    for full_tag, src in img_regex.findall(txt):
        alt_match = re.search(r'alt=["\']([^"\']*)["\']', full_tag, re.IGNORECASE)
        alt = alt_match.group(1) if alt_match else ""
        results.append((rel_h, src, alt))

with open("scratch/all_html_img_tags.txt", "w", encoding="utf-8") as out:
    for r in sorted(results):
        out.write(f"{r[0]} | {r[1]} | alt: '{r[2]}'\n")

print(f"Logged {len(results)} image tags to scratch/all_html_img_tags.txt")
