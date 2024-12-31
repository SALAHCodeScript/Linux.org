#!/usr/bin/python3

# Convert String to Hexadecimal
print(hex(ord('\n'))) # > '0xa'
# Convert String to Decimal
print(ord('\n')) # > 10

# Convert Decimal to Hexadecimal
print(hex(10)) # > '0xa'
# Convert Decimal to String
print(chr(10)) # > '\n'

# Convert Hexadecimal to String
print(chr(0xa)) # > '\n'
# Convert Hexadecimal to Decimal
print(0xa) # > 10
print(int('a', 16)) # > 10
print(int('0xa', 16)) # > 10


# Format
print(format(10, 'x'))  # Output: 'a'
print(format(10, 'X'))  # Output: 'A'
print(format(10, '04x'))  # Output: '0a'
print(format(10, '04X'))  # Output: '0A'

# F-String
print(f"{10:x}")  # Output: 'a'
print(f"{10:X}")  # Output: 'A'
print(f"{10:04x}")  # Output: '0a'
print(f"{10:04X}")  # Output: '0A'
print(f"{97:c}\n")  # a
print(f"{97:o}")    # 141
