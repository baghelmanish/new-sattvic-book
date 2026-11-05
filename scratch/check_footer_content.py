from PIL import Image

f_im = Image.open(r'C:\Users\snssystem\.gemini\antigravity\brain\759ab44a-00fb-4289-9607-47a4eec89958\scratch\footer_large.png')
print("Footer size:", f_im.size)
# Let's save a crop of each column in the footer
w, h = f_im.size
col1 = f_im.crop((0, 0, int(w * 0.35), h))
col1.save(r'C:\Users\snssystem\.gemini\antigravity\brain\759ab44a-00fb-4289-9607-47a4eec89958\scratch\footer_col1.png')

col2 = f_im.crop((int(w * 0.35), 0, int(w * 0.65), h))
col2.save(r'C:\Users\snssystem\.gemini\antigravity\brain\759ab44a-00fb-4289-9607-47a4eec89958\scratch\footer_col2.png')

col3 = f_im.crop((int(w * 0.65), 0, w, h))
col3.save(r'C:\Users\snssystem\.gemini\antigravity\brain\759ab44a-00fb-4289-9607-47a4eec89958\scratch\footer_col3.png')

print("Saved footer columns")

