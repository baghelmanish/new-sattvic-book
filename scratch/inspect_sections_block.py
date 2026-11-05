with open(r'd:\Sattvic Books\style.css', 'r', encoding='utf-8') as f:
    text = f.read()

start_idx = text.find('/* 5. Featured Catalog (Explore Our Catalog)')
end_idx = text.find('/* ==========================================================================\n   UNIFIED LUXURY BUTTON SUITE')
if end_idx == -1:
    end_idx = text.find('UNIFIED LUXURY BUTTON SUITE')
    end_idx = text.rfind('/*', 0, end_idx)

print("Found block length:", end_idx - start_idx)
print(text[start_idx:start_idx+1500])
print("\n... middle ...\n")
print(text[end_idx-1000:end_idx])

