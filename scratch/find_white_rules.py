with open(r'd:\Sattvic Books\style.css', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's check occurrences of color: #FFFFFF !important on buttons
import re

matches = re.findall(r'(\.[a-zA-Z0-9_\-\s,.:>]+)\{\s*([^}]+color:\s*#(?:FFFFFF|fff)\s*!important[^}]*)\}', text, re.IGNORECASE)
print(f"Total rules with color: #FFFFFF !important: {len(matches)}")
for sel, body in matches:
    if any(k in sel for k in ['btn', 'button', 'pill', 'tab', 'asset']):
        print("SELECTOR:", sel.strip())
        for l in body.split(';'):
            if 'color' in l or 'background' in l:
                print("   ", l.strip())
        print("-" * 30)

