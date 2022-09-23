# Python program to organise your folders

# The program checks for folders to organise your files into, and if it doesn't find any, it creates them

import json
import os
import shutil
import time

with open("file_types.json") as f:
    file_types = json.load(f)


def check_for_folders(directory):
    for file_type in file_types:
        folder = directory + "\\" + file_type
        if os.path.isdir(folder):
            print(f"Found {file_type} folder")
        else:
            os.mkdir(folder)
            print(f"Created {file_type} folder")


def organiser():
    directory = os.getcwd()
    conformation = input(f"Working in \"{directory}\"  Continue? (y/n) ")

    if conformation != "y":
        print("Cancelling...")
        return

    check_for_folders(directory)

    files = [f for f in os.listdir() if os.path.isfile(
        os.path.join(directory, f))]

    for file_type in file_types:
        count = 0
        file_extensions = file_types[file_type]
        for file in files:
            if os.path.splitext(file)[1] in file_extensions:
                count += 1
                from_path = directory + "\\" + file
                to_path = directory + "\\" + file_type + "\\" + file
                shutil.move(from_path, to_path)
        print(f"Moved {count} items to {file_type} folder")

    print("sorted")


if __name__ == "__main__":
    organiser()
    time.sleep(15)
