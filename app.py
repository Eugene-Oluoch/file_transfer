from transfer import handle_file_transfer
from directory import gets_allowed_directories_in_home, get_home_path
import os,glob
get_home_path()

from_path = input("Where would you like to transfer from? ")
to_path = input("Where would you like to transfer to? ")
file_extension = input("What is the file extension of the file you want transfer? ")

handle_file_transfer(from_path, to_path, file_extension)


