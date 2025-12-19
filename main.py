import os
import shutil
from extensions import extensions_dict


def list_dir(dir):
    if os.path.isdir(dir):
        return os.listdir(dir)
    else:
        raise Exception(f"Error: {dir} is not a directory")


def move_contents(src, dest):
    contents = list_dir(src)
    for content in contents:
        full_path_to_content = os.path.join(src, content)


def main():
    print("Hello from files-organizer")


if __name__ == "__main__":
    main()
