import os
import shutil
import logging
from config import ORGANIZATION_RULES

# Setup logging
logging.basicConfig(filename='file_organization.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Function to organize files based on rules
def organize_files(source_dir, destination_dir):
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()
            for folder, extensions in ORGANIZATION_RULES.items():
                if file_extension in extensions:
                    destination_folder = os.path.join(destination_dir, folder)
                    if not os.path.exists(destination_folder):
                        os.makedirs(destination_folder)
                    try:
                        shutil.move(file_path, destination_folder)
                        logging.info(f"Moved '{filename}' to '{destination_folder}'")
                    except Exception as e:
                        logging.error(f"Error moving '{filename}': {e}")
                    break

# Main function
def main():
    source_directory = '\Users\Anesu Ndava\Downloads'
    destination_directory = '\Users\Anesu Ndava\Downloads\SDI_AnesuNdava'
    organize_files(source_directory, destination_directory)

if __name__ == "__main__":
    main()
