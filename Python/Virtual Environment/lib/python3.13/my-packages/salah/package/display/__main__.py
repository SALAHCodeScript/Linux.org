"""hey there, you are in SALAH his 'Package Management' library (Python3.13)"""
import os
import sys
import posixpath
import subprocess
import salah.system.path.tools as path_tools
import salah.parsing.python.tools as parse_tools
from rich.console import Console
from rich.table import Table
import click

def get_data(file, function):
    data = {}
    directory = ["__init__.py", "__main__.py"]
    grandparent = file
    parent = path_tools.get_basename(path_tools.get_parent_path(file)) if path_tools.get_basename(file) in directory else path_tools.get_file_basename(file)
    child = function(file)
    data[grandparent] = {}
    data[grandparent][parent] = child
    return data

def display(library, data):
    keys = list(data.keys())
    for key in keys:
        if library == key:
            directory = ["__init__.py", "__main__.py"]
            parent = path_tools.get_basename(path_tools.get_parent_path(library)) if path_tools.get_basename(library) in directory else path_tools.get_file_basename(library)
            if data[key][parent] == []:
                return "[red]Empty[/]"
            return data[key][parent]

def display_as_table(key, value):
    table = Table()
    table.add_column(key)
    table.add_row(value)
    return table

@click.command(help=__doc__)
@click.argument("library", required=False)
@click.option('-t', "--type", type=click.Choice(["function", "class"]), required=False, help="display function or class of a library")
@click.option('-f', "--file", default="init", type=click.Choice(["init", "main"]), required=False, help="choose bettween '__init__.py' or '__main__.py' file")
@click.option('-l', "--list", is_flag=True, required=False, help="listing all existing packages")
@click.option('-h', is_flag=True, required=False, help="get help of a library")
@click.option('-p', "--path", is_flag=True, required=False, help="print path of a library")
@click.option('-t', "--tree", is_flag=True, required=False, help="display tree of a library")
def main(library, type, file, list, h, path, tree):
    console = Console()

    cmd = "salah.package.display"
    library = library if library != None else cmd

    list_pack = sys.path[1:]
    packages = []
    for pack in list_pack:
        if posixpath.isdir(pack):
            for item in os.listdir(pack):
                full_path = f"{pack}{path_tools.get_symbol_path()}{item}"
                skip_items = ['DLLs', 'Doc', 'etc', 'include', 'Lib', 'libs', 'Scripts', 'share']
                if ((posixpath.isfile(full_path) and full_path.endswith(".py")) or posixpath.isdir(full_path)) and item[0] != '_' and not(item.endswith(".dist-info")) and not(item.endswith(".libs")) and not(item in skip_items):
                    packages.append(item[:-3]) if item.endswith(".py") else packages.append(item)

    libs = library.split('.')
    parent = libs[0]
    lib = libs[-1]
    
    displayed_issue = f"'{lib}'"
    if len(libs) == 2:
        displayed_issue = f"'{lib}' of parent '{parent}'"
    elif len(libs) > 2:
        displayed_issue = f"'{lib}' in '{'.'.join(libs[1:-1])}' of parent '{libs[0]}'"

    if not(list) and not(h) and not(path) and not(tree):
        path_lib = subprocess.run(["py", "-c", f"import {library} as pack; print(pack.__file__)"], capture_output=True).stdout.decode()[:-2]

        file = "__init__.py" if file == "init" else "__main__.py"
        path_lib = path_lib.replace("__init__.py", file)
        library_path = path_lib

        if path_lib != "":
            if posixpath.exists(path_lib):
                functions = get_data(library_path, parse_tools.get_functions)
                classes = get_data(library_path, parse_tools.get_classes)

                if type == "function":
                    console.print(display(library_path, functions))
                elif type == "class":
                    console.print(display(library_path, classes))
                elif not type:
                    console.print(display_as_table(library_path, path_tools.get_content(library_path)))

            elif not(posixpath.exists(library_path)) and path_tools.get_basename(library_path) == "__main__.py":
                issue = f"package: {displayed_issue} doesn't have '__main__.py' file!"
                console.print(issue)
        else:
            issue = f"there is no package named: {displayed_issue}!\ntype 'py -m {cmd} --help' for more information"
            import_parent_lib = subprocess.run(["py", "-c", f"import {parent} as pack; print(pack.__file__)"], capture_output=True).stdout.decode()[:-2]
            import_lib_as_name = subprocess.run(["py", "-c", f"import {library} as pack; print(pack.__name__)"], capture_output=True).stdout.decode()[:-2]

            if import_parent_lib == "" and len(libs) > 1:
                issue = f"the parent package: '{parent}' is not exists!\ntype 'py -m {cmd} --help' for more information"
            elif import_lib_as_name != "":
                issue = f"there is package with name: {displayed_issue} but can't find where is it located!\ntype 'py -m {cmd} --help' for more information"

            possible_packages = []
            for pack in packages:
                if parent in pack:
                    possible_packages.append(pack)
            if len(possible_packages) > 0:
                issue_sentence = f"there is no package named: {displayed_issue}!\nmaybe you meant one of these libraries: '{', '.join(possible_packages)}'" if len(possible_packages) > 1 else f"there is no package named: {displayed_issue}!\nmaybe you meant this library: '{packages[0]}'"
                issue = f"{issue_sentence}!\ntype 'py -m {cmd} --help' for more information"

            console.print(issue)
    elif h:
        get_help_for_pack = subprocess.run(["py", "-c", f"import {library} as pack; print(pack.__doc__)"], capture_output=True).stdout.decode()[:-2]
        console.print(get_help_for_pack)
    elif list:
        console.print("\n".join(packages))
    elif path:
        get_path_of_pack = subprocess.run(["py", "-c", f"import {library} as pack; print(pack.__file__)"], capture_output=True).stdout.decode()[:-2]
        if get_path_of_pack == "":
            get_path_of_pack = f"there is package with name: {displayed_issue} but can't find where is it located!\ntype 'py -m {cmd} --help' for more information"
        console.print(get_path_of_pack)
    elif tree:
        get_path_of_pack = subprocess.run(["py", "-c", f"import {library} as pack; print(pack.__file__)"], capture_output=True).stdout.decode()[:-2]
        if path_tools.get_basename(get_path_of_pack) == "__init__.py":
            tree = path_tools.get_tree(path_tools.get_parent_path(get_path_of_pack))
            items = []
            for item in tree:
                basename = path_tools.get_basename(item)
                if not(basename[0] == '_'):
                    items.append(item)
            path_tools.display_tree(path_tools.get_parent_path(get_path_of_pack), items)

if __name__ == "__main__":
    main()
