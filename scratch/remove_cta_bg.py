import os
import shutil
from PIL import Image, ImageDraw

# 1. Update style.css
with open("assets/css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

old_cta_css = """.cta-section {
  position: relative;
  background-image: linear-gradient(135deg, rgba(62, 11, 24, 0.92) 0%, rgba(91, 20, 37, 0.88) 100%),
                    url('../images/banners/cta-bg.jpg');
  background-size: cover;
  background-position: center;
  color: #FFFFFF;
  padding: 85px 0;
  text-align: center;
}"""

new_cta_css = """.cta-section {
  position: relative;
  background: linear-gradient(135deg, #350A14 0%, #521221 50%, #300812 100%);
  color: #FFFFFF;
  padding: 85px 0;
  text-align: center;
  border-top: 2px solid rgba(198, 161, 91, 0.35);
  border-bottom: 2px solid rgba(198, 161, 91, 0.35);
}"""

if old_cta_css in css:
    css = css.replace(old_cta_css, new_cta_css)
    with open("assets/css/style.css", "w", encoding="utf-8") as f:
        f.write(css)
    print("SUCCESS: Updated .cta-section in style.css (removed cta-bg.jpg photo background)")
else:
    # Try regex in case of slight whitespace variance
    import re
    pattern = r"\.cta-section\s*\{[^}]*background-image:[^}]*url\([^)]*cta-bg\.jpg[^)]*\)[^}]*\}"
    if re.search(pattern, css):
        css = re.sub(pattern, new_cta_css, css)
        with open("assets/css/style.css", "w", encoding="utf-8") as f:
            f.write(css)
        print("SUCCESS (regex): Updated .cta-section in style.css")
    else:
        print("FAILED: Could not find old .cta-section rule in style.css")

# 2. Update dark-mode.css
with open("assets/css/dark-mode.css", "r", encoding="utf-8") as f:
    dark_css = f.read()

dark_cta_rules = """
/* Dark Mode CTA Section */
[data-theme="dark"] .cta-section {
  background: linear-gradient(135deg, #1A070D 0%, #280D16 50%, #15050A 100%) !important;
  border-top: 2px solid var(--color-border-gold) !important;
  border-bottom: 2px solid var(--color-border-gold) !important;
}
"""

if "[data-theme=\"dark\"] .cta-section" not in dark_css:
    dark_css += dark_cta_rules
    with open("assets/css/dark-mode.css", "w", encoding="utf-8") as f:
        f.write(dark_css)
    print("SUCCESS: Added dark mode rules for .cta-section in dark-mode.css")
else:
    print("dark-mode.css already has .cta-section rule")

# 3. Backup and replace cta-bg.jpg with clean luxury gradient image
cta_bg_path = "assets/images/banners/cta-bg.jpg"
if os.path.exists(cta_bg_path):
    backup_file = "scratch/backup_original_images/banners_cta-bg.jpg"
    shutil.copy2(cta_bg_path, backup_file)
    print(f"Backed up {cta_bg_path} -> {backup_file}")
    
    # Generate clean luxury gradient image (1920x600)
    w, h = 1920, 600
    img = Image.new("RGB", (w, h))
    draw = ImageDraw.Draw(img)
    # Gradient from #350A14 to #521221 to #300812
    for y in range(h):
        ratio = y / h
        if ratio < 0.5:
            sub = ratio / 0.5
            r = int(53 + (82 - 53) * sub)
            g = int(10 + (18 - 10) * sub)
            b = int(20 + (33 - 20) * sub)
        else:
            sub = (ratio - 0.5) / 0.5
            r = int(82 + (48 - 82) * sub)
            g = int(18 + (8 - 18) * sub)
            b = int(33 + (18 - 33) * sub)
        draw.line([(0, y), (w, y)], fill=(r, g, b))
    img.save(cta_bg_path, "JPEG", quality=95)
    print(f"Replaced {cta_bg_path} with clean luxury gradient")

print("All CTA background removal steps complete!")
