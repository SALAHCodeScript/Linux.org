class Draw:
    def __init__(self, text: str = '#-#'):
        self.text = text
        self.length = len(self.text)

    def consoleText(self):
        return {
#.Zero
        "0": [
         f"{self.text} {self.text} {self.text} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text} {self.text} {self.text} "
        ],
#.One
        "1": [
         f" {self.text:>{self.length*2}} {'':>{self.length}} ",
         f"{self.text} {self.text} {'':>{self.length}} ",
         f" {self.text:>{self.length*2}} {'':>{self.length}} ",
         f" {self.text:>{self.length*2}} {'':>{self.length}} ",
         f" {self.text:>{self.length*2}} {'':>{self.length}} ",
         f" {self.text:>{self.length*2}} {'':>{self.length}} ",
         f"{self.text} {self.text} {self.text} "
        ],
#.Two
        "2": [
         f"{self.text} {self.text} {self.text} ",
         f"  {self.text:>{self.length*3}} ",
         f"  {self.text:>{self.length*3}} ",
         f"{self.text} {self.text} {self.text} ",
         f"{self.text}  {'':>{self.length*2}} ",
         f"{self.text}  {'':>{self.length*2}} ",
         f"{self.text} {self.text} {self.text} "
        ],
#.Three
        "3": [
         f"{self.text} {self.text} {self.text} ",
         f"  {self.text:>{self.length*3}} ",
         f"  {self.text:>{self.length*3}} ",
         f"{self.text} {self.text} {self.text} ",
         f"  {self.text:>{self.length*3}} ",
         f"  {self.text:>{self.length*3}} ",
         f"{self.text} {self.text} {self.text} "
        ],
#.Four
        "4": [
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text} {self.text} {self.text} ",
         f"  {self.text:>{self.length*3}} ",
         f"  {self.text:>{self.length*3}} ",
         f"  {self.text:>{self.length*3}} "
        ],
#.Five
        "5": [
         f"{self.text} {self.text} {self.text} ",
         f"{self.text}  {'':>{self.length*2}} ",
         f"{self.text}  {'':>{self.length*2}} ",
         f"{self.text} {self.text} {self.text} ",
         f"  {self.text:>{self.length*3}} ",
         f"  {self.text:>{self.length*3}} ",
         f"{self.text} {self.text} {self.text} "
        ],
#.Six
        "6": [
         f"{self.text} {self.text} {self.text} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text} {'':>{self.length*2}}  ",
         f"{self.text} {self.text} {self.text} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text} {self.text} {self.text} "
        ],
#.Seven
        "7": [
         f"{self.text} {self.text} {self.text} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"  {self.text:>{self.length*3}} ",
         f"  {self.text:>{self.length*3}} ",
         f"  {self.text:>{self.length*3}} ",
         f"  {self.text:>{self.length*3}} "
        ],
#.Eight
        "8": [
         f"{self.text} {self.text} {self.text} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text} {self.text} {self.text} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text} {self.text} {self.text} "
        ],
#.Nine
        "9": [
         f"{self.text} {self.text} {self.text} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text} {self.text} {self.text} ",
         f"  {self.text:>{self.length*3}} ",
         f"  {self.text:>{self.length*3}} ",
         f"{self.text} {self.text} {self.text} "
        ],
#.A
        "a": [
         f" {self.text:>{self.length*2}} {'':>{self.length}} ",
         f" {self.text}{self.text:>{self.length*2}}  ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text} {self.text} {self.text} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text}  {self.text:>{self.length*2}} "
        ],
#.B
        "b": [
         f"{self.text}{self.text}{self.text}   ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text} {self.text} {self.text[0]}   ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text}{self.text}{self.text}   "
        ],
#.C
        "c": [
         f"   {self.text}{self.text} ",
         f"  {self.text[:-1]}{'':>{self.length*2}}",
         f" {self.text[:-1]} {'':>{self.length*2}}",
         f"{self.text} {'':>{self.length*2}}",
         f" {self.text[:-1]} {'':>{self.length*2}}",
         f"  {self.text[:-1]}{'':>{self.length*2}}",
         f"   {self.text}{self.text} ",
        ],
