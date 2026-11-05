with open(r'd:\Sattvic Books\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

start_marker = "/* ==========================================================================\n   SITE-WIDE CLIENT SPECIFICATION PALETTE"
end_marker = "/* ==========================================================================\n   UNIFIED LUXURY BUTTON SUITE"

s_idx = css.find(start_marker)
e_idx = css.find(end_marker)

print("start_marker at:", s_idx)
print("end_marker at:", e_idx)

