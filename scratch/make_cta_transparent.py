with open("assets/css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

old_cta_block = """.cta-section {
  position: relative;
  background: linear-gradient(135deg, #350A14 0%, #521221 50%, #300812 100%);
  color: #FFFFFF;
  padding: 85px 0;
  text-align: center;
  border-top: 2px solid rgba(198, 161, 91, 0.35);
  border-bottom: 2px solid rgba(198, 161, 91, 0.35);
}

.cta-box {
  max-width: 760px;
  margin: 0 auto;
  position: relative;
  z-index: 2;
}

.cta-box h2 {
  color: #FFFFFF;
  font-size: 2.8rem;
  margin-bottom: 1rem;
}

.cta-box p {
  color: #E2D9D2;
  font-size: 1.15rem;
  margin-bottom: 2rem;
}"""

new_cta_block = """.cta-section {
  position: relative;
  background: transparent;
  color: var(--color-charcoal);
  padding: 85px 0;
  text-align: center;
}

.cta-box {
  max-width: 760px;
  margin: 0 auto;
  position: relative;
  z-index: 2;
}

.cta-box h2 {
  color: var(--color-maroon);
  font-family: var(--font-heading);
  font-size: 2.8rem;
  font-weight: 700;
  margin-bottom: 1rem;
}

.cta-box h2 span {
  color: var(--color-gold-dark);
}

.cta-box p {
  color: var(--color-muted);
  font-size: 1.15rem;
  margin-bottom: 2rem;
  line-height: 1.7;
}

.cta-section .btn-outline-light-custom,
.cta-box .btn-outline-light-custom {
  background: transparent;
  color: var(--color-maroon) !important;
  border: 1.5px solid var(--color-maroon);
}

.cta-section .btn-outline-light-custom:hover,
.cta-box .btn-outline-light-custom:hover {
  background: var(--color-maroon);
  color: #FFFFFF !important;
  border-color: var(--color-maroon);
  box-shadow: 0 4px 14px rgba(91, 20, 37, 0.2);
}"""

if old_cta_block in css:
    css = css.replace(old_cta_block, new_cta_block)
    with open("assets/css/style.css", "w", encoding="utf-8") as f:
        f.write(css)
    print("SUCCESS: Updated cta-section in style.css (background removed)")
else:
    print("FAILED to find old_cta_block in style.css")

# Update dark-mode.css
with open("assets/css/dark-mode.css", "r", encoding="utf-8") as f:
    dark_css = f.read()

old_dark_cta = """/* Dark Mode CTA Section */
[data-theme="dark"] .cta-section {
  background: linear-gradient(135deg, #1A070D 0%, #280D16 50%, #15050A 100%) !important;
  border-top: 2px solid var(--color-border-gold) !important;
  border-bottom: 2px solid var(--color-border-gold) !important;
}"""

new_dark_cta = """/* Dark Mode CTA Section */
[data-theme="dark"] .cta-section {
  background: transparent !important;
  color: #EDE4DE !important;
}

[data-theme="dark"] .cta-box h2 {
  color: #F8EAD6 !important;
}

[data-theme="dark"] .cta-box h2 span {
  color: var(--color-gold-light) !important;
}

[data-theme="dark"] .cta-box p {
  color: #BCAFA8 !important;
}

[data-theme="dark"] .cta-section .btn-outline-light-custom,
[data-theme="dark"] .cta-box .btn-outline-light-custom {
  border-color: var(--color-gold) !important;
  color: var(--color-gold-light) !important;
  background: transparent !important;
}

[data-theme="dark"] .cta-section .btn-outline-light-custom:hover,
[data-theme="dark"] .cta-box .btn-outline-light-custom:hover {
  background: var(--color-gold) !important;
  color: #1A1416 !important;
  border-color: var(--color-gold) !important;
}"""

if old_dark_cta in dark_css:
    dark_css = dark_css.replace(old_dark_cta, new_dark_cta)
    with open("assets/css/dark-mode.css", "w", encoding="utf-8") as f:
        f.write(dark_css)
    print("SUCCESS: Updated dark-mode.css for transparent CTA")
else:
    print("FAILED to find old_dark_cta in dark-mode.css")
