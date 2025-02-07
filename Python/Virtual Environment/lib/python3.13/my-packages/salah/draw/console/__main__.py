#!python3
import os
import sys
import time
from . import Draw

draw = Draw(sys.argv[1])

def drawUp(text, length, isNum, dot):
    consoletext = draw.consoleText()
    if isNum:
        text = f"0{text}" if length == 1 else text
        length = 2 if length == 1 else length
    print()
    for row in range(7):
        if row == 6 and dot:
            print(" ", *[consoletext[text[index]][row] for index in range(length)], end=f".\n\n")
        else:
            print(" ", *[consoletext[text[index]][row] for index in range(length)])

def drawCountTimer():
    start = int(sys.argv[3])
    end = int(sys.argv[4]) if len(sys.argv) > 4 else 0
    step = int(sys.argv[5]) if len(sys.argv) > 5 else 1
    step = step if end > start else step*(-1)
    speed = float(sys.argv[6]) if len(sys.argv) > 6 else 1
    times = int(sys.argv[7]) if len(sys.argv) > 7 else 1
    text = sys.argv[3]
    for t in range(times):
        for n in range(start, end+step, step):
            length = len(text)
            os.system("clear")
            drawUp(text, length, True, True)
            time.sleep(speed)
            text = str(int(text)+step)
        text = sys.argv[3]

try:
    if sys.argv[2] == "consoletimer":
        drawCountTimer()
    elif sys.argv[2] == "consoletext":
        sentence = [word.lower() for word in sys.argv[3:]] if len(sys.argv) > 3 else ['abcdefghij', 'klmnopqrst', 'uvwxyz']
        for word in sentence:
            text = ""
            for char in word:
                text += char
            length = len(text)
            if word == sentence[-1]:
                drawUp(text, length, False, True)
            else:
                drawUp(text, length, False, False)
except Exception:
    print("working on it\nbe paient 😃️")

