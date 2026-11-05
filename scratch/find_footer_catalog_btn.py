with open(r'd:\Sattvic Books\style.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Look for all occurrences of footer-catalog-btn
print("=== All occurrences of footer-catalog-btn ===")
for m in re.finditer(r'footer-catalog-btn', text):
    start = max(0, m.start() - 100)
    end = min(len(text), m.end() + 200)
    print(text[start:end].strip())
    print("-" * 40)

