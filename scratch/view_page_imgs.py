import os
from collections import defaultdict

with open("scratch/all_html_img_tags.txt", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]

page_imgs = defaultdict(list)
for line in lines:
    parts = line.split(" | ")
    if len(parts) >= 2:
        page_imgs[parts[0]].append((parts[1], parts[2] if len(parts) > 2 else ""))

for page, imgs in sorted(page_imgs.items()):
    print(f"\n=== {page} ({len(imgs)} images) ===")
    for src, alt in imgs:
        print(f"   {src} [{alt}]")
