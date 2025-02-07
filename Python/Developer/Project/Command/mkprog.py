import os
import logging
import click


file = __file__
filename = file[::-1][:file[::-1].find('\\')][::-1]
log_path = f"D:\\Data\\SALAH\\home\\salah\\Documents\\.programming\\Python\\Developer\\Project\\Command\\logs\\{filename}.log"
logging.basicConfig(filename=log_path, level=logging.DEBUG,
                   format='%(asctime)s - %(levelname)s - %(message)s')


def hasUnwantedSymbol(string):
    unwanted_symbol = ["\\", "\\", "?", ":", ";", "\"", "'"]
    for char in string:
        if char in unwanted_symbol:
            return True
    return False

def isSymbol(directory):
    return True if not(directory.isalpha()) and not(directory.isdigit()) else False

def isDirectory(directory):
    return True if not(hasUnwantedSymbol(directory)) and not(isSymbol(directory[0])) and not(directory[0].isdigit()) and len(directory) > 2 else False


def print_info(text, isverbose):
    if isverbose:
        print(text)

def make_directory(directory_name, cmd, pack, venv, isverbose):
    directory_name = f"D:\\Data\\SALAH\\home\\salah\\Documents\\.programming\\{directory_name}"
    directories = [f"{directory_name}\\Developer", f"{directory_name}\\Project", f"{directory_name}\\Web", f"{directory_name}\\Developer\\Project", f"{directory_name}\\Developer\\Quick", f"{directory_name}\\Developer\\Tutorial", f"{directory_name}\\Developer\\Tutorial\\Basic", f"{directory_name}\\Developer\\Tutorial\\Learn"]
    extra_dir_structure = [f"{directory_name}\\Developer\\Project\\Command", f"{directory_name}\\Developer\\Packages", f"{directory_name}\\Virtual Environment"]
    for child in directories:
        os.makedirs(child)
        print_info(f"'{child}' has created", isverbose)
        logging.info(f"'{child}' has created")
    extra = [index for index in range(3) if [cmd, pack, venv][index]]
    for index in extra:
        os.makedirs(extra_dir_structure[index])
        print_info(f"'{extra_dir_structure[index]}' has created", isverbose)
        logging.info(f"'{extra_dir_structure[index]}' has created")

def configure_dirprogramming_file(directory_name, short_name, venv, isverbose):
    dir_prog = "D:\\Data\\SALAH\\home\\salah\\Documents\\.programming\\Bash\\Developer\\Project\\Command\\dirprogramming"
    script_list = []
    with open(dir_prog, 'r') as file:
        for line in file.readlines():
            script_list.append(line[0:-1])
        file.close()
    script = f"elif [ \"$lang\" = \"{short_name}\" ]; then\n   cd {directory_name}\n   navigate\nfi\n"
    if venv:
        script = f"elif [ \"$lang\" = \"{short_name}\" ]; then\n   cd {directory_name}\n   virtual_environment=\"Virtual Environment\"\n   navigate\nfi\n"
    script_list = script_list[:-2]
    for line in script.split("\n"):
        script_list.append(line)
    script_list = script_list[:-1]
    script_list.append('\n')
    with open(dir_prog, 'w') as file:
        for word in "\n".join(script_list):
            file.write(word)
        file.close()
    print_info(f"'{dir_prog}' has modified ({directory_name})", isverbose)
    logging.info(f"'{dir_prog}' has modified ({directory_name})")


@click.command()
@click.argument("directory_name", required=True)
@click.argument("short_name", required=False)
@click.option('-d', "--dir", is_flag=True, required=False)
@click.option('-f', "--file", is_flag=True, required=False)
@click.option('-df', "-fd", "--dir-file", "--file-dir", is_flag=True, required=False)
@click.option('-c', "--cmd", is_flag=True, required=False)
@click.option('-p', "--pack", is_flag=True, required=False)
@click.option('-e', "--venv", is_flag=True, required=False)
@click.option('-cp', '-pc', "--cmd-pack", "--pack-cmd", is_flag=True, required=False)
@click.option('-ce', '-ec', "--cmd-venv", "--venv-cmd", is_flag=True, required=False)
@click.option('-pe', '-ep', "--pack-venv", "--venv-pack", is_flag=True, required=False)
@click.option('-v', "--verbose", is_flag=True, required=False)
def main(directory_name, short_name, dir, file, dir_file, cmd, pack, venv, cmd_pack, cmd_venv, pack_venv, verbose):
    short_name = short_name if short_name != None else directory_name.lower()
    cmd = True if cmd_pack or cmd_venv else cmd
    pack = True if cmd_pack or pack_venv else pack
    venv = True if cmd_venv or pack_venv else venv
    if isDirectory(directory_name) and isDirectory(short_name):
        if dir or dir_file:
            make_directory(directory_name, cmd, pack, venv, verbose)
        if file or dir_file:
            configure_dirprogramming_file(directory_name, short_name, venv, verbose)

if __name__ == "__main__":
    main()
