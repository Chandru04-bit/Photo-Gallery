import re

# 1. Update style.css
with open("assets/css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

footer_start = css.find("/* ==========================================================================\n   Footer\n   ========================================================================== */")
if footer_start == -1:
    footer_start = css.find("/* ==========================================================================\r\n   Footer\r\n   ========================================================================== */")

footer_end = css.find("/* ==========================================================================\n   Back to Top Button")
if footer_end == -1:
    footer_end = css.find("/* ==========================================================================\r\n   Back to Top Button")

new_footer_css = """/* ==========================================================================
   Footer
   ========================================================================== */
.site-footer,
.footer-section,
footer {
  background: var(--color-maroon-dark);
  color: #EDE4DE;
  padding-top: 70px;
  border-top: 4px solid var(--color-gold);
  position: relative;
}

.footer-logo img,
.footer-logo {
  height: 52px;
  margin-bottom: 1.25rem;
}

.footer-about,
.site-footer p,
.footer-section p,
footer p {
  color: #EDE4DE !important;
  font-size: 0.95rem;
  line-height: 1.7;
}

.footer-about {
  margin-bottom: 1.25rem;
  color: #EDE4DE !important;
}

.footer-title,
.footer-widget-title,
.site-footer h3,
.site-footer h4,
.site-footer h5,
footer h3,
footer h4,
footer h5 {
  color: #FFFFFF !important;
  font-family: var(--font-heading);
  font-size: 1.25rem;
  margin-bottom: 1.5rem;
  position: relative;
  padding-bottom: 10px;
  font-weight: 700;
  letter-spacing: 0.5px;
}

.footer-title::after,
.footer-widget-title::after {
  content: '';
  position: absolute;
  bottom: 0;
  inset-inline-start: 0;
  left: 0;
  width: 40px;
  height: 2px;
  background: var(--color-gold);
}

.footer-links {
  list-style: none;
  padding: 0;
  margin: 0;
}

.footer-links li {
  margin-bottom: 10px;
}

.footer-links a {
  color: #EDE4DE;
  font-size: 0.9rem;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  transition: var(--transition);
}

.footer-links a i {
  color: var(--color-gold);
  font-size: 0.78rem;
}

.footer-links a:hover {
  color: var(--color-gold-light);
  transform: translateX(4px);
}

.footer-contact-item {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  margin-bottom: 14px;
  font-size: 0.9rem;
  color: #EDE4DE;
}

.footer-contact-item span {
  color: #EDE4DE;
  line-height: 1.5;
}

.footer-contact-item i {
  color: var(--color-gold);
  font-size: 1.1rem;
  margin-top: 2px;
}

.footer-social {
  display: flex;
  gap: 10px;
  margin-top: 1.5rem;
}

.footer-social a {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(198, 161, 91, 0.3);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  color: #FFFFFF;
  transition: var(--transition);
}

.footer-social a[aria-label="WhatsApp"] {
  display: none;
}

.footer-social a:hover {
  background: var(--color-gold);
  color: var(--color-maroon-dark);
  border-color: var(--color-gold);
  transform: translateY(-3px);
}

.footer-bottom {
  margin-top: 50px;
  padding: 20px 0;
  border-top: 1px solid rgba(255, 255, 255, 0.12);
  font-size: 0.85rem;
  color: #D8CCC4;
}

.footer-bottom a {
  color: var(--color-gold-light);
}

.footer-bottom a:hover {
  color: #FFFFFF;
  text-decoration: underline;
}

"""

if footer_start != -1 and footer_end != -1:
    css = css[:footer_start] + new_footer_css + css[footer_end:]
    with open("assets/css/style.css", "w", encoding="utf-8") as f:
        f.write(css)
    print("SUCCESS: Updated footer section in style.css")
else:
    print(f"FAILED to find footer section boundaries in style.css: start={footer_start}, end={footer_end}")

# 2. Update dark-mode.css
with open("assets/css/dark-mode.css", "r", encoding="utf-8") as f:
    dark_css = f.read()

dark_footer_rules = """
/* Dark Mode Footer Rules */
[data-theme="dark"] .site-footer,
[data-theme="dark"] .footer-section,
[data-theme="dark"] footer {
  background-color: #160D10 !important;
  color: #EDE4DE !important;
  border-top-color: var(--color-gold) !important;
}

[data-theme="dark"] .footer-about,
[data-theme="dark"] .site-footer p,
[data-theme="dark"] .footer-section p,
[data-theme="dark"] footer p {
  color: #EDE4DE !important;
}

[data-theme="dark"] .footer-contact-item,
[data-theme="dark"] .footer-contact-item span {
  color: #EDE4DE !important;
}

[data-theme="dark"] .footer-links a {
  color: #EDE4DE !important;
}

[data-theme="dark"] .footer-bottom {
  border-top-color: rgba(255, 255, 255, 0.1) !important;
  color: #D8CCC4 !important;
}
"""

if "[data-theme=\"dark\"] .site-footer" not in dark_css:
    dark_css += dark_footer_rules
    with open("assets/css/dark-mode.css", "w", encoding="utf-8") as f:
        f.write(dark_css)
    print("SUCCESS: Appended dark mode footer rules to dark-mode.css")
else:
    print("dark-mode.css already has footer rules")

# 3. Update register.html
with open("register.html", "r", encoding="utf-8") as f:
    reg_html = f.read()

if '<footer class="footer-section">' in reg_html:
    reg_html = reg_html.replace('<footer class="footer-section">', '<footer class="site-footer">')
    with open("register.html", "w", encoding="utf-8") as f:
        f.write(reg_html)
    print("SUCCESS: Updated register.html to use site-footer class")
