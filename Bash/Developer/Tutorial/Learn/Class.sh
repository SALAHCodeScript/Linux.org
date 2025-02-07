#!/usr/bin/python3

# Without Initiailizing
class Welcome:
   name = "SALAH"
    ## Method
   def hello(self):
      return f"Hello, {self.name}"
## Create A New Class
user1 = Welcome()
print(user1.name)       # Print "SALAH"
print(user1.hello())    # Print "Hello, SALAH"

# Wit Initiailizing
class Welcome:
    def __init__(self, name):
        self.name = name
    ## Method
    def hello(self):
        return f"Hello, {self.name}"
## Create A New Class
user1 = Welcome("SALAH")
print(user1.name)       # Print "SALAH"
print(user1.hello())    # Print "Hello, SALAH"
