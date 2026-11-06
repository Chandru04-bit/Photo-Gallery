with open("assets/css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

target = """.footer-widget-title {
  color: #FFFFFF;
  font-size: 1.25rem;
  margin-bottom: 1.5rem;
  position: relative;
  padding-bottom: 10px;
}

.footer-widget-title::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 40px;
  height: 2px;
  background: var(--color-gold);
}"""

replacement = """.footer-title,
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
}"""

if target in css:
    css = css.replace(target, replacement)
    with open("assets/css/style.css", "w", encoding="utf-8") as f:
        f.write(css)
    print("SUCCESS: Updated footer title rules in style.css")
else:
    print("FAILED: Target not found in style.css")
