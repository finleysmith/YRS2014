#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jamie
#
# Created:     08/07/2014
# Copyright:   (c) Jamie 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
data = raw_input("data goes here: ")
leng = int(input("1 4 16 64: "))
s1 = 0
e1 = 1
c1 = 0
output = ""
l1 = len(data)
if leng == 1:
    while c1 < l1:
        if data[s1:e1] == "a":
            output = output + ">"
        if data[s1:e1] == "b":
            output = output + "D"
        if data[s1:e1] == "c":
            output = output + "F"
        if data[s1:e1] == "d":
            output = output + "`"
        if data[s1:e1] == "e":
            output = output + "c"
        if data[s1:e1] == "f":
            output = output + "%"
        if data[s1:e1] == "g":
            output = output + ")"
        if data[s1:e1] == "h":
            output = output + "9"
        if data[s1:e1] == "i":
            output = output + "P"
        if data[s1:e1] == "j":
            output = output + "]"
        if data[s1:e1] == "k":
            output = output + "U"
        if data[s1:e1] == "l":
            output = output + "u"
        if data[s1:e1] == "m":
            output = output + "t"
        if data[s1:e1] == "n":
            output = output + "O"
        if data[s1:e1] == "o":
            output = output + "+"
        if data[s1:e1] == "p":
            output = output + "h"
        if data[s1:e1] == "q":
            output = output + "f"
        if data[s1:e1] == "r":
            output = output + "L"
        if data[s1:e1] == "s":
            output = output + "Z"
        if data[s1:e1] == "t":
            output = output + "V"
        if data[s1:e1] == "u":
            output = output + "["
        if data[s1:e1] == "v":
            output = output + "W"
        if data[s1:e1] == "w":
            output = output + "_"
        if data[s1:e1] == "x":
            output = output + "8"
        if data[s1:e1] == "y":
            output = output + "~"
        if data[s1:e1] == "z":
            output = output + "/"
        if data[s1:e1] == "A":
            output = output + ","
        if data[s1:e1] == "B":
            output = output + "C"
        if data[s1:e1] == "C":
            output = output + "R"
        if data[s1:e1] == "D":
            output = output + "H"
        if data[s1:e1] == "E":
            output = output + "2"
        if data[s1:e1] == "F":
            output = output + "k"
        if data[s1:e1] == "G":
            output = output + "b"
        if data[s1:e1] == "H":
            output = output + "!"
        if data[s1:e1] == "I":
            output = output + "I"
        if data[s1:e1] == "J":
            output = output + "3"
        if data[s1:e1] == "K":
            output = output + "m"
        if data[s1:e1] == "L":
            output = output + "#"
        if data[s1:e1] == "M":
            output = output + "N"
        if data[s1:e1] == "N":
            output = output + "X"
        if data[s1:e1] == "O":
            output = output + "r"
        if data[s1:e1] == "P":
            output = output + "0"
        if data[s1:e1] == "Q":
            output = output + "1"
        if data[s1:e1] == "R":
            output = output + "{"
        if data[s1:e1] == "S":
            output = output + "i"
        if data[s1:e1] == "T":
            output = output + "G"
        if data[s1:e1] == "U":
            output = output + "&"
        if data[s1:e1] == "V":
            output = output + "K"
        if data[s1:e1] == "W":
            output = output + "g"
        if data[s1:e1] == "X":
            output = output + "6"
        if data[s1:e1] == "Y":
            output = output + "4"
        if data[s1:e1] == "Z":
            output = output + "<"
        if data[s1:e1] == "1":
            output = output + "T"
        if data[s1:e1] == "2":
            output = output + "5"
        if data[s1:e1] == "3":
            output = output + "s"
        if data[s1:e1] == "4":
            output = output + "v"
        if data[s1:e1] == "5":
            output = output + "="
        if data[s1:e1] == "6":
            output = output + "?"
        if data[s1:e1] == "7":
            output = output + "@"
        if data[s1:e1] == "8":
            output = output + "x"
        if data[s1:e1] == "9":
            output = output + "y"
        if data[s1:e1] == "0":
            output = output + "^"
        if data[s1:e1] == "`":
            output = output + "S"
        if data[s1:e1] == "!":
            output = output + "Y"
        if data[s1:e1] == "'":
            output = output + "'"
        if data[s1:e1] == "$":
            output = output + "("
        if data[s1:e1] == "%":
            output = output + "d"
        if data[s1:e1] == "^":
            output = output + "7"
        if data[s1:e1] == "&":
            output = output + "B"
        if data[s1:e1] == "*":
            output = output + "'"
        if data[s1:e1] == "(":
            output = output + "n"
        if data[s1:e1] == ")":
            output = output + " "
        if data[s1:e1] == "_":
            output = output + "w"
        if data[s1:e1] == "+":
            output = output + "A"
        if data[s1:e1] == "-":
            output = output + "J"
        if data[s1:e1] == "=":
            output = output + "j"
        if data[s1:e1] == "{":
            output = output + ":"
        if data[s1:e1] == "[":
            output = output + "z"
        if data[s1:e1] == "]":
            output = output + "Q"
        if data[s1:e1] == "}":
            output = output + "$"
        if data[s1:e1] == ":":
            output = output + "."
        if data[s1:e1] == "'":
            output = output + "q"
        if data[s1:e1] == "@":
            output = output + "l"
        if data[s1:e1] == "#":
            output = output + "p"
        if data[s1:e1] == "~":
            output = output + "M"
        if data[s1:e1] == "/":
            output = output + "e"
        if data[s1:e1] == "?":
            output = output + "-"
        if data[s1:e1] == ".":
            output = output + "}"
        if data[s1:e1] == ">":
            output = output + "E"
        if data[s1:e1] == ",":
            output = output + "a"
        if data[s1:e1] == "<":
            output = output + "*"
        if data[s1:e1] == " ":
            output = output + "o"
        s1 = s1 + 1
        e1 = e1 + 1
        c1 = c1 + 1
        if data[s1:e1] == "a":
            output = output + "1"
        if data[s1:e1] == "b":
            output = output + "2"
        if data[s1:e1] == "c":
            output = output + "h"
        if data[s1:e1] == "d":
            output = output + "P"
        if data[s1:e1] == "e":
            output = output + "<"
        if data[s1:e1] == "f":
            output = output + "]"
        if data[s1:e1] == "g":
            output = output + "T"
        if data[s1:e1] == "h":
            output = output + "J"
        if data[s1:e1] == "i":
            output = output + "c"
        if data[s1:e1] == "j":
            output = output + "^"
        if data[s1:e1] == "k":
            output = output + ","
        if data[s1:e1] == "l":
            output = output + " "
        if data[s1:e1] == "m":
            output = output + "v"
        if data[s1:e1] == "n":
            output = output + "("
        if data[s1:e1] == "o":
            output = output + "j"
        if data[s1:e1] == "p":
            output = output + "`"
        if data[s1:e1] == "q":
            output = output + "+"
        if data[s1:e1] == "r":
            output = output + "9"
        if data[s1:e1] == "s":
            output = output + "/"
        if data[s1:e1] == "t":
            output = output + ">"
        if data[s1:e1] == "u":
            output = output + "f"
        if data[s1:e1] == "v":
            output = output + "e"
        if data[s1:e1] == "w":
            output = output + "["
        if data[s1:e1] == "x":
            output = output + "'"
        if data[s1:e1] == "y":
            output = output + "n"
        if data[s1:e1] == "z":
            output = output + "X"
        if data[s1:e1] == "A":
            output = output + "u"
        if data[s1:e1] == "B":
            output = output + "4"
        if data[s1:e1] == "C":
            output = output + "m"
        if data[s1:e1] == "D":
            output = output + "6"
        if data[s1:e1] == "E":
            output = output + "G"
        if data[s1:e1] == "F":
            output = output + "b"
        if data[s1:e1] == "G":
            output = output + "3"
        if data[s1:e1] == "H":
            output = output + "%"
        if data[s1:e1] == "I":
            output = output + "S"
        if data[s1:e1] == "J":
            output = output + "."
        if data[s1:e1] == "K":
            output = output + "p"
        if data[s1:e1] == "L":
            output = output + "@"
        if data[s1:e1] == "M":
            output = output + "$"
        if data[s1:e1] == "N":
            output = output + "l"
        if data[s1:e1] == "O":
            output = output + "?"
        if data[s1:e1] == "P":
            output = output + "Q"
        if data[s1:e1] == "Q":
            output = output + "W"
        if data[s1:e1] == "R":
            output = output + "H"
        if data[s1:e1] == "S":
            output = output + "{"
        if data[s1:e1] == "T":
            output = output + "K"
        if data[s1:e1] == "U":
            output = output + "L"
        if data[s1:e1] == "V":
            output = output + "w"
        if data[s1:e1] == "W":
            output = output + "&"
        if data[s1:e1] == "X":
            output = output + ":"
        if data[s1:e1] == "Y":
            output = output + "~"
        if data[s1:e1] == "Z":
            output = output + "k"
        if data[s1:e1] == "1":
            output = output + "I"
        if data[s1:e1] == "2":
            output = output + "M"
        if data[s1:e1] == "3":
            output = output + "_"
        if data[s1:e1] == "4":
            output = output + "q"
        if data[s1:e1] == "5":
            output = output + "a"
        if data[s1:e1] == "6":
            output = output + "g"
        if data[s1:e1] == "7":
            output = output + "D"
        if data[s1:e1] == "8":
            output = output + "E"
        if data[s1:e1] == "9":
            output = output + "U"
        if data[s1:e1] == "0":
            output = output + "*"
        if data[s1:e1] == "`":
            output = output + "r"
        if data[s1:e1] == "!":
            output = output + "0"
        if data[s1:e1] == "'":
            output = output + "'"
        if data[s1:e1] == "$":
            output = output + "="
        if data[s1:e1] == "%":
            output = output + ")"
        if data[s1:e1] == "^":
            output = output + "N"
        if data[s1:e1] == "&":
            output = output + "8"
        if data[s1:e1] == "*":
            output = output + "Y"
        if data[s1:e1] == "(":
            output = output + "F"
        if data[s1:e1] == ")":
            output = output + "t"
        if data[s1:e1] == "_":
            output = output + "B"
        if data[s1:e1] == "+":
            output = output + "o"
        if data[s1:e1] == "-":
            output = output + "d"
        if data[s1:e1] == "=":
            output = output + "C"
        if data[s1:e1] == "{":
            output = output + "-"
        if data[s1:e1] == "[":
            output = output + "x"
        if data[s1:e1] == "]":
            output = output + "R"
        if data[s1:e1] == "}":
            output = output + "i"
        if data[s1:e1] == ":":
            output = output + "7"
        if data[s1:e1] == "'":
            output = output + "V"
        if data[s1:e1] == "@":
            output = output + "s"
        if data[s1:e1] == "#":
            output = output + "#"
        if data[s1:e1] == "~":
            output = output + "z"
        if data[s1:e1] == "/":
            output = output + "!"
        if data[s1:e1] == "?":
            output = output + "y"
        if data[s1:e1] == ".":
            output = output + "A"
        if data[s1:e1] == ">":
            output = output + "}"
        if data[s1:e1] == ",":
            output = output + "5"
        if data[s1:e1] == "<":
            output = output + "Z"
        if data[s1:e1] == " ":
            output = output + "O"
        s1 = s1 + 1
        e1 = e1 + 1
        c1 = c1 + 1
        if data[s1:e1] == "a":
            output = output + "0"
        if data[s1:e1] == "b":
            output = output + "D"
        if data[s1:e1] == "c":
            output = output + "+"
        if data[s1:e1] == "d":
            output = output + "*"
        if data[s1:e1] == "e":
            output = output + "9"
        if data[s1:e1] == "f":
            output = output + "l"
        if data[s1:e1] == "g":
            output = output + "i"
        if data[s1:e1] == "h":
            output = output + "y"
        if data[s1:e1] == "i":
            output = output + "Q"
        if data[s1:e1] == "j":
            output = output + "U"
        if data[s1:e1] == "k":
            output = output + "["
        if data[s1:e1] == "l":
            output = output + "t"
        if data[s1:e1] == "m":
            output = output + "Z"
        if data[s1:e1] == "n":
            output = output + "$"
        if data[s1:e1] == "o":
            output = output + "!"
        if data[s1:e1] == "p":
            output = output + "<"
        if data[s1:e1] == "q":
            output = output + "'"
        if data[s1:e1] == "r":
            output = output + "]"
        if data[s1:e1] == "s":
            output = output + "1"
        if data[s1:e1] == "t":
            output = output + "O"
        if data[s1:e1] == "u":
            output = output + "u"
        if data[s1:e1] == "v":
            output = output + " "
        if data[s1:e1] == "w":
            output = output + "2"
        if data[s1:e1] == "x":
            output = output + "^"
        if data[s1:e1] == "y":
            output = output + "c"
        if data[s1:e1] == "z":
            output = output + "g"
        if data[s1:e1] == "A":
            output = output + "x"
        if data[s1:e1] == "B":
            output = output + "k"
        if data[s1:e1] == "C":
            output = output + "d"
        if data[s1:e1] == "D":
            output = output + ")"
        if data[s1:e1] == "E":
            output = output + "}"
        if data[s1:e1] == "F":
            output = output + "C"
        if data[s1:e1] == "G":
            output = output + ">"
        if data[s1:e1] == "H":
            output = output + "J"
        if data[s1:e1] == "I":
            output = output + "F"
        if data[s1:e1] == "J":
            output = output + "&"
        if data[s1:e1] == "K":
            output = output + "L"
        if data[s1:e1] == "L":
            output = output + "j"
        if data[s1:e1] == "M":
            output = output + "%"
        if data[s1:e1] == "N":
            output = output + "T"
        if data[s1:e1] == "O":
            output = output + "?"
        if data[s1:e1] == "P":
            output = output + "p"
        if data[s1:e1] == "Q":
            output = output + "K"
        if data[s1:e1] == "R":
            output = output + "{"
        if data[s1:e1] == "S":
            output = output + "'"
        if data[s1:e1] == "T":
            output = output + "("
        if data[s1:e1] == "U":
            output = output + "#"
        if data[s1:e1] == "V":
            output = output + "o"
        if data[s1:e1] == "W":
            output = output + "-"
        if data[s1:e1] == "X":
            output = output + "N"
        if data[s1:e1] == "Y":
            output = output + "P"
        if data[s1:e1] == "Z":
            output = output + "W"
        if data[s1:e1] == "1":
            output = output + "s"
        if data[s1:e1] == "2":
            output = output + "/"
        if data[s1:e1] == "3":
            output = output + "."
        if data[s1:e1] == "4":
            output = output + "z"
        if data[s1:e1] == "5":
            output = output + "3"
        if data[s1:e1] == "6":
            output = output + "8"
        if data[s1:e1] == "7":
            output = output + ":"
        if data[s1:e1] == "8":
            output = output + "B"
        if data[s1:e1] == "9":
            output = output + "R"
        if data[s1:e1] == "0":
            output = output + "X"
        if data[s1:e1] == "`":
            output = output + "_"
        if data[s1:e1] == "!":
            output = output + "4"
        if data[s1:e1] == "'":
            output = output + "f"
        if data[s1:e1] == "$":
            output = output + "e"
        if data[s1:e1] == "%":
            output = output + "r"
        if data[s1:e1] == "^":
            output = output + "n"
        if data[s1:e1] == "&":
            output = output + "h"
        if data[s1:e1] == "*":
            output = output + "m"
        if data[s1:e1] == "(":
            output = output + "7"
        if data[s1:e1] == ")":
            output = output + "E"
        if data[s1:e1] == "_":
            output = output + "5"
        if data[s1:e1] == "+":
            output = output + "H"
        if data[s1:e1] == "-":
            output = output + "V"
        if data[s1:e1] == "=":
            output = output + "b"
        if data[s1:e1] == "{":
            output = output + "M"
        if data[s1:e1] == "[":
            output = output + "w"
        if data[s1:e1] == "]":
            output = output + "v"
        if data[s1:e1] == "}":
            output = output + "A"
        if data[s1:e1] == ":":
            output = output + "@"
        if data[s1:e1] == "'":
            output = output + "a"
        if data[s1:e1] == "@":
            output = output + "Y"
        if data[s1:e1] == "#":
            output = output + "6"
        if data[s1:e1] == "~":
            output = output + "="
        if data[s1:e1] == "/":
            output = output + "~"
        if data[s1:e1] == "?":
            output = output + "`"
        if data[s1:e1] == ".":
            output = output + "G"
        if data[s1:e1] == ">":
            output = output + "I"
        if data[s1:e1] == ",":
            output = output + "S"
        if data[s1:e1] == "<":
            output = output + "q"
        if data[s1:e1] == " ":
            output = output + ","
        s1 = s1 + 1
        e1 = e1 + 1
        c1 = c1 + 1
        if data[s1:e1] == "a":
            output = output + "$"
        if data[s1:e1] == "b":
            output = output + "~"
        if data[s1:e1] == "c":
            output = output + ">"
        if data[s1:e1] == "d":
            output = output + "L"
        if data[s1:e1] == "e":
            output = output + "X"
        if data[s1:e1] == "f":
            output = output + "2"
        if data[s1:e1] == "g":
            output = output + "}"
        if data[s1:e1] == "h":
            output = output + "'"
        if data[s1:e1] == "i":
            output = output + "m"
        if data[s1:e1] == "j":
            output = output + "8"
        if data[s1:e1] == "k":
            output = output + "r"
        if data[s1:e1] == "l":
            output = output + "i"
        if data[s1:e1] == "m":
            output = output + "`"
        if data[s1:e1] == "n":
            output = output + "G"
        if data[s1:e1] == "o":
            output = output + "e"
        if data[s1:e1] == "p":
            output = output + "o"
        if data[s1:e1] == "q":
            output = output + "@"
        if data[s1:e1] == "r":
            output = output + "S"
        if data[s1:e1] == "s":
            output = output + "Z"
        if data[s1:e1] == "t":
            output = output + "?"
        if data[s1:e1] == "u":
            output = output + "g"
        if data[s1:e1] == "v":
            output = output + "Y"
        if data[s1:e1] == "w":
            output = output + "t"
        if data[s1:e1] == "x":
            output = output + "y"
        if data[s1:e1] == "y":
            output = output + "q"
        if data[s1:e1] == "z":
            output = output + "h"
        if data[s1:e1] == "A":
            output = output + "v"
        if data[s1:e1] == "B":
            output = output + "'"
        if data[s1:e1] == "C":
            output = output + "H"
        if data[s1:e1] == "D":
            output = output + "*"
        if data[s1:e1] == "E":
            output = output + "4"
        if data[s1:e1] == "F":
            output = output + "u"
        if data[s1:e1] == "G":
            output = output + "1"
        if data[s1:e1] == "H":
            output = output + "J"
        if data[s1:e1] == "I":
            output = output + "p"
        if data[s1:e1] == "J":
            output = output + "^"
        if data[s1:e1] == "K":
            output = output + "_"
        if data[s1:e1] == "L":
            output = output + "I"
        if data[s1:e1] == "M":
            output = output + "{"
        if data[s1:e1] == "N":
            output = output + "="
        if data[s1:e1] == "O":
            output = output + ","
        if data[s1:e1] == "P":
            output = output + "N"
        if data[s1:e1] == "Q":
            output = output + "E"
        if data[s1:e1] == "R":
            output = output + "B"
        if data[s1:e1] == "S":
            output = output + "0"
        if data[s1:e1] == "T":
            output = output + "k"
        if data[s1:e1] == "U":
            output = output + "/"
        if data[s1:e1] == "V":
            output = output + " "
        if data[s1:e1] == "W":
            output = output + "c"
        if data[s1:e1] == "X":
            output = output + "+"
        if data[s1:e1] == "Y":
            output = output + "C"
        if data[s1:e1] == "Z":
            output = output + ":"
        if data[s1:e1] == "1":
            output = output + "V"
        if data[s1:e1] == "2":
            output = output + "n"
        if data[s1:e1] == "3":
            output = output + "]"
        if data[s1:e1] == "4":
            output = output + "z"
        if data[s1:e1] == "5":
            output = output + "b"
        if data[s1:e1] == "6":
            output = output + "%"
        if data[s1:e1] == "7":
            output = output + "-"
        if data[s1:e1] == "8":
            output = output + "a"
        if data[s1:e1] == "9":
            output = output + "l"
        if data[s1:e1] == "0":
            output = output + "s"
        if data[s1:e1] == "`":
            output = output + "6"
        if data[s1:e1] == "!":
            output = output + "R"
        if data[s1:e1] == "'":
            output = output + "5"
        if data[s1:e1] == "$":
            output = output + "O"
        if data[s1:e1] == "%":
            output = output + "K"
        if data[s1:e1] == "^":
            output = output + "F"
        if data[s1:e1] == "&":
            output = output + "Q"
        if data[s1:e1] == "*":
            output = output + "D"
        if data[s1:e1] == "(":
            output = output + "A"
        if data[s1:e1] == ")":
            output = output + "x"
        if data[s1:e1] == "_":
            output = output + "d"
        if data[s1:e1] == "+":
            output = output + ")"
        if data[s1:e1] == "-":
            output = output + "<"
        if data[s1:e1] == "=":
            output = output + "."
        if data[s1:e1] == "{":
            output = output + "M"
        if data[s1:e1] == "[":
            output = output + "["
        if data[s1:e1] == "]":
            output = output + "P"
        if data[s1:e1] == "}":
            output = output + "7"
        if data[s1:e1] == ":":
            output = output + "U"
        if data[s1:e1] == "'":
            output = output + "9"
        if data[s1:e1] == "@":
            output = output + "j"
        if data[s1:e1] == "#":
            output = output + "&"
        if data[s1:e1] == "~":
            output = output + "T"
        if data[s1:e1] == "/":
            output = output + "3"
        if data[s1:e1] == "?":
            output = output + "W"
        if data[s1:e1] == ".":
            output = output + "f"
        if data[s1:e1] == ">":
            output = output + "#"
        if data[s1:e1] == ",":
            output = output + "w"
        if data[s1:e1] == "<":
            output = output + "("
        if data[s1:e1] == " ":
            output = output + "!"
        s1 = s1 + 1
        e1 = e1 + 1
        c1 = c1 + 1
