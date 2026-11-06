import os
from PIL import Image

def inspect_folder(folder):
    print(f"\n--- {folder} ---")
    for f in os.listdir(folder):
        p = os.path.join(folder, f)
        if os.path.isfile(p):
            try:
                with Image.open(p) as img:
                    print(f"{f:30} | {img.size[0]}x{img.size[1]} | {img.format} | {os.path.getsize(p)/1024:6.1f} KB")
            except Exception as e:
                print(f"{f:30} | NOT IMAGE ({e})")

inspect_folder("assets/images/banners")
inspect_folder("assets/images/blog")
inspect_folder("assets/images/services")
inspect_folder("assets/images/about")
