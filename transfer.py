from tqdm import tqdm
import glob, shutil, time, os
from directory import get_home_path
from validation import validate_file_copy_existence, validate_value_in_brackets
from file import rename_file_with_brackets, rename_file, rename_and_transfer

def handle_file_transfer(user_data): 
    
    from_path, to_path, file_extentions = user_data["from_path"],user_data["to_path"],user_data["file_extentions"]
    # Remove when packaging
    os.chdir(from_path)
    files = glob.glob(f"*.{file_extentions}")

    if len(files) < 1:
        print(f"\nNo files found with the given Extension: {file_extentions}")
        return

    for file in tqdm(files):
        try:
            time.sleep(0.1)
            shutil.move(f'{from_path}/{file}', to_path)
        except Exception:
            print(f"File: {file} already exists")
            ask_to_rename = input("Transfer anyways?[y/n] ").lower()
            rename_and_transfer(ask_to_rename,file,user_data)
    print("Files transfer was successful ✅")