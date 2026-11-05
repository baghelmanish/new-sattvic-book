import re

with open("D:/Sattvic Books/events.html", "r", encoding="utf-8") as f:
    text = f.read()

sections = re.findall(r'<section[^>]*>[\s\S]*?(?=<section|<footer)', text)
for i, s in enumerate(sections):
    m_h = re.search(r'<h[1-3][^>]*>(.*?)</h[1-3]>', s)
    m_eyebrow = re.search(r'class=["\'][^"\']*eyebrow[^"\']*["\'][^>]*>([^<]+)', s)
    bg = re.search(r'background(?:-color)?:\s*([^;"\']+)', s)
    h_text = m_h.group(1).strip() if m_h else "No H"
    e_text = m_eyebrow.group(1).strip() if m_eyebrow else "No Eyebrow"
    bg_text = bg.group(1).strip() if bg else "default"
    print(f"Sec {i+1}: {bg_text} | Eyebrow: {e_text} | Title: {h_text[:45]}")

