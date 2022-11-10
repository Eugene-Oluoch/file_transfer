from directory import gets_allowed_directories_in_home


def validate_input_directories(from_directory,to_directory):
    all_allowed_directories = gets_allowed_directories_in_home()

    if from_directory not in all_allowed_directories and to_directory not in all_allowed_directories:
        return "both"
    elif from_directory not in all_allowed_directories:
        return "from"
    elif to_directory not in all_allowed_directories:
        return "to"
    else:
        return None
    
def get_error_message(error):
    
    if error == "both":
        return "\nThe given directories are not part of the home directory\n"
    elif error == "from":
        return "\nThe given from directory isn't part of the home directory\n"
    elif error == "to":
        return "\nThe given to directory isn't part of the home directory\n"
        
def validate_user_input(from_directory,to_directory, file_extension):
    has_error = validate_input_directories(from_directory,to_directory)
    continue_to_next_step = False
    while not continue_to_next_step:
        if has_error in ["both", "from", "to"]:
            if has_error == "both":
                print(get_error_message(has_error))
                from_directory = input("\nRe-enter from directory: ")
                to_directory = input("\nRe-enter to directory: ")
            elif has_error == "from":
                print(get_error_message(has_error))
                from_directory = input("\nRe-enter from directory: ")
            elif has_error == "to":
                print(get_error_message(has_error))
                to_directory = input("\nRe-enter to directory: ")

        elif valid_file_extension == False:
            file_extension = input("Invalid file extension. Please provide a valid file extension.  ")
            valid_file_extension = validate_file_extension(file_extension)     
                                       
        else:
            continue_to_next_step = True
        valid_file_extension = validate_file_extension(file_extension)     
        has_error = validate_input_directories(from_directory,to_directory)
        
    return {"from_directory":from_directory,"to_directory":to_directory, "file_extension":file_extension}

def validate_file_extension(extension):
    file_extensions = ["jpg", "jpeg", "png", "mp3", "mp4", "txt", "pdf", "docx"]
    if extension not in file_extensions:
        return False
    return True        