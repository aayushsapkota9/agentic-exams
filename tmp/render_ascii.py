import cv2
import numpy as np

# Load cropped image
img = cv2.imread("/Users/aayushsapkota9/repos/oxford/agentic-exams/tmp/crop_4a.png", cv2.IMREAD_GRAYSCALE)

# Otsu's thresholding
_, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Resize to fit console
w = 220
h = int(thresh.shape[0] * (w / thresh.shape[1]) * 0.45)
resized = cv2.resize(thresh, (w, h), interpolation=cv2.INTER_AREA)

print(f"Otsu ASCII rendering of crop_4a.png ({img.shape[1]}x{img.shape[0]} scaled to {w}x{h}):")
for row in resized:
    # Since background is white (255) and text is black (0):
    line = "".join([" " if pixel > 127 else "#" for pixel in row])
    print(line)
