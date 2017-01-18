#!usr/bin/env python
"""
menu.py, by Pawel Wojcik, 16-01-2017

Function takes title string, menu_name string and menu_content list and returns
string formatted as menu.
"""

def menu(width, title, menu_name, menu_description, menu_content):
    # menu string
    return (" " + title + " [" + menu_name + "]\n" + width*"="
            + "\n" + menu_description + "\n" + width*"-" + "\n  "
            + "\n  ".join(menu_content) + "\n" + width*"-")

def main():
    width = 25
    title = "TITLE"
    menu_name = "Main menu"
    menu_description = "Description goes here..."
    menu_content = ["A - About",
                    "Q - Quit"]

    print(menu(25,title, menu_name, menu_description, menu_content))

if __name__ == '__main__':
    main()
