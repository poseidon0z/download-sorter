# Python program to organise your folders

# The program checks for folders to organise your files into, and if it doesn't find any, it creates them

import json
import os
import shutil
import time

with open("file_types.json") as f:
    file_types = json.load(f)


def check_for_folders(directory):
    '''
    Check if folders for the various file types exist, and creates the folder for that type if it doesnt
    '''
    for file_type in file_types:
        folder = directory + "\\" + file_type
        if not os.path.isdir(folder):
            os.mkdir(folder)

# Main function


def organiser():
    directory = os.getcwd()
    conformation = input(f"Working in \"{directory}\"  Continue? (y/n) ")

    if conformation != "y":
        print("Cancelling...")
        return

    print("Checking files in your folder...")
    files = [f for f in os.listdir() if os.path.isfile(
        os.path.join(directory, f))]

    check_for_folders(directory)
    for file_type in file_types:
        count = 0
        file_extensions = file_types[file_type]
        for file in files:
            if os.path.splitext(file)[1] in file_extensions:
                count += 1
                from_path = directory + "\\" + file
                to_path = directory + "\\" + file_type + "\\" + file
                shutil.move(from_path, to_path)
        if count != 0:
            print(f"Moved {count} items to {file_type} folder")

        # Cleanup code to remove folder for certain file type if it is empty
        folder = directory + "\\" + file_type
        if len(os.listdir(folder)) == 0:
            os.rmdir(folder)

    print("sorted")


if __name__ == "__main__":
    organiser()
    time.sleep(15)
