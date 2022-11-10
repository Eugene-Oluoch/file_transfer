from tqdm import tqdm
import glob, shutil, time, os
from directory import get_home_path
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
            time.sleep(0.5)
            shutil.move(f'{from_path}/{file}', to_path)
        except Exception:
            print(f"File: {file} already exists")
            ask_to_rename = input("Transfer anyways?[y/n] ").lower()

            if ask_to_rename == "y":
                splitted_file = file.split(".")
                file_name, file_extension = splitted_file[0], splitted_file[1]
                if file_name.__contains__("(") and file_name.__contains__(")"):
                    open_bracket_index, close_bracket_index = file_name.index("("), file_name.index(")")
                    value_in_name = file[open_bracket_index+1:close_bracket_index]
                    is_valid = not any(ch.isalpha() for ch in value_in_name)
                    if is_valid:
                        new_value_to_attach = str(int(value_in_name)+1)
                        x = file_name.replace(value_in_name,new_value_to_attach)
                        os.rename(f'{from_path}/{file}', f"{to_path}/{x}.{file_extension}")
                else:
                    renamed_file = f"{file_name}(1)"
                    os.rename(f'{from_path}/{file}', f"{to_path}/{renamed_file}.{file_extension}")
            else:
                print(f"\nFile: {file} skipped")
                continue
    print("Files transfer was successful ✅")