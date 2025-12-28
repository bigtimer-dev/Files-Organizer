from organizer.parser import parse_arguments
from organizer.core import organize


def main():
    try:
        args = parse_arguments()
        organize(args.path, dry_run=args.dry_run, verbose=args.verbose)
    except Exception as e:
        print(f"Error:{e}")
        return


if __name__ == "__main__":
    main()
