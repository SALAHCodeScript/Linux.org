#!/usr/bin/python3
import string

# Variables
myrange = range
array = list(string.ascii_uppercase)
numbbers_set = {1, 2, 3, 4, 5}
double_array1 = ((d, s) for d, s in enumerate(string.ascii_uppercase, 1))
double_array2 = ((d, s) for d, s in enumerate(string.ascii_uppercase, 1))
dictionary = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
name = "SALAH"

# For Loop: Range
## 1
for i in range(10):
    print(i) # Start from 0 to 8
## 2
for i in range(0, 10):
    print(i) # Start from 0 to 8
## 3
for i in range(0, 10, 1):
    print(i) # Start from 0 to 8 for One Step
## 4
for i in myrange(0, 10, 1):
    print(i) # Start from 0 to 8

# For Loop: Enumerate
## 1
for i in enumerate(array):
    print(i)
## 2
for e, i in enumerate(array):
    print(f"{e} | {i}")
## 3
for e, i in enumerate(array, 1):
    print(f"{e} | {i}")

# For Loop: List
for s in array:
    print(s)

# For Loop: Set
for d in numbbers_set:
    print(d)

# For Loop: Tuple
## 1
for t in double_array1:
    print(t)
## 2
for d, s in double_array2:
    print(d, s)

# For Loop: Dict
## 1
for k in dictionary:
    print(k)
## 2
for v in dictionary.values():
    print(v)
## 3
for k in dictionary.keys():
    print(k)
## 4
for k, v in dictionary.items():
    print(f'{k} | {v}')

# For Loop: Strings
for s in range(len(name)):
    print(name[s])
