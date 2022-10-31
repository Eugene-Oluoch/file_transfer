import glob, shutil
def file_transfer(from_path,to_path,file_extension):
    default_path = "/Users/eugene_crabs/"
    current_path = default_path+from_path
    destination_path = default_path+to_path
    file_count = 0
    for _ in glob.glob(f"{current_path}/*.{file_extension}"):
        shutil.move(_,destination_path)
        file_count+=1
    print(f"Successfully transfered {file_count} files.")