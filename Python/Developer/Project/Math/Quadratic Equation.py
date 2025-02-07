import math
import sys
from rich.console import Console

console = Console()

arguments = sys.argv[1:]

def hasOperator(equation):
    operators = ['+', '-']
    for operator in equation:
        if operator in operators:
            return True

def getFunction(arguments):
    

def A(function):
    side_a = function[0]
    if '**2' in side_a and 'x' in side_a:        
        if not(hasOperator(side_a)):
            side_a = f"+{side_a}"
    else:
        sys.exit()
    return side_a

def x1(a, b, delta):
    return (-b + math.sqrt(delta)) / 2*a

def x2(a, b, delta):
    return (-b - math.sqrt(delta)) / 2*a

def displaySolution(a, b, c):
    delta = math.pow(b, 2) - 4*(a)*(c)
    if delta == 0:
        x1(a, b, delta)
    elif delta > 0:
        x1(a, b, delta)
        x2(a, b, delta)
    elif delta < 0:
        return "No solution"

def main():
    # console.print(*function)
    # console.print(displaySolution(a, b, c))
    pass

if __name__ == "__main__":
    main()
