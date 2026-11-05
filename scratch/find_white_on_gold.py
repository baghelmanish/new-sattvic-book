import re

with open(r'd:\Sattvic Books\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Let's search for blocks with background gold and color white
blocks = re.findall(r'([^{}]+)\{([^{}]+)\}', css)
flagged = []
for selector, body in blocks:
    s = selector.strip()
    b = body.strip()
    # Check if selector looks like a button or tab
    if any(k in s.lower() for k in ['btn', 'button', 'cta', 'pill', 'tab']):
        # Check if background has gold and text has white
        has_gold_bg = any(g in b.lower() for g in ['var(--clr-gold)', '#c5a059', '#d4af37', '#e2c27e', '#dfbf77', 'gold']) and 'background' in b.lower()
        has_white_text = any(w in b.lower() for w in ['#ffffff', '#fff', 'white']) and ('color:' in b.lower() or 'color :' in b.lower())
        if has_gold_bg and has_white_text:
            flagged.append((s, b))

print(f"Flagged {len(flagged)} button/tab rules with gold bg and white text:")
for s, b in flagged:
    print(f"Selector: {s}")
    for line in b.split(';'):
        if 'color' in line.lower() or 'background' in line.lower():
            print(f"   {line.strip()}")
    print("-" * 40)

