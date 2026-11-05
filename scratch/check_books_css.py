with open(r'd:\Sattvic Books\style.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'(\.books[^{]*\{[^}]*\})', text)
print(f"Matches for .books: {len(matches)}")
for m in matches[:5]:
    print(m)
    print("---")

card_matches = re.findall(r'(\.sattvic-book-card[^{]*\{[^}]*\})', text)
print(f"Matches for .sattvic-book-card: {len(card_matches)}")
for m in card_matches[:5]:
    print(m)
    print("---")

