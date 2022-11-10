from tqdm import tqdm
import glob, shutil, time, os
from directory import get_home_path
def handle_file_transfer(user_data): 
    
    from_path, to_path, file_extentions = user_data["from_path"],user_data["to_path"],user_data["file_extentions"]
    os.chdir(from_path)
    files = glob.glob(f"*.{file_extentions}")

    for file in tqdm(files):
        try:
            time.sleep(0.5)
            shutil.move(f'{from_path}/{file}', to_path)
        except Exception:
            print(f"File: {file} already exists")
            ask_to_rename = input("Transfer anyways?[y/n] ").lower()
        
            if ask_to_rename == "y":
                splitted_file = file.split(".")
                if splitted_file[0].__contains__("(") and splitted_file[0].__contains__(")"):
                    open_index = splitted_file[0].index("(")
                    close_index = splitted_file[0].index(")")
                    value_in_name = file[open_index+1:close_index]
                    is_valid = True
                    for ch in value_in_name:
                        if ch.isalpha():
                            is_valid = False
                            break
                    if is_valid:
                        
                        new_value_to_attach = str(int(value_in_name)+1)
                        x = splitted_file[0].replace(value_in_name,new_value_to_attach)
                        os.rename(f'{from_path}/{file}', f"{to_path}/{x}.{splitted_file[1]}")

                else:
                    renamed_file = splitted_file[0]+"(1)"
                    a = os.rename(f'{from_path}/{file}', f"{to_path}/{renamed_file}.{splitted_file[1]}")
                    print(a)
                            
    print("Files transfer was successful ✅")