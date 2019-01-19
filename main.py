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
COMMAND_PREFIX = "lemurer@dcg"
COMMAND_SUFFIX = " $ "

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


###################################################################################
#                    E  R  R  O  R    F  U  N  C  T  I  O  N  S

def error01():
    print('''Error 01: Unexpected input
Type <help> for more information
''')


###################################################################################
#                      M  I  S  C     F  U  N  C  T  I  O  N  S

def dcg_credits():
    print('''
Lemurer Discount Code Generator [Version 0.0.0]
Copyright <c> 2019 Lemurer Company

Type <help> fo more information.
''')


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
            decision = input("\nPath doesn't exist, would you like to create it? [Y/n]: ").upper()[0]

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

###################################################################################
#                  M   A   I   N          F  U  N  C  T  I  O  N  S


def random_code():
    pass


def generate_code():
    code = ""
    # Calls validate_discount_amount to enter value and format it as <DXXX>
    discount_amount = validate_discount_amount()
    code += discount_amount
    # Read config file
    # Export the number of bits for the code
    # Generate unique code
    #code += random_code(bits)
    # Suffix the generated code with date of creation
    date_of_creation = f_today()

    # Input days to expire
    # Suffix the days to expire to the generated code
    # Store the code in random/direct access file via hashing algorithm
    # Update stats
    pass


def validate_discount_amount():
    valid = False
    while not valid:
        try:
            discount_amount = int(input("Enter discount percentage [1-100]: "))
        except:  # If discount amount is not an integer
            error01()
            validate_discount_amount()  # Try again
            break  # Not sure about this line of code
        if (discount_amount > 0) and (discount_amount <= 100):
            valid = True

    # Once the discount amount is valid, format it to be 3 digit string
    format_discount_amount = str(discount_amount)

    if len(format_discount_amount) == 2:
        format_discount_amount = "0" + format_discount_amount
    elif len(format_discount_amount) == 1:
        format_discount_amount = "00" + format_discount_amount

    format_discount_amount = "D" + format_discount_amount
    return format_discount_amount


def validate_code():
    # Input code
    # Hash code and look for position in random/direct access file
    # If found:
    #   Check expiration date
    #       If expired:
    #             Move to expired_codes
    #             Print message
    #       Else:
    #             Validate
    #             Print message
    #             Move to expired_codes
    #       Update stats
    # If not found print error
    pass


def clean_expired_codes():
    # Overwrite file with new empty serial file
    pass


def create_settings():
    pass


def read_settings():
    # Read settings file
    # Store all constants in the program
    # Close file
    pass


def change_settings():
    # Read_settings()
    # Show values
    # Input new values
    # Write new values
    pass


def new_file_stats():
    # Create file in specified directory
    # Init all values to 0
    # Close file
    pass


def init_file_stats():
    # Read file stats
    # Store all constants in program
    # Close file
    pass


def close_file_stats():
    # Write stats file will all the constants
    # Close file
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
    folder_name = input("Enter the folder's name: ")
    path = input("\nEnter the path where you want to create it - in the form 'folder/subfolder': ")
    create_dir(folder_name, path)
    pass


def file_menu_help():
    print('''Help ''')
    file_menu()


def file_menu_clear():
    for lines in range(300):
        print(" ")
    dcg_credits()
    file_menu()


def file_menu():
    # All possible commands are inside the commands dictionary (commands_dict)
    commands_dict = {"help": file_menu_help,
                "openfile": open_file,
                "createfile": create_file,
                "clear": file_menu_clear,
                }
    command = input(COMMAND_PREFIX + COMMAND_SUFFIX)

    try:
        commands_dict[command]()  # Call the procedure/function specified by the command
    except:  # If the command is not found:
        error01()
        file_menu()

###################################################################################


# I don't understand what you did here, please explain me
#if __name__ == "__main__":
#    credit_print()
#    commands()
#    file_menu()

###################################################################################
#                              M  A  I  N
def main():
    dcg_credits()
    # User is only allowed to access file menu until the file is specified or created
    file_menu()
    # Once the file is specified, user can access main menu
    main_menu()



main()


# from tkinter.filedialog import *
# Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
# filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
# print(filename)
