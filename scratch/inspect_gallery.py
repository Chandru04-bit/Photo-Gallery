import os
from PIL import Image

for root, dirs, files in os.walk("assets/images/gallery"):
    if files:
        print(f"\n--- {root} ---")
        for f in sorted(files):
            p = os.path.join(root, f)
            try:
                with Image.open(p) as img:
                    print(f"{f:25} | {img.size[0]}x{img.size[1]} | {img.format} | {os.path.getsize(p)/1024:6.1f} KB")
            except Exception as e:
                print(f"{f:25} | {e}")
