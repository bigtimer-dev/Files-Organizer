from parser import parse_arguments
from organizer import organize


def main():
    args = parse_arguments()
    organize(args.path, dry_run=args.dry_run, verbose=args.verbose)
