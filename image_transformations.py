import cv2
import numpy as np
from google.colab import files
from google.colab.patches import cv2_imshow

print("Upload an image file:")
uploaded = files.upload()
filename = next(iter(uploaded))

image = cv2.imread(filename)

if image is None:
    print(f"Error: Could not read image {filename}.")
else:
    print("=== Original Image ===")
    cv2_imshow(image)
    
    # Get image dimensions
    height, width = image.shape[:2]

    # --- 1. Translation ---
    print("\n=== 1. Translation ===")

    tx, ty = 100, 50 # Shift right by 100px, down by 50px
    # Translation matrix: [[1, 0, tx], [0, 1, ty]]
    translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
    translated_img = cv2.warpAffine(image, translation_matrix, (width, height))
    cv2_imshow(translated_img)

    # --- 2. Rotation ---
    print("\n=== 2. Rotation ===")

    # 45 Degrees Rotation
    center = (width // 2, height // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
    rotated_45_img = cv2.warpAffine(image, rotation_matrix, (width, height))
    cv2_imshow(rotated_45_img)

    # 90 Degrees Rotation
    rotated_90_img = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    cv2_imshow(rotated_90_img)

    # 180 Degrees Rotation
    rotated_180_img = cv2.rotate(image, cv2.ROTATE_180)
    cv2_imshow(rotated_180_img)

    # --- 3. Scaling (Resizing) ---
    print("\n=== 3. Scaling ===")

    # Enlarge 1.5x
    enlarged_img = cv2.resize(image, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)
    cv2_imshow(enlarged_img)

    # Shrink 0.5x
    shrunk_img = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    cv2_imshow(shrunk_img)

    # --- 4. Flipping ---
    print("\n=== 4. Flipping ===")
    
    # Horizontal flip (flipCode = 1)
    flipped_h_img = cv2.flip(image, 1)
    cv2_imshow(flipped_h_img)

    # Vertical flip (flipCode = 0)
    flipped_v_img = cv2.flip(image, 0)
    cv2_imshow(flipped_v_img)
