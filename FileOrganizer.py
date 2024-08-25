"""
File Organizer
by Abubakar Bunamay

This script organizes files into folders based on their file types.
It creates a nested folder structure for better organization.

Dependencies: os, shutil, logging, datetime

"""


# Import necessary modules
import os
import shutil
import logging
from datetime import datetime

def setup_logging():
    """Set up logging configuration"""
    # Create a 'logs' directory if it doesn't exist
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
        
    # Create a log file with a timestamp in the filename
    log_file = os.path.join(log_dir, f"organizer_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
     
     # Configure logging settings
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

def get_folder_structure(extension):
    """
        Determine the folder structure based on file extension
    
        To add new file types or modify the folder structure:
        1. Add a new entry to the folder_mapping dictionary
        2. Use the format: "extension": ["MainFolder", "SubFolder"]
        
    """
        
    # Define mapping of file extensions to folder structures
    folder_mapping = {
        "jpg": ["Images", "JPG"],
        "jpeg": ["Images", "JPEG"],
        "png": ["Images", "PNG"],
        "gif": ["Images", "GIF"],
        "mp4": ["Videos", "MP4"],
        "mov": ["Videos", "MOV"],
        "avi": ["Videos", "AVI"],
        "mp3": ["Audio", "MP3"],
        "wav": ["Audio", "WAV"],
        "flac": ["Audio", "FLAC"],
        "pdf": ["Documents", "PDF"],
        "docx": ["Documents", "DOCX"],
        "txt": ["Documents", "TXT"],
        "xlsx": ["Spreadsheets", "XLSX"],
        "csv": ["Spreadsheets", "CSV"],
        "zip": ["Archives", "ZIP"],
        "rar": ["Archives", "RAR"],
        "7z": ["Archives", "7Z"]
        
        # "py": ["Code", "Python"],
        # "js": ["Code", "JavaScript"],
    }
    
    # Return folder structure or default to "Others" if extension not found
    return folder_mapping.get(extension.lower(), ["Others", extension.upper()])

def organize_files(directory_path):
    """Organize files in the given directory"""
    # Check if the directory path is valid
    if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
        logging.error(f"Invalid directory path: {directory_path}")
        print("Invalid directory path.")
        return

    total_files = 0
    organized_files = 0
    
    # Walk through all files in the directory
    for root, _, files in os.walk(directory_path):
        for filename in files:
        
            # Skip AssetOrganizer script and log files
            if filename == 'AssetOrganizer.py' or filename.endswith('.log'):
                continue
            
            total_files += 1
            file_path = os.path.join(root, filename)
            try:
                # Get file extension and determine folder structure
                extension = filename.split('.')[-1].lower()
                main_folder, sub_folder = get_folder_structure(extension)
                
                # Create main folder if it doesn't exist
                # Adjust this if you want to change the folder creation logic
                main_folder_path = os.path.join(directory_path, main_folder)
                if not os.path.exists(main_folder_path):
                    os.makedirs(main_folder_path)
                    
                # Create sub-folder if it doesn't exist
                sub_folder_path = os.path.join(main_folder_path, sub_folder)
                if not os.path.exists(sub_folder_path):
                    os.makedirs(sub_folder_path)

                # Move the file to its new location
                # Modify here if you want to change how files are moved                
                shutil.move(file_path, os.path.join(sub_folder_path, filename))
                organized_files += 1
                logging.info(f"Moved {filename} to {os.path.join(main_folder, sub_folder)}")
            except Exception as e:
                logging.error(f"Error processing {filename}: {str(e)}")

    # Print and log the summary of organized files
    print(f"Organization complete. {organized_files} out of {total_files} files organized.")
    logging.info(f"Organization complete. {organized_files} out of {total_files} files organized.")

def main():
    """Main function to run the File Organizer"""
    setup_logging()
    print("File Organizer")
    print("=======================")
    
    while True:
        # Display menu options
        print("\nOptions:")
        print("1. Organize files in a specific directory")
        print("2. Organize files in the current directory (where this script is located)")
        print("3. Quit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        # Choice handling
        if choice == '1':
            # Option 1: Organize files in a specific directory        
            directory = input("Enter the directory path to organize: ")
            if os.path.exists(directory) and os.path.isdir(directory):
                confirm = input(f"Are you sure you want to organize '{directory}'? (y/n): ") # Delete this line if you don't want the confirmation
                if confirm.lower() == 'y':
                    organize_files(directory)
                else:
                    print("Operation cancelled.")
            else:
                print("Invalid directory. Please try again.")
        elif choice == '2':
            # Option 2: Organize files in the current directory
            current_directory = os.path.dirname(os.path.abspath(__file__))
            confirm = input(f"Are you sure you want to organize the current directory '{current_directory}'? (y/n): ") # Delete this line if you don't want the confirmation
            if confirm.lower() == 'y':
                organize_files(current_directory)
            else:
                print("Operation cancelled.")
        elif choice == '3':
            # Option 3: Quit the program
            break
        else:
            print("Invalid choice. Please try again.")

    print("Thank you for using File Organizer!")

# Entry point of the script
if __name__ == "__main__":
    main()
