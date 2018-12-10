# Filename: countingcharacters.py
# Creator: Abhijit Kumar
# Created On: May 7, 2018


# Description: A simple program illustrating how Python counts the number of characters from a given text file.

"""Get the number of each character in any given text.
Inputs:
A txt file -- You will be asked for an input file. Simply input the name
of the txt file in which you have the desired text.
"""

import pprint
import collections


def main():
    file_input = input('File Name: ')
    try:
        with open(file_input, 'r') as info:
            count = collections.Counter(info.read().upper())
    except FileNotFoundError:
        print("Please enter a valid file name.")
        main()

    value = pprint.pformat(count)
    print(value)
    exit()


if __name__ == "__main__":
    main()
