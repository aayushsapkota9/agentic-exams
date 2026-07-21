import os
from PIL import Image, ImageEnhance, ImageFilter

img_path = "/Users/aayushsapkota9/repos/oxford/agentic-exams/nm/past-qn-images/2024b.png"
img = Image.open(img_path)
width, height = img.size

# Crop the top 35% of the image
crop_box = (0, 0, width, int(height * 0.35))
cropped_img = img.crop(crop_box)

# Convert to grayscale and enhance contrast
cropped_gray = cropped_img.convert("L")
enhancer = ImageEnhance.Contrast(cropped_gray)
cropped_contrast = enhancer.enhance(3.0)

# Save cropped image
output_path = "/Users/aayushsapkota9/repos/oxford/agentic-exams/tmp/crop_4a.png"
cropped_contrast.save(output_path)
print(f"Cropped image saved to {output_path} with size {cropped_contrast.size}")
