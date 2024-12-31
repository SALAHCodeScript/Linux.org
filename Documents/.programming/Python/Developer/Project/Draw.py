#!/usr/bin/python3
import os
import sys as s

class Shape:
    def __init__(self, text):
        self.text = text
        self.length = len(self.text)

    def draw1(self):
        print(f"{self.text:>{self.length*4}}")
        print(f"{self.text:>{self.length*3}}{self.text:>{self.length*2}}")
        print(f"{self.text:>{self.length*2}}{self.text:>{self.length*4}}")
        print(f"{self.text:>{self.length}}{self.text:>{self.length*6}}") # Middle
        print(f"{self.text:>{self.length*2}}{self.text:>{self.length*4}}")
        print(f"{self.text:>{self.length*3}}{self.text:>{self.length*2}}")
        print(f"{self.text:>{self.length*4}}")

    def draw2(self):
        print(f"{self.text} {self.text:>{self.length}} {self.text:>{self.length}}")
        print(f"{self.text} {" "*(self.length)} {self.text:>{self.length}}")
        print(f"{self.text} {" "*(self.length)} {self.text:>{self.length}}") # Middle
        print(f"{self.text} {" "*(self.length)} {self.text:>{self.length}}")
        print(f"{self.text} {self.text:>{self.length}} {self.text:>{self.length}}")

    def draw3(self):
        pass


# shape = Shape(input("Enter A Word\n>_"))
shape = Shape("SAL")
if s.argv[1] == '1':
   shape.draw1()
elif s.argv[1] == '2':
   shape.draw2()
elif s.argv[1] == '3':
   shape.draw3()


#          SAL
#       SAL   SAL
#    SAL         SAL
# SAL               SAL
#    SAL         SAL
#       SAL   SAL
#          SAL

# SAL SAL SAL
# SAL     SAL
# SAL     SAL
# SAL     SAL
# SAL SAL SAL
