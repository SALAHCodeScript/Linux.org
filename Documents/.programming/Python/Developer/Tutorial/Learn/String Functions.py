#!/usr/bin/python3

# Variables
name = "salah"
strip_word = "  string  "
forList = "1,2,3"
listarray = ['one', 'two', 'three']

# Attributes
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())
print(name.isalpha())
print(name.isdigit())
print(name.startswith('s'))
print(name.endswith('a'))
print(name.center(len(name)))
print(strip_word.strip())
print(strip_word.replace('  str', 'replac'))
print(forList.split(','))
print(", ".join(listarray))
