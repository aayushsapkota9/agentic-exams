import cv2
import numpy as np

img = cv2.imread("/Users/aayushsapkota9/repos/oxford/agentic-exams/tmp/crop_4a.png", cv2.IMREAD_GRAYSCALE)
_, thresh = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY_INV)

# Find contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(f"Found {len(contours)} contours")

# Filter contours that look like matrices or large text blocks
candidates = []
for idx, cnt in enumerate(contours):
    x, y, w, h = cv2.boundingRect(cnt)
    # A matrix is usually relatively square and larger than individual letters
    if w > 40 and h > 40:
        candidates.append((x, y, w, h))
        print(f"Candidate {idx}: x={x}, y={y}, w={w}, h={h}")

# Sort candidates by x coordinate
candidates = sorted(candidates, key=lambda c: c[0])

for idx, (x, y, w, h) in enumerate(candidates):
    print(f"\n--- Candidate {idx} at x={x}, y={y}, w={w}, h={h} ---")
    crop = thresh[y:y+h, x:x+w]
    
    # Scale to fit terminal
    scale_w = 60
    scale_h = int(h * (scale_w / w) * 0.5)
    if scale_h < 5: scale_h = 5
    resized = cv2.resize(crop, (scale_w, scale_h), interpolation=cv2.INTER_AREA)
    
    for row in resized:
        line = "".join(["#" if pixel > 127 else " " for pixel in row])
        print(line)
