import os
import cv2


def crop_image(image, top=2, left=2, bottom=4, right=4):
    """
    Crop the image to remove empty pixels.

    Parameters:
    image (numpy.ndarray): Input image
    top (int): Number of pixels to crop from the top
    left (int): Number of pixels to crop from the left
    bottom (int): Number of pixels to crop from the bottom
    right (int): Number of pixels to crop from the right

    Returns:
    numpy.ndarray: Cropped image
    """
    height, width = image.shape[:2]
    cropped_image = image[top:height - bottom, left:width - right]
    return cropped_image


def process_images(input_directory, output_directory):
    """
    Process and crop all images in the input directory and save to the output directory.

    Parameters:
    input_directory (str): Path to the input directory containing images
    output_directory (str): Path to the output directory to save cropped images
    """
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(input_directory):
        if filename.lower().endswith('.bmp'):  # Ensure only BMP files are processed
            image_path = os.path.join(input_directory, filename)
            image = cv2.imread(image_path)
            if image is not None:
                cropped_image = crop_image(image)
                output_path = os.path.join(output_directory, filename)
                cv2.imwrite(output_path, cropped_image)
                print(f"Cropped and saved: {output_path}")
            else:
                print(f"Failed to read image: {image_path}")


# Define the input and output directories
input_dir = r'C:\Skripsi\GenderClassification\datasets\socofing-temp'
output_dir = r'C:\Skripsi\GenderClassification\datasets\socofing'

# Process the images
process_images(input_dir, output_dir)