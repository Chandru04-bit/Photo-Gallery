import glob, os, re

root = "."
files = sorted(glob.glob("*.html") + glob.glob("pages/**/*.html", recursive=True))

print(f"Total HTML files: {len(files)}")

report = []
for f in files:
    with open(f, "r", encoding="utf-8", errors="ignore") as fp:
        c = fp.read()
    has_dark_css = bool(re.search(r'href=["\'][^"\']*dark-mode\.css["\']', c))
    has_theme_btn = bool(re.search(r'id=["\']themeToggleBtn["\']|class=["\'][^"\']*theme-toggle-btn[^"\']*["\']', c))
    has_early_script = "theme" in c[:c.find("</head>")] if "</head>" in c else False
    has_main_js = bool(re.search(r'src=["\'][^"\']*main\.js["\']', c))
    report.append((f, has_dark_css, has_theme_btn, has_early_script, has_main_js))

for r in report:
    print(f"{r[0]:40} | DarkCSS: {str(r[1]):5} | ToggleBtn: {str(r[2]):5} | EarlyHead: {str(r[3]):5} | MainJS: {str(r[4]):5}")
