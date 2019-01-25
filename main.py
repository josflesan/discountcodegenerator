# Lemurer Discount Code Generator [Version Alpha 0.0.4b]
# Last Update: 24.01.19


def project_credits():
    print('''
Lemurer Discount Code Generator [Version Alpha 0.0.4b]
Copyright <c> 2019 Lemurer Company''')

# ---------------
# Program imports


import os  # used for directories and file manipulation
import pickle  # used for binary files manipulations
import time  # give information about dates and time

# ------------------
# Program Constants

MAIN_FILE_NAME = "Discount Code Generator"

# ---------------
# Program Objects


class DiscountCode:

    def __init__(self):
        self.codeID = 0  # unique code ID number given to each code
        self.amount = 0  # amount of discount percentage
        self.code = 0  # code number
        self.creationDate = None  # date of code creation
        self.timeToExpire = 0  # days until expiration
        self.codeValid = True  # boolean flag to indicate whether the code is valid or not


# --------------
# Misc Functions

def create_dir(location):
    # Function that creates a new directory where specified,
    # if the directory already exists it return False.
    try:
        os.mkdir(location)
        return True
    except OSError:
        return False


def today():
    # Function that returns today's date.
    # dd/mm/yyyy format
    todays_date = time.strftime("%d/%m/%Y")
    return todays_date


def lemur():
    print("I love lemurs <3")


# -------------
# Commands Menu
# A list of all the possible commands that can be executed by the user.
# The user may not be able to execute some commands if it lacks from
# priorities to do so.

# List of priorities:
# 0 : Command can be executed whenever the user desires to
# 1 : Command can only be executed when no file has been opened or created
# 2 : Command can only be executed when there is a currently opened file
def commands_menu(priority):
    commands_dict = {
                "help": [help_, 0],
                "commands": [commands_list, 0],
                # "terminate": [terminate, 0]
                "clear": [clear, 0],
                "credits": [project_credits, 0],
                "version": [project_credits, 0],
                "info": [project_credits, 0],
                "lemur": [lemur, 0],
                "openfile": [open_file, 1],
                "newfile": [new_file, 1],
                "newcode": [generate_code, 2],
                "gencode": [generate_code, 2],
                "activecodes": [file_active_codes, 2],
                "acodes": [file_active_codes, 2],
                "inactivecodes": [file_inactive_codes, 2],
                "icodes": [file_inactive_codes, 2],
                "clearinactivecodes": [clear_file_inactive_codes, 2],
                "cicodes": [clear_file_inactive_codes, 2],
                "settings": [file_settings, 2],
                "stats": [file_stats, 2]
                }
    print("")
    print(">> Input a valid command, type \"commands\" to view all commands")
    command = input("main@commands_menu $ ")
    if command == "terminate":
        terminate = terminate_confirm()
        return terminate
    else:
        try:
            if (commands_dict[command][1] == 0) or (commands_dict[command][1] == priority):
                commands_dict[command][0]()  # call the procedure/function specified by the command
            else:
                print(command, ": insufficient priority")

        except KeyError:  # specified key is not found in the dictionary
            print(command, ": command not found")

            return False

# ------------------------
# Priority "zero" commands


def help_():
    print('''
Help [1/1]
Lemurer recommends for a more detailed help to read README.txt.
If you are unable to find this file in your device, go to the
following URL: <insert_url>

''')


def clear():
    for lines in range(100):
        print(" ")


def terminate_confirm():
    print('''
Warning!
If you terminate the program you will loose all the progress
done and you may risk the file becoming corrupt.

Are you sure you want to terminate the program? [Y/n]
''')
    while True:
        option = input("main@comands_menu@terminate $ ")
        if (option == "Y") or (option == "y"):
            return True
        elif (option == "N") or (option == "n"):
            return False
        else:
            print(option, ": input not recognised")


def commands_list():
    # Maximum ten commands per page
    page1 = '''

<help> : display a user help guideline
<commands> : display a list of all possible commands
<terminate> : finish execution of program
<clear> : clear the console
<credits> | <version> | <info> : displays program information
<openfile> : open a program file
<newfile> : create a new program file
<savefile> : save program file changes
<closefile> : close and save opened file
<lemur> : print lemur
'''
    page2 = '''

<newcode> | <gencode> : generate new discount code
<activecodes> | <acodes> : print a list of all active codes
<inactivecodes> | <icodes>: print a list of all inactive codes
<clearinactivecodes> | <cicodes> : delete all inactive codes
<settings> : view and modify configuration of file
<stats> : view file's statistics
'''

    page_number = 1  # starts reading from first page
    pages = [page1, page2]  # array of pages available
    page_header = "Commands List [{0}/{1}]".format(page_number, len(pages))
    page_footer = '''
You are currently reading page number {0}. If you wish to skip
to another page input the desired page number. If you want to
stop reading the commands list input "stop".'''.format(page_number)

    stop = False
    while not stop:
        print(" ")
        print(page_header, pages[page_number - 1], page_footer)
        valid = False
        while not valid:
            page_number = input("main@commands_menu@commands_list $ ")
            if page_number != "stop":
                try:
                    page_number = int(page_number)
                    if (page_number > 0) and (page_number <= len(pages)):
                        valid = True
                        # Update header and footer page number values
                        page_header = "Commands List [{0}/{1}]".format(page_number, len(pages))
                        page_footer = '''
You are currently reading page number {0}. If you wish to skip
to another page input the desired page number. If you want to
stop reading the commands list input "stop".'''.format(page_number)
                    else:
                        print(page_number, ": is not a valid page number")
                except ValueError:
                    print(page_number, ": is not an integer")
            else:
                stop = True
                valid = True


