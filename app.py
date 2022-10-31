from transfer import file_transfer
print("""
***************
*** WELCOME ***
***************

Allowed file paths:
 - Desktop
 - Documents
 - Downloads
 - Movies
 - Music
 - Pictures

""")

from_path = input("Enter path you want to transfer from: ").capitalize()
to_path = input("Enter path you want to transfer to: ").capitalize()


redo = True
while redo:
    file_extension = input("Enter file extension: ")
    file_transfer(from_path,to_path,file_extension)
    ask_to_transfer = input("Do you want to transfer again from the same paths? [y/n/exit] ").lower()
    if ask_to_transfer == 'y':   
        continue
    elif ask_to_transfer == "n":
        ask_path_to_change = input("Which path do you want to change?[to/from/both] ").lower()
        if ask_path_to_change == "to":
            new_to_path = input("Enter new to path: ")
            to_path = new_to_path
            continue
        elif ask_path_to_change == "from":
            new_from_path = input("Enter new from path: ")
            from_path = new_from_path
            continue
        elif ask_path_to_change == "both":
            new_to_path = input("Enter new to path: ")
            new_from_path = input("Enter new from path: ")
            to_path = new_to_path
            from_path = new_from_path
            continue
            
    elif ask_to_transfer == "exit":
        redo = False


