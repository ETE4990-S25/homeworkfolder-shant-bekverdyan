import os
import hashlib

def menu():
    """Menu"""
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
