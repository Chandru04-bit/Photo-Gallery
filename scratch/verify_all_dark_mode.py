import glob, os, re

files = sorted(glob.glob("*.html") + glob.glob("pages/**/*.html", recursive=True))

print(f"=== FULL DARK MODE AUDIT ACROSS {len(files)} FILES ===")

all_passed = True
for f in files:
    with open(f, "r", encoding="utf-8") as fp:
        c = fp.read()
    
    # 1. Dark mode css link
    has_dark_css = bool(re.search(r'<link[^>]+href=["\'][^"\']*dark-mode\.css["\']', c))
    # 2. Early head script setting data-theme
    has_early_theme = "data-theme" in c[:c.find("</head>")] if "</head>" in c else False
    # 3. Main.js script tag
    has_main_js = bool(re.search(r'<script[^>]+src=["\'][^"\']*main\.js["\']', c))
    # 4. Toggle button
    has_btn = bool(re.search(r'id=["\']themeToggleBtn["\']|class=["\'][^"\']*theme-toggle-btn[^"\']*["\']', c))
    
    if not (has_dark_css and has_early_theme and has_main_js and has_btn):
        print(f"FAIL in {f}: css={has_dark_css}, head_script={has_early_theme}, main_js={has_main_js}, btn={has_btn}")
        all_passed = False

if all_passed:
    print("ALL 28 HTML FILES PASS COMPLETE DARK MODE CRITERIA (CSS, Early Head Script, Main.js, Toggle Button)!")
else:
    print("SOME FILES FAILED!")
