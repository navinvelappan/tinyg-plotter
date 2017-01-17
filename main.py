#!usr/bin/env python
"""
main.py, by Pawel Wojcik, 15-01-2017

TINYG PLOTTER - Main screen
"""

import os
from helpers.menu import menu
from helpers.about import about_info

def main():
    title = "TINYG PLOTTER"
    active_menu = "Main"
    menu_list = ["C - Connect",
                      "H - Homing",
                      "L - Load Program",
                      "S - Status",
                      "A - About",
                      "Q - Quit"]

    os.system("clear")      # clear screen
    print(menu(title, active_menu, menu_list))     # print menu

    selection = input(" Select: ")      # wait for user selection
    if (selection == "a" or selection == "A"):
        active_menu = "About"
        menu_list = ["M - Main",
                     "Q - Quit"]
        os.system("clear")
        print(menu(title, active_menu, menu_list))
        print(about_info())
        print(15*"-")
        input(" Select: ")
    else:
        os.system("clear")
        print("Wrong entry")
        print(15*"-")
        input(" Select: ")

if __name__ == '__main__':
    main()
