import glob
import re

html_files = sorted(glob.glob(r'd:\Sattvic Books\*.html'))

old_hexes = ['#FAF7F2', '#2C1E14', '#6A5A4D', '#A07C32', '#4A3319', '#F7E9DC', '#F3E5D0', '#F5ECDB', '#F5E8D6']

print("=== REMAINING OLD HEX CODES SCAN ===")
found_any = False
for h in html_files:
    fname = h.split('\\')[-1]
    if fname in ['podcast_backup.html']:
        continue
    with open(h, 'r', encoding='utf-8') as f:
        content = f.read()
    
    matches = []
    for ox in old_hexes:
        count = content.count(ox)
        if count > 0:
            matches.append((ox, count))
    
    if matches:
        found_any = True
        print(f"[{fname}]: {matches}")

if not found_any:
    print("NO OLD HEX CODES FOUND IN ANY ACTIVE HTML FILE! 100% CLEAN!")