elif leng == 4:
    while c1 < l1:
        if data[s1:e1] == "a":
            output = output + ",3+d"
        if data[s1:e1] == "b":
            output = output + "`z*^"
        if data[s1:e1] == "c":
            output = output + "CTe6"
        if data[s1:e1] == "d":
            output = output + "q9Xi"
        if data[s1:e1] == "e":
            output = output + "[kW9"
        if data[s1:e1] == "f":
            output = output + "5=F3"
        if data[s1:e1] == "g":
            output = output + "8:'o"
        if data[s1:e1] == "h":
            output = output + "uf$n"
        if data[s1:e1] == "i":
            output = output + "6I]6"
        if data[s1:e1] == "j":
            output = output + "Yyj*"
        if data[s1:e1] == "k":
            output = output + "-_?b"
        if data[s1:e1] == "l":
            output = output + "!SG8"
        if data[s1:e1] == "m":
            output = output + "!{h?"
        if data[s1:e1] == "n":
            output = output + "uEl6"
        if data[s1:e1] == "o":
            output = output + "Nl~O"
        if data[s1:e1] == "p":
            output = output + "aP@z"
        if data[s1:e1] == "q":
            output = output + "]3gg"
        if data[s1:e1] == "r":
            output = output + "aM%i"
        if data[s1:e1] == "s":
            output = output + "'%Wq"
        if data[s1:e1] == "t":
            output = output + "E7Ue"
        if data[s1:e1] == "u":
            output = output + "#w.P"
        if data[s1:e1] == "v":
            output = output + "WlLp"
        if data[s1:e1] == "w":
            output = output + "R8.-"
        if data[s1:e1] == "x":
            output = output + "/Ire"
        if data[s1:e1] == "y":
            output = output + "V@)J"
        if data[s1:e1] == "z":
            output = output + "J.~P"
        if data[s1:e1] == "A":
            output = output + "DByu"
        if data[s1:e1] == "B":
            output = output + "He]L"
        if data[s1:e1] == "C":
            output = output + "?$(/"
        if data[s1:e1] == "D":
            output = output + "1}`4"
        if data[s1:e1] == "E":
            output = output + "-Go{"
        if data[s1:e1] == "F":
            output = output + "dJ0<"
        if data[s1:e1] == "G":
            output = output + "'Q=o"
        if data[s1:e1] == "H":
            output = output + "S&0V"
        if data[s1:e1] == "I":
            output = output + "U]av"
        if data[s1:e1] == "J":
            output = output + "c Zw"
        if data[s1:e1] == "K":
            output = output + "s}^Y"
        if data[s1:e1] == "L":
            output = output + "hM=r"
        if data[s1:e1] == "M":
            output = output + "MVJ@"
        if data[s1:e1] == "N":
            output = output + "phBv"
        if data[s1:e1] == "O":
            output = output + "ANB%"
        if data[s1:e1] == "P":
            output = output + "YSDx"
        if data[s1:e1] == "Q":
            output = output + "}m:E"
        if data[s1:e1] == "R":
            output = output + "Uv#8"
        if data[s1:e1] == "S":
            output = output + "(*9x"
        if data[s1:e1] == "T":
            output = output + "yTis"
        if data[s1:e1] == "U":
            output = output + "q?,5"
        if data[s1:e1] == "V":
            output = output + "bczv"
        if data[s1:e1] == "W":
            output = output + "F>X2"
        if data[s1:e1] == "X":
            output = output + "M4sC"
        if data[s1:e1] == "Y":
            output = output + "!Fot"
        if data[s1:e1] == "Z":
            output = output + " DW3"
        if data[s1:e1] == "1":
            output = output + "<H^m"
        if data[s1:e1] == "2":
            output = output + "~'nO"
        if data[s1:e1] == "3":
            output = output + "4YxP"
        if data[s1:e1] == "4":
            output = output + "lGRU"
        if data[s1:e1] == "5":
            output = output + ">)FO"
        if data[s1:e1] == "6":
            output = output + "27/5"
        if data[s1:e1] == "7":
            output = output + "NE:("
        if data[s1:e1] == "8":
            output = output + "5>Hr"
        if data[s1:e1] == "9":
            output = output + "mZH%"
        if data[s1:e1] == "0":
            output = output + "r&XT"
        if data[s1:e1] == "`":
            output = output + "zwLi"
        if data[s1:e1] == "!":
            output = output + "._R2"
        if data[s1:e1] == "'":
            output = output + "NjBC"
        if data[s1:e1] == "$":
            output = output + "Qm[V"
        if data[s1:e1] == "%":
            output = output + "Kcn7"
        if data[s1:e1] == "^":
            output = output + ">{b "
        if data[s1:e1] == "&":
            output = output + ")$47"
        if data[s1:e1] == "*":
            output = output + "DK)R"
        if data[s1:e1] == "(":
            output = output + "1(@<"
        if data[s1:e1] == ")":
            output = output + "[kAZ"
        if data[s1:e1] == "_":
            output = output + "0~jS"
        if data[s1:e1] == "+":
            output = output + "Gs-p"
        if data[s1:e1] == "-":
            output = output + "ud`Q"
        if data[s1:e1] == "=":
            output = output + "$#}c"
        if data[s1:e1] == "{":
            output = output + "K^!g"
        if data[s1:e1] == "[":
            output = output + "#xnk"
        if data[s1:e1] == "]":
            output = output + "hI'K"
        if data[s1:e1] == "}":
            output = output + "O_X9"
        if data[s1:e1] == ":":
            output = output + "fb=2"
        if data[s1:e1] == "'":
            output = output + "&{1f"
        if data[s1:e1] == "@":
            output = output + "ZtLj"
        if data[s1:e1] == "#":
            output = output + "'C&*"
        if data[s1:e1] == "~":
            output = output + "a[:T"
        if data[s1:e1] == "/":
            output = output + "+`/,"
        if data[s1:e1] == "?":
            output = output + ",Qp'"
        if data[s1:e1] == ".":
            output = output + "I1 +"
        if data[s1:e1] == ">":
            output = output + "+0<A"
        if data[s1:e1] == ",":
            output = output + "w'f_"
        if data[s1:e1] == "<":
            output = output + "dqty"
        if data[s1:e1] == " ":
            output = output + "gtkA"
        s1 = s1 + 1
        e1 = e1 + 1
        c1 = c1 + 1
        if data[s1:e1] == "a":
            output = output + "nR/d"
        if data[s1:e1] == "b":
            output = output + "yD{V"
        if data[s1:e1] == "c":
            output = output + "G+1+"
        if data[s1:e1] == "d":
            output = output + "3e:R"
        if data[s1:e1] == "e":
            output = output + "0}))"
        if data[s1:e1] == "f":
            output = output + "HqrU"
        if data[s1:e1] == "g":
            output = output + ">F98"
        if data[s1:e1] == "h":
            output = output + "Dxt~"
        if data[s1:e1] == "i":
            output = output + "3#7L"
        if data[s1:e1] == "j":
            output = output + ",&mv"
        if data[s1:e1] == "k":
            output = output + "56B3"
        if data[s1:e1] == "l":
            output = output + "gQ)p"
        if data[s1:e1] == "m":
            output = output + "Ek[w"
        if data[s1:e1] == "n":
            output = output + ":bHR"
        if data[s1:e1] == "o":
            output = output + "'E'="
        if data[s1:e1] == "p":
            output = output + "{yTG"
        if data[s1:e1] == "q":
            output = output + "X]DS"
        if data[s1:e1] == "r":
            output = output + "s!aa"
        if data[s1:e1] == "s":
            output = output + "r]`2"
        if data[s1:e1] == "t":
            output = output + "uIPh"
        if data[s1:e1] == "u":
            output = output + "9Kug"
        if data[s1:e1] == "v":
            output = output + "<Z4D"
        if data[s1:e1] == "w":
            output = output + "u2OP"
        if data[s1:e1] == "x":
            output = output + "8x O"
        if data[s1:e1] == "y":
            output = output + ", *p"
        if data[s1:e1] == "z":
            output = output + "X}6$"
        if data[s1:e1] == "A":
            output = output + "Qgb."
        if data[s1:e1] == "B":
            output = output + "70<]"
        if data[s1:e1] == "C":
            output = output + "'kpl"
        if data[s1:e1] == "D":
            output = output + "5yvW"
        if data[s1:e1] == "E":
            output = output + "Cizs"
        if data[s1:e1] == "F":
            output = output + "Fy,h"
        if data[s1:e1] == "G":
            output = output + "d7_~"
        if data[s1:e1] == "H":
            output = output + "/G~R"
        if data[s1:e1] == "I":
            output = output + "v'dz"
        if data[s1:e1] == "J":
            output = output + ":~^M"
        if data[s1:e1] == "K":
            output = output + "f:Ek"
        if data[s1:e1] == "L":
            output = output + "L^xG"
        if data[s1:e1] == "M":
            output = output + "=.m9"
        if data[s1:e1] == "N":
            output = output + "Y{C-"
        if data[s1:e1] == "O":
            output = output + "th$?"
        if data[s1:e1] == "P":
            output = output + "(tf$"
        if data[s1:e1] == "Q":
            output = output + "&Z0$"
        if data[s1:e1] == "R":
            output = output + "(N24"
        if data[s1:e1] == "S":
            output = output + "Kcf-"
        if data[s1:e1] == "T":
            output = output + "IPKx"
        if data[s1:e1] == "U":
            output = output + "Na_b"
        if data[s1:e1] == "V":
            output = output + "8wu("
        if data[s1:e1] == "W":
            output = output + "JZYj"
        if data[s1:e1] == "X":
            output = output + "T'q4"
        if data[s1:e1] == "Y":
            output = output + "dkH#"
        if data[s1:e1] == "Z":
            output = output + "%c1["
        if data[s1:e1] == "1":
            output = output + ".MV,"
        if data[s1:e1] == "2":
            output = output + "U>m>"
        if data[s1:e1] == "3":
            output = output + "jelg"
        if data[s1:e1] == "4":
            output = output + "*CnT"
        if data[s1:e1] == "5":
            output = output + "W1c{"
        if data[s1:e1] == "6":
            output = output + "@?ic"
        if data[s1:e1] == "7":
            output = output + "4I8H"
        if data[s1:e1] == "8":
            output = output + "oaVE"
        if data[s1:e1] == "9":
            output = output + "e-=<"
        if data[s1:e1] == "0":
            output = output + "(I^b"
        if data[s1:e1] == "`":
            output = output + "w#. "
        if data[s1:e1] == "!":
            output = output + "Kf3_"
        if data[s1:e1] == "'":
            output = output + "+Jz="
        if data[s1:e1] == "$":
            output = output + "-'[l"
        if data[s1:e1] == "%":
            output = output + "AhwP"
        if data[s1:e1] == "^":
            output = output + "Qz7J"
        if data[s1:e1] == "&":
            output = output + "j!ML"
        if data[s1:e1] == "*":
            output = output + "`*%o"
        if data[s1:e1] == "(":
            output = output + "2/ '"
        if data[s1:e1] == ")":
            output = output + "?eNO"
        if data[s1:e1] == "_":
            output = output + "<}p*"
        if data[s1:e1] == "+":
            output = output + "SJ+B"
        if data[s1:e1] == "-":
            output = output + "SA`q"
        if data[s1:e1] == "=":
            output = output + "?StX"
        if data[s1:e1] == "{":
            output = output + "r6T`"
        if data[s1:e1] == "[":
            output = output + "&LF%"
        if data[s1:e1] == "]":
            output = output + "s#YU"
        if data[s1:e1] == "}":
            output = output + "]Zso"
        if data[s1:e1] == ":":
            output = output + "Q_}j"
        if data[s1:e1] == "'":
            output = output + "WUX!"
        if data[s1:e1] == "@":
            output = output + "9NA5"
        if data[s1:e1] == "#":
            output = output + "qo!n"
        if data[s1:e1] == "~":
            output = output + "nlVi"
        if data[s1:e1] == "/":
            output = output + "B[mW"
        if data[s1:e1] == "?":
            output = output + ">O'@"
        if data[s1:e1] == ".":
            output = output + "F@Y@"
        if data[s1:e1] == ">":
            output = output + "AM^i"
        if data[s1:e1] == ",":
            output = output + "%0Cv"
        if data[s1:e1] == "<":
            output = output + "/rB)"
        if data[s1:e1] == " ":
            output = output + "&561"
        s1 = s1 + 1
        e1 = e1 + 1
        c1 = c1 + 1
        if data[s1:e1] == "a":
            output = output + "qyQb"
        if data[s1:e1] == "b":
            output = output + "i/SV"
        if data[s1:e1] == "c":
            output = output + "gHY1"
        if data[s1:e1] == "d":
            output = output + "/++^"
        if data[s1:e1] == "e":
            output = output + "x,n6"
        if data[s1:e1] == "f":
            output = output + "!=Sk"
        if data[s1:e1] == "g":
            output = output + "F'$e"
        if data[s1:e1] == "h":
            output = output + ",_t "
        if data[s1:e1] == "i":
            output = output + "HTX'"
        if data[s1:e1] == "j":
            output = output + "MW#o"
        if data[s1:e1] == "k":
            output = output + "+Mk5"
        if data[s1:e1] == "l":
            output = output + "c^X("
        if data[s1:e1] == "m":
            output = output + "~u_a"
        if data[s1:e1] == "n":
            output = output + "zmqW"
        if data[s1:e1] == "o":
            output = output + "c3By"
        if data[s1:e1] == "p":
            output = output + "a'mP"
        if data[s1:e1] == "q":
            output = output + "[JtK"
        if data[s1:e1] == "r":
            output = output + "<j~s"
        if data[s1:e1] == "s":
            output = output + "ZF-%"
        if data[s1:e1] == "t":
            output = output + "GCaj"
        if data[s1:e1] == "u":
            output = output + "ms/8"
        if data[s1:e1] == "v":
            output = output + "4NP{"
        if data[s1:e1] == "w":
            output = output + "=PZx"
        if data[s1:e1] == "x":
            output = output + "O]%y"
        if data[s1:e1] == "y":
            output = output + "_W!E"
        if data[s1:e1] == "z":
            output = output + "zo>O"
        if data[s1:e1] == "A":
            output = output + "&hT#"
        if data[s1:e1] == "B":
            output = output + "Fb'9"
        if data[s1:e1] == "C":
            output = output + "KGl/"
        if data[s1:e1] == "D":
            output = output + "9MkI"
        if data[s1:e1] == "E":
            output = output + "$lp}"
        if data[s1:e1] == "F":
            output = output + "2Ae?"
        if data[s1:e1] == "G":
            output = output + "M{?l"
        if data[s1:e1] == "H":
            output = output + "w8.7"
        if data[s1:e1] == "I":
            output = output + "))X9"
        if data[s1:e1] == "J":
            output = output + "+Kft"
        if data[s1:e1] == "K":
            output = output + "C`O*"
        if data[s1:e1] == "L":
            output = output + "h'v0"
        if data[s1:e1] == "M":
            output = output + "`26h"
        if data[s1:e1] == "N":
            output = output + "'YQz"
        if data[s1:e1] == "O":
            output = output + "tS7B"
        if data[s1:e1] == "P":
            output = output + "UJCN"
        if data[s1:e1] == "Q":
            output = output + "6ugD"
        if data[s1:e1] == "R":
            output = output + "&(DT"
        if data[s1:e1] == "S":
            output = output + "pw5-"
        if data[s1:e1] == "T":
            output = output + "G}d4"
        if data[s1:e1] == "U":
            output = output + "LDN*"
        if data[s1:e1] == "V":
            output = output + "ieRV"
        if data[s1:e1] == "W":
            output = output + "Br[*"
        if data[s1:e1] == "X":
            output = output + "}`)K"
        if data[s1:e1] == "Y":
            output = output + "xI@s"
        if data[s1:e1] == "Z":
            output = output + "fZnP"
        if data[s1:e1] == "1":
            output = output + "kWeU"
        if data[s1:e1] == "2":
            output = output + "mA7Y"
        if data[s1:e1] == "3":
            output = output + ":[_8"
        if data[s1:e1] == "4":
            output = output + "UA17"
        if data[s1:e1] == "5":
            output = output + "&Fb2"
        if data[s1:e1] == "6":
            output = output + "6nxT"
        if data[s1:e1] == "7":
            output = output + "l.]R"
        if data[s1:e1] == "8":
            output = output + " ,-u"
        if data[s1:e1] == "9":
            output = output + " *i<"
        if data[s1:e1] == "0":
            output = output + "L!#w"
        if data[s1:e1] == "`":
            output = output + "L-Vr"
        if data[s1:e1] == "!":
            output = output + "pIwH"
        if data[s1:e1] == "'":
            output = output + ":BGd"
        if data[s1:e1] == "$":
            output = output + "4%oq"
        if data[s1:e1] == "%":
            output = output + "{hQQ"
        if data[s1:e1] == "^":
            output = output + "1a3@"
        if data[s1:e1] == "&":
            output = output + "OZzr"
        if data[s1:e1] == "*":
            output = output + "]>f{"
        if data[s1:e1] == "(":
            output = output + "v1#E"
        if data[s1:e1] == ")":
            output = output + "0(XJ"
        if data[s1:e1] == "_":
            output = output + "$u3="
        if data[s1:e1] == "+":
            output = output + "r}&A"
        if data[s1:e1] == "-":
            output = output + "NRf'"
        if data[s1:e1] == "=":
            output = output + ")`RS"
        if data[s1:e1] == "{":
            output = output + "o!'?"
        if data[s1:e1] == "[":
            output = output + "s3~^"
        if data[s1:e1] == "]":
            output = output + "J<i,"
        if data[s1:e1] == "}":
            output = output + "2%5."
        if data[s1:e1] == ":":
            output = output + "?b]<"
        if data[s1:e1] == "'":
            output = output + ":0^g"
        if data[s1:e1] == "@":
            output = output + "n.cj"
        if data[s1:e1] == "#":
            output = output + "9dc>"
        if data[s1:e1] == "~":
            output = output + "vvE~"
        if data[s1:e1] == "/":
            output = output + "0[qg"
        if data[s1:e1] == "?":
            output = output + "y=CL"
        if data[s1:e1] == ".":
            output = output + "HYV4"
        if data[s1:e1] == ">":
            output = output + "U$>D"
        if data[s1:e1] == ",":
            output = output + "5p8@"
        if data[s1:e1] == "<":
            output = output + "dI: "
        if data[s1:e1] == " ":
            output = output + "@E(j"
        s1 = s1 + 1
        e1 = e1 + 1
        c1 = c1 + 1
        if data[s1:e1] == "a":
            output = output + "-z00"
        if data[s1:e1] == "b":
            output = output + "^JL4"
        if data[s1:e1] == "c":
            output = output + "D5u3"
        if data[s1:e1] == "d":
            output = output + "wYu3"
        if data[s1:e1] == "e":
            output = output + "3f-~"
        if data[s1:e1] == "f":
            output = output + "ZZ8("
        if data[s1:e1] == "g":
            output = output + "?341"
        if data[s1:e1] == "h":
            output = output + "'m?/"
        if data[s1:e1] == "i":
            output = output + "t]#y"
        if data[s1:e1] == "j":
            output = output + "6M1q"
        if data[s1:e1] == "k":
            output = output + "DWu_"
        if data[s1:e1] == "l":
            output = output + "i}U'"
        if data[s1:e1] == "m":
            output = output + "z9CS"
        if data[s1:e1] == "n":
            output = output + "OPtG"
        if data[s1:e1] == "o":
            output = output + "gvIj"
        if data[s1:e1] == "p":
            output = output + "'c:^"
        if data[s1:e1] == "q":
            output = output + "x.}*"
        if data[s1:e1] == "r":
            output = output + "ewkc"
        if data[s1:e1] == "s":
            output = output + "y]>y"
        if data[s1:e1] == "t":
            output = output + ">xbl"
        if data[s1:e1] == "u":
            output = output + "AG,&"
        if data[s1:e1] == "v":
            output = output + "NY.'"
        if data[s1:e1] == "w":
            output = output + "A}Fa"
        if data[s1:e1] == "x":
            output = output + "AQ9S"
        if data[s1:e1] == "y":
            output = output + "6oU2"
        if data[s1:e1] == "z":
            output = output + "TqBq"
        if data[s1:e1] == "A":
            output = output + "V!eN"
        if data[s1:e1] == "B":
            output = output + "=%C`"
        if data[s1:e1] == "C":
            output = output + "_fs#"
        if data[s1:e1] == "D":
            output = output + "r2U5"
        if data[s1:e1] == "E":
            output = output + "pmmx"
        if data[s1:e1] == "F":
            output = output + " srv"
        if data[s1:e1] == "G":
            output = output + "'ogJ"
        if data[s1:e1] == "H":
            output = output + "+K#$"
        if data[s1:e1] == "I":
            output = output + "el`!"
        if data[s1:e1] == "J":
            output = output + "I<&<"
        if data[s1:e1] == "K":
            output = output + "8efV"
        if data[s1:e1] == "L":
            output = output + "ubwK"
        if data[s1:e1] == "M":
            output = output + "7>@S"
        if data[s1:e1] == "N":
            output = output + "7(1'"
        if data[s1:e1] == "O":
            output = output + "Zp`T"
        if data[s1:e1] == "P":
            output = output + "*y$*"
        if data[s1:e1] == "Q":
            output = output + "7ER{"
        if data[s1:e1] == "R":
            output = output + "jDW%"
        if data[s1:e1] == "S":
            output = output + "zw~M"
        if data[s1:e1] == "T":
            output = output + "@]6~"
        if data[s1:e1] == "U":
            output = output + "vJ%A"
        if data[s1:e1] == "V":
            output = output + "k>W/"
        if data[s1:e1] == "W":
            output = output + "kVSX"
        if data[s1:e1] == "X":
            output = output + "BQ$*"
        if data[s1:e1] == "Y":
            output = output + "C:Xq"
        if data[s1:e1] == "Z":
            output = output + "a^$B"
        if data[s1:e1] == "1":
            output = output + "-P5H"
        if data[s1:e1] == "2":
            output = output + "hYP#"
        if data[s1:e1] == "3":
            output = output + "8T_F"
        if data[s1:e1] == "4":
            output = output + ":Y= "
        if data[s1:e1] == "5":
            output = output + "_f)<"
        if data[s1:e1] == "6":
            output = output + "p~]0"
        if data[s1:e1] == "7":
            output = output + "d%zl"
        if data[s1:e1] == "8":
            output = output + "M2,["
        if data[s1:e1] == "9":
            output = output + "}ZhH"
        if data[s1:e1] == "0":
            output = output + "EL4N"
        if data[s1:e1] == "`":
            output = output + "rt R"
        if data[s1:e1] == "!":
            output = output + "t FG"
        if data[s1:e1] == "'":
            output = output + "^[0/"
        if data[s1:e1] == "$":
            output = output + "hN2E"
        if data[s1:e1] == "%":
            output = output + "j)so"
        if data[s1:e1] == "^":
            output = output + "P)b/"
        if data[s1:e1] == "&":
            output = output + "JVWH"
        if data[s1:e1] == "*":
            output = output + "p5{G"
        if data[s1:e1] == "(":
            output = output + "Rid."
        if data[s1:e1] == ")":
            output = output + "vn+K"
        if data[s1:e1] == "_":
            output = output + "iIH!"
        if data[s1:e1] == "+":
            output = output + "XcOQ"
        if data[s1:e1] == "-":
            output = output + "K?o)"
        if data[s1:e1] == "=":
            output = output + "jgk7"
        if data[s1:e1] == "{":
            output = output + "@Ox("
        if data[s1:e1] == "[":
            output = output + ",d(B"
        if data[s1:e1] == "]":
            output = output + "8s<`"
        if data[s1:e1] == "}":
            output = output + "{c6F"
        if data[s1:e1] == ":":
            output = output + "b.+="
        if data[s1:e1] == "'":
            output = output + "l[{["
        if data[s1:e1] == "@":
            output = output + "?-a&"
        if data[s1:e1] == "#":
            output = output + "M:L9"
        if data[s1:e1] == "~":
            output = output + "C=Em"
        if data[s1:e1] == "/":
            output = output + "+Xn1"
        if data[s1:e1] == "?":
            output = output + "@Q'L"
        if data[s1:e1] == ".":
            output = output + "dUTi"
        if data[s1:e1] == ">":
            output = output + "h'nI"
        if data[s1:e1] == ",":
            output = output + "94R!"
        if data[s1:e1] == "<":
            output = output + "Dagn"
        if data[s1:e1] == " ":
            output = output + "&Or,"
        s1 = s1 + 1
        e1 = e1 + 1
        c1 = c1 + 1
