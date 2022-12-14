import os,glob

def get_home_path():
    return os.path.expanduser( '~' )

def gets_allowed_directories_in_home():
    home_directory = get_home_path()
    directories_in_home = glob.glob(f"{home_directory}/*", recursive = True)
    allowed_directories = []
    for directory in directories_in_home:
        directory_name = directory[len(home_directory)+1:]
        if directory_name.__contains__(".") == False:
            allowed_directories.append(directory_name)
    return allowed_directories

def print_allowed_directories():
    print("Allowed Directories: \n\n" + ", ".join(gets_allowed_directories_in_home())+"\n\n")

def generate_user_data(from_directory,to_directory,file_extentions):
    home_path = get_home_path()
    return {"from_path": f"{home_path}/{from_directory}", "to_path": f"{home_path}/{to_directory}","file_extentions":file_extentions}