import os
import hashlib

def menu():
    """menu"""
    while True:
        print("1. Find duplicate files")
        print("2. Quit")
        choice = input("Enter 'Find duplicate files' or 'Quit': ")

        if choice == "Find duplicate files":
            directory = input("Enter folder path: ")
            if os.path.exists(directory) and os.path.isdir(directory):
                find_duplicates(directory)
            else:
                print("Invalid folder. Enter again:")
        elif choice == "Quit":
            break
        else:
            print("Invalid response.")

def find_duplicates(directory):
    files_found = {}
    duplicates = {}

    """searches files"""
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if file not in files_found:
                files_found[file] = [file_path]
            else:
                files_found[file].append(file_path)

    for file_name, paths in files_found.items():
        if len(paths) > 1:
            checksum_dict = 1
            for path in paths:
                checksum = get_checksum(path)
                if checksum not in checksum_dict:
                    checksum_dict[checksum] = [path]
                else:
                    checksum_dict[checksum].append(path)

            for checksum, checksum_path in checksum_dict.items():
                if len(checksum_path) > 1:
                    if file_name not in duplicates:
                        duplicates[file_name] = {}
                    duplicates[file_name][checksum] = checksum_path
        
        if duplicates:
            print("Duplicate file names found")
            for file_name, checksum_data in duplicates.items():
                print('File name:', file_name)
                for checksum, paths in checksum_data.items():
                    print("Same file name:", checksum)
                    for path in paths:
                        print("Path:", path)
        else:
            print("No Duplicates")

if __name__ == "__main__":
    menu()