elif leng == 16:
    while c1 < l1:
        if data[s1:e1] == "a":
            output = output + "TC{emM1>ALJH<`Lt"
        if data[s1:e1] == "b":
            output = output + "Z9 *m' jx1z~H-+t"
        if data[s1:e1] == "c":
            output = output + "%bQ:LTWwgDzLE=X&"
        if data[s1:e1] == "d":
            output = output + "'$(PFba`gg-ek~TJ"
        if data[s1:e1] == "e":
            output = output + "yQ!Te YWm$Gy2uv@"
        if data[s1:e1] == "f":
            output = output + "0<Y[5u&tuPuPCL)y"
        if data[s1:e1] == "g":
            output = output + "Ff1r0(:K72Db,PT1"
        if data[s1:e1] == "h":
            output = output + ">G6fGyodR~8ZY/+q"
        if data[s1:e1] == "i":
            output = output + "NH@yUg'MDZ5YC!w^"
        if data[s1:e1] == "j":
            output = output + "'+{a$$h,w77.H>3?"
        if data[s1:e1] == "k":
            output = output + "kNN's'=2-MixM_bi"
        if data[s1:e1] == "l":
            output = output + "bn,9C+Bu>6lwJ41S"
        if data[s1:e1] == "m":
            output = output + "v3,(V6~^<?re'aWj"
        if data[s1:e1] == "n":
            output = output + "(H<^pWf8iPUY+3OR"
        if data[s1:e1] == "o":
            output = output + "-*Yq#t#M )GE's{Q"
        if data[s1:e1] == "p":
            output = output + "sUx3Hb[la,,k$(Ig"
        if data[s1:e1] == "q":
            output = output + "D@1jdAnEeFf#ge2v"
        if data[s1:e1] == "r":
            output = output + "9z9{rm,rFvU,ZX]Q"
        if data[s1:e1] == "s":
            output = output + "{[(D+HDux*!Oos+c"
        if data[s1:e1] == "t":
            output = output + "d/yu.wLldMz]Pf{G"
        if data[s1:e1] == "u":
            output = output + "ozC%E5rx'r(K[sx4"
        if data[s1:e1] == "v":
            output = output + "]Ej=x^56iMTCcIOl"
        if data[s1:e1] == "w":
            output = output + "p%P3Nn#BiDLn}GA0"
        if data[s1:e1] == "x":
            output = output + "cQB?)lF1etk@-`]Z"
        if data[s1:e1] == "y":
            output = output + "oAxo>3[]F{=<t/+Y"
        if data[s1:e1] == "z":
            output = output + "o/hJt?iN#v3/pu@j"
        if data[s1:e1] == "A":
            output = output + "t?jWhGzwUzTX{n9h"
        if data[s1:e1] == "B":
            output = output + "I.$zQc#R6jE[Q4S}"
        if data[s1:e1] == "C":
            output = output + "'&1cB9pou.8fgJ&^"
        if data[s1:e1] == "D":
            output = output + "GIMq]z_'Q:XBd+/R"
        if data[s1:e1] == "E":
            output = output + "GvN7Iv]80}*ZoA.K"
        if data[s1:e1] == "F":
            output = output + "P-.!>{ q=/yI=2qU"
        if data[s1:e1] == "G":
            output = output + "JBKi5WJQkX(E&#1C"
        if data[s1:e1] == "H":
            output = output + "9.XW_}A+_G[mL7*w"
        if data[s1:e1] == "I":
            output = output + ":K%^R_R&1_!y&?69"
        if data[s1:e1] == "J":
            output = output + "]L8_~it!FEUYst#c"
        if data[s1:e1] == "K":
            output = output + "xero(Rowc#*][ude"
        if data[s1:e1] == "L":
            output = output + "n0*no=Vx~GqCD'fl"
        if data[s1:e1] == "M":
            output = output + "IEqw6lfApI4N:g>X"
        if data[s1:e1] == "N":
            output = output + "1[75~L4K%s@3R>gR"
        if data[s1:e1] == "O":
            output = output + "vIxPC,pkqU<8'fHK"
        if data[s1:e1] == "P":
            output = output + "YNx'1UO3)Dk)?z?R"
        if data[s1:e1] == "Q":
            output = output + "<2Vn=dEW-Karg,Q'"
        if data[s1:e1] == "R":
            output = output + "Oro_)&<MmUbh$d!h"
        if data[s1:e1] == "S":
            output = output + "mszc:2WHZ>eLWcWW"
        if data[s1:e1] == "T":
            output = output + "s`_wfAc/4nQauqut"
        if data[s1:e1] == "U":
            output = output + "9l@j3(Z+b$4~.uiO"
        if data[s1:e1] == "V":
            output = output + "H&9QC!d'~c/h!Y&a"
        if data[s1:e1] == "W":
            output = output + "L#^F0K{ xsCSe2yV"
        if data[s1:e1] == "X":
            output = output + "6<`IQ:Vj{%k+5605"
        if data[s1:e1] == "Y":
            output = output + "%p@Xm:2ez'xPT'2}"
        if data[s1:e1] == "Z":
            output = output + "T%4~F5R/S}hgW`yv"
        if data[s1:e1] == "1":
            output = output + "-)z7U>$K{o'kEts>"
        if data[s1:e1] == "2":
            output = output + "@uhx``Vg'6(jX*_f"
        if data[s1:e1] == "3":
            output = output + "m@Y<<_}*]1[*5%dn"
        if data[s1:e1] == "4":
            output = output + "(XyDRT%la+AX(pNO"
        if data[s1:e1] == "5":
            output = output + "aBm03%NS viqZ/r "
        if data[s1:e1] == "6":
            output = output + "]sc4N%K2 Y(Z'H9X"
        if data[s1:e1] == "7":
            output = output + "N^D#Kh w?:D(=b$7"
        if data[s1:e1] == "8":
            output = output + "6hFSPPhI }qvP3Q["
        if data[s1:e1] == "9":
            output = output + "Vfj<Jpyp5.!'%EBV"
        if data[s1:e1] == "0":
            output = output + "`R-@4J5TZj>DacLs"
        if data[s1:e1] == "`":
            output = output + "dN{8,4 ed=6]C:gJ"
        if data[s1:e1] == "!":
            output = output + "7=A9`[iHKQo}BjGh"
        if data[s1:e1] == "'":
            output = output + "Wykn&'R,{r!S7zn:"
        if data[s1:e1] == "$":
            output = output + "lX0$,i.?-7F^h FZ"
        if data[s1:e1] == "%":
            output = output + "fR{>)T?.l.w:&G78"
        if data[s1:e1] == "^":
            output = output + "p[6^naiIqH}rm$,&"
        if data[s1:e1] == "&":
            output = output + "JAOnF)lfW^/*M=U1"
        if data[s1:e1] == "*":
            output = output + "@GJ}8aS+8Ci`3f5x"
        if data[s1:e1] == "(":
            output = output + "`?#ZVN~TPUs+_'qS"
        if data[s1:e1] == ")":
            output = output + "SUYc)jV-!qE0Loz9"
        if data[s1:e1] == "_":
            output = output + "!/^O@p5eP}c5~b3B"
        if data[s1:e1] == "+":
            output = output + "rkZB.k1jw*SZUDJb"
        if data[s1:e1] == "-":
            output = output + "4_zlbc)K3:B7T%QF"
        if data[s1:e1] == "=":
            output = output + "9#J=%?Ft-)0GYv2p"
        if data[s1:e1] == "{":
            output = output + "/'8aUC_h''}Mda8M"
        if data[s1:e1] == "[":
            output = output + "M}K.gV8!klnS$2*:"
        if data[s1:e1] == "]":
            output = output + "Rm vT)5B>y:VZ0SJ"
        if data[s1:e1] == "}":
            output = output + "1y*~PH=+E_>Xd#Bu"
        if data[s1:e1] == ":":
            output = output + "_or-LY<Xp] s8)9B"
        if data[s1:e1] == "'":
            output = output + "kCA`kL?NNHOd?('O"
        if data[s1:e1] == "@":
            output = output + "F/mteOA}HgA^[OE~"
        if data[s1:e1] == "#":
            output = output + "lhX2a9k`Vm4f42>`"
        if data[s1:e1] == "~":
            output = output + "$bqltJSwvbSOwb$m"
        if data[s1:e1] == "/":
            output = output + "'4BC/<-=j^I'!?]["
        if data[s1:e1] == "?":
            output = output + ".6~bMV}*)7S.Ms~0"
        if data[s1:e1] == ".":
            output = output + "'AIi6VY3VDa4T&O&"
        if data[s1:e1] == ">":
            output = output + "r8&<Dmq@t0v^$)n,"
        if data[s1:e1] == ",":
            output = output + "7id!@ vK%]E^,w@2"
        if data[s1:e1] == "<":
            output = output + "`#:0eIrW--A{I]p7"
        if data[s1:e1] == " ":
            output = output + "pM*g80y#6u'OG<=["
        s1 = s1 + 1
        e1 = e1 + 1
        c1 = c1 + 1
        if data[s1:e1] == "a":
            output = output + "&mYzFJ<alZg76bJu"
        if data[s1:e1] == "b":
            output = output + "<KXB~}##SK=<J_JB"
        if data[s1:e1] == "c":
            output = output + "AlItG2aLnaM1zMw^"
        if data[s1:e1] == "d":
            output = output + "e!8(cYtEqEx(esHL"
        if data[s1:e1] == "e":
            output = output + "PYrVn@39SRFs?Q@v"
        if data[s1:e1] == "f":
            output = output + ")m_w%n*gT`FMF<5a"
        if data[s1:e1] == "g":
            output = output + ">o&Cky!4IQL&309c"
        if data[s1:e1] == "h":
            output = output + "KbMoy6gl^+PP<YwU"
        if data[s1:e1] == "i":
            output = output + "l66_-g4'''d'0Ar:"
        if data[s1:e1] == "j":
            output = output + "4B}Xu$-H.oO5Wj_c"
        if data[s1:e1] == "k":
            output = output + "+u~'$6dIW1m~1kjj"
        if data[s1:e1] == "l":
            output = output + ",bdw.Y0,>bC%~]xv"
        if data[s1:e1] == "m":
            output = output + "'Hj!,}1Bz/% nt`W"
        if data[s1:e1] == "n":
            output = output + "A$F[_)'n)]q.2Yr)"
        if data[s1:e1] == "o":
            output = output + "XFw0ay,0-F>V8Rk3"
        if data[s1:e1] == "p":
            output = output + "Nn{9V3m'`o%AK<5C"
        if data[s1:e1] == "q":
            output = output + "qeVc:N`@pWJW@GHM"
        if data[s1:e1] == "r":
            output = output + "g+oxaqUima<}S`-P"
        if data[s1:e1] == "s":
            output = output + "g+%!dCK4N[xRk^W2"
        if data[s1:e1] == "t":
            output = output + "((^Tp0upeqP/4N.v"
        if data[s1:e1] == "u":
            output = output + "uh,e`ME_=p&v_A!/"
        if data[s1:e1] == "v":
            output = output + "fZ:!)zD01_>=L}75"
        if data[s1:e1] == "w":
            output = output + "{K*Mjf_KeS3ii5Ry"
        if data[s1:e1] == "x":
            output = output + "Q#Kl8>m0E4P&cgQW"
        if data[s1:e1] == "y":
            output = output + "q'LB'f?t(U-D&nWK"
        if data[s1:e1] == "z":
            output = output + "Gqj'-mMYTY M!+/l"
        if data[s1:e1] == "A":
            output = output + "sI=zi.As%E_R $Y?"
        if data[s1:e1] == "B":
            output = output + "('[b!3!hSO~7rmLN"
        if data[s1:e1] == "C":
            output = output + "{R2T8'Z?)UG[O*F{"
        if data[s1:e1] == "D":
            output = output + "pXIzr&Wg?E6<)O2N"
        if data[s1:e1] == "E":
            output = output + "OLtPg#S0Jg6'v2]I"
        if data[s1:e1] == "F":
            output = output + "k.,V3 =]:Nb'3`#B"
        if data[s1:e1] == "G":
            output = output + "RGlC2,aInJl#_#RU"
        if data[s1:e1] == "H":
            output = output + "'w'gIMR^21s7hyaG"
        if data[s1:e1] == "I":
            output = output + ">hN{ `AXXD]7kXSK"
        if data[s1:e1] == "J":
            output = output + "TB!Ps yNus~[S$i-"
        if data[s1:e1] == "K":
            output = output + "*`81[D!MDQMQvX2w"
        if data[s1:e1] == "L":
            output = output + "jA6,F/5k7MV#}HAS"
        if data[s1:e1] == "M":
            output = output + "O[z*W)zct]kN]j.f"
        if data[s1:e1] == "N":
            output = output + "c*}=Q.jXV>lmi@y?"
        if data[s1:e1] == "O":
            output = output + "5*t{:[6)8&zTo1Q)"
        if data[s1:e1] == "P":
            output = output + "HW'c),sTXu(C/hb_"
        if data[s1:e1] == "Q":
            output = output + "Yi%!@l0?eFVO9_yf"
        if data[s1:e1] == "R":
            output = output + "v%g6vt$iu wr~hT0"
        if data[s1:e1] == "S":
            output = output + "'HXI~-:f6/q.+W~5"
        if data[s1:e1] == "T":
            output = output + "75ja:yi~Be<) //4"
        if data[s1:e1] == "U":
            output = output + "/m%JaE?]HkhUYmiU"
        if data[s1:e1] == "V":
            output = output + "s@hq}&db'wr}9G/^"
        if data[s1:e1] == "W":
            output = output + "EDZ$lA w]@:8s8K8"
        if data[s1:e1] == "X":
            output = output + ",EQ,*,X}Ap( HR %"
        if data[s1:e1] == "Y":
            output = output + ".zth& E^Ej:>a(n3"
        if data[s1:e1] == "Z":
            output = output + "AXZ*v4J+l'm=z&4{"
        if data[s1:e1] == "1":
            output = output + "6b6~{g-~cdP*7@Ga"
        if data[s1:e1] == "2":
            output = output + "@(wQcBz/Ih[oJUu("
        if data[s1:e1] == "3":
            output = output + "H9[V>`W^n3f/P[k#"
        if data[s1:e1] == "4":
            output = output + "qViZb(=iW7O#2^>x"
        if data[s1:e1] == "5":
            output = output + "9%epq=/FH'k?+{Jx"
        if data[s1:e1] == "6":
            output = output + "ch8}`?r:%28G182a"
        if data[s1:e1] == "7":
            output = output + "fU_DIR]wn%TKdo`B"
        if data[s1:e1] == "8":
            output = output + "+TuQ2yj eKdEd$+="
        if data[s1:e1] == "9":
            output = output + "t1x4fJD@w.fNxkwa"
        if data[s1:e1] == "0":
            output = output + "$N!8W$16QZAOYF@W"
        if data[s1:e1] == "`":
            output = output + ")BUdeFiR`Nkc-E'>"
        if data[s1:e1] == "!":
            output = output + "/G4yHvg$Q}bO627@"
        if data[s1:e1] == "'":
            output = output + "vbl)pPLZ>Z&C>x9}"
        if data[s1:e1] == "$":
            output = output + "ZopPq{^S&rg']o[Q"
        if data[s1:e1] == "%":
            output = output + "]sOs(pX[G~cK<=uO"
        if data[s1:e1] == "^":
            output = output + "UtO}M=P3oB52~S+!"
        if data[s1:e1] == "&":
            output = output + "eVu?fnR>*@=d`x'S"
        if data[s1:e1] == "*":
            output = output + ":LZDD/Ef{`t 73x8"
        if data[s1:e1] == "(":
            output = output + "L>_Zk^tLly:Z<[^J"
        if data[s1:e1] == ")":
            output = output + "CB--{.iiC<TmV,,8"
        if data[s1:e1] == "_":
            output = output + "UppH4w,FqRRD=9Bb"
        if data[s1:e1] == "+":
            output = output + "<-p#%n@*yM_9^K:'"
        if data[s1:e1] == "-":
            output = output + "OX P7+g^k7h>1z{e"
        if data[s1:e1] == "=":
            output = output + "v'mCirIC-EpY^PhY"
        if data[s1:e1] == "{":
            output = output + "dtqo&*=?'vaC9Nz!"
        if data[s1:e1] == "[":
            output = output + "#XGhoIc3+T{xUnCr"
        if data[s1:e1] == "]":
            output = output + "B5rL7^o$7x#(tAd2"
        if data[s1:e1] == "}":
            output = output + "9*}Jju']4IxQccTh"
        if data[s1:e1] == ":":
            output = output + "Dd1rJ#G<jZf&54<$"
        if data[s1:e1] == "'":
            output = output + "-pv-sCZ]d}zK'[H:"
        if data[s1:e1] == "@":
            output = output + "D]#.,s+9(NfFdR9$"
        if data[s1:e1] == "#":
            output = output + "(#1?AwVIxGO+mux!"
        if data[s1:e1] == "~":
            output = output + "{Hv0tnV$3'. r+9z"
        if data[s1:e1] == "/":
            output = output + "JbVy5YSy&54$:eBF"
        if data[s1:e1] == "?":
            output = output + "?feC`*qV7*Tn?P3~"
        if data[s1:e1] == ".":
            output = output + "4{lO0T6r5mU=L[qf"
        if data[s1:e1] == ">":
            output = output + "So1oMEG.9LT3j0Le"
        if data[s1:e1] == ",":
            output = output + "Dup:hbD]l)G?sA05"
        if data[s1:e1] == "<":
            output = output + "Sj%LkU0YI1DQ8C~H"
        if data[s1:e1] == " ":
            output = output + ".<sr@yvZNS%u'bU)"
        s1 = s1 + 1
        e1 = e1 + 1
        c1 = c1 + 1
        if data[s1:e1] == "a":
            output = output + "X]1V7dN=bD9'DYrU"
        if data[s1:e1] == "b":
            output = output + "R^~ch$.-[vryRU@-"
        if data[s1:e1] == "c":
            output = output + "z!T qdwGiy1)B4kO"
        if data[s1:e1] == "d":
            output = output + "I7#[{aH^vdxp~0wf"
        if data[s1:e1] == "e":
            output = output + "qcTHOm(dB/7@Vfbe"
        if data[s1:e1] == "f":
            output = output + "F:%!f#`@MMmI(yK'"
        if data[s1:e1] == "g":
            output = output + "UB0P0eQ7R_[YX.x "
        if data[s1:e1] == "h":
            output = output + "WRHY}V#y5,a.EB=7"
        if data[s1:e1] == "i":
            output = output + "5'rIDk?yez=Fn`m!"
        if data[s1:e1] == "j":
            output = output + "`f~WobEXT'[&C-,7"
        if data[s1:e1] == "k":
            output = output + "xzr]=?5qKNAG*O.N"
        if data[s1:e1] == "l":
            output = output + "~=gX4%%-'o{zF`5I"
        if data[s1:e1] == "m":
            output = output + "JhMJb6R6:mgs]?%X"
        if data[s1:e1] == "n":
            output = output + "Yz`yZJ&a>(~O9'7+"
        if data[s1:e1] == "o":
            output = output + ":'K#,8]It>Zav&2F"
        if data[s1:e1] == "p":
            output = output + "46I}s1A]Yr<S$)qQ"
        if data[s1:e1] == "q":
            output = output + "viv@T4mAGLF3J9pA"
        if data[s1:e1] == "r":
            output = output + "dP'g_mvoZ+ mUDjl"
        if data[s1:e1] == "s":
            output = output + "sJI@Ul[!N(!>DE4y"
        if data[s1:e1] == "t":
            output = output + "Q'V<h_*ua/'8Qy1D"
        if data[s1:e1] == "u":
            output = output + "iI,Bu2'EOSzeA?=t"
        if data[s1:e1] == "v":
            output = output + "!X{r]3BQi1BD6`3_"
        if data[s1:e1] == "w":
            output = output + "Z1bgz}p@Q?C^VLTR"
        if data[s1:e1] == "x":
            output = output + "_tidaKL^xd%CNriq"
        if data[s1:e1] == "y":
            output = output + "zk[!-)NRPlna_,!H"
        if data[s1:e1] == "z":
            output = output + "tbmY>:%(}QShNBy."
        if data[s1:e1] == "A":
            output = output + "n(6#GV:ckT*&psX,"
        if data[s1:e1] == "B":
            output = output + "{Z+d.*G(C30ab2`6"
        if data[s1:e1] == "C":
            output = output + "GsM:^wHk0,_+I*E."
        if data[s1:e1] == "D":
            output = output + "8qcE/$b*i~K)`}9}"
        if data[s1:e1] == "E":
            output = output + "zWz^^,nL_tCV9PWx"
        if data[s1:e1] == "F":
            output = output + "VF`s<a`JU7D>LY.1"
        if data[s1:e1] == "G":
            output = output + "84lQ4M'RxkNmEH)>"
        if data[s1:e1] == "H":
            output = output + "GxwbtIU&#H<C3i*'"
        if data[s1:e1] == "I":
            output = output + "APJ7m+c9c1sw8dMf"
        if data[s1:e1] == "J":
            output = output + "Vw0c]5#6t1X~gp7f"
        if data[s1:e1] == "K":
            output = output + ")__9ls8<vL ghhoG"
        if data[s1:e1] == "L":
            output = output + "TeX/5uT7nEL4JZNU"
        if data[s1:e1] == "M":
            output = output + "oXw>F%gS&m4AIG38"
        if data[s1:e1] == "N":
            output = output + "ef~Hnor-C7[nR>hW"
        if data[s1:e1] == "O":
            output = output + "dreQtX2V<F%iw&9~"
        if data[s1:e1] == "P":
            output = output + "krc'!^+Pw81?JG+T"
        if data[s1:e1] == "Q":
            output = output + "-)Wg9$L/$b$*J6Pl"
        if data[s1:e1] == "R":
            output = output + "2DGOf)sfZmWtyTa{"
        if data[s1:e1] == "S":
            output = output + "h4[shug+]Z?%5Swq"
        if data[s1:e1] == "T":
            output = output + "LTMYC<3e}*cdK Sq"
        if data[s1:e1] == "U":
            output = output + "cA0[-b$2#)HsI`p="
        if data[s1:e1] == "V":
            output = output + "L>a6jrtE~xk}=0D9"
        if data[s1:e1] == "W":
            output = output + "R@nKu9j)c'k.XRdj"
        if data[s1:e1] == "X":
            output = output + "EjV&'@G2Hx'N[2t?"
        if data[s1:e1] == "Y":
            output = output + "k'9)GO{:I/4UP&$R"
        if data[s1:e1] == "Z":
            output = output + "qWL5gpaq]OkiVF_H"
        if data[s1:e1] == "1":
            output = output + "%Jt=@e2pl:U8P<Ck"
        if data[s1:e1] == "2":
            output = output + "+cY,sDZ$u.Yeh5H:"
        if data[s1:e1] == "3":
            output = output + "l*#36/,f<g~-x%-("
        if data[s1:e1] == "4":
            output = output + "N.l#0])+G&QKzQoS"
        if data[s1:e1] == "5":
            output = output + "J{>h^>$'p5Ynw^l "
        if data[s1:e1] == "6":
            output = output + "#%ZnztmyugKSa9vi"
        if data[s1:e1] == "7":
            output = output + "`!W=Eu7f@3H`^(yb"
        if data[s1:e1] == "8":
            output = output + "5hQ<$aB2=pu!BS$S"
        if data[s1:e1] == "9":
            output = output + "BozuKFWPYX gM-!6"
        if data[s1:e1] == "0":
            output = output + " o=r(#su1fmSqiih"
        if data[s1:e1] == "`":
            output = output + "Fr}oIWc=U]bjv/'_"
        if data[s1:e1] == "!":
            output = output + "]AEnj(b]!(AK2$D/"
        if data[s1:e1] == "'":
            output = output + "[sEHZ0Eh7cySxPc~"
        if data[s1:e1] == "$":
            output = output + "`{A0Pjt.KN& v-%:"
        if data[s1:e1] == "%":
            output = output + "A-CsMZy6t>o13jJi"
        if data[s1:e1] == "^":
            output = output + "/ }${{~wUD[/fu?Y"
        if data[s1:e1] == "&":
            output = output + "8(+gBl/jTMRXdurp"
        if data[s1:e1] == "*":
            output = output + "wY[?~6Z.n.}=?vJV"
        if data[s1:e1] == "(":
            output = output + "dOXeNMTx=W&v3M4>"
        if data[s1:e1] == ")":
            output = output + "o*BS%6,K8'3_2ZQ'"
        if data[s1:e1] == "_":
            output = output + "W)F#{+*EjuOM@^@l"
        if data[s1:e1] == "+":
            output = output + "0k{TNVD0<bdUC+Vj"
        if data[s1:e1] == "-":
            output = output + ".f)^Ip5(814HRc:m"
        if data[s1:e1] == "=":
            output = output + "}Bf2OuneKwn-U7xr"
        if data[s1:e1] == "{":
            output = output + "8U)peC2A@KeMSO$}"
        if data[s1:e1] == "[":
            output = output + "u{ZOe,zpLDz'wak3"
        if data[s1:e1] == "]":
            output = output + "^e8qROoFIF38!5Uq"
        if data[s1:e1] == "}":
            output = output + "Mty!Pg?C?9N4C:R("
        if data[s1:e1] == ":":
            output = output + "Ho%l0> },Xlr<?B_"
        if data[s1:e1] == "'":
            output = output + "gE(]-LCl'A,>LPbM"
        if data[s1:e1] == "@":
            output = output + "a9AF6AlPTD*& 'B2"
        if data[s1:e1] == "#":
            output = output + "!<L]W/[3 <<&}Wnk"
        if data[s1:e1] == "~":
            output = output + ":'O1xZ'wiJ3:`i%8"
        if data[s1:e1] == "/":
            output = output + "k5#Ljv2o9 1q[h=O"
        if data[s1:e1] == "?":
            output = output + "/+5?vQq @#.N'}&q"
        if data[s1:e1] == ".":
            output = output + "^'sm`h@YyY'[ n6{"
        if data[s1:e1] == ">":
            output = output + "p{&7*oQfQ)p>VG?j"
        if data[s1:e1] == ",":
            output = output + "$:0]J4xdTv0K,G+'"
        if data[s1:e1] == "<":
            output = output + "-P*_x/SWSzj*,+/v"
        if data[s1:e1] == " ":
            output = output + "{_^1jC~:5#'<4@~F"
        s1 = s1 + 1
        e1 = e1 + 1
        c1 = c1 + 1
        if data[s1:e1] == "a":
            output = output + "u3j/CdB_3/tMU/>9"
        if data[s1:e1] == "b":
            output = output + "Dl!!8R#@Er&rL&*m"
        if data[s1:e1] == "c":
            output = output + "TLcuMu.Xj iIoq`-"
        if data[s1:e1] == "d":
            output = output + "Z%tRl{.KMg$Lw2Q7"
        if data[s1:e1] == "e":
            output = output + "~-?Pt$0'[~>T' vy"
        if data[s1:e1] == "f":
            output = output + ",$g'ZVX!g('[gX6S"
        if data[s1:e1] == "g":
            output = output + "r79P8MrY7N5HqU $"
        if data[s1:e1] == "h":
            output = output + "^BpZ#1g*z1z6y*o&"
        if data[s1:e1] == "i":
            output = output + "8_q%Lwx( ,I0+JjM"
        if data[s1:e1] == "j":
            output = output + "0,pVvRp*9u:,mICI"
        if data[s1:e1] == "k":
            output = output + "a5:]KoZBH0ZY`(BO"
        if data[s1:e1] == "l":
            output = output + ">iuHQar0k`S2T(Ju"
        if data[s1:e1] == "m":
            output = output + "VG#olvLi%%aEY7tk"
        if data[s1:e1] == "n":
            output = output + "jL0:Fd#AU#8[B1z@"
        if data[s1:e1] == "o":
            output = output + "Yu=e`H@u,MXAek[A"
        if data[s1:e1] == "p":
            output = output + "-M7  ~K[]3s`8Rd^"
        if data[s1:e1] == "q":
            output = output + "[MIR]vf^G]<.`*!S"
        if data[s1:e1] == "r":
            output = output + ">G7MWqwU2O_.hY4="
        if data[s1:e1] == "s":
            output = output + "J^xd}PAC6&*WT]5_"
        if data[s1:e1] == "t":
            output = output + "S2LMj+kJ_bIr4opW"
        if data[s1:e1] == "u":
            output = output + "!ChlX{B4p#lU'^sC"
        if data[s1:e1] == "v":
            output = output + "*'Ed36@Q-n3pt1fA"
        if data[s1:e1] == "w":
            output = output + "xcQNKMwS{HGB9K`3"
        if data[s1:e1] == "x":
            output = output + "wm}lOxZRh=Tq>w}%"
        if data[s1:e1] == "y":
            output = output + "/ dF-!#t6eV?qIkF"
        if data[s1:e1] == "z":
            output = output + "rFRR2[wH(:7O+8Z."
        if data[s1:e1] == "A":
            output = output + ":0r&zCLQ,}5=D!!]"
        if data[s1:e1] == "B":
            output = output + "V@7@X~~sHFYCr83U"
        if data[s1:e1] == "C":
            output = output + "_<&}yG,'d $o-O+g"
        if data[s1:e1] == "D":
            output = output + "t~lMw@u$v!asiy]g"
        if data[s1:e1] == "E":
            output = output + "Sk18X/.>/LvT+z:n"
        if data[s1:e1] == "F":
            output = output + "Ak@i.j b'=@<aU4:"
        if data[s1:e1] == "G":
            output = output + "@3+&G:'b*NwoTb2`"
        if data[s1:e1] == "H":
            output = output + "t9HlZ'N=k_z}4i$#"
        if data[s1:e1] == "I":
            output = output + "'g{QP?L<cK%9O/oZ"
        if data[s1:e1] == "J":
            output = output + "NcFn+/'KiAxsqZeP"
        if data[s1:e1] == "K":
            output = output + "}W/o,sVn=&2G-w=>"
        if data[s1:e1] == "L":
            output = output + "0kzzqf05{{<:#(j6"
        if data[s1:e1] == "M":
            output = output + "O_Nk9zaUP%WYpgM)"
        if data[s1:e1] == "N":
            output = output + "=qBrK8DO1,13Og~o"
        if data[s1:e1] == "O":
            output = output + "!eVDB?W)(aJ)9U3B"
        if data[s1:e1] == "P":
            output = output + "fa%vKxX{Aqv+gbyt"
        if data[s1:e1] == "Q":
            output = output + "MZDhRnnC?l$(&xOe"
        if data[s1:e1] == "R":
            output = output + ":kV[YK/W5<J*e#`p"
        if data[s1:e1] == "S":
            output = output + "C33YW*10hR>T=/+D"
        if data[s1:e1] == "T":
            output = output + "`./$]apmBl6(7e)J"
        if data[s1:e1] == "U":
            output = output + "E?rQfP^5$0y{KJn4"
        if data[s1:e1] == "V":
            output = output + "1LcTFCcy]4D.}jXb"
        if data[s1:e1] == "W":
            output = output + "^u5O{5sRvEA)BG:("
        if data[s1:e1] == "X":
            output = output + "s !?8c'Xz+JLilt("
        if data[s1:e1] == "Y":
            output = output + "9&Q{r,b5gAOe3.V^"
        if data[s1:e1] == "Z":
            output = output + "PF[9p,T6?1*N+@i`"
        if data[s1:e1] == "1":
            output = output + "QlWw/'')'AC'>f?,"
        if data[s1:e1] == "2":
            output = output + "aBXDtI1r3n9vwyjg"
        if data[s1:e1] == "3":
            output = output + "c)=E.r6-4175Byq "
        if data[s1:e1] == "4":
            output = output + "&&546D<:NSPN>vkN"
        if data[s1:e1] == "5":
            output = output + "l@lQ<kiQRQYSFw+0"
        if data[s1:e1] == "6":
            output = output + ")bnA=A'7*z$iCMD~"
        if data[s1:e1] == "7":
            output = output + "/ia+O]3V<Y>R:J:y"
        if data[s1:e1] == "8":
            output = output + "S8}oc??$K.2v'<Y$"
        if data[s1:e1] == "9":
            output = output + "'q<:5Ci+-J51^S#h"
        if data[s1:e1] == "0":
            output = output + "2m?~:G)qghHHwa's"
        if data[s1:e1] == "`":
            output = output + "j6{dl!n^s'Hz^WXs"
        if data[s1:e1] == "!":
            output = output + "VmB)fc-j0dhW9H^9"
        if data[s1:e1] == "'":
            output = output + "~xbNWHI00]7Ssh!U"
        if data[s1:e1] == "$":
            output = output + "xr_W#>~WVoJ7pbj*"
        if data[s1:e1] == "%":
            output = output + "E'Xn!zQc-CxRW'~h"
        if data[s1:e1] == "^":
            output = output + "F4K{z%.JYID5}*H}"
        if data[s1:e1] == "&":
            output = output + "=>NVat0[Idm$8fpq"
        if data[s1:e1] == "*":
            output = output + "e7ufbGX<h>bRX{V9"
        if data[s1:e1] == "(":
            output = output + "+@ZWI1E?Fp%?m%>~"
        if data[s1:e1] == ")":
            output = output + "Z[cu24GQ_~4[_bEx"
        if data[s1:e1] == "_":
            output = output + "vvL{A}=JsY#GTu3f"
        if data[s1:e1] == "+":
            output = output + "mI](F-4FNaEuACP'"
        if data[s1:e1] == "-":
            output = output + "GX@)P&%}%{^hsRJf"
        if data[s1:e1] == "=":
            output = output + "HcIpn2TihU8xtkY-"
        if data[s1:e1] == "{":
            output = output + "+eN-Txy_E<UmU$in"
        if data[s1:e1] == "[":
            output = output + "I#.hEvr6DEfc>~Q`"
        if data[s1:e1] == "]":
            output = output + "1'v_,&s8zKPd?Mws"
        if data[s1:e1] == "}":
            output = output + ",NE''yP4Z(^/Fq`L"
        if data[s1:e1] == ":":
            output = output + "GL=1jjd)UpS''C[-"
        if data[s1:e1] == "'":
            output = output + "_<-zd#oe}pOZd)b_"
        if data[s1:e1] == "@":
            output = output + "2Td]mo{!Oxey<6l]"
        if data[s1:e1] == "#":
            output = output + "nh9L'j2)7(6f%[m}"
        if data[s1:e1] == "~":
            output = output + "dZ%ge`cS8o&}U Sb"
        if data[s1:e1] == "/":
            output = output + "7*y~58kw.m2<V[@E"
        if data[s1:e1] == "?":
            output = output + "yuJ,tcxA*DODYS.f"
        if data[s1:e1] == ".":
            output = output + "x?IPFmfF6B$ty^42"
        if data[s1:e1] == ">":
            output = output + "iDmVn%2Q' 6e^ T("
        if data[s1:e1] == ",":
            output = output + ")H@heUmD_Ng4a!(E"
        if data[s1:e1] == "<":
            output = output + "Sf]=aqot#GTbukK`"
        if data[s1:e1] == " ":
            output = output + "[,P 9]K nP/j&G`)"
        s1 = s1 + 1
        e1 = e1 + 1
        c1 = c1 + 1
