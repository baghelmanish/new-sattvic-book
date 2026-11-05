import re

with open("D:/Sattvic Books/reading-partners.html", "r", encoding="utf-8") as f:
    text = f.read()

lines = text.split("\n")
for i, line in enumerate(lines):
    if re.search(r'<(a|button)[^>]*class=["\'][^"\']*btn', line):
        print(f"Line {i+1}: {line.strip()[:140]}")

