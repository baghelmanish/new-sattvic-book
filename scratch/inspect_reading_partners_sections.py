with open(r'd:\Sattvic Books\reading-partners.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'<section', text)]
for idx in matches:
    print(text[idx:idx+150])
    print("-" * 30)

