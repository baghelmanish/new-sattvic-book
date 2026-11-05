import re

with open("D:/Sattvic Books/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Look for button-like classes on :hover that have transform translateY
btn_hover_blocks = re.findall(r'(\.[^{]*btn[^{]*:hover\s*\{[^}]*\})', css, re.IGNORECASE)
print(f"Total .btn:hover blocks found: {len(btn_hover_blocks)}")

violating_rules = []
for b in btn_hover_blocks:
    if "transform" in b and "translate" in b and "none" not in b:
        violating_rules.append(b)

print(f"Violating button hover rules with transform translate: {len(violating_rules)}")
for v in violating_rules:
    print(v)

