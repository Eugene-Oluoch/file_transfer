from directory import *
from utils.map_check import *

def validate_input_directories(from_directory,to_directory):
    all_allowed_directories = gets_allowed_directories_in_home()
    errors = {}

    if from_directory not in all_allowed_directories and to_directory not in all_allowed_directories:
        errors["both"] = "The given directories are not part of the home directory"
    elif from_directory not in all_allowed_directories:
        errors["from"] = "The given from directory isn't part of the home directory"
    elif to_directory not in all_allowed_directories:
        errors["to"] = "The given to directory isn't part of the home directory"

    return None if is_map_empty(errors) else get_error_key(errors)
    

def getting_data_from_user():

    from_directory = input("Where would you like to transfer from? ")
    to_directory = input("Where would you like to transfer to? ")
    file_extentions = input("What is the file extension of the file you want transfer? ")

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
        else:
            continue_to_next_step = True
        has_error = validate_input_directories(from_directory,to_directory)
        




    return generate_user_data(from_directory,to_directory,file_extentions)

