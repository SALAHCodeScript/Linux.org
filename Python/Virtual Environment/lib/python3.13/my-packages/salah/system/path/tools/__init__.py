import os
import posixpath
import salah.system.os.tools as os_tools
from rich.console import Console

console = Console()

def can_be_created(name):
    if os_tools.get_machine_name() == "Windows":
        unwanted_symbol = ["\\", "/", "?", ":", ";", "\"", "'"]
        for char in name:
            if char in unwanted_symbol:
                return False
        return True
    else:
        return True

def get_symbol_path():
    return '/' if os_tools.get_machine_name() == "Linux" else '\\'    

def get_items(path, item_type = None):
    listdir = os.listdir(path)
    if item_type != None:
        listdir = [directory for directory in listdir if posixpath.isdir(f"{path}{get_symbol_path()}{directory}")]
        if item_type == 'file':
            listdir = [filename for filename in listdir if posixpath.isfile(f"{path}{get_symbol_path()}{filename}")]
    return listdir

def get_full_path(path):
    return posixpath.realpath(path)

def get_parent_path(path):
    parent_path = path[::-1][path[::-1].find(get_symbol_path())+1:][::-1]
    if parent_path[-1] == '.':
        parent_path = parent_path[:-1]
    return parent_path

def get_spreated_path(path):
    spreated_list = path.split(get_symbol_path())
    if path[0] == get_symbol_path():
        spreated_list = spreated_list[1:]
    return spreated_list

def get_basename(path):
    return get_spreated_path(path)[-1]

def get_file_basename(path):
    filename = get_basename(path)
    return filename[::-1][filename[::-1].find('.')+1:][::-1]

def get_content(path):
    if posixpath.isfile(path):
        with open(path, 'r') as file:
            load_file = file.read()
    return load_file

items = []
def get_tree(path):
    global items
    current_path = path
    for item in os.listdir(path):
        path = f"{current_path}{get_symbol_path()}{item}"
        items.append(path)
        if posixpath.isdir(path):
            get_tree(path)
    return items

def display_tree(path, items):
    display_path = f"[dir]{path}[/]"
    length = path.count('\\')
    console.print(display_path)
    for item in items:
        count_item = item.count('\\')
        tab = count_item - length
        symbol = '|'
        multiple_symbol = symbol + f'  {symbol}' * (tab - 1)
        symbol_line = '_'
        additions =  f"{multiple_symbol}{symbol_line*2}"
        item_name = get_basename(item)
        if item_name[0] == symbol_line:
            additions += '> '
        additions = f"[symbol]{additions}[/]"
        display_item = f"{additions}{item_name}"
        if posixpath.isdir(item):
            display_item = f"{additions}[dir]{item_name}[/]"
        console.print(display_item)

def fix_path(path):
    # spreated_list = get_spreated_path(path)
    # fixed_path = ""
    # if '.' in spreated_list:
    #     spreated_list.pop(spreated_list.index('.'))
    # for item in spreated_list:
    #     fixed_path += f"/{item}" if os_tools.get_machine_name() == "Linux" else f"{item}\\"
    if path[-1] == get_symbol_path():
        path = path[:-1]
    return path
