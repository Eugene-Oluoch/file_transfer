import glob, shutil,os
from directory import get_home_path
def handle_file_transfer(paths,file_extension): 
    
    from_path, to_path = paths["from_path"],paths["to_path"]
    
    os.chdir(from_path)
    
    for file in glob.glob(f"*.{file_extension}"):
        shutil.move(f'{from_path}/{file}', to_path)
        
    print("Files transfered successfully.")