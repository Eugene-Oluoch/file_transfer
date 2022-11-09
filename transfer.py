from tqdm import tqdm
import glob, shutil, time, os
from directory import get_home_path
def handle_file_transfer(user_data): 
    
    from_path, to_path, file_extentions = user_data["from_path"],user_data["to_path"],user_data["file_extentions"]
    files = glob.glob(f"*.{file_extentions}",root_dir=from_path)

    for file in files:
        try:
            time.sleep(0.5)
            shutil.move(f'{from_path}/{file}', to_path)
        except Exception:
            print(f"File: {file} already exists")
            ask_to_rename = input("Transfer anyways?[y/n] ").lower()
            if ask_to_rename == "y":
                splitted_file = file.split(".")
                renamed_file = f"{splitted_file[0]}(1).{splitted_file[1]}"
                print(renamed_file)

    print("Files transfer was successful ✅")