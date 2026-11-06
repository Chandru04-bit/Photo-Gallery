with open("assets/css/rtl.css", "r", encoding="utf-8") as f:
    rtl_css = f.read()

target = """/* Footer in RTL */
[dir="rtl"] .footer-links {"""

replacement = """/* Footer in RTL */
[dir="rtl"] .footer-title::after,
[dir="rtl"] .footer-widget-title::after {
  left: auto !important;
  right: 0 !important;
}

[dir="rtl"] .footer-links {"""

if target in rtl_css:
    rtl_css = rtl_css.replace(target, replacement)
    with open("assets/css/rtl.css", "w", encoding="utf-8") as f:
        f.write(rtl_css)
    print("SUCCESS: Added RTL rule for footer-title::after in rtl.css")
else:
    print("FAILED: Target not found in rtl.css")
