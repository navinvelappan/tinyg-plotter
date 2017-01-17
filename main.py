#!usr/bin/env python
"""
main.py, by Pawel Wojcik, 15-01-2017

TINYG PLOTTER - Main screen
"""

import os
from helpers.menu import menu

def main():
    title = "TINYG PLOTTER"
    active_menu = "Main"
    main_menu_list = ["C - Connect",
                      "H - Homing",
                      "L - Load Program",
                      "S - Status",
                      "A - About",
                      "Q - Quit"]

    os.system("clear")      # clear screen
    print(menu(title, active_menu, main_menu_list))     # print menu
    input(" Select: ")      # wait for user selection

if __name__ == '__main__':
    main()
