from transfer import handle_file_transfer
from directory import *
import os,glob

from_directory = input("Where would you like to transfer from? ")
to_directory = input("Where would you like to transfer to? ")
file_extension = input("What is the file extension of the file you want transfer? ")

paths = generate_paths(from_directory,to_directory)

handle_file_transfer(paths, file_extension)

