import cv2
import numpy as np

# Load image
img = cv2.imread("/Users/aayushsapkota9/repos/oxford/agentic-exams/tmp/crop_4a.png", cv2.IMREAD_GRAYSCALE)
_, thresh = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY_INV)

# Let's detect vertical lines using morphological opening
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 15))
vertical_lines = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

# Find coordinates of vertical lines
y_indices, x_indices = np.where(vertical_lines > 0)
if len(x_indices) > 0:
    min_x, max_x = np.min(x_indices), np.max(x_indices)
    min_y, max_y = np.min(y_indices), np.max(y_indices)
    print(f"Detected vertical line bounding box: x in [{min_x}, {max_x}], y in [{min_y}, {max_y}]")
    
    # Crop slightly wider to include brackets and all numbers
    # Let's crop y from min_y-10 to max_y+10, and x from min_x-20 to max_x+20
    crop_y1 = max(0, min_y - 20)
    crop_y2 = min(img.shape[0], max_y + 20)
    crop_x1 = max(0, min_x - 30)
    crop_x2 = min(img.shape[1], max_x + 30)
    
    matrix_crop = img[crop_y1:crop_y2, crop_x1:crop_x2]
    
    # Save the crop
    cv2.imwrite("/Users/aayushsapkota9/repos/oxford/agentic-exams/tmp/matrix_only.png", matrix_crop)
    print(f"Saved matrix crop to /Users/aayushsapkota9/repos/oxford/agentic-exams/tmp/matrix_only.png")
    
    # Print ASCII of just the matrix
    w = 80
    h = int(matrix_crop.shape[0] * (w / matrix_crop.shape[1]) * 0.5)
    resized = cv2.resize(matrix_crop, (w, h), interpolation=cv2.INTER_AREA)
    
    print("\n--- MATRIX ONLY ASCII ART ---")
    for row in resized:
        line = "".join([" " if pixel > 127 else "#" for pixel in row])
        print(line)
else:
    print("No vertical lines detected.")
