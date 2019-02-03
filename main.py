# Lemurer Discount Code Generator [Version Alpha 0.0.6e]
# Last Update: 03.02.19


# ---------------
# Program imports

import os  # used for directories and file manipulation
import pickle  # used for binary files manipulations
import time  # give information about dates and time
import hashlib  # hashing algorithms
import uuid  # random, unique code ID


# ---------------
# Program Credits
def project_credits():
    print('''
Lemurer Discount Code Generator [Version Alpha 0.0.6a]
Copyright <c> 2019 Lemurer Company''')


# ------------------
# Program Constants

MAIN_FILE_NAME = "Discount Code Generator"


# ---------------
# Program Objects


class DiscountCode:

    num = 0  # Counter (increases every time new code is created)

    def __init__(self, cID):  # constructor
        self.__codeID = cID  # unique code ID number given to each code
        self.__amount = 0  # amount of discount percentage
        self.__code = self.num  # code number
        self.__creationDate = today()  # date of code creation
        self.__timeToExpire = 0  # days until expiration
        self.__codeValid = True  # boolean flag to indicate whether the code is valid or not

        self.num += 1

    def SetDiscount(self, amount):  # setter
        self.__amount = amount

    def SetCodeValid(self, valid):  # setter
        self.__codeValid = valid

    def SetTimeToExpire(self, time_to_exp):  # setter
        self.__timeToExpire = time_to_exp

    def GetDiscount(self):  # setter
        return self.__amount

    def GetCode(self):  # getter
        return self.__codeID

    def GetNumber(self): # getter
        return self.__code

    def GetCreationDate(self):  # getter
        return self.__creationDate

    def GetTimeToExpire(self):  # getter
        return self.__timeToExpire

    def GetValid(self):  # getter
        return self.__codeValid

    def UpdateCode(self):  # setter
        # procedure that checks if the code has expired or not, it will update the codeValid flag accordingly
        pass

    def PrintCode(self):
        print('''
---------------------------
CodeID : {0}
Code Number: {1}
Discount Amount: {2}
Creation Date: {3}
Time To Expire: {4}
Valid: {5}
----------------------------'''.format(self.GetCode(),
                                       self.GetNumber(),
                                       self.GetDiscount(),
                                       self.GetCreationDate(),
                                       self.GetTimeToExpire(),
                                       self.GetValid()))


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

    today_date = time.strftime("%d/%m/%Y")
    return today_date


def table_output(codes):
    # Function that contains code for enhanced output of code details
    # Parameter: list of code objects

    sep = '-' * 113  # Separator for table

    print("{:^82}".format("CODES"))
    print(sep)
    print("{:<8s}{:>12s}{:>25s}{:>21s}{:>25s}".format("CODE #", "CODE ID", "DISCOUNT PERCENTAGE", "CREATION DATE",
                                               "DAYS FOR EXPIRATION"))
    print(sep)

    for c in codes:
        print("{:<12}{:>15s}{:^55s}{:>17s}{:>28}".format(c.code, c.codeID, c.amount, c.creationDate,
                                                   c.timeToExpire))

    print(sep)


