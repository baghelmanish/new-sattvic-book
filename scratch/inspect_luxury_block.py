with open(r'd:\Sattvic Books\style.css', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('LUXURY CREAM & GOLD MASTER PALETTE ENHANCEMENTS')
if idx != -1:
    print(text[idx:idx+5000])

