from pathlib import Path
import shutil


def main():
    print("=== JPG File Organizer ===")
    source_text = input("Enter the source folder path: ").strip().strip('"')
    destination_text = input("Enter the destination folder path: ").strip().strip('"')

    source = Path(source_text).expanduser()
    destination = Path(destination_text).expanduser()

    if not source.is_dir():
        print("Error: source folder does not exist.")
        return

    # Avoid moving files into the same folder or a folder inside the source.
    if source.resolve() == destination.resolve():
        print("Error: source and destination folders must be different.")
        return

    destination.mkdir(parents=True, exist_ok=True)
    moved_count = 0

    for file_path in source.iterdir():
        if file_path.is_file() and file_path.suffix.lower() == ".jpg":
            target = destination / file_path.name
            if target.exists():
                print(f"Skipped {file_path.name}: a file with that name already exists.")
                continue
            shutil.move(str(file_path), str(target))
            print(f"Moved: {file_path.name}")
            moved_count += 1

    print(f"Done. Moved {moved_count} JPG file(s).")


if __name__ == "__main__":
    main()