def code_output(codes):
    # Procedure that prints codes data of an array.
    # If the codeID is 0 (a dummy record) it will not consider it.
    for i in range(len(codes)):
        if codes[i].GetCode() != 0:
            codes[i].PrintCode()


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
                "stats": [file_stats, 2],
                "savefile": [save_file, 2],
                "closefile": [close_file, 2],
                "usecode": [use_code, 2]
                }
    print("")
    print(">> Input a valid command, type \"commands\" to view all commands")
    command = input("main@commands_menu $ ")
    if command == "terminate":
        terminate = terminate_confirm()
        return terminate, priority
    elif command == "openfile":
        priority = open_file()
    elif command == "closefile":
        priority = close_file()
    else:
        try:
            if (commands_dict[command][1] == 0) or (commands_dict[command][1] == priority):
                commands_dict[command][0]()  # call the procedure/function specified by the command
            else:
                print(command, ": insufficient priority")

        except KeyError:  # specified key is not found in the dictionary
            print(command, ": command not found")

    return False, priority


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
If you terminate the program you will lose all the progress
done and you may risk the file becoming corrupt.
Are you sure you want to terminate the program? [Y/N]
''')
    while True:
        option = input("main@comands_menu@terminate $ ").upper()[0]
        if option == "Y":
            return True
        elif option == "N":
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
<usecode> : use a discount code
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
    global new_file_location
    new_file_location = current_location + "/" + file_name

    # Load config.dat into config_data
    try:
        file_handle = open(new_file_location + "/config.dat", "rb")
    except FileNotFoundError:
        print(file_name, ": file not found")
        return 1

    try:
        global config_data
        config_data = (pickle.load(file_handle))
    except EOFError:
        print("Failed to load config file data")
        return 1
    file_handle.close()

    # Validate file password
    print(">> Input file password")
    password = input("main@commands_menu@openfile $ ")
    hash_object = hashlib.md5(password.encode())
    hash_password = hash_object.hexdigest()

    if hash_password != config_data["password"]:
        print(password, ": invalid password")
        return 1

    # Load stats.dat into stats_data
    try:
        file_handle = open(new_file_location + "/stats.dat", "rb")
    except FileNotFoundError:
        print(file_name, ": file not found")
        return 1
    try:
        global stats_data
        stats_data = (pickle.load(file_handle))
    except EOFError:
        print("Failed to load stats data")
        return 1
    file_handle.close()

    # Load active.codes into active_data
    try:
        file_handle = open(new_file_location + "/active.codes", "rb")
    except FileNotFoundError:
        print(file_name, ": file not found")
        return 1

    global active_data
    active_data = []  # initialise inactive_data array

    EOF = False
    while not EOF:
        try:
            active_data.append(pickle.load(file_handle))
        except EOFError:
            EOF = True
    file_handle.close()

    # Load inactive.codes into inactive_data
    try:
        file_handle = open(new_file_location + "/inactive.codes", "rb")
    except FileNotFoundError:
        print(file_name, ": file not found")
        return 1

    try:
        global inactive_data
        inactive_data = (pickle.load(file_handle))
    except EOFError:
        print("Failed to load inactive codes data")
        return 1
    file_handle.close()

    return 2  # When the file is opened successfully the priority is updated


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
    file_content = ('''Discount Code Generator README.txt file\n
    \n
