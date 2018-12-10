# Script Name   : create_dir_home.py
# Author        : Abhijit Kumar
# Created       : 9th September 2018

# Description   : Checks to see if a directory exists in the users home directory, if not then creates it. 

import os  # Import the OS module

MESSAGE = 'It exits already!'
TESTDIR = 'temp'
try:
    home = os.path.expanduser("~")  # Set the variable home by expanding the user's set home directory
    print(home)  # Print the location

    if not os.path.exists(os.path.join(home, TESTDIR)):  # os.path.join() for making a full path safely
        os.makedirs(os.path.join(home, TESTDIR))  # If not create the directory, inside their home directory
    else:
        print(MESSAGE)
except Exception as e:
    print(e)
