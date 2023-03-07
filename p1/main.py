import argparse
from pathlib import Path
from threading import Thread
from cleaner import list_folders, move_to_category_folder, delet_folders


def main():
    parser = argparse.ArgumentParser(description="Sorting folder")
    parser.add_argument("--source", "-s", help="Source folder", required=True)
    parser.add_argument("--output", "-o", help="Output folder", default="dist")

    args = vars(parser.parse_args())

    preassigned_path = Path(args.get("source"))
    destination_folder = Path(args.get("output"))

    folders = list_folders(preassigned_path)

    threads = []
    for folder in folders:
        th = Thread(target=move_to_category_folder,
                    args=(folder, destination_folder))
        th.start()
        threads.append(th)

    [th.join() for th in threads]

    delet_folders(preassigned_path)


if __name__ == "__main__":
    main()
