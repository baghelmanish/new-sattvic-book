with open(r'd:\Sattvic Books\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Let's inspect line 1475 to 1525
import re
match = re.search(r'/\* Footer Download Free Catalog Button \*/.*?(?=\.social-links)', css, re.DOTALL)
if match:
    print("Found old footer button block:")
    print(match.group(0)[:200])
else:
    print("Could not find footer button block with regex")

