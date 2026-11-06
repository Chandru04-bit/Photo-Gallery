import os
import glob
import hashlib
from collections import defaultdict
import re

root_dir = os.path.abspath(".")
images_dir = os.path.join(root_dir, "assets", "images")

# 1. Get all image files on disk
disk_images = {}
for root, dirs, files in os.walk(images_dir):
    for f in files:
        if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.svg', '.gif')):
            full_p = os.path.join(root, f)
            rel_p = os.path.relpath(full_p, root_dir).replace("\\", "/")
            with open(full_p, "rb") as fp:
                data = fp.read()
                h = hashlib.md5(data).hexdigest()
                size = len(data)
            disk_images[rel_p] = {"hash": h, "size": size, "full_path": full_p}

print(f"Total disk images in assets/images: {len(disk_images)}")

# Check duplicate hashes
hash_to_files = defaultdict(list)
for rel_p, info in disk_images.items():
    hash_to_files[info["hash"]].append(rel_p)

duplicates = {h: files for h, files in hash_to_files.items() if len(files) > 1}
print(f"\nDuplicate image contents ({len(duplicates)} sets):")
for h, files in duplicates.items():
    print(f"  Hash {h[:8]}: {', '.join(files)}")

# 2. Check all html files and find all image references
html_files = glob.glob(os.path.join(root_dir, "*.html")) + \
             glob.glob(os.path.join(root_dir, "pages", "**", "*.html"), recursive=True)

print(f"\nTotal HTML files found: {len(html_files)}")

all_refs = defaultdict(list)
missing_refs = []

img_regex = re.compile(r'(?:src=["\']|url\(["\']?)([^"\'\)\s]+\.(?:jpg|jpeg|png|webp|svg|gif))', re.IGNORECASE)

for html_path in html_files:
    rel_html = os.path.relpath(html_path, root_dir).replace("\\", "/")
    html_dir = os.path.dirname(html_path)
    with open(html_path, "r", encoding="utf-8", errors="ignore") as fp:
        content = fp.read()
    
    matches = img_regex.findall(content)
    for m in matches:
        if m.startswith("http") or m.startswith("//") or m.startswith("data:"):
            continue
        # Resolve target path relative to html file
        target_path = os.path.normpath(os.path.join(html_dir, m))
        rel_target = os.path.relpath(target_path, root_dir).replace("\\", "/")
        all_refs[rel_target].append((rel_html, m))
        if not os.path.exists(target_path):
            missing_refs.append((rel_html, m, rel_target))

print(f"\nTotal unique local image targets referenced in HTML: {len(all_refs)}")
if missing_refs:
    print(f"\nMISSING IMAGE REFERENCES ({len(missing_refs)}):")
    for src, raw, norm in missing_refs:
        print(f"  In {src}: {raw} -> {norm} (NOT FOUND!)")
else:
    print("\nNo missing image references found!")

# Let's list by folder in assets/images
folders = defaultdict(list)
for img in disk_images:
    folder = os.path.dirname(img)
    folders[folder].append(img)

print("\nImages by folder:")
for folder, imgs in sorted(folders.items()):
    print(f"\n{folder}/ ({len(imgs)} images):")
    for img in sorted(imgs):
        ref_count = len(all_refs.get(img, []))
        h = disk_images[img]["hash"][:8]
        dup = f"[DUP: {len(hash_to_files[disk_images[img]['hash']])} files]" if len(hash_to_files[disk_images[img]['hash']]) > 1 else ""
        print(f"  {os.path.basename(img):30} | {disk_images[img]['size']/1024:6.1f} KB | hash:{h} | Refs: {ref_count} {dup}")
