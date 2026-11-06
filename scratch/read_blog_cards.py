with open('blog.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'blog-' in line:
        start = max(0, i-5)
        end = min(len(lines), i+15)
        print(f"--- Line {i+1} ---")
        print("".join(lines[start:end]))
