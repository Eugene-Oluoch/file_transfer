import glob, shutil,os
from directory import get_home_path
def handle_file_transfer(user_data): 
    
    from_path, to_path, file_extentions = user_data["from_path"],user_data["to_path"],user_data["file_extentions"]
    
    os.chdir(from_path)
    
    for file in glob.glob(f"*.{file_extentions}"):
        shutil.move(f'{from_path}/{file}', to_path)
        
    print("Files transfered successfully.")