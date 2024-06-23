import os
import cv2
from fingerprint_image_enhancer import FingerprintImageEnhancer

# specify the file path
input_file = r'C:\Skripsi\GenderClassification\datasets\family\raw\M\FM003_F1.png'
output_directory = r'C:\Skripsi\GenderClassification\untitled'

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

# process the input file
if os.path.isfile(input_file):
    # Read the raw image
    raw_img = cv2.imread(input_file, 0)
    base_filename = os.path.splitext(os.path.basename(input_file))[0]

    # Enhance the raw image
    enhancer = FingerprintImageEnhancer(**default_params)
    processed_img = enhancer.enhance(raw_img, resize=True)  # Enhance without resizing

    # construct the output file path for processed image
    processed_out_filename = base_filename + '_processed.png'
    processed_out_path = os.path.join(output_directory, processed_out_filename)

    # Save the processed image
    cv2.imwrite(processed_out_path, processed_img)

    # Enhance the raw image
    enhancer = FingerprintImageEnhancer(**lower_params)
    processed_img = enhancer.enhance(raw_img, resize=True)  # Enhance without resizing

    # construct the output file path for processed image
    processed_out_filename = base_filename + '_processed_low.png'
    processed_out_path = os.path.join(output_directory, processed_out_filename)

    # Save the processed image
    cv2.imwrite(processed_out_path, processed_img)

    # Enhance the raw image
    enhancer = FingerprintImageEnhancer(**higher_params)
    processed_img = enhancer.enhance(raw_img, resize=True)  # Enhance without resizing

    # construct the output file path for processed image
    processed_out_filename = base_filename + '_processed_high.png'
    processed_out_path = os.path.join(output_directory, processed_out_filename)

    # Save the processed image
    cv2.imwrite(processed_out_path, processed_img)
else:
    print("Input file does not exist.")
