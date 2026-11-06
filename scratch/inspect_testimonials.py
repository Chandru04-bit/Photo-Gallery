import os
from PIL import Image

for f in sorted(os.listdir('assets/images/testimonials')):
    p = os.path.join('assets/images/testimonials', f)
    with Image.open(p) as img:
        print(f"{f:20} | {img.size[0]}x{img.size[1]} | {img.format} | {os.path.getsize(p)/1024:.1f} KB")
