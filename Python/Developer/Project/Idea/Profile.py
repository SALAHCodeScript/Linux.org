#!/usr/bin/python3.13
import sys as s
import rich as r

def hasNumber(string):
    is_all_true = []
    for char in string:
        if char.isdigit() and not(char.isalpha()) and not(hasSymbol(char)):
            is_all_true.append(True)
        else:
            is_all_true.append(False)
    return True if True in is_all_true else False

def hasSymbol(string):
    is_all_true = []
    for char in string:
        if not(char.isdigit()) and not(char.isalpha()):
            is_all_true.append(True)
        else:
            is_all_true.append(False)
    return True if True in is_all_true else False

def isName(data):
    return True if not(hasNumber(data)) and not(hasSymbol(data)) and len(data) > 2 else False

def isAge(data):
    return True if data.isdigit() and int(data) > 0 and int(data) < 100 else False

def isEmail(data):
    is_all_true = []
    for char in data:
        if char == "@" and data[-4:] == ".com":
            is_all_true.append(True)
        else:
            is_all_true.append(False)
    return True if True in is_all_true else False

def isPhoneNumber(data):
    if len(data) == 11:
        if data[3] == '-' and data[7] == '-':
            if data.replace('-', '').isdigit():
                return True
    return False

def getData(*arguments):
    arguments = list(arguments)
    data = {"names":[], "ages":[], "emails":[], "phone numbers":[]}
    for arg in arguments:
        if isName(arg):
            data["names"].append(arg)
        elif isAge(arg):
            data["ages"].append(arg)
        elif isEmail(arg):
            data["emails"].append(arg)
        elif isPhoneNumber(arg):
            data["phone numbers"].append(arg)
    for person in range(len(data["emails"])):
        try:
            if not(data["emails"][person] == "") and len(data["emails"]) > len(data["names"]) and data["names"][person] == "":
                name = data["emails"][person][:data["emails"][person].find("@")]
                data["names"].append(name)
        except IndexError:
                name = data["emails"][person][:data["emails"][person].find("@")]
                data["names"].append(name)
    return data

def buildData(data, people):
    dict_data = {}
    for person in range(people):
        key_name = data["names"][person].capitalize()
        dict_data[key_name] = {}
        for d in range(4):
            try:
                key = list(data.keys())[d][:-1].capitalize()
                value = data[list(data.keys())[d]][person]
                dict_data[key_name][key] = value
            except IndexError:
                key = list(data.keys())[d][:-1].capitalize()
                dict_data[key_name][key] = None
    return dict_data

def displayProfile():
    data = getData(*[arg for arg in s.argv[1:]])
    r.print_json(data=buildData(data, len(data["names"])))

displayProfile()

