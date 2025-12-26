import os
from os.path import isdir
import shutil


def list_dir(dir):
    if os.path.isdir(dir):
        return os.listdir(dir)
    else:
        raise Exception(f"Error: {dir} is not a directory")


def confirm_dir(path, dry_run):
    if dry_run:
        print(f"[DRY-RUN] mkdir:{path}")
    else:
        print(f"[RUN] mkdir:{path}")
        os.makedirs(path, exist_ok=True)


def confirm_move(src, dst, dry_run):
    if dry_run:
        print(f"[DRY-RUN] move: {src} -> {dst}")
    else:
        print(f"[RUN] move: {src} -> {dst}")
        shutil.move(src, dst)


def organize(src, dry_run=True):
    list_files = list_dir(src)
    for file in list_files:
        if file.endswith("_container"):
            continue
        path_to_file = os.path.join(src, file)
        if os.path.isdir(path_to_file):
            folder_dest = os.path.join(src, "folder_container")
            confirm_dir(folder_dest, dry_run)
            confirm_move(path_to_file, folder_dest, dry_run)

        elif os.path.isfile(file):
            name, ext = os.path.splitext(file)
            if not ext:
                container = "no_extension_container"
            else:
                container = ext[1:].lower() + "_container"
            file_dest = os.path.join(src, container)
            confirm_dir(file_dest, dry_run)
            confirm_move(path_to_file, file_dest, dry_run)


def main():
    print("Hello from files-organizer")


if __name__ == "__main__":
    main()