# -----------------------
# Priority "one" commands


def open_file():
    current_location = os.getcwd() + "/" + MAIN_FILE_NAME  # get current .py location
    print(">> Input file name")
    file_name = input("main@commands_menu@openfile $ ")
    new_file_location = current_location + "/" + file_name

    # Load config.dat into config_data
    file_handle = open(new_file_location + "/config.dat", "rb")

    try:
        config_data = (pickle.load(file_handle))
    except EOFError:
        pass
    file_handle.close()

    # Load stats.dat into stats_data
    file_handle = open(new_file_location + "/stats.dat", "rb")

    try:
        stats_data = (pickle.load(file_handle))
    except EOFError:
        pass
    file_handle.close()

    pass


def new_file():
    # This function will create a total of 5 different files in a new sub-directory located
    # in the program's file directory. The files that will be created are:

    # README.txt : Text file that contains details about the manipulation of the program
    # active.codes : Random/Direct access binary file that contains all active codes
    # inactive.codes : Serial  access binary file that contains all codes that have been used or expired
    # stats.doc : Binary file that contains all the statistics of the file
    # config.doc : Binary file that contains all the config details of the file

    current_location = os.getcwd()  # get current .py location

    # Check if MAIN_FILE_NAME directory exists, if not create it

    program_location = str(current_location) + "/" + MAIN_FILE_NAME
    create_dir(program_location)  # create MAIN_FILE_NAME if it does not exist

    # Create new directory (folder) inside MAIN_FILE_NAME
    print(">> Input new file name")
    new_file_name = input("main@commands_menu@create_file $ ")  # users specifies new file name
    new_file_location = program_location + "/" + new_file_name  # format new file name to be a valid directory
    valid_name = create_dir(new_file_location)  # create new file name
    if not valid_name:  # if file name already exists
        print(new_file_location, ": File already exists")
        return  # stop running procedure

    # Create README.txt inside new_file_location
    file_handle = open(new_file_location + "/README.txt", "w")
    file_content = ('''Discount Code Generator README.txt file
Line Number 1                                             
Line Number 2                                             
Line Number 3''')
    file_handle.write(file_content)
    file_handle.close()

    # Create config.dat inside new_fie_location
    file_handle = open(new_file_location + "/config.dat", "wb")  # open file for binary write

    print(">> Input maximum number of codes that can be generated")
    valid = False  # validate that the code limit is a positive integer
    while not valid:
        try:
            codes_limit = input("main@commands_menu@new_file $ ")
            codes_limit = int(codes_limit)
            if codes_limit > 1:
                valid = True
            else:
                print(codes_limit, ": is not a positive integer")
        except ValueError:
            print(codes_limit, ": is not an integer")

    config_details = {"file_location": new_file_location,
                      "codes_limit": codes_limit,
                      "code_digits": len(str(codes_limit)),
                      }  # dictionary containing configuration details
    pickle.dump(config_details, file_handle)  # write whole dictionary to the binary file config.dat
    file_handle.close()  # close binary file config.dat

    # Create stats.dat inside new_file_location
    file_handle = open(new_file_location + "/stats.dat", "wb")  # open file for binary write
    config_details = {"file_creation": today(),
                      "last_update": today(),
                      "generated_codes": 0,
                      "inactive_codes": 0,
                      }  # dictionary containing configuration details
    pickle.dump(config_details, file_handle)  # write whole dictionary to the binary file stats.dat
    file_handle.close()  # close binary file stats.dat

    # Create active.codes inside new_file_location
    # Create inactive.codes inside new_file_location


# -------------------------
# Priority "three" commands

def generate_code():
    pass


def file_active_codes():
    pass


def file_inactive_codes():
    pass


def clear_file_inactive_codes():
    pass


def file_settings():
    pass


def file_stats():
    pass


# ****************** Main program ******************
def main():
    priority = 1    # user starts with priority "one" since no file has been opened/created
    _terminate_ = False
    while not _terminate_:
        _terminate_ = commands_menu(priority)
    lemur()


main()


# try:
    # main()
# except Exception:
    # print("Unknown Exception, please report your incidence to Lemurer.")
