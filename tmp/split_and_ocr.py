import cv2
import os
import subprocess

def split_and_ocr(img_path, output_name):
    img = cv2.imread(img_path)
    h, w, _ = img.shape
    num_blocks = 10
    block_h = h // num_blocks
    
    print(f"\n==================== OCR FOR {output_name} ====================")
    for i in range(num_blocks):
        y1 = i * block_h
        y2 = (i + 1) * block_h if i < num_blocks - 1 else h
        crop = img[y1:y2, 0:w]
        
        temp_path = f"/Users/aayushsapkota9/repos/oxford/agentic-exams/tmp/{output_name}_block_{i}.png"
        cv2.imwrite(temp_path, crop)
        
        # Run Tesseract
        try:
            result = subprocess.run(
                ["tesseract", "--psm", "6", temp_path, "stdout"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            text = result.stdout.strip()
            if text:
                print(f"--- Block {i} (y: {y1} to {y2}) ---")
                print(text)
        except Exception as e:
            print(f"Error on block {i}: {e}")
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

split_and_ocr("/Users/aayushsapkota9/repos/oxford/agentic-exams/nm/past-qn-images/2024b.png", "2024b")
split_and_ocr("/Users/aayushsapkota9/repos/oxford/agentic-exams/nm/past-qn-images/2025back.png", "2025back")