PYTHON CODE GENERATOR MODULE\n
Module allows for the manipulation and creation of unique codes,\n
user interface based on command line prompts. \n
For documentation on the various different commands and their uses, \n
run command command_list() in the main program. \n
\n
Source Code: https://github.com/Alestiago/discountcodegenerator\n
Lemurer Company 2019\n
''')
    file_handle.write(file_content)
    file_handle.close()

    # Create config.dat inside new_fie_location
    file_handle = open(new_file_location + "/config.dat", "wb")  # open file for binary write

    # Create file password
    print(">> Input a file password")
    password = input("main@commands_menu@new_file $ ")
    hash_object = hashlib.md5(password.encode())
    hash_password = hash_object.hexdigest()

    # Specify amount of codes that can be generated
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
                      "password": hash_password,
                      "codes_limit": codes_limit,
                      "code_digits": len(str(codes_limit)),
                      }  # dictionary containing configuration details
    pickle.dump(config_details, file_handle)  # write whole dictionary to the binary file config.dat
    file_handle.close()  # close binary file config.dat

    # Create stats.dat inside new_file_location
    file_handle = open(new_file_location + "/stats.dat", "wb")  # open file for binary write
    stats_details = {"file_creation": today(),
                      "last_update": today(),
                      "generated_codes": 0,
                      "validated_codes" : 0,
                      "expired_codes": 0,
                      }  # dictionary containing configuration details
    pickle.dump(stats_details, file_handle)  # write whole dictionary to the binary file stats.dat
    file_handle.close()  # close binary file stats.dat

    # Create active.codes inside new_file_location
    file_handle = open(new_file_location + "/active.codes", "wb")  # open active codes file for binary write
    active_codes = []  # initialise inactive codes array
    for i in range(codes_limit):
        # Fill all the file with dummy records
        #active_codes.append(DiscountCode(0))  # making active codes as:
        active_codes = [DiscountCode(0) for i in range(codes_limit)]
        pickle.dump(active_codes[i], file_handle)  # write a whole record to binary file active.codes

    file_handle.close()  # close active.codes file

    # Create inactive.codes inside new_file_location
    file_handle = open(new_file_location + "/inactive.codes", "wb")  # open inactive codes file for binary write
    inactive_codes = [DiscountCode(0)]  # initialise inactive codes array
    pickle.dump(inactive_codes, file_handle)  # write a whole array to binary file inactive.codes

    file_handle.close()  # close inactive.codes file


# -------------------------
# Priority "three" commands

def generate_code():
    # Generates code and inserts it into codes object list

    code_id = str(uuid.uuid4().fields[-1])[:5]

    # Input amount of discount
    print(">> Input discount amount for code")
    amount = input("main@commands_menu@generate_code $ ")
    while True:
        try:
            assert(0 < int(amount) <= 100)
            break
        except AssertionError:
            print(amount, " : is not a valid integer")
            amount = input("main@commands_menu@generate_code $ ")
            continue

    # Input days until expiration
    print(">> Input amount of days until code expires")
    days_until_expire = input("main@commands_menu@generate_code $ ")
    while True:
        try:
            assert(0 < int(days_until_expire) <= 999999)
            break
        except AssertionError:
            print(amount, " : is not a valid  integer")
            days_until_expire = input("main@commands_menu@generate_code $ ")
            continue

    # Create new code record
    new_code = DiscountCode(code_id)
    new_code.SetDiscount(amount)
    new_code.SetTimeToExpire(days_until_expire)

    # Store new code record inside hash table
    codes_limit = config_data["codes_limit"]
    code_address = hash(new_code.GetCode()) % codes_limit

    active_data[code_address] = c
    stats_data["generated_codes"] += 1
    save_file()


def use_code():
    # Validate the discount code, by using it it becomes inactive.
    pass


def update_codes():
    # Procedure that checks all codes and check if they have expired or not
    codes_limit = config_data["codes_limit"]
    for i in range(codes_limit):
        active_data[i].UpdateCode()  # check if code has expired
        if not active_data[i].GetValid():
            inactive_data.append(active_data[i])
            active_data[i] = DiscountCode(0)
            global stats_data
            stats_data["expired_codes"] += 1


def file_active_codes():
    #table_output(active_data)
    code_output(active_data)


def file_inactive_codes():
    #table_output(inactive_data)
    code_output(inactive_data)


def clear_file_inactive_codes():
    global inactive_data
    inactive_data = [DiscountCode(0)]


def file_settings():
    pass


def file_stats():
    print('''
---------------------------
File Creation: {0}
Last Update: {1}
Generated Codes: {2}
Validated Codes: {3}
Expired Codes: {4}
---------------------------'''.format(stats_data["file_creation"],
                                      stats_data["last_update"],
                                      stats_data["generated_codes"],
                                      stats_data["validated_codes"],
                                      stats_data["expired_codes"]))


def save_file():
    # Saving config.dat
    file_handle = open(new_file_location + "/config.dat", "wb")  # open file for binary write
    pickle.dump(config_data, file_handle)  # write whole dictionary to the binary file config.dat
    file_handle.close()  # close binary file config.dat
    # Saving stats.dat
    file_handle = open(new_file_location + "/stats.dat", "wb")  # open file for binary write
    global stats_data
    stats_data["last_update"] = today()
    pickle.dump(stats_data, file_handle)  # write whole dictionary to the binary file stats.dat
    file_handle.close()  # close binary file stats.dat
    # Saving active.codes
    file_handle = open(new_file_location + "/active.codes", "wb")  # open active codes file for binary write
    codes_limit = config_data["codes_limit"]
    for i in range(codes_limit):
        # Fill all the file with dummy records
        pickle.dump(active_data[i], file_handle)  # write a whole record to binary file active.codes

    file_handle.close()  # close active.codes file
    # Saving inactive.codes
    file_handle = open(new_file_location + "/inactive.codes", "wb")
    pickle.dump(inactive_data, file_handle)  # write whole array to the binary file inactive.codes
    file_handle.close()  # close inactive.codes file
    print("File Saved")
    print("")


def close_file():
    save_file()
    return 1


# ****************** Main program ******************

def main():
    priority = 1  # user starts with priority "one" since no file has been opened/created
    _terminate_ = False
    while not _terminate_:
        _terminate_, priority = commands_menu(priority)
    lemur()


if __name__ == "__main__":  # please add a comment to this to explain what it does.
    main()


# try:
    # main()
# except Exception:
    # print("Unknown Exception, please report your incidence to Lemurer.")
