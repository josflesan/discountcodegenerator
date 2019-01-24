# Lemurer Discount Code Generator [Version Alpha 0.0.2]
# Last Update: 24.01.19


def project_credits():
    print('''
Lemurer Discount Code Generator [Version Alpha 0.0.2]
Copyright <c> 2019 Lemurer Company''')


# ------------------
# Program Constants

# -------------
# Commands Menu
# A list of all the possible commands that can be executed by the user.
# The user may not be able to execute some commands if it lacks from
# priorities to do so.

# List of priorities:
# 0 : Command can be executed whenever the user desires to
# 1 : Command can only be executed when no file has been opened or created
# 2 : Command can only be executed when there is a currently opened file
def commands_menu():
    commands_dict = {
                "help": [help_, 0],
                "commands": [commands_list, 0],
                "clear": [clear, 0],
                "credits": [project_credits, 0],
                "version": [project_credits, 0],
                "info": [project_credits, 0],
                "openfile": [open_file, 1],
                "newfile": [new_file, 1],
                }
    print("")
    command = input("main@commands_menu $ ")
    try:
        commands_dict[command][0]()  # call the procedure/function specified by the command
    except KeyError:  # specified key is not found in the dictionary
        print(command, ": command not found")
    commands_menu()

# ------------------------
# Priority "zero" commands


def help_():
    print('''
Help [1/1]
Lemurer recommends for a more detailed help to read README.txt.
If you are unable to find this file in your device, go to the
following URL: <insert_url>

''')


def commands_list():
    # Maximum ten commands per page
    page1 = '''

<help> : display a user help guideline
<commands> : display a list of all possible commands
<clear> : clear the console
<credits> | <version> | <info> : displays program information
<openfile> : open a program file
<newfile> : create a new program file
<savefile> : save program file changes
<closefile> : close and save opened file
<> :
<> :
'''
    page_number = 1  # starts reading from fist page
    pages = [page1, ]  # array of pages available
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
                    else:
                        print(page_number, ": is not a valid page number")
                except ValueError:
                    print(page_number, ": is not an integer")
            else:
                stop = True
                valid = True


def clear():
    for lines in range(100):
        print(" ")

# -----------------------
# Priority "one" commands


def open_file():
    pass


def new_file():
    # This function will create a total of 5 different files in a new sub-folder located in the program
    # file directory. The files that will be created are:

    # README.txt : Text file that contains details about the manipulation of the program
    # active.CODES : Random/Direct access file that contains all active codes
    # inactive.CODES : Serial  access file that contains all codes that have been used or expired
    # stats.DOC : Sequential access file that contains all the statistics of the file
    # config.DOC : Sequential access file that contains all the config details of the file
    pass


# -------------------------
# Priority "three" commands


# ****************** Main program ******************
commands_menu()