#.D
        "d": [
         f"{self.text} {self.text} {'':>{self.length}} ",
         f"{self.text}{self.text:>{self.length*2}}   ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text}{self.text:>{self.length*2}}   ",
         f"{self.text} {self.text} {'':>{self.length}} "
        ],
#.E
        "e": [
         f" {self.text}{self.text}{self.text}  ",
         f"{self.text} {'':>{self.length*2}}  ",
         f"{self.text} {'':>{self.length*2}}  ",
         f"{self.text}{self.text}{self.text}   ",
         f"{self.text} {'':>{self.length*2}}  ",
         f"{self.text} {'':>{self.length*2}}  ",
         f" {self.text}{self.text}{self.text}  "
        ],
#.F
        "f": [
         f" {self.text}{self.text}{self.text}  ",
         f"{self.text} {'':>{self.length*2}}  ",
         f"{self.text} {'':>{self.length*2}}  ",
         f"{self.text}{self.text}{self.text}   ",
         f"{self.text} {'':>{self.length*2}}  ",
         f"{self.text} {'':>{self.length*2}}  ",
         f"{self.text} {'':>{self.length*2}}  "
        ],
#.G
        "g": [
         f" {self.text}{self.text}{self.text}  ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text} {'':>{self.length*2}}  ",
         f"{self.text}  {self.text}{self.text} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f" {self.text}{self.text}{self.text}  ",
        ],
#.H
        "h": [
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text} {self.text} {self.text} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text}  {self.text:>{self.length*2}} "
        ],
#.I
        "i": [
         f"{self.text} {self.text} {self.text} ",
         f" {self.text:>{self.length*2}} {'':>{self.length}} ",
         f" {self.text:>{self.length*2}} {'':>{self.length}} ",
         f" {self.text:>{self.length*2}} {'':>{self.length}} ",
         f" {self.text:>{self.length*2}} {'':>{self.length}} ",
         f" {self.text:>{self.length*2}} {'':>{self.length}} ",
         f"{self.text} {self.text} {self.text} "
        ],
#.J
        "j": [
         f"{'':>{self.length}}  {self.text}{self.text} ",
         f"  {self.text:>{self.length*3}} ",
         f"  {self.text:>{self.length*3}} ",
         f"  {self.text:>{self.length*3}} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f" {self.text}{self.text}{self.text}  "
        ],
#.K
        "k": [
         f"{self.text}      {self.text} ",
         f"{self.text}    {self.text}   ",
         f"{self.text}  {self.text}     ",
         f"{self.text}{self.text}       ",
         f"{self.text}  {self.text}     ",
         f"{self.text}    {self.text}   ",
         f"{self.text}      {self.text} "
        ],
#.L
        "l": [
         f"{self.text}  {'':>{self.length*2}} ",
         f"{self.text}  {'':>{self.length*2}} ",
         f"{self.text}  {'':>{self.length*2}} ",
         f"{self.text}  {'':>{self.length*2}} ",
         f"{self.text}  {'':>{self.length*2}} ",
         f"{self.text}  {'':>{self.length*2}} ",
         f"{self.text} {self.text} {self.text} "
        ],
#.M
        "m": [
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text}{self.text[0]}{'':>{self.length}}{self.text[0]}{self.text} ",
         f"{self.text} {self.text} {self.text} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text}  {self.text:>{self.length*2}} "
        ],
#.N
        "n": [
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text}{self.text[0]} {self.text:>{self.length*2}} ",
         f"{self.text} {self.text[0]}{self.text:>{self.length*2}} ",
         f"{self.text}  {self.text[0]}  {self.text} ",
         f"{self.text}   {self.text[0]} {self.text} ",
         f"{self.text}    {self.text[0]}{self.text} ",
         f"{self.text}  {self.text:>{self.length*2}} "
        ],
