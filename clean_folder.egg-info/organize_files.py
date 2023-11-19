import os
import shutil
from normalize import normalize
from concurrent.futures import ThreadPoolExecutor

def organize_files(src_folder, dest_folder, file_extensions):
    try:
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)

        with ThreadPoolExecutor() as executor:
            for root, _, files in os.walk(src_folder):
                for filename in files:
                    file_path = os.path.join(root, filename)
                    executor.submit(organize_file, file_path, dest_folder, file_extensions)

    except Exception as e:
        print(f"Error organizing files: {e}")

def organize_file(file_path, dest_folder, file_extensions):
    try:
        extension = get_extension(filename)
        for category, extensions in file_extensions.items():
            if extension in extensions:
                category_folder = os.path.join(dest_folder, category)
                if not os.path.exists(category_folder):
                    os.makedirs(category_folder)
                move_to_category(file_path, category_folder)
                break
    except Exception as e:
        print(f"Error organizing file {file_path}: {e}")
