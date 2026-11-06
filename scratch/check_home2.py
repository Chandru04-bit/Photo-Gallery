import re

with open('home-2.html', 'r', encoding='utf-8') as f:
    c = f.read()

imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*alt=["\']([^"\']*)["\']', c)
for s, a in imgs:
    print(f"{s:50} | alt: {a}")
