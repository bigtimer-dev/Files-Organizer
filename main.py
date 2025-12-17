import os
from extensions import extensions_dict


def list_dir(dir):
    if os.path.isdir(dir):
        return os.listdir(dir)
    else:
        raise Exception(f"Error: {dir} is not a directory")


def main():
    print("Hello from files-organizer!")


if __name__ == "__main__":
    main()