#.O
        "o": [
         f" {self.text}{self.text}{self.text}  ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f" {self.text}{self.text}{self.text}  "
        ],
#.P
        "p": [
         f" {self.text}{self.text}{self.text}  ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text}{self.text}{self.text}   ",
         f"{self.text}  {'':>{self.length*2}} ",
         f"{self.text}  {'':>{self.length*2}} ",
         f"{self.text}  {'':>{self.length*2}} "
        ],
#.Q
        "q": [
         f" {self.text}{self.text}{self.text}  ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"  {self.text}{self.text}{self.text} ",
         f"  {self.text:>{self.length*3}} ",
         f"  {self.text:>{self.length*3}} ",
         f"  {self.text:>{self.length*3}} ",
        ],
#.R
        "r": [
         f"{self.text}{self.text}{self.text}{self.text[0]} ",
         f"{self.text}    {self.text} ",
         f"{self.text}   {self.text}  ",
         f"{self.text}{self.text}{self.text[0]}    ",
         f"{self.text}  {self.text}   ",
         f"{self.text}   {self.text}  ",
         f"{self.text}    {self.text} "
        ],
#.S
        "s": [
         f" {self.text} {self.text}{self.text} ",
         f"{self.text}  {'':>{self.length*2}} ",
         f"{self.text}  {'':>{self.length*2}} ",
         f" {self.text}{self.text}{self.text}  ",
         f"  {self.text:>{self.length*3}} ",
         f"  {self.text:>{self.length*3}} ",
         f"{self.text} {self.text}{self.text}  "
        ],
#.T
        "t": [
         f"{self.text} {self.text} {self.text} ",
         f" {self.text:>{self.length*2}} {'':>{self.length}} ",
         f" {self.text:>{self.length*2}} {'':>{self.length}} ",
         f" {self.text:>{self.length*2}} {'':>{self.length}} ",
         f" {self.text:>{self.length*2}} {'':>{self.length}} ",
         f" {self.text:>{self.length*2}} {'':>{self.length}} ",
         f" {self.text:>{self.length*2}} {'':>{self.length}} "
        ],
#.U
        "u": [
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f" {self.text}   {self.text}  ",
         f"   {self.text[0]}{self.text}{self.text[0]} {'':>{self.length}}"
        ],
#.V
        "v": [
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f" {self.text}   {self.text}  ",
         f"  {self.text} {self.text}   ",
         f"{'':>{self.length}} {self.text} {'':>{self.length}} "
        ],
#.W
        "w": [
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text}  {self.text:>{self.length*2}} ",
         f"{self.text} {self.text} {self.text} ",
         f"{self.text}{self.text[0]}{'':>{self.length}}{self.text[0]}{self.text} ",
         f"{self.text}  {self.text:>{self.length*2}} "
        ],
#.X
        "x": [
         f"{self.text[:-1]}{' ':>{self.length*2-1}}{self.text[:-1]} ",
         f" {self.text[:-1]}   {self.text[:-1]}  ",
         f"  {self.text[:-1]} {self.text[:-1]}   ",
         f"{' ':>{self.length}}{self.text}    ",
         f"  {self.text[:-1]} {self.text[:-1]}   ",
         f" {self.text[:-1]}   {self.text[:-1]}  ",
         f"{self.text[:-1]}{' ':>{self.length*2-1}}{self.text[:-1]} ",
        ],
 #.Y
        "y": [
         f"{self.text[:-1]}{' ':>{self.length*2-1}}{self.text[:-1]} ",
         f" {self.text[:-1]}   {self.text[:-1]}  ",
         f"  {self.text[:-1]} {self.text[:-1]}   ",
         f"{' ':>{self.length}}{self.text}    ",
         f"{' ':>{self.length}}{self.text}    ",
         f"{' ':>{self.length}}{self.text}    ",
         f"{' ':>{self.length}}{self.text}    ",
        ],
