from transfer import handle_file_transfer
from directory import gets_allowed_directories_in_home, get_home_path, print_allowed_directories
import os,glob


all_allowed_directories = gets_allowed_directories_in_home()
print_allowed_directories(all_allowed_directories)

from_Directory = input("Where would you like to transfer from? ")
to_Directory = input("Where would you like to transfer to? ")
file_extension = input("What is the file extension of the file you want transfer? ")

home_directory = get_home_path()

from_path = home_directory+f"/{from_Directory}"
to_path = home_directory+f"/{to_Directory}"

os.chdir(from_path)

handle_file_transfer(from_path, to_path, file_extension)


