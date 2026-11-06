import glob, re

root = "."
files = sorted(glob.glob("*.html") + glob.glob("pages/**/*.html", recursive=True))

found_headings = []
for f in files:
    with open(f, "r", encoding="utf-8", errors="ignore") as fp:
        c = fp.read()
    m_footer = re.search(r'<footer[^>]*>(.*?)</footer>', c, re.DOTALL)
    if m_footer:
        footer_content = m_footer.group(1)
        headings = re.findall(r'<h[1-6][^>]*>(.*?)</h[1-6]>', footer_content, re.DOTALL)
        for h in headings:
            clean_h = re.sub(r'<[^>]+>', '', h).strip()
            found_headings.append((f, clean_h))

print(f"Total footer headings found across {len(files)} files: {len(found_headings)}")
unique_headings = set(h for _, h in found_headings)
print("Unique footer headings:")
for uh in sorted(unique_headings):
    print(f"  - '{uh}'")
