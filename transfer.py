import glob, shutil,os
def handle_file_transfer(from_path,to_path,file_extension):    
    for file in glob.glob(f"*.{file_extension}"):
        shutil.move(f"{from_path}/{file}",to_path)
        
    print("Files transfered successfully.")