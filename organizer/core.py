import os
import shutil


def list_dir(dir):
    if os.path.isdir(dir):
        return os.listdir(dir)
    else:
        raise Exception(f"Error: {dir} is not a directory")


def confirm_dir(path, dry_run, verbose):
    if dry_run:
        print(f"[DRY-RUN] mkdir:{path}")
    else:
        if verbose:
            print(f"[RUN] mkdir:{path}")
        os.makedirs(path, exist_ok=True)


def confirm_move(src, dst, dry_run, verbose):
    if dry_run:
        print(f"[DRY-RUN] move: {src} -> {dst}")
    else:
        if verbose:
            print(f"[RUN] move: {src} -> {dst}")
        shutil.move(src, dst)


def duplicate_resolver(file_dest, file):
    name, ext = os.path.splitext(file)
    file_name = file
    count = 1
    resolver = 0

    while os.path.exists(os.path.join(file_dest, file_name)):
        file_name = f"{name}({count}){ext}"
        count += 1
        resolver += 1
    return os.path.join(file_dest, file_name), resolver


def console_print(
    skip_files, conflict_resolve, file_moved, folder_moved, folder_created
):
    print("\nSUMMARY")
    print("--------")
    print(f"skip_files: {skip_files}")
    print(f"conflicts_resolve: {conflict_resolve}")
    print(f"files_moved: {file_moved}")
    print(f"folder_moved: {folder_moved}")
    print(f"folder_created: {folder_created}")


def organize(src, dry_run=False, verbose=False):
    list_files = list_dir(src)
    skip_files = 0
    conflict_resolve = 0
    file_moved = 0
    folder_moved = 0
    folder_created = 0

    for file in list_files:
        if file.endswith("_container"):
            skip_files += 1
            continue

        path_to_file = os.path.join(src, file)
        if os.path.isdir(path_to_file):
            folder_dest = os.path.join(src, "folder_container")
            if not os.path.exists(folder_dest):
                folder_created += 1
            confirm_dir(folder_dest, dry_run, verbose)
            final_dest, folder_conflict = duplicate_resolver(folder_dest, file)
            conflict_resolve += folder_conflict
            confirm_move(path_to_file, final_dest, dry_run, verbose)
            folder_moved += 1

        elif os.path.isfile(path_to_file):
            name, ext = os.path.splitext(file)
            if not ext:
                container = "no_extension_container"
            else:
                container = ext[1:].lower() + "_container"
            file_dest = os.path.join(src, container)
            if not os.path.exists(file_dest):
                folder_created += 1
            confirm_dir(file_dest, dry_run, verbose)
            final_dest, files_confict = duplicate_resolver(file_dest, file)
            conflict_resolve += files_confict
            confirm_move(path_to_file, final_dest, dry_run, verbose)
            file_moved += 1

    console_print(
        skip_files, conflict_resolve, file_moved, folder_moved, folder_created
    )
