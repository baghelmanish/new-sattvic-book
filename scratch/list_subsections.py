with open(r'd:\Sattvic Books\style.css', 'r', encoding='utf-8') as f:
    text = f.read()

start_idx = text.find('/* 5. Featured Catalog (Explore Our Catalog)')
end_idx = text.find('UNIFIED LUXURY BUTTON SUITE')
end_idx = text.rfind('/*', 0, end_idx)

block = text[start_idx:end_idx]
import re
for m in re.finditer(r'/\*\s*(\d+\.[^*]+)\*/', block):
    print(m.group(1).strip())

