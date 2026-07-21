import cv2
import numpy as np

def print_ascii(img_path, y_range, x_range, w=80):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    h_img, w_img = img.shape
    
    y1, y2 = int(y_range[0] * h_img), int(y_range[1] * h_img)
    x1, x2 = int(x_range[0] * w_img), int(x_range[1] * w_img)
    
    crop = img[y1:y2, x1:x2]
    _, thresh = cv2.threshold(crop, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Scale to fit terminal
    scale_w = w
    scale_h = int(crop.shape[0] * (scale_w / crop.shape[1]) * 0.45)
    resized = cv2.resize(thresh, (scale_w, scale_h), interpolation=cv2.INTER_AREA)
    
    for row in resized:
        line = "".join([" " if pixel > 127 else "#" for pixel in row])
        print(line)

print("\n--- 2024 Back (2024b.png) - Q4a Matrix ---")
# Q4a matrix is located in the upper portion of 2024b.png, typically on the right or center.
# Let's crop y from 0.05 to 0.15, x from 0.35 to 0.65
print_ascii("/Users/aayushsapkota9/repos/oxford/agentic-exams/nm/past-qn-images/2024b.png", (0.02, 0.14), (0.35, 0.65), w=60)

print("\n--- 2025 Back (2025back.png) - Q4b Crout Method ---")
# Q4b is located in the upper middle portion of 2025back.png
# Let's crop y from 0.10 to 0.25, x from 0.05 to 0.95
print_ascii("/Users/aayushsapkota9/repos/oxford/agentic-exams/nm/past-qn-images/2025back.png", (0.12, 0.22), (0.05, 0.95), w=100)
