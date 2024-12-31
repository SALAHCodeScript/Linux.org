#!/usr/bin/python3

# Variables
numbers = [1, 3, 2, 4]
alphabet = ["a", "b", "c", "d"]

# max()
print(max(numbers))

# min()
print(min(numbers))

# sorted()
print(sorted(numbers))
print(sorted(alphabet))

# zip()
zipped = list(zip(sorted(numbers), sorted(alphabet)))
print(zipped)

# map()
squared = list(map(lambda x: x ** 2, numbers))

# filter()
evens = list(filter(lambda x: x % 2 == 0, numbers))

# all()
print(all([x > 0 for x in numbers]))

# any()
print(any([x < 0 for x in numbers]))

# join()
print(", ".join(alphabet))

