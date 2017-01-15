#!usr/bin/env python
"""
main.py, by Pawel Wojcik, 15-01-2017

TINYG PLOTTER - Main menu
"""

import os

# set variables
title = "TINYG PLOTTER"
active_menu = "Main"
menu_width = len(title)+len(active_menu)+5
main_menu = ["C - Connect","H - Homing","L - Load Program","S - Status","C - Configuration","A - About","Q - Quit"]

def main():
    # clear screen
    os.system("clear")

    # print menu
    print(" " + title + " [" + active_menu + "]")
    print(menu_width * "=")
    for menu_item in main_menu:
        print("  " + menu_item)
    print(menu_width * "-")

    # menu selected by user
    input(" Select: ")

if __name__ == '__main__':
    main()
