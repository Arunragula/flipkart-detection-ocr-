import os
import random
import shutil
from pathlib import Path

def split_dataset(source_dir, train_dir, val_dir, split_ratio=0.2):
    # Create necessary directories
    for dir in [train_dir, val_dir]:
        os.makedirs(os.path.join(dir, 'images'), exist_ok=True)
        os.makedirs(os.path.join(dir, 'labels'), exist_ok=True)
    
    # Get all image files
    image_files = [f for f in os.listdir(os.path.join(source_dir, 'allimages')) 
                   if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    
    if not image_files:
        print(f"No image files found in {os.path.join(source_dir, 'allimages')}")
        return

    # Randomly select validation files
    num_val = int(len(image_files) * split_ratio)
    val_files = set(random.sample(image_files, num_val))
    
    # Move files
    for img_file in image_files:
        src_img = os.path.join(source_dir, 'allimages', img_file)
        src_label = os.path.join(source_dir, 'labels', 'obj_train_data', Path(img_file).stem + '.txt')
        
        if img_file in val_files:
            dst_dir = val_dir
        else:
            dst_dir = train_dir
        
        # Copy image
        dst_img = os.path.join(dst_dir, 'images', img_file)
        shutil.copy(src_img, dst_img)
        
        # Copy label if it exists
        if os.path.exists(src_label):
            dst_label = os.path.join(dst_dir, 'labels', Path(img_file).stem + '.txt')
            shutil.copy(src_label, dst_label)
        else:
            print(f"Warning: Label file not found for {img_file}")

    print(f"Dataset split completed. {len(image_files) - num_val} images in training, {num_val} images in validation.")

# Usage
source_directory = r"C:\Users\USER\arun"
train_directory = r"C:\Users\USER\arun\train"
val_directory = r"C:\Users\USER\arun\val"

split_dataset(source_directory, train_directory, val_directory)