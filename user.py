from directory import *

# = "The given directories are not part of the home directory"
# "The given from directory isn't part of the home directory"
# "The given to directory isn't part of the home directory"
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
    

def getting_data_from_user():

    from_directory = input("Where would you like to transfer from? ")
    to_directory = input("Where would you like to transfer to? ")
    file_extension = input("What is the file extension of the file you want transfer? ")

    has_error = validate_input_directories(from_directory,to_directory)

    
    continue_to_next_step = False
    while not continue_to_next_step:
        if has_error in ["both", "from", "to"]:
            if has_error == "both":
                from_directory = input("Re-enter from directory: ")
                to_directory = input("Re-enter to directory: ")
            elif has_error == "from":
                from_directory = input("Re-enter from directory: ")
            elif has_error == "to":
                to_directory = input("Re-enter to directory: ")

        elif valid_file_extension == False:
            file_extension = input("Invalid file extension. Please provide a valid file extension.  ")
            valid_file_extension = validate_file_extension(file_extension)     
                       
        else:
            continue_to_next_step = True
        valid_file_extension = validate_file_extension(file_extension)    
        has_error = validate_input_directories(from_directory,to_directory)
        

    return generate_user_data(from_directory,to_directory,file_extension)

def validate_file_extension(extension):
    file_extensions = ["jpg", "jpeg", "png", "mp3", "mp4", "txt", "pdf", "docx"]
    if extension not in file_extensions:
        return False
    return True    