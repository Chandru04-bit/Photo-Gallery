with open("assets/css/dark-mode.css", "r", encoding="utf-8") as f:
    dark_css = f.read()

# Let's check common bootstrap utility overrides in dark-mode.css
utilities = [".bg-white", ".bg-light", ".text-dark", ".text-muted", ".card", ".navbar", ".breadcrumb", ".table", ".accordion", ".modal", ".badge"]

print("Bootstrap classes in dark-mode.css:")
for u in utilities:
    print(f"  {u:20}: {'FOUND' if u in dark_css else 'NOT FOUND'}")
