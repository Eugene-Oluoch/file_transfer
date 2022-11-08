import glob, shutil,os
from directory import get_home_path
def handle_file_transfer(paths,file_extension): 
    
    os.chdir(paths["from_path"])
    
    for file in glob.glob(f"*.{file_extension}"):
        shutil.move(f'{paths["from_path"]}/{file}', paths["to_path"])
        
    print("Files transfered successfully.")