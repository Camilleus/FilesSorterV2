import os
import sys
from normalize import normalize
from organize_files import organize_files

# Lista rozszerzeń plików dla każdej kategorii
file_extensions = {
    'Images': ('.jpeg', '.jpg', '.png', '.svg'),
    'Videos': ('.avi', '.mp4', '.mov', '.mkv'),
    'Documents': ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'),
    'Music': ('.mp3', '.ogg', '.wav', '.amr'),
    'Archives': ('.zip', '.gz', '.tar')
}

def get_extension(filename):
    return os.path.splitext(filename)[1].lower()

def move_to_category(file_path, category_folder):
    try:
        shutil.move(file_path, os.path.join(category_folder, os.path.basename(file_path)))
    except Exception as e:
        print(f"Error moving file: {e}")


def list_files_in_category(category_folder):
    files_list = []
    for _, _, files in os.walk(category_folder):
        for filename in files:
            files_list.append(filename)
    return files_list


def list_files_in_categories(dest_folder):
    try:
        # Tworzy listę plików w każdej kategorii
        for category, _ in file_extensions.items():
            category_folder = os.path.join(dest_folder, category)
            print(f'{category}:')
            files_list = list_files_in_category(category_folder)
            for filename in files_list:
                print(f'    {filename}')
    except Exception as e:
        print(f"Error listing files in categories: {e}")


def list_known_extensions(dest_folder):
    try:
        # Tworzy listę znanych rozszerzeń plików w folderze docelowym
        known_extensions = set()
        for _, _, files in os.walk(dest_folder):
            for filename in files:
                extension = get_extension(filename)
                known_extensions.add(extension)
        print('Known File Extensions:')
        for ext in known_extensions:
            print(f'    {ext}')
    except Exception as e:
        print(f"Error listing known extensions: {e}")


def main():
    try:
        if len(sys.argv) != 2:
            print("Usage: python sort.py C:\\Users\\Camil\\OneDrive\\Pulpit\\Nowyfolder")
            sys.exit(1)

        src_folder = sys.argv[1]
        dest_folder = os.path.join(src_folder, 'Sorted')
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)

        organize_files(src_folder, dest_folder)
        list_files_in_categories(dest_folder)
        list_known_extensions(dest_folder)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()