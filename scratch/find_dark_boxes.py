import os, re

html_files = [f for f in os.listdir("D:/Sattvic Books") if f.endswith(".html") and not f.startswith("podcast")]

for hf in html_files:
    with open(os.path.join("D:/Sattvic Books", hf), "r", encoding="utf-8") as f:
        text = f.read()

    # Find elements with dark backgrounds #322214 or linear-gradient
    matches = re.finditer(r'<([a-zA-Z0-9]+)[^>]*style=["\'][^"\']*(?:#322214|#20150D|#2C1E14)[^"\']*["\'][^>]*>', text)
    print(f"=== {hf} ===")
    for m in matches:
        print("  ", m.group(0)[:120])

