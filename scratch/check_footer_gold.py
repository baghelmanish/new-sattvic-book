from PIL import Image
import numpy as np

im = Image.open(r'C:\Users\snssystem\.gemini\antigravity\brain\759ab44a-00fb-4289-9607-47a4eec89958\scratch\footer_col1.png')
# Check if there is gold color in footer_col1
arr = np.array(im)
# gold is high R, high G, lower B (e.g. R > 180, G > 140, B < 100)
gold_pixels = (arr[:, :, 0] > 180) & (arr[:, :, 1] > 140) & (arr[:, :, 2] < 120)
print("Gold pixel count in footer col 1:", np.sum(gold_pixels))

