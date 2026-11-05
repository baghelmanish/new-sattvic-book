from PIL import Image

im = Image.open(r'C:\Users\snssystem\.gemini\antigravity\brain\759ab44a-00fb-4289-9607-47a4eec89958\scratch\footer_col1.png')
pixels = list(im.getdata())
gold_count = sum(1 for p in pixels if p[0] > 180 and p[1] > 140 and p[2] < 120)
print("Gold pixel count in footer col 1:", gold_count)
print("Total pixels:", len(pixels))

