with open(r'd:\Sattvic Books\style.css', 'r', encoding='utf-8') as f:
    text = f.read()

root_start = text.find(':root')
root_end = text.find('}', root_start)
print(text[root_start:root_end+1])

