#!/usr/bin/python3

# open()
file = open("Files/read.txt", "r")
print(file.read())

# with open()
with open("Files/read.txt", "r") as file:
    print(file.read())

# Read File
with open("Files/read.txt", "r") as rfile:
    print(rfile.read())
    rfile.close()

# Write File
with open("Files/write.txt", "w") as wfile:
    wfile.write("Hello, file!")
    wfile.close()

# Append to File
with open("Files/append.txt", "a") as afile:
    afile.write("Hello, User")
    afile.close()

# Read & Write File
with open("Files/read_write.txt", "w+") as rwfile:
    rwfile.write("Hello, World")
    print(rwfile.read())
    rwfile.close()