elif leng == 64:
    while c1 < l1:
        if data[s1:e1] == "a":
            output = output + "u1*Gt?fd[#~t$2j<NGx.o2&i0_CUZ`3cfR.Lv5L+yOV&Ii{.by#3:c+5'P01#)3_"
        if data[s1:e1] == "b":
            output = output + "^ko'ph%uzs.b.WGWA{^WWtyr(Rxs{XAM(yE29_Hu,eM1Ng#ncl~'8I IPoZ!9yKJ"
        if data[s1:e1] == "c":
            output = output + "*z#Zb>tmt'6a!Ky*#0aMk#ma JPSsg69G*~OQ6</OKX>.xABb:k/9e<]hi H^Md)"
        if data[s1:e1] == "d":
            output = output + "*yAk5%ILJFwB?bzDz1<X> 8]eR-P0#alQk4`*vgTL&iqKx[c7/@~-qbn%Ul8XV&n"
        if data[s1:e1] == "e":
            output = output + "`0oZn,]a)H!vWPk_@#mJcG>ONnAFb)fzBm=GYU=B<=2FsvfvC2{PGM[`'sDI&+B)"
        if data[s1:e1] == "f":
            output = output + "rg'u=uVy$c'X668[y~LewEcZ+ Zo+Os{8_f9Pjj%)y?'B2OI-7Rd[OE7ad:9JGV{"
        if data[s1:e1] == "g":
            output = output + "Ot!3+=X=ICp>:^ `g~TSfd(C`~L0&.c66D'!8/JjL-K[4<i>S}q@:=ohNF~<D}eD"
        if data[s1:e1] == "h":
            output = output + "pg<%lB9E5b=SJ/1<#Z}ao@z(zf`HWs~LB_V*_x@6o'r06(X@~AF.!F,o02~5K5C9"
        if data[s1:e1] == "i":
            output = output + "1NJ(?v4Gqe_@$J}Z5aX'3b%cv'q~'V$azjK}9Bf>QJ1s/AH{GVQ5!O RBPg/?}SS"
        if data[s1:e1] == "j":
            output = output + "tFGH}<z(sqTAI#7Fmv-jRb&J+P' vd8xGEKIP^AH2']V:Lh1CA`N]MW?<si^!gav"
        if data[s1:e1] == "k":
            output = output + "'Uo'i(9=Iv18-WdT03RD$>xFpH,-B8lQfM#9zUG^<zHHT77Oe)*:m1NfBcr(oGh$"
        if data[s1:e1] == "l":
            output = output + "#$K,]A]yR`[GU`?&$O%$Ky)`Dg9#GkvH-cxK*V_PL9rw},wsOIoQ(]1zYn(@OQK0"
        if data[s1:e1] == "m":
            output = output + "roPd&%@<2Kf,,RlR5mbw{&GTN4n:igNHX+4a&U5Vo=I[~mpcTiwC+'h2iF$!s+Ak"
        if data[s1:e1] == "n":
            output = output + "W@SY,&tP'))]jF}(W+ui]K{3UUBCgQ%jV]xCyA^~m7l)}#[9X[Q<.n- K{`8x^om"
        if data[s1:e1] == "o":
            output = output + "N)?-vQ8fBs7.]8Zco_WOQ*CRNK{=_zj37YfD(hbhU=j9`c.)Mx& mPw$o{$KH'YE"
        if data[s1:e1] == "p":
            output = output + "7'wtWqACX]E1OP8q{{<6N=#KcXb^:h(:d6tST/4hZ[u= m4yCi(41qUZhjVExNX9"
        if data[s1:e1] == "q":
            output = output + "x&F?3Insb.xT'&u4hcbO-jNYb6_']?*CIG<e/nPt%4,ax&.@11 LR/usWHvo7}>v"
        if data[s1:e1] == "r":
            output = output + "(<@<Pppdw:=BC#a7:*'Cv'l+/+4maAey)jSK>lU*j.cy'rze4cU,=m!) 9>x()}%"
        if data[s1:e1] == "s":
            output = output + "HZ'jb@Kt,H@0F@'k7GeMNgr{Cro_?&Ei}UkG#*=0R>ww{LaXX2^%[#FQ/5o+13NI"
        if data[s1:e1] == "t":
            output = output + "SDd9XAJ#m]nsL!-+nww~0+*`M:Zol'!f2hH3/f70aYQ%$(_q~&.(^mS[h?GecntU"
        if data[s1:e1] == "u":
            output = output + "KuNQ)PQQ(2R*+P3Gj1Ok:4J7l2:RK}&U I):n6hM=n*.D'IB}E1{Sg2_Fxu75!Xe"
        if data[s1:e1] == "v":
            output = output + "}fc+foRUt7-.`0tAw?jlA.p[,q&K'[F3ZcvjB6E9,ClTXk'f/RNq/i$B>Y&Knlaj"
        if data[s1:e1] == "w":
            output = output + "7urMcAdHNedQ7}Vn7[6.2scz2P%Q/wD+2LmUG3p=/fVV0T`9/Hl&lRmeoN=%hWgJ"
        if data[s1:e1] == "x":
            output = output + "ug*f38sR2n'hWt}^27?>>weX%EKJ@<3FW<G^v?xzatx=8v}'m@FXw(*7cc'0T'0R"
        if data[s1:e1] == "y":
            output = output + "d!`@nX9Yi5JC_ZO7~GyCH>U_y_vAfM@PJEW)K[!m:'a~%2RC$q>bLx_T<+vT %M4"
        if data[s1:e1] == "z":
            output = output + "P,CtyWeWhX%-%Y#xvhr,M'%38eI(0%3!l-mW`mZT=-LCFmi'f8^=nX@~stHqnknK"
        if data[s1:e1] == "A":
            output = output + "2[797 $Vn'P5I~e%'Mub1#Qn7R:56Cf?gd:}u%E_wfEK&vqjL^naaE-glDlIT0/$"
        if data[s1:e1] == "B":
            output = output + "U-WLw_'7/9gGg-]v?4RFg8TM&6%wp9qW@D1Xp~5SpQb@'c<RN.0%^@ipsr&!ND'M"
        if data[s1:e1] == "C":
            output = output + "^~0cQ@9ZY^N^D Xb9f2n s/(VE#uw--jZ~2UYWgg*bv6')h+}1W`@up'V1n2F!*a"
        if data[s1:e1] == "D":
            output = output + "lA3%3!Ju,UU,~/A[[,l?,W-xr'J/CER[FY&R@K9pzG#k4R0_nxoaVx.{_q1q%E/>"
        if data[s1:e1] == "E":
            output = output + "?)q=^ySldTrk/ Eym2Lt &Ou!,_e^(vV8.-r%LtBUqIl<E-F{Fm'71!H=RK'&}%V"
        if data[s1:e1] == "F":
            output = output + "}bZDB'{ycri&gjm'uv5`B_VI]jo_Agy17F*}M'3N:]pbh0:71.J{puJ<$NlO4]#`"
        if data[s1:e1] == "G":
            output = output + "T,HXgr-L=^3M-xqVI'lA^c#vINh({F#>!Rc]4iC{?D7e5}83gI7f?<J9S.M,3#_8"
        if data[s1:e1] == "H":
            output = output + "KZ'kve<,RyIt> &iJ'bTy<X]:8QeI(zf)_/3zrvA%Y-3kb4#gNk~ss53VoQ=T$&t"
        if data[s1:e1] == "I":
            output = output + "=6g52Kl)MSi2[0CvHY[+5f2iQK2Yg)+LbgnxYOgXL=jT<3b'h76Q[4{5z'Cws/MS"
        if data[s1:e1] == "J":
            output = output + "kTEHrI>It'O?2raKO- X:?8+9x~:{Ls'h'~H'7OkZ!2SOrA}{3 m'!YDAiAUk_Bf"
        if data[s1:e1] == "K":
            output = output + "H-ok}0XL>-hEW7RJl5r8Dk:o=z.28j-P/'i^ q]bV39@Pb5S558s5`zn-LYZ+'Vb"
        if data[s1:e1] == "L":
            output = output + "N$$uZvlQ1,uqc#!l]x}K 0Cp%}{nz08B*Do%mceYT`=~-*  G5lVS^n,k*In+_@v"
        if data[s1:e1] == "M":
            output = output + "s`*TorB8%0vVI,l'+h)snJ`--]p'ja_Ug?RjHdvJqakJ+S:X8'O,[4``x[P'pMca"
        if data[s1:e1] == "N":
            output = output + "z$yw UsGP=4NBgt/0rO4)(~@pe8Y9~5>3c=.ezT0~f!!1r7CB:wVPuGaVGF[=h_U"
        if data[s1:e1] == "O":
            output = output + "]#)UR=V^-h4?~*'+]wNJ%j?<(#OGN1DwF db4.6'+YP0i'6e_aEJb$K$=z_'RDy0"
        if data[s1:e1] == "P":
            output = output + "dFL+c[OD]]IGYEm [`Om24@]f$0{4^U&6Nd`F,e*{}Do}_eJitz&6izDI70':!_O"
        if data[s1:e1] == "Q":
            output = output + "}/Op<Zp7dV@S{S'E^Y4PdbRih+}E8jlv>pM9fbAPaNaXg/I%kPyV#Bts3.u}>L4'"
        if data[s1:e1] == "R":
            output = output + "U3~_+ttfrQ1q)!Wf[?jK%M8OuY07v$RrVdt?/C3Uh3,YXC3jaN5=LrzDf!$r*+*="
        if data[s1:e1] == "S":
            output = output + "f-#a<?jMXnea>W$,$rb?7a?QEk/tg>!MN'fQI6^9zOOqNKf}~0NK6)Jaxh(yZL2Y"
        if data[s1:e1] == "T":
            output = output + "wBu#D(k=SE^0xxigg n>*B`2CO't/F@rlR9('Yxw)k.'x.Kg+Meo<-}gmkTjsk&F"
        if data[s1:e1] == "U":
            output = output + "D'hordB`!b]7xv(PcWDZ-Vjw}EQ?5IuPm=uown%9`j?JCxh35W2:HU4z7pFsF`[^"
        if data[s1:e1] == "V":
            output = output + "`c.tz[}~,`]s-}qW>hWC ]~r_CH$P#G5#G4`vt?1y'WA&97ckAv2orW~krIckhD~"
        if data[s1:e1] == "W":
            output = output + "pAC<=4'0Ds7N+uN~`K,NFk,1k61LWic)<+S8hT:Su4[{9,@#{^2SJ3}+-{/Ja%R*"
        if data[s1:e1] == "X":
            output = output + ">-cC@!o$'TABF.m6AcEh,eZy:F`as-d7IjCsO*[-}8=/)Hy5fF+cn<C]rJg/aDhU"
        if data[s1:e1] == "Y":
            output = output + "f$!@T7'rEBOho_Hp^<4YnXyQ)RWY,Wj:-km]kI8&k3N7'PL4(kR+uqxL6CAG2#y'"
        if data[s1:e1] == "Z":
            output = output + "kKH(q^lBRgS+Ye*e,Iiho^Gib+3Ek&5bGxmoFT.(qxX[4Gb.$TY^Lo?a[J]7A{k]"
        if data[s1:e1] == "1":
            output = output + "j<{KKOz`>m(`]Jm,@hkkz5@XHQGZuuh55>:Ld4VXEhf`fobhi7h 8RN[Hgn9(!j`"
        if data[s1:e1] == "2":
            output = output + "1'9B%f9>]maN/>[/E@!gVulL9zpG-P'er_Txs(!7(1VcD*u(G IX6HLHl1rH6B~T"
        if data[s1:e1] == "3":
            output = output + "MyBZi24pp-P]#{}#lD85RVP8##d2$aW4>d_^ep>zd0(]W.kLfZk*1QR$KY1Og0N~"
        if data[s1:e1] == "4":
            output = output + "~Md}??{YPTsY]wsmtriuzQ`Vv*???@*ef #0yY#8TmQ{iD*y=p#bC>/'Y*N+LgnD"
        if data[s1:e1] == "5":
            output = output + "m'zEYYp(PO+6Knvd}=pCqcGruQ2.Bb'?lL@+t:^Mp1H&wTCOvmD?u^BA@AttMPZ%"
        if data[s1:e1] == "6":
            output = output + "4N5&zY'#F<MF<z4S~'iu)60uOI]4E`%xm:y&UqQ__e JT)A{E]%L.j3Sefu`@:)5"
        if data[s1:e1] == "7":
            output = output + "dmrJeLEy1^)7{Szu6TbGZ/5f-cOp0OA@o}Up:&/ M3xL2cWJk!(nXI9K[A8t@{:Q"
        if data[s1:e1] == "8":
            output = output + "eoZu'@g=<4&}YSI[9b1DXz2Uw[R1h1ecd'N&.j3DgM'*?Q~_Z3QNQ^/{r{S){KlY"
        if data[s1:e1] == "9":
            output = output + "tHh.> n#ig =dLK98>WC:NUqHtR:F](~zFM[q&m_AjGMnNM zM4J:2M$Bh0P<&k4"
        if data[s1:e1] == "0":
            output = output + "rHDe:&+0dq5Df_t..e%cECq#/fVM2+6>Rpw$ser2^wN28m7bE*)TW'GT]4u<i=fz"
        if data[s1:e1] == "`":
            output = output + "Uz$1l.[GpeX$%T&3Go+Md]UBb#),Y6yr)5)X~o*0E'6?aPpbH!$?@vhc'ZHGHnQp"
        if data[s1:e1] == "!":
            output = output + "RE@&wO649l@qnT?'btpapj/fC7q@Jz><qyYO`Q [:9&%cSfCg05+ydz+^[6]S>:F"
        if data[s1:e1] == "'":
            output = output + "jptY%W$wJhcZ<v8w%}NC_jVv3 l_}uO#le_SgUsQ,MS:JTp'AI,PSVE!'[?6[gr#"
        if data[s1:e1] == "$":
            output = output + "r*Ial#S=LSZi{Rh'Z(=ccEoT^/k'm Z$^J]SJPHa:%BPpEQJVio>5Cnye:QUs2ux"
        if data[s1:e1] == "%":
            output = output + "cSF6Xan!SwxwZ&F?K{>M/=)4`R4H&1>KJt^z@[ebb 9SCL*#d90ds68yV}fcl =%"
        if data[s1:e1] == "^":
            output = output + "%%o+8gpP)0jo@:Ll*Z1mDY9-8r)qjvwbM-Z=8rAgD%F<L9L Z?WN(y8gl^#NI'ox"
        if data[s1:e1] == "&":
            output = output + "d~mhA8=A1T$3TYoq:lkf3@d6+DDMA/El .3R X1 xCZqQ?QxwbN`m3a?Wd65otpA"
        if data[s1:e1] == "*":
            output = output + "b&Lf=^tX6wq# f29}Tui~nI0Bt/m).2S$<$<P1Q!4q'k5JIyo_5PpoY6x.`^wxr#"
        if data[s1:e1] == "(":
            output = output + " #j=dui!E+On_Q)eUiFVE'uAK}&:d<aV&:jr9p*a'^lB,O(-[*k6I~~Tzr+3< R6"
        if data[s1:e1] == ")":
            output = output + "!i?rG:lM2jwZ ' (H~!~D<HwnW7.BS:T-8uh^OYk'^T'*aQ8-5v,L*iXIH=BLI`d"
        if data[s1:e1] == "_":
            output = output + "$T9!`vlEPo<{Vu1M{.V~gn0SwiBJ.EHv_5LfC:/Lg`T(4`8O&N(iUt,J,3#{!E'R"
        if data[s1:e1] == "+":
            output = output + "8BMRW3lme`>MTHBV{KLtJ_tz u(d&~kvI@}>.H-/Pd4:0 4+z<h-dwsdEUjwup`Y"
        if data[s1:e1] == "-":
            output = output + ":<I2dzeD0#/TQ8W46wMyI5UL0OJs`s8xNt1ZKDwZC7SpXm?5OmyS:[bGGpQq_).s"
        if data[s1:e1] == "=":
            output = output + "Lq>iR^sw?DZ@brLSEiBfxU7=Gfs3FBBR<g.hqh.RyorX[sgCavxc@*MGg8^K4m1Z"
        if data[s1:e1] == "{":
            output = output + "Jj7dWNS?Z>#Zw)j'69%b]BW3@)PFbi1$WTl+Sm%A'Kt&?!pEL~.+:<qFWx,.3H,y"
        if data[s1:e1] == "[":
            output = output + "IQ.rOUOJX+<tZ!vcezC&>V9 6qeLekE^^7!'*3BP(bqB9]/WYA9<0RF$f#P[Wxf`"
        if data[s1:e1] == "]":
            output = output + "rMFG'd09CB.S !t yQ4PSig[9CJF`6X,^[EuAMGAkQM0l*iC)EyuX>$x,Uxh,aHM"
        if data[s1:e1] == "}":
            output = output + "{O22!eE`wulPnXa=~Cu-vgRUvHL6GAkb]9zFYuMQ'Ul%S,!GR^qZ4-Sx]+q=>z/t"
        if data[s1:e1] == ":":
            output = output + "_3<@]}74D,:L$,Or_P_w.YgH&,-,P!.qjOG5NB~a*QI{i]FEA2iO$uV}:4t+0,}t"
        if data[s1:e1] == "'":
            output = output + "a(g_qD.^5~8z]dS<TP:d$KYX%VQY20?I2@)U[K]W1Z`x,j6ozAd> ~+a[5n6lDm1"
        if data[s1:e1] == "@":
            output = output + "o.wv1{nNZhc/k!vyB$O{<FsU}hDi1/ei>AyZ(iK%zb3iAoDeVCnmjH/sE4Y&J(Dz"
        if data[s1:e1] == "#":
            output = output + "r[]S&nokFp%{Y$RE,sUy!vFBEc% Y8mkz_0T3*a43Wu0^CD}3b?>hUPrc]$x)21>"
        if data[s1:e1] == "~":
            output = output + ",#Cu2/wxriil}-r{7B2HX57(,GD$TQIvb0Zn%KA>h4=XDravs7lJBh]6w*e{a*W!"
        if data[s1:e1] == "/":
            output = output + "mdd'[IsU>q>*TB$VDisUG*CyJm6L])@yznzq,Zt-XH'e[X5gjy]6qJy<X!:_[8p{"
        if data[s1:e1] == "?":
            output = output + "?dKKN&ys%'{hl>MMKDqWP]OSsa#1n`U)x$2yyD{y6XI&d)?(q w3)Ml??}a`hT/{"
        if data[s1:e1] == ".":
            output = output + "]5)~()k3~pv=)oVTsMTsv!~fWj6AV{sHNQnS+f`j)VU$Rp}pa.X?$Zd@wV'}/(Sx"
        if data[s1:e1] == ">":
            output = output + "YXi=U}G:%Wte(nv8@s'Zd%R{5(HAY<!@VF@ pU`/=7m9A5FDm)1cA*eUI_xloSXx"
        if data[s1:e1] == ",":
            output = output + "}]6nqBq)_>1{Jw5.wt0E>-5te6-vU9'HBYK_$jWNsb.=HuMY<wV^km8uWd)-[a~S"
        if data[s1:e1] == "<":
            output = output + "6ywI*S1o-$J8dXC*8PNZOWc(p'9kp,98qOF~s!F4^:*Dz}_'P7Ie>&Yjl[<QJqY'"
        if data[s1:e1] == " ":
            output = output + "'TZ/+>$p!Fq,!jGA[6V*GDtJQ'V[(Q^/?5W2jRoLZ d/1.UM1B!Z@ptc(f+$4iVj"
        s1 = s1 + 1
        e1 = e1 + 1
        c1 = c1 + 1
        if data[s1:e1] == "a":
            output = output + "'sq7?r6>XKoX,9RCRX%N&i[ _) 5>F-+=25C%G39Y4J>'Y['gVzM6_Q6mA&gaT:o"
        if data[s1:e1] == "b":
            output = output + "('Ih,t#/aH*9+N]/}FBw=0-qgLv?pvOCrDZXqw34@~^N?}:4OS ~_w)MG04n.@JA"
        if data[s1:e1] == "c":
            output = output + "{)HyPe?yLG!Alj>w:Cd4{5<8*h#6y%wPuLbi/sDMgW'#(A:rvt4C<2(t2xm'R/4-"
        if data[s1:e1] == "d":
            output = output + "IEV`It9FV+hEiEH(s?J*NU,6kzu9.K3*^sR#n3:jJDi}iqM4!D$uWrMS!2}]4)fr"
        if data[s1:e1] == "e":
            output = output + "F D[qnD-YqhlRU*_v)%Qjl1GNF^Yk?Bk6',57k5D2Fa(1@o{zWjq'6t]!Jz:krxw"
        if data[s1:e1] == "f":
            output = output + "8W&Xxedz>e3@9D-Reql:)Y?6vy!t+( DX8DSdvB(U*G<d{Q3yxfzizN2zb2O={I9"
        if data[s1:e1] == "g":
            output = output + "AV&)'ZeZ{/E`zQ>qE55pM9oFkv&{i'#<1,LzI(S/isx%XQ/EX272+8qwMp3yWm{p"
        if data[s1:e1] == "h":
            output = output + "c<LWEK,#/p1}K1UTqp4GfoWC}g!gzC4Dfp#MgP~gf1@UR L_<X%2Q7Q#B5=7Ot1 "
        if data[s1:e1] == "i":
            output = output + "I%ADWc1d'(o3[oWcf5Phr.*wS{e>(yVEE9voy#r7ku9cO&*(Y>.Az9'qiQ)_GaL?"
        if data[s1:e1] == "j":
            output = output + "bh]w+0!sXK9r8A,8A%G I={'pwHm3uATJ>'9dZZF!~>uxTzY`@#<[1CC4#KZq*VX"
        if data[s1:e1] == "k":
            output = output + "eVR=k[MNNnWS$xpl,^@U%2YfL*hnV=83sfFoy[VAzB}(MWXV]odF6jF9gq0+A]@Y"
        if data[s1:e1] == "l":
            output = output + "W4QB~]F~NA9HDK&/y@?2dO(=-,zT2sl'Y06[_E,MHi3<>{$]msxcmBm,J%}XQcHR"
        if data[s1:e1] == "m":
            output = output + "!F<I&{GB{.'VKy-'r7+51SE){vh^lR>>'8A`+o>+yi:HMEiR2L@?An=GP::6s3uG"
        if data[s1:e1] == "n":
            output = output + "%G3q4S{[K0W E'}KKaPI]W`.tjl*p,Qc8ZC6X._~!6U`B'nhcLq5R*#^1mp{Pjz["
        if data[s1:e1] == "o":
            output = output + "To#2(/~5T0SSWcHHdV.f@?^Tlot0mODIhT[TC-@yOs/c-T_8B!JgbDg6I]dY@{U1"
        if data[s1:e1] == "p":
            output = output + "=<^yUm=d{<sy?H?aNu,OWu?>bdb!BCHwB1o?{80M)inV!E=MO%s8*Hk#Y['g7XwC"
        if data[s1:e1] == "q":
            output = output + "R')8EaY,m).137t@.OpT~lolG@N]i1H[IE7DLL?{y'#qjZON_gsJt+'$cy)!q+,#"
        if data[s1:e1] == "r":
            output = output + "V$9LSV)v}j> BaoV1JgZV+Shh8$X7WOws#'Tc&(H&/z34#tDEdoyh$:B/HMagFZy"
        if data[s1:e1] == "s":
            output = output + "5Kj}Y%Zxgm&XNI#9i)Uu5?]'B%Awny]H&:w)<hEoX%H/'Fe-w(,)TU`PseBP}X b"
        if data[s1:e1] == "t":
            output = output + "kSB`KN<H?*yds0Zz68(8&B'hy/'-I@9W=tVt4-}TjbRBOW.xdQy,U/`+b%2I)}0+"
        if data[s1:e1] == "u":
            output = output + "dGLDJRBlbuvo5R. [^^s[cD$k>u2%LOnlVLy/*w9C70T C@x'muu.W)BOVJK i*l"
        if data[s1:e1] == "v":
            output = output + "MD>w]Z9]GR@?a$f -h{ly_/:J{{E%ZznN8Qt&2UURfEQD}:cVE^(YF=RVb$c391q"
        if data[s1:e1] == "w":
            output = output + "h^%sP1@HxdtCYe[OvHGd%+*sWsG.9:e1ah8FR#vj/l<d/GMB+$CDn'ja'u+J~6<j"
        if data[s1:e1] == "x":
            output = output + "gt$KVbX,-4ex07gK!q3aTrQ}*F4OxmOE)tPzj?K-'W&H}*&CyhN]ZANz{#5N%H<x"
        if data[s1:e1] == "y":
            output = output + "VA=AW]q6)T!9~`r1egHL+.7Kh9(yXs*32!P)OaTmAb+52mBup0/!1t&]fbfNIPbO"
        if data[s1:e1] == "z":
            output = output + "Fp_cCg_mx-m7MaOfTh1`Ue*3iM9='97f=>4ub+jSdv9q=-vJ,d+L{G7))I8T'-@0"
        if data[s1:e1] == "A":
            output = output + "3:Y/_ $)+(C^EY[lcl= rM`vE1fIL1t:,'l'6Pb}.]vaULConErB{xb2,T%H8SW["
        if data[s1:e1] == "B":
            output = output + "hiY>lkA0`JO W=Yc_7rD>Nu2+q(0xf'=P1zbp{p%_cFE8^(4GA0T^VDg3mQg'H*k"
        if data[s1:e1] == "C":
            output = output + ")G*S?Nrv:oB}inpY?wKnG,/ @K.PG.*b`v-*v`0aK*[QGI^UC&(A]e>rM+FQ0=ds"
        if data[s1:e1] == "D":
            output = output + "h?uO%VtWVjwj(MxHflh,ZIl0fQXtp9s?5CGA5b>#$ef*ss{'?8'-gwE[_:alo`1X"
        if data[s1:e1] == "E":
            output = output + "]=4:R&*`w**t^dW_q.b+pP1FRUIZX/Vv'FmD31'y%}aQT39>Nax)>4aFgji9c)''"
        if data[s1:e1] == "F":
            output = output + "?SD-~luI!vs1&Q'*@}}{8:plF),&7 =ji}y(yl0><Tfft()dGu0k%vXi2!_r$Y~."
        if data[s1:e1] == "G":
            output = output + "cFj?Tn@%7c_FMA g1!+=J<=mtWnPk8G<xf{'xxAy6{m:i0-@n_D`S'NmISDh4kVh"
        if data[s1:e1] == "H":
            output = output + ":)i#Q0>aTP#NLD)U<+}oA<e<Jua.gY^u!W]9Zuv,ZtUT2VkRK=k@cipHae yZa2`"
        if data[s1:e1] == "I":
            output = output + "g<Z}1p#eRO4HVk{[CXZh8LK'<YU$~MBR!cH6 1TG_K^ACdU*m6]Jv4f6LS~xMXOR"
        if data[s1:e1] == "J":
            output = output + "O2HY{%WYLlrBo'/a7Rx[kuBkD+IhEFnKfJ<A%DiX@vxbM.l6ywINT ZP$va6e/'v"
        if data[s1:e1] == "K":
            output = output + "GAg?gmol89diBWzNP'^rtyPI>MV(In'0O&t'u-Ew-JF~~R ZX.DJghra!$G&c(-R"
        if data[s1:e1] == "L":
            output = output + "(`p3Rk_W'6&6re<4wSN&hwy)w66Qf8rX37xFL6r$B}`wz*nn`&)gvnF=aeLyVpH0"
        if data[s1:e1] == "M":
            output = output + "o3^XS4_'?q?]AO!5olWclwf.KND!PdWb+DCAPB#f2k!R0(_9QXhT`'rfwF<`7,HC"
        if data[s1:e1] == "N":
            output = output + "QmIu]TtPj[EYC@'oFAVtXPz)-r!7q!8sHc2*Omuot-3_v^$VKV>eG'$'+%MUB!OC"
        if data[s1:e1] == "O":
            output = output + "Y8*Nl@ueWJ_:]uGh$'n)WZO^-Xf&:I,r1Qf>n@SFV/OF 2m-BhvEuC{/V`sZ4dpt"
        if data[s1:e1] == "P":
            output = output + "r-/^ZQ{DCad`w.wBrLE[6C)8#Q^ZeS'igTdlG-}]'K:(Ji[^if2wn3e5}Y~~(LH="
        if data[s1:e1] == "Q":
            output = output + "ho25PI?CdUY552-qIO$AT1S^FZypk2(@@o0X]:73v@<O ?PA~xdH]X#_=NWCBr'Z"
        if data[s1:e1] == "R":
            output = output + ",~+f:uyRxRRLzTrgYp6vKl]D2ZVSyV_.FN8Zx5b@HNfS6ks=89Tt5R3,.t'74X=>"
        if data[s1:e1] == "S":
            output = output + "#o`$3o4jQgC.2h98E2w}e5]59<5!X9FGN0a.<e~,/{eh*^0&c3$M`t]jca_V?@8t"
        if data[s1:e1] == "T":
            output = output + "`J^czF.+6u:bab7?USjuYrG!z']d,:ARV/Gv0WLjr%zAi+9BJ{~eGc]FMor4ajx]"
        if data[s1:e1] == "U":
            output = output + "1S)tj(~cpYNuN*'{<{$^[cF1MFlG5=XvjD~rtuN,s?2LWAT*rUWnA.IKJ&ti!<%m"
        if data[s1:e1] == "V":
            output = output + "cgi4kR*!P!~]M-?O-k?+F])^Ud]q!W09RjA '0^fCdHbRTnZ}t8mJ$:SvE~0hvE@"
        if data[s1:e1] == "W":
            output = output + "%Ks($.=?P rna^&hx0&N61[7)k?d`~H4SC.pq8&T>rm]wem+T^0Yu8_,3NF+/C'5"
        if data[s1:e1] == "X":
            output = output + "O(YZM4QpP8RoMS72-8.0e#Tv8Km@?.1>n8d.JI5&g&< 6ZWMZS)!<&:n/6xK#Qj~"
        if data[s1:e1] == "Y":
            output = output + "jNae d1%)<i3s?'z/[c *bUv&,l)JZ7nLwvzIlaMUO8t]]vo4rT-k=G~ri=Wz=C4"
        if data[s1:e1] == "Z":
            output = output + "@!Ew_K{s%/l{el{_gszpkf05#oZ]`]1Ja?S!!&]+Oi(%p9r<ImeFGnS.:2xndlN["
        if data[s1:e1] == "1":
            output = output + "?Swf`*m>%sc,g43@w<Dp_kUw-:?YiiTD=1(75Fc(U-c.0IYoqB',Js3h'h</(`u/"
        if data[s1:e1] == "2":
            output = output + "m,DWFS~<{iRZwb=H,bX&[~X'QD/C>4FFvpT5u~38J5LkXew2qE=t3akI.)>d*eB@"
        if data[s1:e1] == "3":
            output = output + " -AzhU-'r`YI'5kh[lIp $IW^=/n'3/^+ENIN1f%gsG 0>edO ,QwWe]7Ho2rpIi"
        if data[s1:e1] == "4":
            output = output + ":LbR.0wb-1a:06YTMYeJk>KcM'x>0G'A7ukz%S>5NRhe ?UAu)qf mBLQP#wCtcd"
        if data[s1:e1] == "5":
            output = output + "7lH?k$jCpE3pg:'z5sp*?sJ]=k'jd'(K6tBOW+Leax^'Qzy n6Z%[n$4f#K9_.[v"
        if data[s1:e1] == "6":
            output = output + "k!mFaD_l$<x4R+I3W8V2<>O`Pc<Lie~<FtFJ Q:~YjqhPsQm#SEXQ7G@/`HtuQrS"
        if data[s1:e1] == "7":
            output = output + "L>Aj[*o:$#'u<f#M2fPaZQG''7kH7Hw7ktLYUx^qC :4&7`W<x]eL}hfPkfN~eoE"
        if data[s1:e1] == "8":
            output = output + "ja=']EQ6YKfgW]n%{:@Ii<1fOWA{d{ot+pXp#y)yBjJ}TP B5oNe:Z%nU?6lM}&<"
        if data[s1:e1] == "9":
            output = output + "/clu'A'<s=Y)AUV:g`8aO3*78q]27h+K th#M 6~lPMqbqVdk*Gg3:D=[:m^U4z~"
        if data[s1:e1] == "0":
            output = output + "'0p.-zYTHjvp``T`Bt43.sOVE`9]<T5!2LoePAcx+}IoY07cW^(U&/#J.zeb<jSw"
        if data[s1:e1] == "`":
            output = output + "}`Phjmf(Y9-aUu,JW~m1M$9R&/7f2LKU[EsL,#F_a_mVAO86JCwmZ(J_-c'pXYjl"
        if data[s1:e1] == "!":
            output = output + "5X,f-S!!*qp'=b^!cJS.2Jhm!M*9x(MA0Rj$vx3r/X'PiOiX<}uOsYmo2LJ-%~l$"
        if data[s1:e1] == "'":
            output = output + "wvzJZbmi&A~YAidMe&'(jE}RCZ}#bv6^M62HBO$k*$gmbE+xza%Oj2o%X^RUd1[l"
        if data[s1:e1] == "$":
            output = output + "6jDfi6n+p=<cA82pg[qb.BY%5_4GI'+wksSKR#e%}*@}~Ko!MqpZz&mGDt`v^!5I"
        if data[s1:e1] == "%":
            output = output + "'W4c <2q~Swu`BIU~#:ERG-?kdAS3yonk0]cSg_K*iNtFXav9tg}U5dwTy1$3H$O"
        if data[s1:e1] == "^":
            output = output + "C.u$^$PxneU/[r,x^dM($Q6'){)qMBYi14XV{.JCqRvVf!tg>5oL} OP!$sv.U/i"
        if data[s1:e1] == "&":
            output = output + "izfH}}+Ys{-5Ik-'GKlVxMvU6l9o%RHPP$G9/1qfjnI$*'#B^C`H$*qIrm9R+z@u"
        if data[s1:e1] == "*":
            output = output + ":>(_FpoPR/~QFlM=UT}bs!abdw(<qIt.h4 56GbTGNVODUk~1i`[K/Kr=wfah@R/"
        if data[s1:e1] == "(":
            output = output + "'SsYjfJ>{JQ0ykHBbHuK'mD)3=4,96+&qV6p5Yo0U[*'PSz5hL<$Ej8:9w^Hm2'a"
        if data[s1:e1] == ")":
            output = output + "W(e]0CNVkLMfkr&zHk>c`Lyo'u?_IY?#>H^Q^T2<:x^1#}kF{,r8j,s2j-@ymxw^"
        if data[s1:e1] == "_":
            output = output + "9D$@)PD$pGDS*rE!yPr#,gn#[5t$~8Syfz{MXxU,M4/Qc4EBJ1Z{bqK3_0X'}cjr"
        if data[s1:e1] == "+":
            output = output + "w&DC~'%@@Sgn_[1D`K,Z3qIWToN':,V=XxCru*RBI>>)&%6EzL>gH0zl[s&^l`~&"
        if data[s1:e1] == "-":
            output = output + "4t8'Au'j)*[( BYsl7/tpnPL[B:#[p8Md}lWbr$zB%I!4@Yg(l9WjBw1>/2 qe n"
        if data[s1:e1] == "=":
            output = output + "xdnz{n-J59L_W?)OJ#@4Z-W$5zhQZjK%i2hFz}{^zh`77-9<!#T//KUq1~%x$SY@"
        if data[s1:e1] == "{":
            output = output + "x1ZC `+rnhQ0+,)MqbqLZ*!m=/Rn*v$?cO{g61j:)^'s]AIdO[x'U.9'Es]?TH@h"
        if data[s1:e1] == "[":
            output = output + "-_EK7 A(}+bWJBsvIEV'Qnp{%`]_aTGAogq='Qb)3S8U'0X>b'X#PS_6P[):c>jZ"
        if data[s1:e1] == "]":
            output = output + "uvhr!G5GVU,U'$@^_50[qIA}7'`Mi[e,PgY!+e4n~_y#}Unko4i_JC%Z[=^nt+Kq"
        if data[s1:e1] == "}":
            output = output + "~<Pn@Dzb.` eh6L,wrqU>O<cP+ pP8TD^fA=%XICya&`Sb[FyS@52gmPJu04,J0c"
        if data[s1:e1] == ":":
            output = output + "!1=$QR1q6]Y+%i(Qc7nTyK&hQs$%/r*KQ=_?_#r`k&'1!RQ8uN&/&rc4G@39a7Z'"
        if data[s1:e1] == "'":
            output = output + "[ggX,G~yTI57 :<CR<botpMaQSxCpjLzxi!j>`g3fB!DE=1k_?k`KVX,Z0ceDlX("
        if data[s1:e1] == "@":
            output = output + "uxUH) ZP6`^QcXR4?vhkQl7]ZT_sumi~.>~HbD5,O`nKCU,3+y@:8Pv..eKn*zc:"
        if data[s1:e1] == "#":
            output = output + "=7au 5'l&Ube!#$ )QVa=8k3ipD*T2>6o>&>wi/D.5<8d#kxLc:'~HB4=d7@bC&O"
        if data[s1:e1] == "~":
            output = output + "O~.m>SBq:dd!sZ#{vs.72q(vYyLU-rkj,lX}P7~]}6F<J,XFNi_/K3U~D?ln.6Z "
        if data[s1:e1] == "/":
            output = output + "`xS3fw.2-auf6aun^9DRtbb=sx>,^J(Zm8(13>}_[q?(~vw>[Nn~q#xNj)H.s1(E"
        if data[s1:e1] == "?":
            output = output + ")tU^{p'@$bi}y]V%[IaS{GE-vqo:5bzdyV:#CT[ep&zr`.J[96Z+FZJ+!?a:dN#7"
        if data[s1:e1] == ".":
            output = output + "-waD^'3N7Qc_iN:EvGWj&l%)Bo3.^T%''(}h{hkK[m]`0-0~=)Lm7Qi Be_Eg }4"
        if data[s1:e1] == ">":
            output = output + "9KXo+G$MW}$fx__2?HN<p3,EpFm/xy#r@Ls.EQ5~@v+AV('o}V#}O8j}bR@+-u b"
        if data[s1:e1] == ",":
            output = output + "A*J5CB%p3'IINaEBu4_2[E-(9eyQRhoNO{n'>J-&%CY?Pl=V@$+BLP9Q&H0dve53"
        if data[s1:e1] == "<":
            output = output + "(ed_O ykWt4NG4PCAMDc&*z%fyAJp-gD@6}J2xS/[8UN[MzZCL#0mj],G?SM:fg{"
        if data[s1:e1] == " ":
            output = output + "gM1Gu8mLO79L4gdyVY7CK{9[zK]]~0tL73dLK}?/87SNy:m$-JPFNbswz nENqb7"
        s1 = s1 + 1
        e1 = e1 + 1
        c1 = c1 + 1
        if data[s1:e1] == "a":
            output = output + "Mg[ZIq(]-Sn!m3MNCNg^tL:)w8i(0U[ZNF0y_wkm/59'J:F~vBakr`:x-Su(e:%f"
        if data[s1:e1] == "b":
            output = output + "$'%]tpjm ?R{Vf#4o7~k)@tD&k/=8I#H}ENT6^#A8?sDiWI{ld'qvIhNr96~$k_&"
        if data[s1:e1] == "c":
            output = output + "nQiI_+[hLYg}'b+DcS't6O6L[g~1JiV8H'vb:>5)fBd7!iUZ)j3$f^'Z@}nxm4$p"
        if data[s1:e1] == "d":
            output = output + "fjMwo$lob(-y%4>2g[?-ktpziL9JP<DE0Z'M2k)Jql0%zE9_l)]2_0c6$2]d$4LG"
        if data[s1:e1] == "e":
            output = output + "r>-<RJmESr {S4VT,jlf)@E>h.Cc@$F{O9'm<yThy^b'S[X5Ybyt~<<E3bm][]'x"
        if data[s1:e1] == "f":
            output = output + "v==ZN)@kJiHP62+7E0sos.1%N.YO1,q8Tio:w[%rt[C~awcDqg-&tk!G)sjp&8uD"
        if data[s1:e1] == "g":
            output = output + "(Bxp+qTdGgrU<d87*mB<QRP,L@vV+k.u1x_jHds5kiM_^^96S<3?2Vld+Q6UMe>:"
        if data[s1:e1] == "h":
            output = output + "fgxFlJ#sdVZrQ8kB(->:sem#wd}eMP1_Fn:*i?P+Q(c>Aq2wg)8}'j'<5kHc[WxR"
        if data[s1:e1] == "i":
            output = output + "But}YBgtB*xoXr/VAV9~?rto76.l5G:R77QU?2z,7/?>g~ nk[Sge+menZ-$^{F,"
        if data[s1:e1] == "j":
            output = output + "Si`S`&%B>NAID[u4lad5AL%:.!v<[t-4 7?*Jvb42M{_+(3CQ>#Xg'I^AI$*ymN`"
        if data[s1:e1] == "k":
            output = output + "-HiHvs{`pR%Cq2{QC9{l)'6'{(olGcG$9XsF8,]5MOX($yi8'}Q&oE8`>e]fqrmc"
        if data[s1:e1] == "l":
            output = output + "#defBYmBB97(E0:Ct-t5B1?rcy.wD,~czb^asR$',Xf<<jGUt5_7Z6~fEs-5C~66"
        if data[s1:e1] == "m":
            output = output + "IjxZuH@7T,,$3K4~]#F4h0c5?X6zXK=Vm AGNTwlV*L`jNLcdz21g&5LpXg#Y4-1"
        if data[s1:e1] == "n":
            output = output + "p:u0KWHGzG,h3u7xdMWG]5{j&'`W}V-6{fiP.au97+kvw?/rfrpw3yU?3m0UV?<h"
        if data[s1:e1] == "o":
            output = output + " +^Oq@Xp?yz~ ii]O'{Xp`xqW>OMQwPUU7Lt?*+7NZQP0%0,74?Z^b=@>i.9/H78"
        if data[s1:e1] == "p":
            output = output + "%y'XFGM=Y9d:S7{^r&u(+$lLsF1WcUKOj--CE23oT&6rz5wa^0!`v9RoS?)&^tUS"
        if data[s1:e1] == "q":
            output = output + "fTm>E>zS%w9wrz*c_A8b>'nys8>F+x~[H!dn%{%a#a3%i Nxrn_80a`D%0(%NZRE"
        if data[s1:e1] == "r":
            output = output + "0AK'aJH>}c,e:,DO*wD9'dfY&(nCcnH^JOp~n[!4jPC8qFXXj)[[(K<Rg['zYD*X"
        if data[s1:e1] == "s":
            output = output + "Z,mgbZ#wLe2Q#t=zOAhBN'?7Mp~`~c'l#S@b~+!T^<Y++J-0yt(< ,-NkZh&nFDC"
        if data[s1:e1] == "t":
            output = output + "Vk>sLR>&6(2I~AS1r89W-^tG?cT!bC~at:0`q`O'fF ''9MG`hjUD<XDb'nDAA?j"
        if data[s1:e1] == "u":
            output = output + "+yFaOxu7q,_[.P3 P=G8ewlTcM+GH4'T&[ BA!Pb#MZH7! !:OMPh[6l*dkM'Bvs"
        if data[s1:e1] == "v":
            output = output + "gn{[C=''p3KJ=omwyA^a#e8T{QYnfZ-B^cI.Rj93RnkL]'g9isL1qg =JIWALe=A"
        if data[s1:e1] == "w":
            output = output + "KppBL1Tk6k_No^t%F^d[)}XLVY',9dtBIO/+ys.5F?ge rkI0p,681^4<n'}2[T["
        if data[s1:e1] == "x":
            output = output + "^y .{y0&5M-I<AE~GFRpca8cEul$Jobh'oAIS1USyurU~tC`'^^ 8%ygg4UH#S5A"
        if data[s1:e1] == "y":
            output = output + "CQ1DlFgI)raD=n7zK&jQ9l pHV[?J3tk*k:ZK}zz1sF+q'#?0/ n@OeyvK!L0A$S"
        if data[s1:e1] == "z":
            output = output + "pN{CzfT*`P<,ENy8.ZwT<EF_3L!]wC!6H3yVcPI+R3b.rjX*D?>0??a![WEZTvA("
        if data[s1:e1] == "A":
            output = output + "}HOu*z]WG/Y@p08B 6U62V~qa`CSaK)YlQTG{kX40+kYdWe0//2HZTI0`qj:}P+M"
        if data[s1:e1] == "B":
            output = output + "&i6]X4Z pH(Z{cRACG2)-fJ_8W~}9W[%+eM1v1sd8@uwbl-J$1_NT*y@op&_anWx"
        if data[s1:e1] == "C":
            output = output + ",txK=[atKV0%f#NG9/(/$eta>.#'&[P$zPPesb?t7Sg&/ /zDQ+JbM$,'16,,<9K"
        if data[s1:e1] == "D":
            output = output + "8r`'Jyu2&kxYb`f>e,1<S$:hM~LWAleQ4dQjHWQmi,mu:V*y6M{M[&iJO<%oCU:&"
        if data[s1:e1] == "E":
            output = output + "mGaJ*oCe Kc=6*:&Eu3g1AE'1jKz3$MtQ%rw~mD#i%N</RgtUB8OsO<TIk`Npvns"
        if data[s1:e1] == "F":
            output = output + "FBHk6uMCQdBZhI)<KturL5_B#boAJ@WC0%  y4$~{]RLNs3rZoexf5$%27=>`wmQ"
        if data[s1:e1] == "G":
            output = output + "K!FY}hoPvINn(2A'nC5&avL]76sC)wVxt@Wz}i@c#j:/P*C3vb:7xA]rQ]i7g)Tx"
        if data[s1:e1] == "H":
            output = output + "4?< /SNoU5jyY#!kolFx):ve/({'aJ^ygnDUWlCD19UH=*H``'oG.}@k[zxZnb.L"
        if data[s1:e1] == "I":
            output = output + "PN1xSK(h-V1(5@K)1#[Yl+}]>c':%[%EcN>*d0z8j_6w}5bg&bUV2Bg_hTh0K}=U"
        if data[s1:e1] == "J":
            output = output + "42>)I#2$r~]{BVR%cz],zXbv`vDp08n:mM3:wN}PkS]jRf~B3I?1f2s~g+mz4+iq"
        if data[s1:e1] == "K":
            output = output + "qGo?)od1lWrxW5^UnU3l&dbz3,/(V2=NSDED[}2fm}WM,g[-V7F2m?d<-9wkc'uB"
        if data[s1:e1] == "L":
            output = output + "N^Cr~wzZjCNsnY<0g!/{'n/K&u_XLOF5FI:4_^cd3ll`P0.9~I)T1UFEL4 PhK#y"
        if data[s1:e1] == "M":
            output = output + "YFU%'R+W?3LoTk?bx)0!uHJn*BZK/7.{22To}3:PD=1q9(}S,23hd (L<ZmV4%-U"
        if data[s1:e1] == "N":
            output = output + "ICPG&BL~d/bu0*n-~wNgXDZ,PyFL[)i,=Uc@>}-^lcn00R^}KLS)&me&g@y8Vs7/"
        if data[s1:e1] == "O":
            output = output + "*H)bQDxZ-,0 3Sf9Gh^q0Mgzylc,M~W#g<sT1Ww'K8<<C*i,d*rVm>yexl-WJj<7"
        if data[s1:e1] == "P":
            output = output + "HtcG=ioKu'@m,tgQ%zy'eRA!Jew.8fuvtQ@}(v4MSFcznrQQ#!-W$)Uvn fTOF0v"
        if data[s1:e1] == "Q":
            output = output + "/W#57g&<=.l*PhK=^XQ:>UXf,WmF(uXKDG>q3b#Lb>E$md{~3d?gOmog}e+*9wMX"
        if data[s1:e1] == "R":
            output = output + "'yzN!%y>3klYQ&wV)=!M^Z)`OlcGP7@2br_Grp{pxni7?v^#KFAC}3xV/,d1AtCl"
        if data[s1:e1] == "S":
            output = output + "3yCitEi^@@Fd#RW}Ram_&dfu>*]+Gj'~v'r&UqvpC<NSU:ON1A&Yum=+l`.Fvb0("
        if data[s1:e1] == "T":
            output = output + ":f'b/lzzAVeC&U:7.&4_Djy/Y:EY/x.)5MP!sWb$<n/ =4<@_7yCjID],2w<,wVS"
        if data[s1:e1] == "U":
            output = output + "h7(iQho)[UmN<A~WHQk6s's'I-3h_=h{!P14{d_mbc%~N(Dz]H[MQa[K'Zf!D*lY"
        if data[s1:e1] == "V":
            output = output + "a$PLt!i=7>qdBIsH8Xf2f--*67>`n+X's7!O/*oe`ev{Fk ofC9+MQSR/Z^=@j@E"
        if data[s1:e1] == "W":
            output = output + "PlISi_98k^v4Tv]puXv66J!Gn}]l4WFg^kZ.N/dhur1<$I)MKhyV)BKuEdJJss%Q"
        if data[s1:e1] == "X":
            output = output + "a~pP~1OMg)-RUaH-o]QmhsOGB,T{FXHRV9*,e.DXQJ2YTdX x>{2C!QIDVDi'}}G"
        if data[s1:e1] == "Y":
            output = output + "e2}o$76 >zwy'Qe!LpBj(LtzKxN596SD. S/Iu['6fGaR'#tUXhw_aKM.K^v'-z#"
        if data[s1:e1] == "Z":
            output = output + "ve!r:'!?}:pT&OL!4'FP,I/%gWvz1$:zB-gKCOh5$Kn#A%x7tr/oF2.a]yN32Ed7"
        if data[s1:e1] == "1":
            output = output + "6B )o~ca&X3X'6K8 9}hW}%gAiy8y+O06G23`ViHG>3)QKZ`<bdi4I%9m.)$V&e4"
        if data[s1:e1] == "2":
            output = output + "YEEN>Vvd)VN{~ZEZuisgV}0?*qQ=iS-U-RI-(#fJM`{l*Yhx!Jw?l8+}a()b.k`L"
        if data[s1:e1] == "3":
            output = output + "5E/a[{thJ:=4YZ'_s[=j(mWRGxEB4__]Mk0d#^:!]k`9/ipXBm{OW$1VC$8y2TSD"
        if data[s1:e1] == "4":
            output = output + "6x.(y W%8_^ub$jy3Ia/oWi}*RF3Q 5h%VD~mZ-Ybwg~'.@oS@'FUpb:RC][:*c#"
        if data[s1:e1] == "5":
            output = output + "x_g8s(`Xq]]lB['1bx'WzUHqY^ `z+krgr0)V)3=xa9uKsRnO$i$+XkedW{oVF&#"
        if data[s1:e1] == "6":
            output = output + "izay'ikjo9=/R<hXXH4#N{nU}Tt@~w#Jn{T5^ETH9Q%NG:WU<:c@w44e>CAn=GqD"
        if data[s1:e1] == "7":
            output = output + "+q ,bPYu:U -eqrp'5oP?Q.RE=E5fCwH5p5/66SFS*kh3ri`rXwj,1=y?HK^'a=H"
        if data[s1:e1] == "8":
            output = output + "(v_'}{Ej'JTn'''a)2(><P+Im5+<*]aRPPk GVx:.1x::n.Z/cm`M$`~uLoI7s<)"
        if data[s1:e1] == "9":
            output = output + "S}'J'O:h(J>/-Se9 jsNU[D'7-pKtSfxs{^xc* y_l3@_/~:gRI8@z)}YtJD%.+J"
        if data[s1:e1] == "0":
            output = output + "O77X~g^5$cq]qHB$$.xK.Wq8j[1'tuUOAWqFP@Vn=izEG+8Wkx+BCI{v>2zlBto]"
        if data[s1:e1] == "`":
            output = output + "+jUqIEcR9($MlO_<?P`uJ09Sv@Uoe>ZXI%DNUBJ1@OuOJQj=+VJ5k))Cu>G9LhEr"
        if data[s1:e1] == "!":
            output = output + "-z[%nl1Pp?.Z}'V%:}`d2#wsTT!TrZzqFR3-2jL{?J@$Cd]=u*OEW='#IL36wGj4"
        if data[s1:e1] == "'":
            output = output + "Q*G+vv!'D5}QT_3'3'R8=(9P'V>yDlG''p2-b(uME.,BqLR)j3)u}tO3mD^HNlTB"
        if data[s1:e1] == "$":
            output = output + "3]JEWa=ZeA#8WG%L?>uDGa}uJkHR5b<<9kN:0ObX/pu(6i!MEj.evr/S[P+(bcRt"
        if data[s1:e1] == "%":
            output = output + "zYUZ2?[3`+Yhi_' t[V*)-ueW^!N1j'6~7x8ANh_iVfa7@<m>rRC+*$0zD5MsSkP"
        if data[s1:e1] == "^":
            output = output + "SR>'1jhC$,mgnJTC'.5=OB~GfKFyN7a!Cq5tB&WPF_+su=s+ARB:*o__&6#GT/5T"
        if data[s1:e1] == "&":
            output = output + "-i41'*zE}Mm^Rz([9@JI7K?ovkP.=ucH#ywvELbrat_7OpEj6Sr]h]w,MKX%G4py"
        if data[s1:e1] == "*":
            output = output + "cLEf`gQB?v!%W!$z6lRs9(.bM<%Q7AA`Vqm**Q!avT956Z~n-tAj$NvA>.`~FY(v"
        if data[s1:e1] == "(":
            output = output + "?`-6=R~]x@IAIrV 0AKEtM1lfaOg,^ta)4^w:b/=8HM/1tk?1J6#q=oH$n]HGhN*"
        if data[s1:e1] == ")":
            output = output + ".EpN%Tx]TM1aMOEvd7&=<'s_2e1>U^Hl.i?'hp1n}f3DK{BL]pb5na9t'alcDUyA"
        if data[s1:e1] == "_":
            output = output + "7DMZXSaK.d5Ne61KRnIQ_i}:*YXXqUP&xq4~Lg?{o,.WVO7HpmJ!rUY0UVA2`q#k"
        if data[s1:e1] == "+":
            output = output + "v22 /(RfW)Y47JpA>hYbIy+ru^pX5z=G21P}bI'9EeIFz`k#aGGDiwqZ'$~+i@?X"
        if data[s1:e1] == "-":
            output = output + "Ie$%Fo!]rHi&@bLXk*5e(xuKDf&Jn8uWF/>)'>tsHY`M:#vy4C6c*h}s@'-o8]K#"
        if data[s1:e1] == "=":
            output = output + "@PQ{R.'`{_2!'^J,hr4iug#-@JBx$I3llI.[==Z Nn](X>cYbMxwwBe^d&.OyoRY"
        if data[s1:e1] == "{":
            output = output + "Lc4@YVpo3Z(eTi_A'6,BI+@!fhsVh8$&mXv&c_Zj'Ld-*+[KJ! ,OaHG?[H}Of,I"
        if data[s1:e1] == "[":
            output = output + "ZJN#e(O,!N@euWlxYmF2iQ08FcPBV{<}1_O)Ov#*]+(q13Tv^0edrzYsvf.(P=2$"
        if data[s1:e1] == "]":
            output = output + "9Hp6w^dG0i(=pTQmfJc3lhq8#]O6@Tph$jMh! YscC?$*x*6O2{<R54SYO}-ZHz$"
        if data[s1:e1] == "}":
            output = output + "UL2D#97,c<mwaeBqX!0Q`5gIfms%yx@!1*tLWYq?nVz~E]vhEc*4!!c$&0wDVS`]"
        if data[s1:e1] == ":":
            output = output + "SX5f5'YGJmsy?X!w .+=-9%E~A~E`# du<CR6%+_,PYpq2'mRRrC+.Fhf/) Axb_"
        if data[s1:e1] == "'":
            output = output + "fNz(Gock_j>Sz@=<a-*cM^'XJp6>Gv,@/YZP@,rBX%fV['3YlEOPUfI@O#t~qAaY"
        if data[s1:e1] == "@":
            output = output + "Lh8*!wd{8oIR pW9]H=4s4S_/$`pDkN8s>JQ_Mh.-'F/serT)HAm!$ K_V}-SuHY"
        if data[s1:e1] == "#":
            output = output + "wn5{?j0{xWoTZMZ~^+zk'}5FmSWS>lTug4n`GKNt0 @{?ELj3I*l&kq7QDfsp4C&"
        if data[s1:e1] == "~":
            output = output + "L>~d]dXAHKkYv=1S'a<599Xa.[JU/!/M[XoWD]GHEP!]8VTo.Eq5/M,r@,#@V<KG"
        if data[s1:e1] == "/":
            output = output + ")e(f:ZIk4Dj]8jz7UI [`t[`^w4PUaAoBvBYj.Fnb+&fy'qfySS5Tx&:w?TAJ<q-"
        if data[s1:e1] == "?":
            output = output + "1eYCOBltQ2A-DILDO`B#Ac5.Lxad^BQ&jR:Ch'Fz?7)m?Eqophqw,/FCj:ZQXX _"
        if data[s1:e1] == ".":
            output = output + "%`4?[4Db%v4j}W@U6YYFj%T#KK'oZRd uY:eEeu2{l6A]g3i{rehP])+E@$ T!qs"
        if data[s1:e1] == ">":
            output = output + "ML]_3FSAHN^8fgbLmxr%jfS~9O@6,=104T0,/sPi=ZwL'WU>%J&-6]cbq8'qReFD"
        if data[s1:e1] == ",":
            output = output + "O?lL(Pp.4)rfc1o80/TB%'pq&hLh)'Uvd<!2u#^R599x8dKsx#o&N5_{.(jqm3[&"
        if data[s1:e1] == "<":
            output = output + "('``'W9{~2<xr_PBeg{A%:kZKC*Y94u1Cr>b%nu)wAp57d[{ ]CRpbvKnwH/9aB/"
        if data[s1:e1] == " ":
            output = output + "`dC4QhU{0#{PG0]}QpqJ2Q f{_@0hgq}nOsY(m$ov&[(=>O :y8H!*7&2HapZ@in"
        s1 = s1 + 1
        e1 = e1 + 1
        c1 = c1 + 1
        if data[s1:e1] == "a":
            output = output + "]d)c!$YLlX)kX:<u7/G>4<Q!]`#Arh0&xi^HZ9X:xkF~+Dpq0VsKqlh-}Pa1 uu^"
        if data[s1:e1] == "b":
            output = output + "D4u',-hHa4YW)_v=qiW+(M,JYw5kCKX,]8gKVfSL3B[=YxNuRJ2&=FATRK$QuE0n"
        if data[s1:e1] == "c":
            output = output + "6kHUN21Sj&YyQ~05e#4:{U+K&Vt i.*((_2EkmyjEV*!bFM=:FI6 $5~PbS]r,2%"
        if data[s1:e1] == "d":
            output = output + "Mmb`BA.sQ'3,trXg[D]mF3AIDa'pca'TkPdx$x{1S/0<EJjO,<RIpa<C2>gC:!9("
        if data[s1:e1] == "e":
            output = output + "`WyywsSWc'`3&g$b$r<GX%L9d`g8>m<I]iSgBbTo%~vfYBAP7cfu4SN{O+$Z.@cE"
        if data[s1:e1] == "f":
            output = output + "MM8B)-[.$BMm#J(Iqy*?/ISYg#G{a,?mV)-zcnO-XV)N0_sp'OP~^Q@&}<?%!'UI"
        if data[s1:e1] == "g":
            output = output + " o k##X[gv~S<_?YYlb@Kq=pR{`~3hkOF:bHYzjnH]dafjs^obf?,v~N,F+_9mpd"
        if data[s1:e1] == "h":
            output = output + "O]K+eQSC)m7nv4Ko=2Y(k'Cu{0d^N !LnO5.4^='VLvQjXsWKz'bv 7~}MGkl_M'"
        if data[s1:e1] == "i":
            output = output + "x~h5F3o?sH[iI<DDin~y(9{G8L?[h.]*q5's=WeR$fZ4dZ$UXL(m8-^/l@&'6k7S"
        if data[s1:e1] == "j":
            output = output + "nx'U%-^&fwT5URIFnjA^r+5)X!5AyN%V:iHX'%-T{Ol5:lTaMTmxWDT!S`yDO0kW"
        if data[s1:e1] == "k":
            output = output + "[/xw7eK6ERz_wj&%Vop)B.WYvoA(/CpqtflYr4d[K99OK.cF@&G6GK9A}o8JO+_,"
        if data[s1:e1] == "l":
            output = output + "GP[Q,Zrx2eZK}uf0JZHMe3::x5piZVB%M@FWT`WI>oJhnFs@e,_Inhu2A#=fl=^h"
        if data[s1:e1] == "m":
            output = output + "u[YOImxVTG~5 &!*1?R50bVWsvQT`W=_Jf~0MXI1 ldyrB7'E#hJLF.g_{Po?P6]"
        if data[s1:e1] == "n":
            output = output + "9m5}pl)Sk^G/+48@k2-b=+opCCm]nCF`lyl/j2%5(/Nc2}az'*B1$EJ$DA +X?4U"
        if data[s1:e1] == "o":
            output = output + "]-D?`(XE7b8HP_MP3B+7@Kt<e%_-4%:mgb7<)EjDUX G#{z2'OE]Wk*.`}Yr5BAA"
        if data[s1:e1] == "p":
            output = output + "AmM xa'~b:/RZL1]8ROV`<I1((YpaL[8*v#mN^bSA:}bEo:iT^{H**)B$lUF.KRI"
        if data[s1:e1] == "q":
            output = output + "cl8MUPa9qlQwI$Zx^?D3MEz`z'9T7[MnU[:`^JT3JU`wbMcC5~{'Yd7`DxDSL*DG"
        if data[s1:e1] == "r":
            output = output + "li'(F5f-s',_kV#?5hg$>_l:c3F1jhM$ai^RG>vZB6&j3+0I'X5j4l@}9&aHhp^f"
        if data[s1:e1] == "s":
            output = output + "@5d:*88~^'QSF9PaJ1kV1dG#UF.>B5o%]Vu`2LZ1UI>U[9k0`&UKJZ+TI=G2T6OO"
        if data[s1:e1] == "t":
            output = output + "m!GV{:L,<=+<#mw_,94e=}E8PT:b-V&p72Zr4RMz0:/!P0mrGCBE+0/sHJ-6-K1d"
        if data[s1:e1] == "u":
            output = output + "!9]y]zF%W??KwDm:Uf}>Dh)>_{KEV+3qrYVk2~T%]eivCiTv?oS!4.<$0}K:l&6Q"
        if data[s1:e1] == "v":
            output = output + "ODdP6@GSx.:IXth_cqahE1}bv@701^2i 2gj'vdMz#THSmN:Pvoeubr,6wrR@v.v"
        if data[s1:e1] == "w":
            output = output + "Ec0L5ht/Flewx&'1D8Ala7v&^yO%W_TzDp?)Mz((l_i~`*(!gYcj~}#4 H+ys!['"
        if data[s1:e1] == "x":
            output = output + "'Ct33.*B<be9))q^-GzZqXB/p'~(j%]d'/oWn2xF/,Wo>y8Id{4m?Dc~(]}tKwj?"
        if data[s1:e1] == "y":
            output = output + "/RrU~d]&iiCfA:M`IYr@AeTtddKE.UkG*7C<PN+U!^u&RKQ@WA*P_SrK>]{<MG{="
        if data[s1:e1] == "z":
            output = output + "Rl0=%5B)h{l!wJzu.UQBl3Ue/]B}k wKOJ*AKVJm*~Rk]A*:BrgCIySw_e1&Ou[#"
        if data[s1:e1] == "A":
            output = output + "GbEGxy9uS=v~m}TPYzp$1{!t$#o2s%}pjhQWHun,I/y-*# r[74Hc!y%/iB6IP e"
        if data[s1:e1] == "B":
            output = output + "3N={D<%$9Xs)7iu~K!eA}'~j.cv=%PZ>-8%,[8ut4-J&7T D['7IK!jUGK.'`GO="
        if data[s1:e1] == "C":
            output = output + "+q?No<Qy#}6elN#6n1'2Am5zwd5r6e6yV.=X'[dv`wBc0wL_{qFZ`MN(RC50$Ke("
        if data[s1:e1] == "D":
            output = output + "x/ST#G6Art?Dn57=czC^tbQDi>je3CoE2-j7ceC8O K't=P9F>xm&JM#c=7526C)"
        if data[s1:e1] == "E":
            output = output + "[N~CTh^s#0?.Z%KCGV)jwq3{kc/^5z&1%>1(lYg$m ?(Tsrcx^$W4cM~@a5tugdj"
        if data[s1:e1] == "F":
            output = output + "1^!8Pw+k~gS,^PQdBB~`UE<<b7_qly,o{v]NuI(%4g@a[1OgGWD2f~?>4OmAS/qk"
        if data[s1:e1] == "G":
            output = output + "*x*vcwxc 9Etsas4)&2IVjZXZk6W'tq2zcoblyd}H'8w8(x&E-HnN3CZWT8v@)qn"
        if data[s1:e1] == "H":
            output = output + "]C[''Lh'g/#Sn2Dr@=TVFlax'){uGP( 5h??+-'*Lqs~cdq9gao%pI@Ouu+=L,,d"
        if data[s1:e1] == "I":
            output = output + "_1'hD1q=bTTlH7)v[z`Rc&]P)a4 T'BlDVGhIb3dy^4Ar9/=Z0y4JMI'5s:@'U^z"
        if data[s1:e1] == "J":
            output = output + "@xG7Z}}*wT>g@+MX}?G`Z0^JA5g]}qr7z7Hag6Bqn+`Ep3ymka_gW1=7<M*pzp6%"
        if data[s1:e1] == "K":
            output = output + "@RW.j#!*N3)! 8NP-{4_'[L`h[{HP=$:BboGk 6+m/wweAS_d:%-bfv?g~@}HDr!"
        if data[s1:e1] == "L":
            output = output + "SPuE&X[+N25sza&g J#'am}?I@VB~*h2-}50~>bdU8HX?'S}B.{yO.9YC&)ngY1y"
        if data[s1:e1] == "M":
            output = output + "D)550&<@s3hx=.E<&#]{MeHfy~<9Qf]yl>EQWTx>Z_o3gHs{L~w>Sxw57TWGMoB$"
        if data[s1:e1] == "N":
            output = output + "iG]NMfe',<#h5cpC)Q71b} -.x/= NjX}zs%('Q<fHMKOTge8L{iINFNt%YNxXOw"
        if data[s1:e1] == "O":
            output = output + "~'Kntn+Nb`B'895mBzZ&)h1(>mJyZUK?qjpN]rlW)euC^m@AOt^3jyE>qC(Tse''"
        if data[s1:e1] == "P":
            output = output + "0/8 GoNUH+3Fp~!R9?:`HEu?:UWAzD>E?UchJ.Z/IxmV(#z)*os'eg!x!$IxXW:X"
        if data[s1:e1] == "Q":
            output = output + "XN'Nj@ZC$kF'd.-pa-k8Sv8oDH4C6aWEZSz#~28Fd_Di0LDWzViXiz%0@rcNX2@-"
        if data[s1:e1] == "R":
            output = output + "7-E-_Wv4>T<yXQjGN}Qq(Y&nsm~'sa' _hwn[KVY0lH0RD}vY<yKp4W}fi~3XoQ6"
        if data[s1:e1] == "S":
            output = output + "AY$ti)m]uQ,]kLA>9'6v'zFfA`(RFw*RPGW0v0=LB3p(6?JNoSJj{GM7S`f-a?7>"
        if data[s1:e1] == "T":
            output = output + "^?})aj}rejlrqPf&-fkYfE{FHJOj>y_BFkJH(Pc'dr.4J[}f]B-!wtRvQY0,tvvd"
        if data[s1:e1] == "U":
            output = output + "C@_TkNZ,~VDQe:LlXcv[.+5I4GWPj:q@8seSQISFE!&knG+%y9F_:70rvAZV'g.l"
        if data[s1:e1] == "V":
            output = output + "'h~,eDmY[e#A#=C#M{4f0 I2?Wot%CL~Z1>GzE19v1%`]S%sOI2?oklM][vwp-`A"
        if data[s1:e1] == "W":
            output = output + "tH(@R.)8,I*g`OVfWA%{2'4d>5^<<X.<=9>(tp'/&!NgGo}b(f,}amnE734Kt6&S"
        if data[s1:e1] == "X":
            output = output + "9oLdtPgZO{VB5 v]3vR}$f!'4(Oy}F32cO)LwP2T5(l4y6DRhM{SMs,VV{,kAAb~"
        if data[s1:e1] == "Y":
            output = output + "(gmWyFx{xtR ya XK]az'O~Aj4tf]s1=Liabb76ff'27H'ol!d7Q-p_o,eu']}:~"
        if data[s1:e1] == "Z":
            output = output + "!YHEMTj#{^stna1sq-K)*?vw@n~^K- {hGlifF*#1qF.yAgWDeQ$~Hw{,Qq>w$3g"
        if data[s1:e1] == "1":
            output = output + "Oc kt7^'Xje3)AD`S{_1Q@W#fW<i11=0-p2B=G&RAs.>)i-pVc0vJK2 69B5A{y6"
        if data[s1:e1] == "2":
            output = output + "Sq~D1]hzjQj: {Oo.8AhilY1`>N,t9p.t],2jF'[Ys]W~L E-=*i ,o9aX4Jn?s."
        if data[s1:e1] == "3":
            output = output + "rX=nLSCI)5cCXIxh?Y[)3LK)}C!7gr>8.d-YtBq-KY5RviOpd`*L3Wi+t:>pJeW$"
        if data[s1:e1] == "4":
            output = output + "l#.MUz3dL>T!!JQE'T`poHtzPYj_VnFj%fWZps+R[P HXWF}k->HWMAM2pbQa6kZ"
        if data[s1:e1] == "5":
            output = output + "c0%QF[j,`~{+3A q<e:N>PSa?k}@[xu4zzed yr_&Z/W]f#?:OM*{zQJn'G=c6KJ"
        if data[s1:e1] == "6":
            output = output + "fGhSEJz5irQl#X<dOU^d/o/fBE5=<.6.[{v@`ue3&9.J^6wce:x4g$4k1K4E0NEq"
        if data[s1:e1] == "7":
            output = output + "xjpH,iDbI8T!iC<^g'ttfe'ELyTq$}K#m00ggY6%}H!no_{rxh8'6x2{_X*/P!vj"
        if data[s1:e1] == "8":
            output = output + "rLi_V&LVJ&W[-2'M$b083D_c***zqDhPJaprqg'#wbhwImj7A3Hv5<]sq1n+%5fM"
        if data[s1:e1] == "9":
            output = output + "*e*pU*HTZg%18q8++RYgl3tt'ZSQ3%*8IU%3*QR6,Z,R.Qb}S,BO^f4!Q-^L77/ "
        if data[s1:e1] == "0":
            output = output + "E/@OucGK:C'Z@$'@L(=T9Q6+qe(&= z:i/{7>$Hor=n`bi}!~wa{Y^=0.6u'/MZ1"
        if data[s1:e1] == "`":
            output = output + "[$U=,wYh)PH[6:_/FpPA9dYl$OR}i&^R'e!u'Vcjd8s3Zi/v>Z1?`:F$6rmb&u6g"
        if data[s1:e1] == "!":
            output = output + "21*,(Ctp%,h7,Lud--/=}5vEqYL:TuPxJkjM{0({9PPd@6E:h]]9'V-n,@D+~7iO"
        if data[s1:e1] == "'":
            output = output + "+$CJ#klTMd7-P!n#mZvu5_:j}os^$,9XnP(G=&?'YgN$k['!khb92N'1'P0s4`nu"
        if data[s1:e1] == "$":
            output = output + "n`r@R<m4Ayyv6Urbyw@AY[]+lj6=okhUs3 IAeF0u3S>0nR'FJEn*8'=v-0m]{69"
        if data[s1:e1] == "%":
            output = output + "8`mDdxzhk<.+dDLU9dAhrZ',x3U_xJ%Nd=MVSaSk!f#.oQ/fmEbLDurZ@2WhDJUF"
        if data[s1:e1] == "^":
            output = output + "8QCFR0CZ!Q wtryL?YO=ff^L&=qKKJHu uVO=*@ZT{*oUfesO&`GR+r'bZl4RP!T"
        if data[s1:e1] == "&":
            output = output + "w@sGsU1p$`PZ Oe&LV6b5-hY,oY?D[l-yta*syNa'xl uG'cGz#6'.JO?J aE!68"
        if data[s1:e1] == "*":
            output = output + "<<$p^*PlJnPV2MLm*LL=}Ts1n$o/m3RZoN4D9B[yH8mMa&4.mo)qpn{O_cWrRfqZ"
        if data[s1:e1] == "(":
            output = output + "X_^_/IUy9V)#n3u z:(+? f>sT3vT]0%`!XmGG7=!o%&^J0G)NH9<9FkaAsU<z#C"
        if data[s1:e1] == ")":
            output = output + "/Nrcqc3U~/xueIn/Ux@gGI)Oiq[>27 ~#vQug^KJECV$41IR%ZNdU{]]&W*QKJ$b"
        if data[s1:e1] == "_":
            output = output + "(yJeNS@(7bZW(JR=YK]kI1UX(_j&7YD2$b<.&#/I^W1v<1>(809fN<*Qi%utV>[ "
        if data[s1:e1] == "+":
            output = output + "wBSr)NU-e=U9)LcpcO}3)rRN)Lh'nV`d3*r0Q*C/x%@%WCI~$#:7V8g!n89CR+)j"
        if data[s1:e1] == "-":
            output = output + "Og6sE+'b>xDksDOi^GXz<sXU8R]gI#A_<S 4BJ+#G+qYS'RzE2SLq*~LHUk_^pr+"
        if data[s1:e1] == "=":
            output = output + "%yIa>N7}@2gwO#GRo.q$x$4o>Jq]<VP(#v'Fb.u?^8la[nfX>SXi(nQSFt<ZUPK`"
        if data[s1:e1] == "{":
            output = output + "<'kby+CAhd{[#p4&'VqN*VBt[pc1JDa'l?r6_-b]>'ivD: capJQ:2HA:c:}xoRI"
        if data[s1:e1] == "[":
            output = output + "TzYW2yzVk?bf5h@-y>?hlqC8OiP4l))_0~C33u'Kp':6SeV<!cw?#1(SxL:4O29J"
        if data[s1:e1] == "]":
            output = output + "BH3BtejC$e7/%udzI`+$lTEpu.Lk4[,gARla@dE(TkO+AT)_Ca?ctzCO0JER,Fy*"
        if data[s1:e1] == "}":
            output = output + "rw%8'9R'L0ib*n(a2}~.b>!S' dT1RP)!d/K{'HTF@CsWQu2*XNS`.~/3kCTBiQ7"
        if data[s1:e1] == ":":
            output = output + "[j`M}[C=t!(8un9lvMzi`#Eb)wvjT:^%OM,6Y(_HmAt8<EVMht92hJ6,)?cgmt8g"
        if data[s1:e1] == "'":
            output = output + "}Bi>n$HHtcubM?ifwRU@OPDne'ao8{'p.15rk%U<9_9o%NaEQq7Mg'7.&qtw/)p("
        if data[s1:e1] == "@":
            output = output + "tK>{YwXv!UCTpFrZa$ LHGQ-JZAa4<-=)P,#0[&/J?t=dp'f:$`$D^Qim]Iwf#OH"
        if data[s1:e1] == "#":
            output = output + "!8:S-jQUW^9ox5&Us&@S 6[NI@wX^'vm%3/+Ko~evD$_Whp[x+BP[fdMk,>xamfq"
        if data[s1:e1] == "~":
            output = output + "fFPs5sFc2vQVyqK+=j8245`9cU!CXB3BfIiBi^B,Y?utcX.tcM8.}@`)* R Nk9I"
        if data[s1:e1] == "/":
            output = output + "[S1On%<iY}g6B^v#y<:>zw!nap]xiC+:>AkN^q<[$FfQwC+/R`Qpmh(YINt#H+wQ"
        if data[s1:e1] == "?":
            output = output + "ynm{)FHaN<'o`*UIt:z-tB?cF!0g'j_j8/.e!5''zND:B#w]&)+?BU'E_(-{q2s4"
        if data[s1:e1] == ".":
            output = output + "#1R,4wJ9rZ8737s6LXG]a5HhqMHf1,Vkh5oxX3q?K`lu(1DXjQ]g[lez'sUuobYh"
        if data[s1:e1] == ">":
            output = output + ",Lei70Ph^iwKZZos)@j/@]F-%dDcLHN!`K:mProiB>Ca8VRZh}Z42YV<bnm$(*&Y"
        if data[s1:e1] == ",":
            output = output + "1/76rp7y sRY,Xn_TK4+nn3W%-h_gnpx/dE9B]_mC0A$DyzfF>7Zx(1cVx@-z9uB"
        if data[s1:e1] == "<":
            output = output + "H0kj@VGF,V~'3 L[UXpbMl5rSAPN1uuwXe+Uy6${,6W#&[ME&wL,G>+0ueLwPtzN"
        if data[s1:e1] == " ":
            output = output + ">/2+y.g6bgWC.?r2[.Fu^Xd*e[!%'z+t_9>R}%`z/Y4Hx2Lr/rsq<6EMI/iqBm$w"
        s1 = s1 + 1
        e1 = e1 + 1
        c1 = c1 + 1
print(output)