#.Z
        "z": [
         f"{self.text} {self.text} {self.text} ",
         f"{'':>{self.length*2}}  {self.text[:-1]}{'':>{self.length-1}}",
         f"{'':>{self.length+2}} {self.text[:-1]}{'':>{self.length}} ",
         f"   {self.text[:-1]}{'':>{self.length*2}} ",
         f" {self.text[:-1]}{'':>{self.length*2}}   ",
         f"{self.text[:-1]}{'':>{self.length*2}}    ",
         f"{self.text} {self.text} {self.text} "
        ],
#.Space
        " ": [
         f"{' ':>{self.length}} ",
         f"{' ':>{self.length}} ",
         f"{' ':>{self.length}} ",
         f"{' ':>{self.length}} ",
         f"{' ':>{self.length}} ",
         f"{' ':>{self.length}} ",
         f"{' ':>{self.length}} ",
        ],
#.'
        "'": [
         f"{self.text[1]}{' ':>{self.length}}",
         f"{self.text[1]}{' ':>{self.length}}",
         f"{self.text[1]}{' ':>{self.length}}",
         f"{self.text[1]}{' ':>{self.length}}",
         f"{' ':>{self.length}} ",
         f"{' ':>{self.length}} ",
         f"{' ':>{self.length}} "
        ],
#."
        "\"": [
         f"{self.text[1]*2}{' ':>{self.length}}",
         f"{self.text[1]*2}{' ':>{self.length}}",
         f"{self.text[1]*2}{' ':>{self.length}}",
         f"{self.text[1]*2}{' ':>{self.length}}",
         f"{' ':>{self.length*2}}",
         f"{' ':>{self.length*2}}",
         f"{' ':>{self.length*2}}"
        ],
#.!
        "!": [
         f" {self.text:>{self.length*2}} {'':>{self.length}} ",
         f" {self.text:>{self.length*2}} {'':>{self.length}} ",
         f" {self.text:>{self.length*2}} {'':>{self.length}} ",
         f" {self.text:>{self.length*2}} {'':>{self.length}} ",
         f" {self.text:>{self.length*2}} {'':>{self.length}} ",
         f"{' ':>{self.length*4}}",
         f" {self.text:>{self.length*2}} {'':>{self.length}} "
        ],
#.?
        "?": [
         f"{'':>{self.length}}{self.text}{self.text}  ",
         f" {self.text[:-1]:>{self.length}}{self.text[:-1]:>{self.length*2}} ",
         f"{self.text[0]:>{self.length}}{self.text[:-1]:>{self.length*2}}  ",
         f"  {self.text:>{self.length*2}}{'':>{self.length}}",
         f"{self.text[:-1]:>{self.length*2}} {'':>{self.length}} ",
         f" {' ':>{self.length*3}}",
         f"{self.text[:-1]:>{self.length*2}} {'':>{self.length}} "
        ],
#.#
        "#": [
         f" {self.text}{self.text:>{self.length*2}} ",
         f" {self.text}{self.text:>{self.length*2}} ",
         f"{self.text[:-1]} {self.text[:-1]} {self.text[:-1]} {self.text[:-1]}",
         f" {self.text}{self.text:>{self.length*2}} ",
         f"{self.text[:-1]} {self.text[:-1]} {self.text[:-1]} {self.text[:-1]}",
         f" {self.text}{self.text:>{self.length*2}} ",
         f" {self.text}{self.text:>{self.length*2}} ",
        ],
#.$
        "$": [
         f"{'':>{self.length}} {self.text[:-1]} {'':>{self.length}} ",
         f" {self.text[0]} {self.text}{self.text}  ",
         f"{self.text[:-1]}  {self.text[:-1]} {'':>{self.length}} ",
         f" {self.text}{self.text}{self.text} ",
         f" {'':>{self.length}}{self.text[:-1]}  {self.text[:-1]} ",
         f" {self.text}{self.text} {self.text[0]}  ",
         f"{'':>{self.length}} {self.text[:-1]} {'':>{self.length}} ",
        ]
}

