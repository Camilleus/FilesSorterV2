import os
import sys
import shutil
from normalize import *
from organize_files import *
import threading

file_extensions = {
    'Images': ('.jpeg', '.jpg', '.png', '.svg'),
    'Videos': ('.avi', '.mp4', '.mov', '.mkv'),
    'Documents': ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'),
    'Music': ('.mp3', '.ogg', '.wav', '.amr'),
    'Archives': ('.zip', '.gz', '.tar')
}

def organize_files(src_folder, dest_folder, file_extensions):
    try:
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)

        threads = []
        for root, _, files in os.walk(src_folder):
            for filename in files:
                file_path = os.path.join(root, filename)
                thread = threading.Thread(target=organize_file, args=(file_path, dest_folder, file_extensions))
                threads.append(thread)
                thread.start()

        for thread in threads:
            thread.join()

    except Exception as e:
        print(f"Error organizing files: {e}")

def organize_file(file_path, dest_folder, file_extensions):
    try:
        extension = get_extension(file_path)
        for category, extensions in file_extensions.items():
            if extension in extensions:
                category_folder = os.path.join(dest_folder, category)
                if not os.path.exists(category_folder):
                    os.makedirs(category_folder)
                move_to_category(file_path, category_folder)
                break
    except Exception as e:
        print(f"Error organizing file {file_path}: {e}")

def list_files_in_categories(dest_folder):
    try:
        for category, _ in file_extensions.items():
            category_folder = os.path.join(dest_folder, category)
            print(f'{category}:')
            files_list = list_files_in_category(category_folder)
            for filename in files_list:
                print(f'    {filename}')
    except Exception as e:
        print(f"Error listing files in categories: {e}")

def list_of_known_extensions(dest_folder):
    try:
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
            print("Usage: python Main.py C:\\Users\\Camil\\OneDrive\\Pulpit\\Nowyfolder")
            sys.exit(1)

        src_folder = sys.argv[1]
        dest_folder = os.path.join(src_folder, 'Sorted')
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)

        organize_files(src_folder, dest_folder, file_extensions)
        list_files_in_categories(dest_folder)
        list_of_known_extensions(dest_folder)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

