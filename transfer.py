import glob, shutil,os
def handle_file_transfer(from_path,to_path,file_extension):  
    all_files_with_given_extension = glob.glob(f"*.{file_extension}")
    for file in all_files_with_given_extension:
        shutil.move(f"{from_path}/{file}",to_path)
    print(f"Successfully transfered {len(all_files_with_given_extension)} files.")
    