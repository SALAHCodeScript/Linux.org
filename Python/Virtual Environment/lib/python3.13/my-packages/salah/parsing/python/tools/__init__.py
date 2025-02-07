import os
import posixpath
import salah.system.path.tools as path_tools

def get_python_file_list(path):
    file_content = path_tools.get_content(path)
    lines = file_content.split('\n')[:-1]
    return lines

def get_functions(path):
    list_file = get_python_file_list(path)
    list_functions = []
    for line in list_file:
        if "def" in line and line.find("def") == 0 and line[-1] == ':':
            list_functions.append(line[line.find("def"):line.find(':')])
    return list_functions

def get_classes(path):
    list_file = get_python_file_list(path)
    list_clases = []
    for line in list_file:
        if "class" in line and line.find("class") == 0 and line[-1] == ':':
            list_clases.append(line[line.find("class"):line.find(':')])
    return list_clases




















#def get_description(path, function):
#    list_file = get_python_file_list(path)
#    list_names = function(path)
#    description_list = []
#    for name in list_names:
#        specific_func = list_file[list_file.index(f"{name}:"):]
#        dot = "    \"\"\""
#        if dot in list_file:
#            description = specific_func[specific_func.index(dot)+1:]
#            description = description[:description.index(dot)][0]
#            description_list.append(description)
#    return description_list

