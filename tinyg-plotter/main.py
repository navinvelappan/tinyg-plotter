#!usr/bin/env python
"""
main.py, by Pawel Wojcik, 20-01-2017

TINYG PLOTTER - Main screen
"""

import os


# Program main menu
def main_menu():
    menu_width = 32
    title = "TINYG PLOTTER"
    active_menu = "Main"
    menu_description = "* ITSligo - L7 in Mechatronics *"
    menu_list = ["C - Connect",
                 "A - About",
                 "Q - Quit"]

    os.system("clear")      # clear screen

    print(menu(menu_width,title, active_menu, menu_description, menu_list))     # print menu

    selection = input("Select: ").lower()      # wait for user selection

    if selection == "a":
        about()

    elif selection == "q":
        close()

    else:
        invalid_selection()


# About information
def about():
    menu_width = 26
    title = "TINYG PLOTTER"
    active_menu = "About"
    menu_description = "Author: Pawel Wojcik\nEmail: wojcikpwl@gmail.com\nVersion: 0.1"
    menu_list = ["M - Main menu",
                 "Q - Quit"]
    os.system("clear")

    print(menu(menu_width, title, active_menu, menu_description, menu_list))

    selection = input("Select: ").lower()

    if selection == "m":
        main_menu()

    elif selection == "q":
        close()

    else:
        invalid_selection()


# Menu generator
def menu(width, title, menu_name, menu_description, menu_content):
    return (title + " [" + menu_name + "]\n" + width * "="
            + "\n" + menu_description + "\n" + width * "-" + "\n"
            + "\n".join(menu_content) + "\n" + width * "-")

# Wrong selection message
def invalid_selection():
    os.system("clear")
    menu_width = 27
    title = "TINYG PLOTTER"
    active_menu = "Error"
    menu_description = "Wrong entry"
    menu_list = ["Press ENTER to try again..."]

    os.system("clear")
    print(menu(menu_width, title, active_menu, menu_description, menu_list))

    input()

    main_menu()


# Closing message
def close():
    menu_width = 33
    title = "TINYG PLOTTER"
    active_menu = "Exit"
    menu_description = "Thank you for using TinyG Plotter"
    menu_list = ["Press ENTER to quit..."]

    os.system("clear")
    print(menu(menu_width, title, active_menu, menu_description, menu_list))

    input()

    os.system("clear")


if __name__ == '__main__':
    main_menu()
