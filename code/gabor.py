import os
import cv2
from fingerprint_image_enhancer import FingerprintImageEnhancer

# Source directories
raw_base_dir = r'C:\Skripsi\GenderClassification\datasets\family\raw'

# Destination directories
processed_base_dir_default = r'C:\Skripsi\GenderClassification\datasets\family\gabor'
processed_base_dir_low = r'C:\Skripsi\GenderClassification\datasets\family\gabor-low'
processed_base_dir_high = r'C:\Skripsi\GenderClassification\datasets\family\gabor-high'

# Create output directories if they don't exist
os.makedirs(processed_base_dir_default, exist_ok=True)
os.makedirs(processed_base_dir_low, exist_ok=True)
os.makedirs(processed_base_dir_high, exist_ok=True)

# Default parameters
default_params = {
    'ridge_segment_blksze': 16,
    'ridge_segment_thresh': 0.1,
    'gradient_sigma': 1,
    'block_sigma': 7,
    'orient_smooth_sigma': 7,
    'ridge_freq_blksze': 38,
    'ridge_freq_windsze': 5,
    'min_wave_length': 5,
    'max_wave_length': 15,
    'kx': 0.65,
    'ky': 0.65,
    'angleInc': 3.0,
    'ridge_filter_thresh': -3
}

# Lower parameters
lower_params = {
    'ridge_segment_blksze': 12,
    'ridge_segment_thresh': 0.05,
    'gradient_sigma': 0.5,
    'block_sigma': 5,
    'orient_smooth_sigma': 5,
    'ridge_freq_blksze': 30,
    'ridge_freq_windsze': 4,
    'min_wave_length': 4,
    'max_wave_length': 12,
    'kx': 0.5,
    'ky': 0.5,
    'angleInc': 2.0,
    'ridge_filter_thresh': -4
}

# Higher parameters
higher_params = {
    'ridge_segment_blksze': 20,
    'ridge_segment_thresh': 0.15,
    'gradient_sigma': 1.5,
    'block_sigma': 9,
    'orient_smooth_sigma': 9,
    'ridge_freq_blksze': 46,
    'ridge_freq_windsze': 6,
    'min_wave_length': 6,
    'max_wave_length': 18,
    'kx': 0.8,
    'ky': 0.8,
    'angleInc': 4.0,
    'ridge_filter_thresh': -2
}

# Function to process and enhance fingerprint images
def process_and_enhance(input_file, output_directory, enhancement_params):
    try:
        if os.path.isfile(input_file):
            img = cv2.imread(input_file, 0)
            base_filename = os.path.splitext(os.path.basename(input_file))[0]

            # Construct the output file path for enhanced image
            enhanced_out_filename = base_filename + '_enhanced.png'
            enhanced_out_path = os.path.join(output_directory, enhanced_out_filename)

            # Check if the file has already been processed
            if os.path.exists(enhanced_out_path):
                print(f"File {enhanced_out_filename} already processed. Skipping.")
                return

            enhancer = FingerprintImageEnhancer(**enhancement_params)
            enhanced_img = enhancer.enhance(img, resize=True)

            # Save the processed enhanced image
            cv2.imwrite(enhanced_out_path, enhanced_img)

            # Print the number of processed images
            global processed_count
            processed_count += 1
            print(f"Processed {processed_count} files: {base_filename}")

        else:
            print(f"Input file {input_file} does not exist.")

    except Exception as e:
        print(f"Error processing file: {input_file}, Error: {str(e)}")

# Initialize counter for processed images
processed_count = 0

# Helper function to process directory
def process_directory(raw_dir, processed_dir, params):
    global processed_count
    processed_count = 0
    for subdir in ['F', 'M']:
        raw_subdir = os.path.join(raw_dir, subdir)
        processed_subdir = os.path.join(processed_dir, subdir)
        os.makedirs(processed_subdir, exist_ok=True)
        for file_name in os.listdir(raw_subdir):
            input_file = os.path.join(raw_subdir, file_name)
            process_and_enhance(input_file, processed_subdir, params)
    print(f"Total processed images for directory {processed_dir}: {processed_count}")

# Process directories
process_directory(raw_base_dir, processed_base_dir_default, default_params)
process_directory(raw_base_dir, processed_base_dir_low, lower_params)
process_directory(raw_base_dir, processed_base_dir_high, higher_params)
