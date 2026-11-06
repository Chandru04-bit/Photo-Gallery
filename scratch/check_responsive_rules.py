import re

def check_css(filename):
    print(f"\n=== {filename} ===")
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    queries = re.findall(r'@media[^{]+\{', content)
    for q in queries:
        print("  ", q.strip())

check_css("assets/css/responsive.css")
check_css("assets/css/rtl.css")
