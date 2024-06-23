import os
import shutil

# Define the source directory and the destination directories
source_dir = r'C:\Skripsi\GenderClassification\datasets\socofing'
male_dest_dir = r'C:\Skripsi\GenderClassification\datasets\socofing\raw\M'
female_dest_dir = r'C:\Skripsi\GenderClassification\datasets\socofing\raw\F'

# Ensure destination directories exist
os.makedirs(male_dest_dir, exist_ok=True)
os.makedirs(female_dest_dir, exist_ok=True)

# Loop through all files in the source directory
for filename in os.listdir(source_dir):
    if filename.endswith('.BMP'):
        # Check if the filename contains 'M' or 'F'
        if '__M_' in filename:
            shutil.move(os.path.join(source_dir, filename), os.path.join(male_dest_dir, filename))
            print(f'Moved {filename} to {male_dest_dir}')
        elif '__F_' in filename:
            shutil.move(os.path.join(source_dir, filename), os.path.join(female_dest_dir, filename))
            print(f'Moved {filename} to {female_dest_dir}')

print("File moving process completed.")