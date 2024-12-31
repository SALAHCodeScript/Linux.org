#!/usr/bin/python3

# Variables
x, y = 0, 10

# While Loop: While
while x < y:
   print(x)
   x += 1

# While Loop: And
while x < y and x == 0:
   print(x)
   x += 1

# While Loop: And
while x < y or y > x:
   print(x)
   x += 1

# While Loop: Multiple Conditions
while (x < y and x == 0) or y > x:
   print(x)
   x += 1
