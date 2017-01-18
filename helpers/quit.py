#!usr/bin/env python
"""
quit.py, by Pawel Wojcik, 18-01-2017

Quit
"""

import os
from helpers.menu import menu

def main():
    menu_width = 33
    title = "TINYG PLOTTER"
    active_menu = "Quit"
    menu_description = "Thank you for using TinyG Plotter"
    menu_list = ["Press ENTER to quit..."]

    os.system("clear")
    print(menu(menu_width, title, active_menu, menu_description, menu_list))

    input()

    os.system("clear")
if __name__ == '__main__':
    main()
