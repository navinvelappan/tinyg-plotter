#!usr/bin/env python
"""
about.py, by Pawel Wojcik, 16-01-2017

About info
"""

def about_info():
    author = "Author: Pawel Wojcik"
    email = "Email: wojcikpwl@gmail.com"
    version = "Version: 0.1"

    return ("  " + author + "\n  " + email + "\n  " + version)

def main():
    print(about_info())

if __name__ == '__main__':
    main()
