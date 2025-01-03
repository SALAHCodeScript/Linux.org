#!/usr/bin/python3.13
import sys as s
import os

# Check if Symbol is True or not
def hasUnwantedSymbol(file):
    unwanted_symbol = ["\\", "/", "?", ":", ";", "\"", "'"]
    for char in file:
        if char in unwanted_symbol:
            return True
    return False

# Check if Symbol is True or not
def isSymbol(string):
    return True if not(string.isalpha()) and not(string.isdigit()) else False

# Check if Option is True or not
def isOption(option):
    options = ["f", "d"]
    items = []
    for char in option[1:]:
        if (option[0] == '-') and (char in options) and (option[1:].count(char) == 1):
            items.append(True)
        else:
            items.append(False)
    return False if (False in items or items == []) else True

def mergeOptions(options):
    option = ""
    for opt in options[1:]:
        option += opt
    items = []
    for char in option:
        print(char)
    #     if option.count(char) == 1:
    #         items.append(True)
    #     else:
    #         items.append(False)
    # return False if (False in items or items == []) else True

# Check if File is True or not
def isFile(file):
    return True if not(isOption(file)) and not(hasUnwantedSymbol(file)) and not(isSymbol(file[0])) and not(file[0].isdigit()) else False

# Get Argument Variables
arguments = s.argv[1:]
files = list(filter(isFile, arguments))
options = list(filter(isOption, arguments))
structure = list(filter(lambda x: True if x.isdigit() else False, arguments))

# Files
file_name = [file for file in files if file.istitle()]
file_name = file_name[0] if not(file_name == []) else s.exit()
short_name = [file for file in files if file.islower()]
short_name =  short_name if not(short_name == []) else file_name.lower()

# Options
options = options if not(options == []) else ["-df"]

# Structure
structure = structure[0] if not(structure == []) else ["1"]


# Test
mergeOptions(options)
