with open(r'd:\Sattvic Books\style.css', 'r', encoding='utf-8') as f:
    text = f.read()

root_idx = text.find(':root')
if root_idx != -1:
    print(text[root_idx:root_idx+1200])

