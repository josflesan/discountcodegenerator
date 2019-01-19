import os
import sys
#from dependencies.txtFileManager.txtFileManager.txtFileManager import *

###################################################################################
#                       H   E   A   D   E   R
#
# DiscountCodeGenerator  Copyright (C) 2019  Lemur
# This program comes with ABSOLUTELY NO WARRANTY.
# This is free software, and you are welcome to redistribute it
# under certain conditions.
#
###################################################################################

CODE_DELIMITER = "-"
FILE_DELIMITER = "/"
COMMAND_PREFIX = "lemurer@dcg $ "

# def generate_code():
#     code = ""
#
#     discount_value = int(input("Input discount value: "))
#     if (discount_value > 0) and (discount_value < 100):
#         code += str(discount_value) + CODE_DELIMITER
#     else:
#         return 13  # Error Code 13: The data is invalid.
#
#     code_id = f_codeID(seed)
#     code += str(code_id) + CODE_DELIMITER
#
#     today_date += f_today()
#     code += today_date + CODE_DELIMITER
#
#     expiration_days = int(input("Input expiration days: "))
#     if expiration_days > 0:
#         code += str(expiration_days) + CODE_DELIMITER
#     else:
#         return 13  # Error Code 13: The data is invalid.
#
#     valid_flag = f_validate(code)
#     code += valid_flag
#
#     return code


###################################################################################
#                      M  I  S  C     F  U  N  C  T  I  O  N  S

def f_today():
    import datetime
    now = datetime.datetime.now()
    today = str(now.day) + str(now.month) + str(now.year)

    return today


def create_dir(name, path):

    files = ['config', 'stats', 'activecodes', 'inactivecodes', 'README']

    while True:
        try:
            os.chdir(path)  # Change directory to path entered by the user
            break

        except OSError:
            print("Invalid path entered...")
            path = input("\nPlease, try again: ")
            continue

    os.mkdir(name)  # Create the new directory

    os.chdir(os.path.join(path, name))  # Change into newly created directory

    for f in files:
        with open(f+'.txt') as fh: # Create different files in the directory
            if f == "README":
                fh.write("We recommend not to delete or modify these files under any \n"
                         "circumstances for it may lead to irregularities in the module's \n"
                         "functioning. \n"
                         "\n"
                         "~ LEMURER COMPANY")

            fh.close()


def open_dir(path):

    files = ['config', 'stats', 'activecodes', 'inactivecodes', 'README']

    if not os.path.exists(path):
        while True:
            decision = input("\nPath doesn't exist, would you like to create it?: (Yes, or No) ").upper()[0]

            if decision in ['Y', 'N']:
                break
            else:
                print("Please, only yes or no here... ")
                continue

        if decision == "Y":
            name = path.split("/")[-1]  # Get folder name
            path = "/".join(path.split("/")[:-1])  # Get path name
            create_dir(name, path)

        else:
            sys.exit()  # Other action?

    os.chdir(path)
    validfile = []
    for file in os.listdir(path):
        f = os.path.splitext(file)[1]
        validfile.append(f)

    valid = True

    for i in validfile:
        if i not in files:
            print("Invalid path was entered, correct tree structure should be present in the file...")
            valid = False

    if valid:
        print("Path opened successfully")
        return 1
    else:
        return 0

# ---- MAIN FUNCTIONS ----


def generate_code():
    pass


def active_codes():
    pass


def expired_codes():
    pass


def settings():
    pass


def file_stats():
    pass


def credit():
    pass


###################################################################################


###################################################################################
#                  M   A   I   N          M    E    N    U

def main_menu():
    menu = {1: ("Generate Code", generate_code),
            2: ("Active Codes", active_codes),
            3: ("Expired/ Validated Codes", expired_codes),
            4: ("Settings", settings),
            5: ("File Stats", file_stats),
            6: ("Credit", credit)}

    for key in sorted(menu.keys()):
        print(str(key) + ": " + menu[key][0])

    while True:
        try:
            choice = int(input("\nPlease input your choice (1-6): "))

            if 1 <= choice <= 6:
                menu.get(choice)[1]()  # Call the option chosen
                break

            else:
                print("Only 6 options, try again...")
                continue

        except ValueError:
            print("\nOnly integers here, please...")
            continue

###################################################################################


###################################################################################
#                   F   I   L   E       M   E   N   U

def open_file():
    path = input("\nPlease, input the path where your folder exists: ")
    valid = open_dir(path)
    if not valid:
        main()  # if invalid, rerun main menu
    pass

def create_file():
    name = input("\nPlease, input the folder name: ")
    path = input("\nPlease enter the path where you want to create it in the form 'folder/subfolder': ")
    create_dir(name, path)
    pass
###################################################################################


def credit_print():
    print('''
Lemurer Discount Code Generator [Version 0.0.0]
Copyright <c> 2019 Lemurer Company

Type <help> fo more information.
''')


def help_print():
    print('''Help''')
    commands()


def commands():
    # This is a dictionary menu for the command line
    # All possible commands are inside the commands dictionary (commands_dict)
    commands_dict = {"help": help_print,
                "openfile": open_file,
                "createfile": create_file,
                }
    command = input(COMMAND_PREFIX)

    try:
        commands_dict[command]()  # Call the procedure/function specified by the command
    except:  # If the command is not found:
        print("Type <help> fo more information")
        commands()

# I don't understand what you did here, please explain me
#if __name__ == "__main__":
#    credit_print()
#    commands()
#    file_menu()


def main():
    credit_print()
    commands()


main()
