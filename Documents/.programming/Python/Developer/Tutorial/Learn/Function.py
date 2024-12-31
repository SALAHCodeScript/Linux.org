#!/usr/bin/python3

# Normal Function
## Without Parmaters
def hello1():
   print(f"Hello SALAH")
## With Parmaters
def hello2(user):
    print(f"Hello {user}")

# Return Function
## Without Parmaters
def sum1():
    return 1 + 1
## With Parmaters
def sum2(x, y):
    return x + y

# Function Inside Function
def calculator():
    def addition(x, y):
        return x + y
    def subtract(x, y):
        return x - y
    def multiple(x, y):
        return x * y
    def division(x, y):
        return x / y
    return addition

# Call Function
hello1()
hello2('SALAH')
print(sum1())
print(sum2(1, 1))
add = calculator()(1, 1)
print(f"{add}")
