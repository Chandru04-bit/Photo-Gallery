import glob
import os
import re

# 1. Update style.css
with open("assets/css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Replace process section rules
proc_css_pattern = r"\.process-section\s*\{.*?(?=\/\* ==========================================================================\s*Pricing Packages Section)"
new_proc_css = """.process-section {
  padding: 90px 0;
  background: #FFFFFF;
}

.process-step-card {
  text-align: center;
  position: relative;
  padding: 30px 20px;
  background: #FFFFFF;
  border: 1px solid var(--color-border) !important;
  border-radius: var(--radius-md);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04);
  transition: all 0.35s cubic-bezier(0.25, 0.8, 0.25, 1);
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
}

.process-step-card:hover {
  transform: translateY(-8px);
  border-color: var(--color-gold) !important;
  box-shadow: 0 16px 36px rgba(91, 20, 37, 0.12) !important;
}

.process-icon-wrap {
  width: 72px;
  height: 72px;
  margin: 0 auto 1.25rem;
  border-radius: 50%;
  background: var(--color-cream);
  border: 2px solid var(--color-gold);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.75rem;
  color: var(--color-maroon);
  position: relative;
  transition: var(--transition);
  box-shadow: 0 4px 12px rgba(198, 161, 91, 0.18);
  flex-shrink: 0;
}

.process-step-card:hover .process-icon-wrap {
  background: var(--color-maroon);
  color: var(--color-gold);
  border-color: var(--color-gold);
  transform: scale(1.08);
  box-shadow: 0 6px 18px rgba(91, 20, 37, 0.25);
}

.process-step-num {
  position: absolute;
  top: -4px;
  right: -4px;
  background: var(--color-gold);
  color: var(--color-maroon-dark);
  font-weight: 700;
  font-size: 0.78rem;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 2px solid #FFFFFF;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
  transition: var(--transition);
}

.process-step-card:hover .process-step-num {
  background: #FFFFFF;
  color: var(--color-maroon);
  border-color: var(--color-gold);
}

.process-step-card h5,
.process-step-card h6 {
  color: var(--color-maroon);
  font-family: var(--font-heading);
  font-size: 1.1rem;
  font-weight: 700;
  letter-spacing: 0.3px;
  margin-bottom: 0.6rem;
  transition: var(--transition);
}

.process-step-card:hover h5,
.process-step-card:hover h6 {
  color: var(--color-maroon-light);
}

.process-step-card p {
  color: var(--color-muted);
  line-height: 1.55;
  font-size: 0.85rem;
  margin-bottom: 0;
}

.step-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background: var(--color-cream);
  color: var(--color-maroon);
  border: 2px solid var(--color-gold);
  font-weight: 700;
  font-size: 1.2rem;
  margin-bottom: 1rem;
  transition: var(--transition);
}

.process-step-card:hover .step-badge {
  background: var(--color-maroon);
  color: var(--color-gold);
  transform: scale(1.08);
}

"""

if re.search(proc_css_pattern, css, re.DOTALL):
    css = re.sub(proc_css_pattern, new_proc_css, css, flags=re.DOTALL)
    with open("assets/css/style.css", "w", encoding="utf-8") as f:
        f.write(css)
    print("SUCCESS: Updated process cards CSS in style.css")
else:
    print("FAILED: Could not find process-section block in style.css")

# 2. Update dark-mode.css
with open("assets/css/dark-mode.css", "r", encoding="utf-8") as f:
    dark_css = f.read()

dark_proc_rules = """
/* Dark Mode Process Step Cards */
[data-theme="dark"] .process-step-card {
  background-color: #22181C !important;
  border-color: var(--color-border) !important;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3) !important;
}

[data-theme="dark"] .process-step-card:hover {
  border-color: var(--color-gold) !important;
  box-shadow: 0 16px 36px rgba(0, 0, 0, 0.5) !important;
}

[data-theme="dark"] .process-icon-wrap {
  background: #2E1F24 !important;
  border-color: var(--color-gold) !important;
  color: var(--color-gold-light) !important;
}

[data-theme="dark"] .process-step-card:hover .process-icon-wrap {
  background: var(--color-gold) !important;
  color: #1A1416 !important;
}

[data-theme="dark"] .process-step-num {
  border-color: #22181C !important;
  background: var(--color-gold);
  color: #1A1416;
}

[data-theme="dark"] .process-step-card:hover .process-step-num {
  background: #2E1F24 !important;
  color: var(--color-gold-light) !important;
  border-color: var(--color-gold) !important;
}

[data-theme="dark"] .process-step-card h5,
[data-theme="dark"] .process-step-card h6 {
  color: #F8EAD6 !important;
}

[data-theme="dark"] .process-step-card p {
  color: #BCAFA8 !important;
}

[data-theme="dark"] .step-badge {
  background: #2E1F24 !important;
  border-color: var(--color-gold) !important;
  color: var(--color-gold-light) !important;
}
"""

if "[data-theme=\"dark\"] .process-step-card" not in dark_css:
    dark_css += dark_proc_rules
    with open("assets/css/dark-mode.css", "w", encoding="utf-8") as f:
        f.write(dark_css)
    print("SUCCESS: Appended dark mode process step rules to dark-mode.css")
else:
    print("dark-mode.css already has process step card rules")

# 3. Update all 9 HTML files
step_cards_replacement = """      <div class="row g-4">
        <div class="col-lg col-md-4 col-sm-6 reveal-fade-up">
          <div class="process-step-card p-4 rounded-4 border text-center h-100 shadow-sm bg-white">
            <div class="process-icon-wrap mb-3">
              <span class="process-step-num">1</span>
              <i class="bi bi-rulers"></i>
            </div>
            <h6 class="fw-bold mb-2">Venue Survey</h6>
            <p class="text-muted small mb-0">We measure venue dimensions, doorway clearance, and electrical breaker capacity.</p>
          </div>
        </div>

        <div class="col-lg col-md-4 col-sm-6 reveal-fade-up delay-100">
          <div class="process-step-card p-4 rounded-4 border text-center h-100 shadow-sm bg-white">
            <div class="process-icon-wrap mb-3">
              <span class="process-step-num">2</span>
              <i class="bi bi-diagram-3-fill"></i>
            </div>
            <h6 class="fw-bold mb-2">CAD Blueprint</h6>
            <p class="text-muted small mb-0">Detailed 3D models with elevation views, color scheme, and guest sightlines.</p>
          </div>
        </div>

        <div class="col-lg col-md-4 col-sm-6 reveal-fade-up delay-200">
          <div class="process-step-card p-4 rounded-4 border text-center h-100 shadow-sm bg-white">
            <div class="process-icon-wrap mb-3">
              <span class="process-step-num">3</span>
              <i class="bi bi-tools"></i>
            </div>
            <h6 class="fw-bold mb-2">Fabrication</h6>
            <p class="text-muted small mb-0">Hardware staging, carpentry check, and direct farm fresh flower procurement.</p>
          </div>
        </div>

        <div class="col-lg col-md-4 col-sm-6 reveal-fade-up delay-300">
          <div class="process-step-card p-4 rounded-4 border text-center h-100 shadow-sm bg-white">
            <div class="process-icon-wrap mb-3">
              <span class="process-step-num">4</span>
              <i class="bi bi-hammer"></i>
            </div>
            <h6 class="fw-bold mb-2">On-Site Erection</h6>
            <p class="text-muted small mb-0">Platform leveled, pillars anchored, drapery steamed, and floral garlands hung.</p>
          </div>
        </div>

        <div class="col-lg col-md-4 col-sm-6 reveal-fade-up delay-400">
          <div class="process-step-card p-4 rounded-4 border text-center h-100 shadow-sm bg-white">
            <div class="process-icon-wrap mb-3">
              <span class="process-step-num">5</span>
              <i class="bi bi-lightbulb-fill"></i>
            </div>
            <h6 class="fw-bold mb-2">Lighting & Handover</h6>
            <p class="text-muted small mb-0">Lighting calibrated with photographer, stage swept clean, and handed over 5 hrs early.</p>
          </div>
        </div>
      </div>"""

target_pattern = r'<div class="row g-4">\s*<div class="col-lg col-md-4 col-sm-6 reveal-fade-up">.*?Lighting & Handover.*?</div>\s*</div>\s*</div>'

html_files = ["service-details.html"] + glob.glob("pages/services/*.html")
updated_count = 0

for hf in html_files:
    with open(hf, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "Venue Survey" in content:
        # Match from row g-4 up to the 5th card closing div
        new_content = re.sub(target_pattern, step_cards_replacement, content, flags=re.DOTALL)
        if new_content != content:
            with open(hf, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"SUCCESS: Updated {hf}")
            updated_count += 1
        else:
            print(f"PATTERN MISMATCH: Could not regex replace in {hf}")

print(f"\nTotal HTML files updated: {updated_count} / {len(html_files)}")
