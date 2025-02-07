import os
import subprocess as subp

path = "D:\\Data\\SALAH\\home\\salah\\Documents\\.programming"
command_path = "Developer\\Project\\Command"

for dir in os.listdir(path):
	if os.path.exists(fr"{path}\{dir}\{command_path}") and not(os.listdir(f"{path}\\{dir}\\{command_path}") == []):
		print(f"{dir}:")
		return_code = subp.run(["ls", f"{path}\\{dir}\\{command_path}"], capture_output=True).stdout.decode()
		print(return_code[:-1].split("\n"))
