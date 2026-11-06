import glob, os, re

files = sorted(glob.glob("*.html") + glob.glob("pages/**/*.html", recursive=True))

standard_head_script = """  <script>
    (function() {
      try {
        const savedDir = localStorage.getItem('utsav_direction') || localStorage.getItem('direction') || 'ltr';
        document.documentElement.setAttribute('dir', savedDir);
        const savedTheme = localStorage.getItem('utsav_theme') || localStorage.getItem('theme') || 'light';
        document.documentElement.setAttribute('data-theme', savedTheme);
      } catch (e) {}
    })();
  </script>"""

updated_files = 0

for f in files:
    with open(f, "r", encoding="utf-8") as fp:
        content = fp.read()
    
    # Check if there is an existing early script before </head>
    # Pattern to match the existing early direction script
    pattern = re.compile(r'  <script>\s*\(function\(\)\s*\{.*?\}\)\(\);\s*</script>', re.DOTALL)
    
    if pattern.search(content):
        new_content = pattern.sub(standard_head_script, content, count=1)
        if new_content != content:
            with open(f, "w", encoding="utf-8") as fp:
                fp.write(new_content)
            updated_files += 1
            print(f"Updated early script in {f}")
    else:
        # If no script exists, insert right before </head>
        if "</head>" in content:
            new_content = content.replace("</head>", f"{standard_head_script}\n</head>", 1)
            with open(f, "w", encoding="utf-8") as fp:
                fp.write(new_content)
            updated_files += 1
            print(f"Inserted early script in {f}")

print(f"\nCompleted early script update across {updated_files} / {len(files)} files.")
