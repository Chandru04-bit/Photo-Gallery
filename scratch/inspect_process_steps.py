import glob
import os
import re

files = glob.glob('*.html') + glob.glob('pages/**/*.html', recursive=True)
matching_files = []

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    if 'Venue Survey' in c:
        matching_files.append(f)
        # Find start of the row
        idx = c.find('Venue Survey')
        row_start = c.rfind('<div class="row', 0, idx)
        row_end = c.find('</section>', idx)
        print(f"\n--- {f} ---")
        print(c[row_start:idx+150])

print(f"\nTotal matching files: {len(matching_files)}")
