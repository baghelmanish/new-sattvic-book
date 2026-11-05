import re

with open("D:/Sattvic Books/events.html", "r", encoding="utf-8") as f:
    text = f.read()

lines = text.split("\n")
for i, line in enumerate(lines):
    if "class=" in line and "btn" in line:
        print(f"Line {i+1}: {line.strip()[:140]}")

