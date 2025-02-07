#!/usr/bin/python3
import datetime

# Variables
name = "SALAH"
x, y, z = 1, 2.0, 123

# Methods
## Method 1: % C-Style
print("%d + %f = %.1f" % (x, y, x+y))
## Method 2: Format Function
print("{} + {} = {}".format(x, y, x+y))
print("{:d} + {:f} = {:.1f}".format(x, y, x+y))
## Method 3: F-String
print(f"{x} + {y} = {x+y}")
print(f"{x:d} + {y:f} = {x+y:.1f}")

# Format Specifiers: String
print(f"{name:s}")
print(f"{name:>10}")
print(f"{name:^10}")
print(f"{name:<10}")
## 0o
print(f"{0o123:o}")
print(f"{0o40:x}") # 41-66 > A-Z | 73-98 > a-z
print(f"{0o123:c}") # 16-25 > 0-9 | 33-58 > A-Z | 65-90 > a-z ! Last Number is 1114111
## 0x
print(f"{0x123:c}")
## 0b
print(f"{0b0} {0b1}") # ! Working Only with 0b0 & 0b1
## Important > :o :c :x | Doesn't Work With 8 & 9

# Format Specifiers: Integer
print(f"{x:d}")
print(f"{z:o}")
print(f"{z:x}")
print(f"{z:c}")
print(f"{1e5}")
print(f"{x+y=}")
print(f"{0o123}")
print(f"{0x123}")
print(f"{0x123:o}")
print(f"{0x123:x}")

# Format Specifiers: Float
print(f"{y:.2f}")
print(f"{y:.5e}")
print(f"{y:g}")

# Format Specifiers: Time
date1 = datetime.datetime.now()
date2 = datetime.datetime.now().strftime('%D/%m/%Y - %I:%M:%S %p')
print(f'{date1:%D/%m/%Y - %I:%M:%S %p}')
print(f"{date2}")
