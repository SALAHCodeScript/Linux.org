import os
import sys
import posixpath
from rich.console import Console
from rich.theme import Theme

file_manager = Theme({"dir": "bold blue", "symbol": "white"})
console = Console(theme=file_manager)

class Command():
    def __init__(self, path: str = '.', options: list[str] = []):
        self.path = path
        self.main_path = path
        self.length = path.count('/')
        self.options = options
        self.list_options = ['-a']
        self.items = []

    def displayTree(self):
        display_path = f"[dir]{self.main_path}[/]"
        console.print(display_path)
        for item in self.items:
            count_item = item.count('/')
            tab = count_item - self.length
            symbol = '|'
            multiple_symbol = symbol + f'  {symbol}' * (tab - 1)
            symbol_line = '_'
            additions =  f"{multiple_symbol}{symbol_line*2}"
            item_name = posixpath.basename(item)
            if item_name[0] == symbol_line:
                additions += '> '
            additions = f"[symbol]{additions}[/]"
            display_item = f"{additions}{item_name}"
            if posixpath.isdir(item):
                display_item = f"{additions}[dir]{item_name}[/]"
            console.print(display_item)

    def tree(self):
        current_path = self.path
        for item in os.listdir(current_path):
            self.path = f"{current_path}/{item}"
            hidden = True if item[0] == '.' else False
            if '-a' in self.options:
                self.items.append(self.path)
                if posixpath.isdir(self.path):
                    self.tree()
            elif not('-a' in self.options) and not(hidden):
                self.items.append(self.path)
                if posixpath.isdir(self.path):
                    self.tree()

    def execute(self):
        self.tree()
        self.displayTree()

def getPath(path):
    return posixpath.realpath(path)

def getOptions(option):
    list_options = Command().list_options
    arguments = sys.argv[1:]
    return True if option[0] == '-' and option in list_options and arguments.count(option) == 1 else False

def main():
    path = getPath('.') if len(sys.argv) == 1 else getPath(sys.argv[1])
    path = getPath('.') if posixpath.basename(path) in Command().list_options else path
    arguments = sys.argv[1:]
    options = list(filter(getOptions, arguments))
    command = Command(path, options)
    command.execute()

if __name__ == "__main__":
    main()
