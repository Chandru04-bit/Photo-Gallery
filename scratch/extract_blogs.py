import re
import glob

with open('blog.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Find all occurrences of blog image files
pattern = re.compile(r'<img[^>]*src=["\']([^"\']*blog-\d\.jpg)["\'][^>]*alt=["\']([^"\']*)["\'][^>]*>', re.IGNORECASE)
for m in pattern.finditer(c):
    # Find next heading after image
    pos = m.end()
    snippet = c[pos:pos+500]
    heading = re.search(r'<h[2345][^>]*>(.*?)</h[2345]>', snippet, re.DOTALL)
    h_text = re.sub(r'<[^>]+>', '', heading.group(1)).strip() if heading else "None"
    print(f"Img: {m.group(1)} | Alt: {m.group(2)} | Title: {h_text}")

print("\n--- Blog Details Pages ---")
for f in sorted(glob.glob('pages/blog/*.html') + ['blog-details.html']):
    with open(f, 'r', encoding='utf-8') as fp:
        txt = fp.read()
    h1 = re.search(r'<h1[^>]*>(.*?)</h1>', txt, re.DOTALL)
    h1_text = re.sub(r'<[^>]+>', '', h1.group(1)).strip() if h1 else "No H1"
    imgs = re.findall(r'src=["\']([^"\']*blog-\d\.jpg)["\']', txt, re.IGNORECASE)
    print(f"{f:30} | H1: {h1_text[:60]} | Imgs: {imgs}")
