import os
import argparse
from ByteConverter import Bytes, MegaBytes, human_readable_size

# Function to prompt for deletion
def prompt_for_deletion(file_path: str) -> bool:
    while True:
        user_input = input(f"Delete '{file_path}'? (y/n): ").strip().lower()
        if user_input == 'y':
            os.remove(file_path)
            print(f"Deleted '{file_path}'")
            return True
        elif user_input == 'n':
            print(f"Skipped '{file_path}'")
            return False
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")
def check_valid_directory(directory_path: str) -> bool:
    # Check if the directory is empty
    try:
        if not os.listdir(directory_path):
            print("The directory is empty.")
            exit(1)
    except:
        print("No such file or directory")
        exit(1)

def delete_files(directory_path: str, min_size_megabytes: MegaBytes) -> bool:
    delete_happened = False
    check_valid_directory(directory_path)
    print(f"Filtering for files under {human_readable_size(min_size_megabytes)} under folder: {directory_path}")
    # Walk through the directory and list large files
    for root, dirs, files in os.walk(directory_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_size_in_bytes = Bytes(os.path.getsize(file_path))
                
            if file_size_in_bytes.bytes > min_size_megabytes.bytes:
                print(f"File: '{file_path}' Size: {file_size_in_bytes.bytes} Bytes {human_readable_size(file_size_in_bytes)}")
                delete_happened = prompt_for_deletion(file_path) or delete_happened
    return delete_happened

def parse_arguments():
    parser = argparse.ArgumentParser(description="Delete files from a directory.")
    parser.add_argument("--directory", type=str, help="Path to the directory to delete files from", required=True)
    parser.add_argument("--min-size", type=float, default=1, help="Minimum file size (in megabytes) to consider as 'large'")
    args = parser.parse_args()
    return (args.directory, args.min_size)

if __name__ == "__main__":
    directory_path, min_size_megabytes = parse_arguments()

    delete_happened = False
    try:
        delete_happened = delete_files(directory_path=directory_path, min_size_megabytes=MegaBytes(min_size_megabytes))
    except KeyboardInterrupt:
        print("\nOperation canceled by user.")

    if delete_happened:
        print("\nDeletion completed.")
    else:
        print("\nDeletion was unsuccessful.")