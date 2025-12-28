import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description="Organize files by extension")

    parser.add_argument("path", help="Directory to organize")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what files will be moved if you run without this flag",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Add info for what is happenning while running the script",
    )

    return parser.parse_args()
