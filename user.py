from directory import *
from validation import *


def getting_data_from_user():

    from_directory = input("Where would you like to transfer from? ")
    to_directory = input("Where would you like to transfer to? ")
    file_extentions = input("What is the file extension of the file you want transfer? ")

    valid_user_data = validate_user_input(from_directory,to_directory)
    valid_from_directory, valid_to_directory = valid_user_data["from_directory"], valid_user_data["to_directory"]
    
    return generate_user_data(valid_from_directory,valid_to_directory,file_extentions)

