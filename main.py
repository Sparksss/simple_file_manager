import os

def main():
    files = {".jpg": "pictures", ".docx": "documents", ".mp3": "music", ".pdf": "documents", ".mp4": "videos"}
    target_dir = input("Please enter a path to folder here: ")

    if not os.path.isdir(target_dir):
        print("Invalid path")
        return

    for filename in os.listdir(target_dir):
        print(filename)
        _, extension = os.path.splitext(filename)
        if extension in files:
            move_file(filename, target_dir, target_dir)


def move_file(filename: str, folder_name: str, target_dir: str):
    destination_folder = os.path.join(target_dir, folder_name)
    os.makedirs(destination_folder, exist_ok=True)
    os.rename(filename, folder_name + "/" + filename)
    print(f"Moved {filename} to {folder_name}/")


if __name__ == '__main__':
    main()
