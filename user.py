from directory import *

def getting_data_from_user():
    all_allowed_directories = gets_allowed_directories_in_home()

    from_directory = input("Where would you like to transfer from? ")
    to_directory = input("Where would you like to transfer to? ")
    file_extentions = input("What is the file extension of the file you want transfer? ")

    return generate_user_data(from_directory,to_directory,file_extentions)

