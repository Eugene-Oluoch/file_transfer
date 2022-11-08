import glob, shutil
from directory import get_home_path
def handle_file_transfer(user_data): 
    
    from_path, to_path, file_extentions = user_data["from_path"],user_data["to_path"],user_data["file_extentions"]
    
    for file in glob.glob(f"*.{file_extentions}",root_dir=from_path):
        shutil.move(f'{from_path}/{file}', to_path)
        
    print("Files transfered successfully.")