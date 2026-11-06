import os, glob, re

for f in sorted(glob.glob('pages/blogs/*.html')):
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*alt=["\']([^"\']*)["\']', c)
    print(f"\n=== {f} ===")
    for src, alt in imgs:
        print(f"   {src} | alt: '{alt}'")
