# -*- coding: utf-8 -*-
"""Exploring_Dataset.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11RRedtgFVmZIB5H3vYyiaB0qrV6U7rNt

Exploring Dataset for Skin Cancer MNIST: HAM10000 dataset

Author: Erwin Cazares, Alex Watson, Maria Reyna
"""

import os
import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

from google.colab import drive

# Mount Google Drive
drive.mount('/content/drive', force_remount=True)

folder_path = '/content/drive/MyDrive/CS_6361_Project/Ensemble_U_Net_Project/'

# List contents of the root directory in your Google Drive
!ls $folder_path

# Define the path to the images folder
image_path = folder_path + 'Dataset/images/'
masks_path = folder_path + 'Dataset/masks/'

# Get a list of all image files in the folder
image_files = [f for f in os.listdir(image_path) if f.endswith('.png')]
mask_files = [f for f in os.listdir(masks_path) if f.endswith('.png')]

# Sort the dataset
image_files.sort()
mask_files.sort()

# Pair image and mask filenames
image_mask_pairs = list(zip(image_files, mask_files))

# Select 5 random image-mask pairs
random_image_mask_pairs = random.sample(image_mask_pairs, 5)

# Display the selected images and masks
plt.figure(figsize=(15, 6))

# Display images and masks
for i, (image_file, mask_file) in enumerate(random_image_mask_pairs, 1):
    # Display image
    plt.subplot(2, 5, i)

    img_path = os.path.join(image_path, image_file)
    img = mpimg.imread(img_path)
    plt.imshow(img)

    plt.axis('off')
    plt.title(f'Image {i}')

    # Display mask
    plt.subplot(2, 5, 5 + i)

    mask_path = os.path.join(masks_path, mask_file)
    mask = mpimg.imread(mask_path)
    plt.imshow(mask, cmap='gray')

    plt.axis('off')
    plt.title(f'Mask {i}')

plt.show()

print()
print(f'Images in the dataset = {len(image_files)}')
print(f'Shape of images is = {img.shape}')
print(f'Image dtype is = {img.dtype}')

print()
print(f'Masks in the dataset = {len(mask_files)}')
print(f'Shape of Masks is = {mask.shape}')
print(f'Masks dtype is = {mask.dtype}')
print(f'Labels on masks are = {np.unique(mask)}')

def find_duplicates(lst):
    seen = set()
    duplicates = set()

    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)

    return list(duplicates)

duplicates = find_duplicates(image_files)

print("Duplicate items in the list:", duplicates)

print(image_mask_pairs)

import os

# Specify the root directory containing subdirectories for images and masks
dataset_directory = folder_path + 'Dataset/'
masks_directory = os.path.join(dataset_directory, 'masks')

# List all files in the masks directory
mask_files = os.listdir(masks_directory)

# Rename each mask file to remove the "_segmentation" suffix
for mask_file in mask_files:
    if '_segmentation' in mask_file:
        new_mask_file = mask_file.replace('_segmentation', '')  # Remove the "_segmentation" suffix
        old_path = os.path.join(masks_directory, mask_file)
        new_path = os.path.join(masks_directory, new_mask_file)
        os.rename(old_path, new_path)

print("Mask files renamed successfully.")