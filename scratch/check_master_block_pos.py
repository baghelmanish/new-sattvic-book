with open(r'd:\Sattvic Books\style.css', 'r', encoding='utf-8') as f:
    text = f.read()

start_marker = "/* ==========================================================================\n   HOMEPAGE CLIENT SPECIFICATION PALETTE"
end_marker = "/* ==========================================================================\n   UNIFIED LUXURY BUTTON SUITE"

s_idx = text.find(start_marker)
e_idx = text.find(end_marker)

print("start_marker at:", s_idx)
print("end_marker at:", e_idx)
print("Block length:", e_idx - s_idx if s_idx != -1 and e_idx != -1 else "NOT FOUND")

