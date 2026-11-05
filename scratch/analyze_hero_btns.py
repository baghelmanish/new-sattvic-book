from PIL import Image

img = Image.open(r'C:\Users\snssystem\.gemini\antigravity\brain\759ab44a-00fb-4289-9607-47a4eec89958\scratch\hero_buttons_crop.jpg')
w, h = img.size
# left button is approx x: 50 to 180, right button is x: 190 to 330
left_btn = img.crop((int(w*0.1), int(h*0.2), int(w*0.48), int(h*0.8)))
right_btn = img.crop((int(w*0.52), int(h*0.2), int(w*0.95), int(h*0.8)))

def avg_color(im):
    pixels = list(im.getdata())
    r = sum(p[0] for p in pixels) // len(pixels)
    g = sum(p[1] for p in pixels) // len(pixels)
    b = sum(p[2] for p in pixels) // len(pixels)
    return f"RGB({r},{g},{b}) / #{r:02x}{g:02x}{b:02x}"

print("Left button avg color:", avg_color(left_btn))
print("Right button avg color:", avg_color(right_btn))

