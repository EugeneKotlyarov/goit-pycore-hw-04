from colorama import Fore, Back, Style
import os
import time as t


# constants for print results colors (success or error)
# for full book display color
# and full commands menu

COLOR_DONE = Fore.GREEN
COLOR_ERROR = Fore.RED
COLOR_MENU = Fore.WHITE
COLOR_BOOK = Fore.BLUE
COMMANDS_MENU = f"""
Welcome! Assistant bot's commands menu:
 add <name> <number> \t\t# to add new single contact to phone book
 change <name> <new_number> \t# to change contact's number
 phone <name> \t\t\t# show contact's phone number by its name (if exist)
 all\t\t\t\t# show all contacts in the book
 exit | close \t\t\t# exit from assistant
"""


# action results printed with their colors
# after each command COMMANDS_MENU will be displayed
#
# arguments count in main function so its not implemented in others
#
# function PARSE_INPUT was already implemented in the task, just copied
#
# function ADD_CONTACT adds record if KeyError exception raised
# and NOT modify existing records
#
# function CHANGE_CONTACT changes record if it exists
#
# function SHOW_PHONE return contact's number if exists
#
# function ALL displays all book


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    try:
        if contacts[name]:
            return f'{COLOR_ERROR}Contact "{name}" WAS NOT added. Already exist. Please use "change" command for edit'
    except KeyError:
        contacts[name] = phone
        return f'{COLOR_DONE}Contact "{name}" with number "{phone}" was added'


def change_contact(args, contacts):
    name, phone_new = args
    try:
        if contacts[name]:
            phone_old = contacts[name]
            contacts[name] = phone_new
            return f'{COLOR_DONE}Phone number for "{name}" was changed from "{phone_old}" to "{phone_new}"'
    except KeyError:
        return f'{COLOR_ERROR}Contact "{name}" WAS NOT found. Please use "add" command to create one'


def show_phone(args, contacts):
    name = args
    try:
        if contacts[name]:
            return f'{COLOR_DONE}Phone number found. Name: "{name}", phone: {contacts[name]}'
    except KeyError:
        return f'{COLOR_ERROR}Contact "{name}" WAS NOT found. Please use "add" command to create one'
    except TypeError:
        return f'{COLOR_ERROR}Contact "{name}" WAS NOT found. Phone book is empty now'


def main():

    contacts = {}

    while True:
        # os.system("clear")
        print(f"{COLOR_MENU}{COMMANDS_MENU}")
        user_input = input(f"Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print(f"{COLOR_MENU}Good bye!")
            break

        elif command == "add" and len(args) == 2:
            print("\n" + add_contact(args, contacts))

        elif command == "change" and len(args) == 2:
            print("\n" + change_contact(args, contacts))

        elif command == "phone" and len(args) == 1:
            print("\n" + show_phone(args, contacts))

        elif command == "all":
            print(
                f'\n{COLOR_BOOK}Full address book [numbers in base: {len(contacts)}]\n{"Name":^12}{"phone":^12}'
            )
            for k, v in contacts.items():
                print(f"{k:^12}{v:^12}")

        else:
            print(f"\n{COLOR_ERROR}Invalid command or too few/many arguments")


if __name__ == "__main__":
    main()
