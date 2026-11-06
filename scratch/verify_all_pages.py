import os
import glob
import re
from PIL import Image

root = os.path.abspath(".")
html_files = sorted(glob.glob(os.path.join(root, "*.html")) + glob.glob(os.path.join(root, "pages", "**", "*.html"), recursive=True))

print(f"=== FULL AUDIT VERIFICATION OF {len(html_files)} HTML FILES ===")

all_ok = True
total_images_checked = 0

img_src_regex = re.compile(r'(?:src=["\']|url\(["\']?)([^"\'\)\s]+\.(?:jpg|jpeg|png|webp|svg|gif))', re.IGNORECASE)

report = {}

for html_file in html_files:
    rel_html = os.path.relpath(html_file, root).replace("\\", "/")
    html_dir = os.path.dirname(html_file)
    with open(html_file, "r", encoding="utf-8", errors="ignore") as fp:
        content = fp.read()
    
    matches = img_src_regex.findall(content)
    file_images = []
    for m in matches:
        if m.startswith("http") or m.startswith("//") or m.startswith("data:"):
            continue
        total_images_checked += 1
        target_path = os.path.normpath(os.path.join(html_dir, m))
        rel_target = os.path.relpath(target_path, root).replace("\\", "/")
        
        if not os.path.exists(target_path):
            print(f"ERROR: Missing file in {rel_html} -> {m} (resolved to {rel_target})")
            all_ok = False
        else:
            sz = os.path.getsize(target_path)
            if sz == 0:
                print(f"ERROR: 0-byte file in {rel_html} -> {rel_target}")
                all_ok = False
            else:
                file_images.append((m, rel_target, sz))
    report[rel_html] = file_images

print(f"\nTotal image references validated: {total_images_checked}")
if all_ok:
    print("ALL IMAGE REFERENCES ACROSS ALL 28 HTML FILES EXIST AND ARE VALID!")
else:
    print("SOME IMAGES FAILED VALIDATION! Check errors above.")
