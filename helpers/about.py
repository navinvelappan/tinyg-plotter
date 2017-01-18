#!usr/bin/env python
"""
about.py, by Pawel Wojcik, 16-01-2017

About info
"""

import os
from helpers.menu import menu

def main():
    menu_width = 26
    title = "TINYG PLOTTER"
    active_menu = "About"
    menu_description = "Author: Pawel Wojcik\nEmail: wojcikpwl@gmail.com\nVersion: 0.1"
    menu_list = ["M - Main menu",
                 "Q - Quit"]

    os.system("clear")
    print(menu(menu_width,title, active_menu, menu_description, menu_list))

    input(" Select: ")

if __name__ == '__main__':
    main()
