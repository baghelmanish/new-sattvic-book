import os, re

html_files = [f for f in os.listdir("D:/Sattvic Books") if f.endswith(".html") and not f.startswith("podcast")]
for hf in html_files:
    with open(os.path.join("D:/Sattvic Books", hf), "r", encoding="utf-8") as f:
        content = f.read()
    footer_idx = content.find("<footer")
    if footer_idx != -1:
        after_footer = content[footer_idx:]
        buttons = re.findall(r'<a[^>]*class=["\'][^"\']*btn[^"\']*["\'][^>]*>.*?</a>', after_footer, re.DOTALL)
        print(f"=== {hf} (Total buttons in/after footer: {len(buttons)}) ===")
        for b in buttons:
            clean_b = re.sub(r'\s+', ' ', b)[:140]
            print("  ", clean_b)

