import os
from PIL import Image

def list_image_files(directory):
    # Define the image file patterns to look for
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
    
    # Initialize a list to hold the image filenames
    image_files = []
    
    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            if any(file.lower().endswith(ext) for ext in image_extensions):
                # Append the full path of the image file
                image_files.append(os.path.join(root, file))
    
    return image_files

def resize_image(image_path, output_path, output_size=(1600, 1200)):
    try:
        with Image.open(image_path) as img:
            img = img.resize(output_size, Image.LANCZOS)
            img.save(output_path)
            print(f"Resized {image_path} and saved to {output_path}.")
    except Exception as e:
        print(f"Error resizing image {image_path}: {e}")

# Define the directory paths
input_directory_path = r'[Input Path]'
output_directory_path = r'[Output Path]'

# Create the output directory if it doesn't exist
os.makedirs(output_directory_path, exist_ok=True)

# Get the list of image files
image_files = list_image_files(input_directory_path)

# Resize each image and save to the output directory with sequential filenames
for idx, image in enumerate(image_files, start=1):
    # Define the output path for the resized image with sequential filename
    output_filename = f"{idx}.jpg"
    output_path = os.path.join(output_directory_path, output_filename)
    # Resize and save the image
    resize_image(image, output_path)

print("Image resizing and renaming complete.")
