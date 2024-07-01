import os
import cv2


def resize_image(input_path, output_path, new_height=256):
    # Read the image from file
    img = cv2.imread(input_path)
    height, width = img.shape[:2]

    # Calculate the aspect ratio
    aspect_ratio = height / width

    # Calculate the new width while maintaining the aspect ratio
    new_width = int(new_height / aspect_ratio)

    # Resize the image with the new dimensions
    resized_img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)

    # Save the image to the output path
    cv2.imwrite(output_path, resized_img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])  # Quality parameter to maintain quality


def resize_images_in_directory(input_directory, output_directory, new_height=256):
    # Ensure output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Iterate over files in the input directory
    for filename in os.listdir(input_directory):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            input_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, filename)

            # Resize the image
            resize_image(input_path, output_path, new_height)
            print(f'Resized and saved {filename} to {output_path}')


# Example usage
input_directory = r'C:\Skripsi\GenderClassification\datasets\socofing\270x291\gabor-high\M'
output_directory = r'C:\Skripsi\GenderClassification\datasets\socofing\gabor-high\M'
resize_images_in_directory(input_directory, output_directory)
