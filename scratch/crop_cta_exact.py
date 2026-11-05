from PIL import Image

# Let's crop just the button in the left box of cta_large.png
im = Image.open(r'C:\Users\snssystem\.gemini\antigravity\brain\759ab44a-00fb-4289-9607-47a4eec89958\scratch\cta_large.png')
w, h = im.size

# Left half is Get Started box, bottom part is the button
btn_crop = im.crop((int(w * 0.05), int(h * 0.65), int(w * 0.45), int(h * 0.98)))
btn_crop.save(r'C:\Users\snssystem\.gemini\antigravity\brain\759ab44a-00fb-4289-9607-47a4eec89958\scratch\cta_btn_get_started.png')

# Right half is Subscribe box button
sub_crop = im.crop((int(w * 0.52), int(h * 0.65), int(w * 0.95), int(h * 0.98)))
sub_crop.save(r'C:\Users\snssystem\.gemini\antigravity\brain\759ab44a-00fb-4289-9607-47a4eec89958\scratch\cta_btn_subscribe.png')

print("Cropped cta_btn_get_started.png and cta_btn_subscribe.png")

