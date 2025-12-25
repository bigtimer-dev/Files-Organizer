import os
from os.path import isdir
import shutil
from extensions import extensions_dict


def list_dir(dir):
    if os.path.isdir(dir):
        return os.listdir(dir)
    else:
        raise Exception(f"Error: {dir} is not a directory")


def organize(src):
    list_files = list_dir(src)
    for file in list_files:
        if os.path.isdir(file):
            folder_dest = os.path.join(src, "folder_container")
            os.makedirs(folder_dest, exist_ok=True)
            folder_src = os.path.join(src, file)
            print(f"Moving:{folder_src} to {folder_dest}")
            shutil.move(folder_src, folder_dest)
        elif os.path.isfile(file):
            g_extention = file.split(".")
            container = g_extention[1] + "_container"
            file_dest = os.path.join(src, container)
            os.makedirs(file_dest, exist_ok=True)
            file_src = os.path.join(src, file)
            print(f"Moving: {file_src} to {file_dest}")
            shutil.move(file_src, file_dest)


def main():
    print("Hello from files-organizer")


if __name__ == "__main__":
    main()
