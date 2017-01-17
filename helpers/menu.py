#!usr/bin/env python
"""
menu.py, by Pawel Wojcik, 16-01-2017

Function takes title string, menu_name string and menu_content list and returns
string formatted as menu.
"""

def menu(title, menu_name, menu_content):
    width_title = len(title)+len(menu_name) + 5         # number of characters in first line + 5
    width_content = len(max(menu_content, key=len)) + 4 # number of characters in longest list entry + 4
    width = max(15,width_title,width_content)           # menu width, min 15 characters

    # menu string
    return (" " + title + " [" + menu_name + "]\n" + width*"="
            + "\n  " + "\n  ".join(menu_content) + "\n" + width*"-")

def main():
    title = "TITLE"
    menu_name = "Main menu"
    menu_content = ["A - About",
                    "Q - Quit"]

    print(menu(title, menu_name, menu_content))

if __name__ == '__main__':
    main()
