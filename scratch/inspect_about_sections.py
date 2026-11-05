with open(r'd:\Sattvic Books\about.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'<section', text)]
for idx in matches:
    print(text[idx:idx+200])
    print("-" * 30)

