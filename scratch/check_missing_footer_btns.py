with open(r'd:\Sattvic Books\press-kit.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'<a[^>]*footer-catalog-btn[^>]*>.*?</a>', text, re.DOTALL)
print("press-kit.html footer btn:", matches)

with open(r'd:\Sattvic Books\reading-partners.html', 'r', encoding='utf-8') as f:
    rp_text = f.read()
rp_matches = re.findall(r'<a[^>]*footer-catalog-btn[^>]*>.*?</a>', rp_text, re.DOTALL)
print("reading-partners.html footer btn:", rp_matches)

