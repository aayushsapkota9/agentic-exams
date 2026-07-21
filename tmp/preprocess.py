import cv2
import numpy as np
from PIL import Image
import os

images_dir = "/Users/aayushsapkota9/repos/oxford/agentic-exams/nm/past-qn-images"
output_dir = "/Users/aayushsapkota9/repos/oxford/agentic-exams/tmp/preprocessed"
os.makedirs(output_dir, exist_ok=True)

for name in os.listdir(images_dir):
    if name.endswith(".png"):
        img_path = os.path.join(images_dir, name)
        print(f"Preprocessing {name}...")
        
        # Load image
        img = Image.open(img_path)
        
        # Convert to grayscale
        img_gray = img.convert("L")
        
        # Resize 2x for better OCR
        w, h = img_gray.size
        img_large = img_gray.resize((w * 2, h * 2), Image.Resampling.LANCZOS)
        
        # Save preprocessed image
        out_path = os.path.join(output_dir, name)
        img_large.save(out_path)
        print(f"Saved to {out_path}")
