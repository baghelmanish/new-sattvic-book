from PIL import Image

# Let's crop the buttons area specifically from crop_hero.jpg
img = Image.open(r'C:\Users\snssystem\.gemini\antigravity\brain\759ab44a-00fb-4289-9607-47a4eec89958\crop_hero.jpg')
w, h = img.size
# Buttons are near the bottom of hero crop
btn_crop = img.crop((0, int(h * 0.5), w, h))
btn_crop.save(r'C:\Users\snssystem\.gemini\antigravity\brain\759ab44a-00fb-4289-9607-47a4eec89958\scratch\hero_buttons_crop.jpg')
print("Saved hero_buttons_crop.jpg")

