import os
import shutil
from normalize import normalize

def get_extension(filename):
    return os.path.splitext(filename)[1].lower()

def move_to_category(file_path, category_folder):
    try:
        shutil.move(file_path, os.path.join(category_folder, os.path.basename(file_path)))
    except Exception as e:
        print(f"Error moving file: {e}")

def organize_files(src_folder, dest_folder):
    try:
        unknown_folder = os.path.join(dest_folder, 'Unknown')
        image_extensions = ('.jpeg', '.jpg', '.png', '.svg')

        for root, _, files in os.walk(src_folder):
            for filename in files:
                extension = get_extension(filename)
                found = False

                for category, extensions in file_extensions.items():
                    category_folder = os.path.join(dest_folder, category)

                    if extension in extensions:
                        if extension in image_extensions:
                            destination_folder = os.path.join(dest_folder, 'Zdjecia')
                            os.makedirs(destination_folder, exist_ok=True)
                            new_file_path = os.path.join(destination_folder, normalize(filename))
                            move_to_category(os.path.join(root, filename), destination_folder)

                        if not os.path.exists(category_folder):
                            os.makedirs(category_folder)
                        move_to_category(os.path.join(root, filename), category_folder)
                        found = True
                        break

                if not found:
                    if not os.path.exists(unknown_folder):
                        os.makedirs(unknown_folder)
                    move_to_category(os.path.join(root, filename), unknown_folder)
    except Exception as e:
        print(f"Error organizing files: {e}")
