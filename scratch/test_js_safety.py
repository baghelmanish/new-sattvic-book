import re

with open("D:/Sattvic Books/script.js", "r", encoding="utf-8") as f:
    js = f.read()

print("script.js byte length:", len(js))

# Check for unguarded document.getElementById or querySelector calls that might crash if element not found
lines = js.split("\n")
potential_unsafe_lines = []
for i, line in enumerate(lines):
    # If line does getElementById('xyz').addEventListener without checking if xyz exists
    if re.search(r'document\.(getElementById|querySelector)\([^)]+\)\.add', line):
        potential_unsafe_lines.append((i + 1, line.strip()))

print(f"Direct chained addEventListener calls without null check: {len(potential_unsafe_lines)}")
for ln, lstr in potential_unsafe_lines:
    print(f"  Line {ln}: {lstr}")

