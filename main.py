#!usr/bin/env python
"""
main.py, by Pawel Wojcik, 15-01-2017

TINYG PLOTTER - Main screen
"""

import os
from helpers.menu import menu
from helpers.about import main as about

def main():
    menu_width = 32
    title = "TINYG PLOTTER"
    active_menu = "Main"
    menu_description = "* ITSligo - L7 in Mechatronics *"
    menu_list = ["C - Connect",
                 "H - Homing",
                 "L - Load Program",
                 "S - Status",
                 "A - About",
                 "Q - Quit"]

    os.system("clear")      # clear screen

    print(menu(menu_width,title, active_menu, menu_description, menu_list))     # print menu

    selection = input(" Select: ")      # wait for user selection
    if (selection == "a" or selection == "A"):
        about()
    else:
        os.system("clear")
        print("Wrong entry")
        print(15*"-")
        input(" Select: ")

if __name__ == '__main__':
    main()
