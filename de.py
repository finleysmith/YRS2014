#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Jamie
#
# Created:     30/07/2014
# Copyright:   (c) Jamie 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys
insert1 = sys.argv[1]   #data
insert2 = int(sys.argv[2])   #complexity
insert3 = int(sys.argv[3])   #key1  (line1)
insert4 = int(sys.argv[4])   #key2  (line2)
insert5a = sys.argv[5]   #lat
insert5b = sys.argv[6]   #long(line5)
insert6 = int(sys.argv[7])   #key4  (line3)
insert7 = int(sys.argv[8])   #key5  (line4)




insert5a = float(insert5a)
insert5b = float(insert5b)
insert5a = insert5a * 100000
insert5b = insert5b * 100000
insert5a = int(insert5a)
insert5b = int(insert5b)




def check(x):
    temp = str(x)
    if temp[0:1] == "0":
        exit()


check(insert2)
check(insert3)
check(insert4)
check(insert6)
check(insert7)



len1a = len(str(insert5a))
len1b = len(str(insert5b))
if len1a == 7:
    insert5a = "1" + str(insert5a)
if len1a == 6:
    insert5a = "11" + str(insert5a)
if len1b == 7:
    insert5b = "1" + str(insert5b)
if len1b == 6:
    insert5b = "11" + str(insert5b)

insert5 = str(insert5a) + str(insert5b)



data = insert1
leng = insert2
s1 = 0
e1 = 1
c1 = 0
output = ""
l1 = len(data)
if leng == 1:
    while c1 < l1:
        if data[s1:e1] == ">":
            output = output + "a"
        if data[s1:e1] == "D":
            output = output + "b"
        if data[s1:e1] == "F":
            output = output + "c"
        if data[s1:e1] == "`":
            output = output + "d"
        if data[s1:e1] == "c":
            output = output + "e"
        if data[s1:e1] == "%":
            output = output + "f"
        if data[s1:e1] == ")":
            output = output + "g"
        if data[s1:e1] == "9":
            output = output + "h"
        if data[s1:e1] == "P":
            output = output + "i"
        if data[s1:e1] == "]":
            output = output + "j"
        if data[s1:e1] == "U":
            output = output + "k"
        if data[s1:e1] == "u":
            output = output + "l"
        if data[s1:e1] == "t":
            output = output + "m"
        if data[s1:e1] == "O":
            output = output + "n"
        if data[s1:e1] == "+":
            output = output + "o"
        if data[s1:e1] == "h":
            output = output + "p"
        if data[s1:e1] == "f":
            output = output + "q"
        if data[s1:e1] == "L":
            output = output + "r"
        if data[s1:e1] == "Z":
            output = output + "s"
        if data[s1:e1] == "V":
            output = output + "t"
        if data[s1:e1] == "[":
            output = output + "u"
        if data[s1:e1] == "W":
            output = output + "v"
        if data[s1:e1] == "_":
            output = output + "w"
        if data[s1:e1] == "8":
            output = output + "x"
        if data[s1:e1] == "~":
            output = output + "y"
        if data[s1:e1] == "/":
            output = output + "z"
        if data[s1:e1] == ",":
            output = output + "A"
        if data[s1:e1] == "C":
            output = output + "B"
        if data[s1:e1] == "R":
            output = output + "C"
        if data[s1:e1] == "H":
            output = output + "D"
        if data[s1:e1] == "2":
            output = output + "E"
        if data[s1:e1] == "k":
            output = output + "F"
        if data[s1:e1] == "b":
            output = output + "G"
        if data[s1:e1] == "!":
            output = output + "H"
        if data[s1:e1] == "I":
            output = output + "I"
        if data[s1:e1] == "3":
            output = output + "J"
        if data[s1:e1] == "m":
            output = output + "K"
        if data[s1:e1] == "#":
            output = output + "L"
        if data[s1:e1] == "N":
            output = output + "M"
        if data[s1:e1] == "X":
            output = output + "N"
        if data[s1:e1] == "r":
            output = output + "O"
        if data[s1:e1] == "0":
            output = output + "P"
        if data[s1:e1] == "1":
            output = output + "Q"
        if data[s1:e1] == "{":
            output = output + "R"
        if data[s1:e1] == "i":
            output = output + "S"
        if data[s1:e1] == "G":
            output = output + "T"
        if data[s1:e1] == "&":
            output = output + "U"
        if data[s1:e1] == "K":
            output = output + "V"
        if data[s1:e1] == "g":
            output = output + "W"
        if data[s1:e1] == "6":
            output = output + "X"
        if data[s1:e1] == "4":
            output = output + "Y"
        if data[s1:e1] == "<":
            output = output + "Z"
        if data[s1:e1] == "T":
            output = output + "1"
        if data[s1:e1] == "5":
            output = output + "2"
        if data[s1:e1] == "s":
            output = output + "3"
        if data[s1:e1] == "v":
            output = output + "4"
        if data[s1:e1] == "=":
            output = output + "5"
        if data[s1:e1] == "?":
            output = output + "6"
        if data[s1:e1] == "@":
            output = output + "7"
        if data[s1:e1] == "x":
            output = output + "8"
        if data[s1:e1] == "y":
            output = output + "9"
        if data[s1:e1] == "^":
            output = output + "0"
        if data[s1:e1] == "S":
            output = output + "`"
        if data[s1:e1] == "Y":
            output = output + "!"
        if data[s1:e1] == "'":
            output = output + "'"
        if data[s1:e1] == "(":
            output = output + "$"
        if data[s1:e1] == "d":
            output = output + "%"
        if data[s1:e1] == "7":
            output = output + "^"
        if data[s1:e1] == "B":
            output = output + "&"
        if data[s1:e1] == "'":
            output = output + "*"
        if data[s1:e1] == "n":
            output = output + "("
        if data[s1:e1] == " ":
            output = output + ")"
        if data[s1:e1] == "w":
            output = output + "_"
        if data[s1:e1] == "A":
            output = output + "+"
        if data[s1:e1] == "J":
            output = output + "-"
        if data[s1:e1] == "j":
            output = output + "="
        if data[s1:e1] == ":":
            output = output + "{"
        if data[s1:e1] == "z":
            output = output + "["
        if data[s1:e1] == "Q":
            output = output + "]"
        if data[s1:e1] == "$":
            output = output + "}"
        if data[s1:e1] == ".":
            output = output + ":"
        if data[s1:e1] == "q":
            output = output + "'"
        if data[s1:e1] == "l":
            output = output + "@"
        if data[s1:e1] == "p":
            output = output + "#"
        if data[s1:e1] == "M":
            output = output + "~"
        if data[s1:e1] == "e":
            output = output + "/"
        if data[s1:e1] == "-":
            output = output + "?"
        if data[s1:e1] == "}":
            output = output + "."
        if data[s1:e1] == "E":
            output = output + ">"
        if data[s1:e1] == "a":
            output = output + ","
        if data[s1:e1] == "*":
            output = output + "<"
        if data[s1:e1] == "o":
            output = output + " "
        s1 = s1 + 1
        e1 = e1 + 1
        c1 = c1 + 1
        if data[s1:e1] == "1":
            output = output + "a"
        if data[s1:e1] == "2":
            output = output + "b"
        if data[s1:e1] == "h":
            output = output + "c"
        if data[s1:e1] == "P":
            output = output + "d"
        if data[s1:e1] == "<":
            output = output + "e"
        if data[s1:e1] == "]":
            output = output + "f"
        if data[s1:e1] == "T":
            output = output + "g"
        if data[s1:e1] == "J":
            output = output + "h"
        if data[s1:e1] == "c":
            output = output + "i"
        if data[s1:e1] == "^":
            output = output + "j"
        if data[s1:e1] == ",":
            output = output + "k"
        if data[s1:e1] == " ":
            output = output + "l"
        if data[s1:e1] == "v":
            output = output + "m"
        if data[s1:e1] == "(":
            output = output + "n"
        if data[s1:e1] == "j":
            output = output + "o"
        if data[s1:e1] == "`":
            output = output + "p"
        if data[s1:e1] == "+":
            output = output + "q"
        if data[s1:e1] == "9":
            output = output + "r"
        if data[s1:e1] == "/":
            output = output + "s"
        if data[s1:e1] == ">":
            output = output + "t"
        if data[s1:e1] == "f":
            output = output + "u"
        if data[s1:e1] == "e":
            output = output + "v"
        if data[s1:e1] == "[":
            output = output + "w"
        if data[s1:e1] == "'":
            output = output + "x"
        if data[s1:e1] == "n":
            output = output + "y"
        if data[s1:e1] == "X":
            output = output + "z"
        if data[s1:e1] == "u":
            output = output + "A"
        if data[s1:e1] == "4":
            output = output + "B"
        if data[s1:e1] == "m":
            output = output + "C"
        if data[s1:e1] == "6":
            output = output + "D"
        if data[s1:e1] == "G":
            output = output + "E"
        if data[s1:e1] == "b":
            output = output + "F"
        if data[s1:e1] == "3":
            output = output + "G"
        if data[s1:e1] == "%":
            output = output + "H"
        if data[s1:e1] == "S":
            output = output + "I"
        if data[s1:e1] == ".":
            output = output + "J"
        if data[s1:e1] == "p":
            output = output + "K"
        if data[s1:e1] == "@":
            output = output + "L"
        if data[s1:e1] == "$":
            output = output + "M"
        if data[s1:e1] == "l":
            output = output + "N"
        if data[s1:e1] == "?":
            output = output + "O"
        if data[s1:e1] == "Q":
            output = output + "P"
        if data[s1:e1] == "W":
            output = output + "Q"
        if data[s1:e1] == "H":
            output = output + "R"
        if data[s1:e1] == "{":
            output = output + "S"
        if data[s1:e1] == "K":
            output = output + "T"
        if data[s1:e1] == "L":
            output = output + "U"
        if data[s1:e1] == "w":
            output = output + "V"
        if data[s1:e1] == "&":
            output = output + "W"
        if data[s1:e1] == ":":
            output = output + "X"
        if data[s1:e1] == "~":
            output = output + "Y"
        if data[s1:e1] == "k":
            output = output + "Z"
        if data[s1:e1] == "I":
            output = output + "1"
        if data[s1:e1] == "M":
            output = output + "2"
        if data[s1:e1] == "_":
            output = output + "3"
        if data[s1:e1] == "q":
            output = output + "4"
        if data[s1:e1] == "a":
            output = output + "5"
        if data[s1:e1] == "g":
            output = output + "6"
        if data[s1:e1] == "D":
            output = output + "7"
        if data[s1:e1] == "E":
            output = output + "8"
        if data[s1:e1] == "U":
            output = output + "9"
        if data[s1:e1] == "*":
            output = output + "0"
        if data[s1:e1] == "r":
            output = output + "`"
        if data[s1:e1] == "0":
            output = output + "!"
        if data[s1:e1] == "'":
            output = output + "'"
        if data[s1:e1] == "=":
            output = output + "$"
        if data[s1:e1] == ")":
            output = output + "%"
        if data[s1:e1] == "N":
            output = output + "^"
        if data[s1:e1] == "8":
            output = output + "&"
        if data[s1:e1] == "Y":
            output = output + "*"
        if data[s1:e1] == "F":
            output = output + "("
        if data[s1:e1] == "t":
            output = output + ")"
        if data[s1:e1] == "B":
            output = output + "_"
        if data[s1:e1] == "o":
            output = output + "+"
        if data[s1:e1] == "d":
            output = output + "-"
        if data[s1:e1] == "C":
            output = output + "="
        if data[s1:e1] == "-":
            output = output + "{"
        if data[s1:e1] == "x":
            output = output + "["
        if data[s1:e1] == "R":
            output = output + "]"
        if data[s1:e1] == "i":
            output = output + "}"
        if data[s1:e1] == "7":
            output = output + ":"
        if data[s1:e1] == "V":
            output = output + "'"
        if data[s1:e1] == "s":
            output = output + "@"
        if data[s1:e1] == "#":
            output = output + "#"
        if data[s1:e1] == "z":
            output = output + "~"
        if data[s1:e1] == "!":
            output = output + "/"
        if data[s1:e1] == "y":
            output = output + "?"
        if data[s1:e1] == "A":
            output = output + "."
        if data[s1:e1] == "}":
            output = output + ">"
        if data[s1:e1] == "5":
            output = output + ","
        if data[s1:e1] == "Z":
            output = output + "<"
        if data[s1:e1] == "O":
            output = output + " "
        s1 = s1 + 1
        e1 = e1 + 1
        c1 = c1 + 1
        if data[s1:e1] == "0":
            output = output + "a"
        if data[s1:e1] == "D":
            output = output + "b"
        if data[s1:e1] == "+":
            output = output + "c"
        if data[s1:e1] == "*":
            output = output + "d"
        if data[s1:e1] == "9":
            output = output + "e"
        if data[s1:e1] == "l":
            output = output + "f"
        if data[s1:e1] == "i":
            output = output + "g"
        if data[s1:e1] == "y":
            output = output + "h"
        if data[s1:e1] == "Q":
            output = output + "i"
        if data[s1:e1] == "U":
            output = output + "j"
        if data[s1:e1] == "[":
            output = output + "k"
        if data[s1:e1] == "t":
            output = output + "l"
        if data[s1:e1] == "Z":
            output = output + "m"
        if data[s1:e1] == "$":
            output = output + "n"
        if data[s1:e1] == "!":
            output = output + "o"
        if data[s1:e1] == "<":
            output = output + "p"
        if data[s1:e1] == "'":
            output = output + "q"
        if data[s1:e1] == "]":
            output = output + "r"
        if data[s1:e1] == "1":
            output = output + "s"
        if data[s1:e1] == "O":
            output = output + "t"
        if data[s1:e1] == "u":
            output = output + "u"
        if data[s1:e1] == " ":
            output = output + "v"
        if data[s1:e1] == "2":
            output = output + "w"
        if data[s1:e1] == "^":
            output = output + "x"
        if data[s1:e1] == "c":
            output = output + "y"
        if data[s1:e1] == "g":
            output = output + "z"
        if data[s1:e1] == "x":
            output = output + "A"
        if data[s1:e1] == "k":
            output = output + "B"
        if data[s1:e1] == "d":
            output = output + "C"
        if data[s1:e1] == ")":
            output = output + "D"
        if data[s1:e1] == "}":
            output = output + "E"
        if data[s1:e1] == "C":
            output = output + "F"
        if data[s1:e1] == ">":
            output = output + "G"
        if data[s1:e1] == "J":
            output = output + "H"
        if data[s1:e1] == "F":
            output = output + "I"
        if data[s1:e1] == "&":
            output = output + "J"
        if data[s1:e1] == "L":
            output = output + "K"
        if data[s1:e1] == "j":
            output = output + "L"
        if data[s1:e1] == "%":
            output = output + "M"
        if data[s1:e1] == "T":
            output = output + "N"
        if data[s1:e1] == "?":
            output = output + "O"
        if data[s1:e1] == "p":
            output = output + "P"
        if data[s1:e1] == "K":
            output = output + "Q"
        if data[s1:e1] == "{":
            output = output + "R"
        if data[s1:e1] == "'":
            output = output + "S"
        if data[s1:e1] == "(":
            output = output + "T"
        if data[s1:e1] == "#":
            output = output + "U"
        if data[s1:e1] == "o":
            output = output + "V"
        if data[s1:e1] == "-":
            output = output + "W"
        if data[s1:e1] == "N":
            output = output + "X"
        if data[s1:e1] == "P":
            output = output + "Y"
        if data[s1:e1] == "W":
            output = output + "Z"
        if data[s1:e1] == "s":
            output = output + "1"
        if data[s1:e1] == "/":
            output = output + "2"
        if data[s1:e1] == ".":
            output = output + "3"
        if data[s1:e1] == "z":
            output = output + "4"
        if data[s1:e1] == "3":
            output = output + "5"
        if data[s1:e1] == "8":
            output = output + "6"
        if data[s1:e1] == ":":
            output = output + "7"
        if data[s1:e1] == "B":
            output = output + "8"
        if data[s1:e1] == "R":
            output = output + "9"
        if data[s1:e1] == "X":
            output = output + "0"
        if data[s1:e1] == "_":
            output = output + "`"
        if data[s1:e1] == "4":
            output = output + "!"
        if data[s1:e1] == "f":
            output = output + "'"
        if data[s1:e1] == "e":
            output = output + "$"
        if data[s1:e1] == "r":
            output = output + "%"
        if data[s1:e1] == "n":
            output = output + "^"
        if data[s1:e1] == "h":
            output = output + "&"
        if data[s1:e1] == "m":
            output = output + "*"
        if data[s1:e1] == "7":
            output = output + "("
        if data[s1:e1] == "E":
            output = output + ")"
        if data[s1:e1] == "5":
            output = output + "_"
        if data[s1:e1] == "H":
            output = output + "+"
        if data[s1:e1] == "V":
            output = output + "-"
        if data[s1:e1] == "b":
            output = output + "="
        if data[s1:e1] == "M":
            output = output + "{"
        if data[s1:e1] == "w":
            output = output + "["
        if data[s1:e1] == "v":
            output = output + "]"
        if data[s1:e1] == "A":
            output = output + "}"
        if data[s1:e1] == "@":
            output = output + ":"
        if data[s1:e1] == "a":
            output = output + "'"
        if data[s1:e1] == "Y":
            output = output + "@"
        if data[s1:e1] == "6":
            output = output + "#"
        if data[s1:e1] == "=":
            output = output + "~"
        if data[s1:e1] == "~":
            output = output + "/"
        if data[s1:e1] == "`":
            output = output + "?"
        if data[s1:e1] == "G":
            output = output + "."
        if data[s1:e1] == "I":
            output = output + ">"
        if data[s1:e1] == "S":
            output = output + ","
        if data[s1:e1] == "q":
            output = output + "<"
        if data[s1:e1] == ",":
            output = output + " "
        s1 = s1 + 1
        e1 = e1 + 1
        c1 = c1 + 1
        if data[s1:e1] == "$":
            output = output + "a"
        if data[s1:e1] == "~":
            output = output + "b"
        if data[s1:e1] == ">":
            output = output + "c"
        if data[s1:e1] == "L":
            output = output + "d"
        if data[s1:e1] == "X":
            output = output + "e"
        if data[s1:e1] == "2":
            output = output + "f"
        if data[s1:e1] == "}":
            output = output + "g"
        if data[s1:e1] == "'":
            output = output + "h"
        if data[s1:e1] == "m":
            output = output + "i"
        if data[s1:e1] == "8":
            output = output + "j"
        if data[s1:e1] == "r":
            output = output + "k"
        if data[s1:e1] == "i":
            output = output + "l"
        if data[s1:e1] == "`":
            output = output + "m"
        if data[s1:e1] == "G":
            output = output + "n"
        if data[s1:e1] == "e":
            output = output + "o"
        if data[s1:e1] == "o":
            output = output + "p"
        if data[s1:e1] == "@":
            output = output + "q"
        if data[s1:e1] == "S":
            output = output + "r"
        if data[s1:e1] == "Z":
            output = output + "s"
        if data[s1:e1] == "?":
            output = output + "t"
        if data[s1:e1] == "g":
            output = output + "u"
        if data[s1:e1] == "Y":
            output = output + "v"
        if data[s1:e1] == "t":
            output = output + "w"
        if data[s1:e1] == "y":
            output = output + "x"
        if data[s1:e1] == "q":
            output = output + "y"
        if data[s1:e1] == "h":
            output = output + "z"
        if data[s1:e1] == "v":
            output = output + "A"
        if data[s1:e1] == "'":
            output = output + "B"
        if data[s1:e1] == "H":
            output = output + "C"
        if data[s1:e1] == "*":
            output = output + "D"
        if data[s1:e1] == "4":
            output = output + "E"
        if data[s1:e1] == "u":
            output = output + "F"
        if data[s1:e1] == "1":
            output = output + "G"
        if data[s1:e1] == "J":
            output = output + "H"
        if data[s1:e1] == "p":
            output = output + "I"
        if data[s1:e1] == "^":
            output = output + "J"
        if data[s1:e1] == "_":
            output = output + "K"
        if data[s1:e1] == "I":
            output = output + "L"
        if data[s1:e1] == "{":
            output = output + "M"
        if data[s1:e1] == "=":
            output = output + "N"
        if data[s1:e1] == ",":
            output = output + "O"
        if data[s1:e1] == "N":
            output = output + "P"
        if data[s1:e1] == "E":
            output = output + "Q"
        if data[s1:e1] == "B":
            output = output + "R"
        if data[s1:e1] == "0":
            output = output + "S"
        if data[s1:e1] == "k":
            output = output + "T"
        if data[s1:e1] == "/":
            output = output + "U"
        if data[s1:e1] == " ":
            output = output + "V"
        if data[s1:e1] == "c":
            output = output + "W"
        if data[s1:e1] == "+":
            output = output + "X"
        if data[s1:e1] == "C":
            output = output + "Y"
        if data[s1:e1] == ":":
            output = output + "Z"
        if data[s1:e1] == "V":
            output = output + "1"
        if data[s1:e1] == "n":
            output = output + "2"
        if data[s1:e1] == "]":
            output = output + "3"
        if data[s1:e1] == "z":
            output = output + "4"
        if data[s1:e1] == "b":
            output = output + "5"
        if data[s1:e1] == "%":
            output = output + "6"
        if data[s1:e1] == "-":
            output = output + "7"
        if data[s1:e1] == "a":
            output = output + "8"
        if data[s1:e1] == "l":
            output = output + "9"
        if data[s1:e1] == "s":
            output = output + "0"
        if data[s1:e1] == "6":
            output = output + "`"
        if data[s1:e1] == "R":
            output = output + "!"
        if data[s1:e1] == "5":
            output = output + "'"
        if data[s1:e1] == "O":
            output = output + "$"
        if data[s1:e1] == "K":
            output = output + "%"
        if data[s1:e1] == "F":
            output = output + "^"
        if data[s1:e1] == "Q":
            output = output + "&"
        if data[s1:e1] == "D":
            output = output + "*"
        if data[s1:e1] == "A":
            output = output + "("
        if data[s1:e1] == "x":
            output = output + ")"
        if data[s1:e1] == "d":
            output = output + "_"
        if data[s1:e1] == ")":
            output = output + "+"
        if data[s1:e1] == "<":
            output = output + "-"
        if data[s1:e1] == ".":
            output = output + "="
        if data[s1:e1] == "M":
            output = output + "{"
        if data[s1:e1] == "[":
            output = output + "["
        if data[s1:e1] == "P":
            output = output + "]"
        if data[s1:e1] == "7":
            output = output + "}"
        if data[s1:e1] == "U":
            output = output + ":"
        if data[s1:e1] == "9":
            output = output + "'"
        if data[s1:e1] == "j":
            output = output + "@"
        if data[s1:e1] == "&":
            output = output + "#"
        if data[s1:e1] == "T":
            output = output + "~"
        if data[s1:e1] == "3":
            output = output + "/"
        if data[s1:e1] == "W":
            output = output + "?"
        if data[s1:e1] == "f":
            output = output + "."
        if data[s1:e1] == "#":
            output = output + ">"
        if data[s1:e1] == "w":
            output = output + ","
        if data[s1:e1] == "(":
            output = output + "<"
        if data[s1:e1] == "!":
            output = output + " "
        s1 = s1 + 1
        e1 = e1 + 1
        c1 = c1 + 1
elif leng == 4:
    e1 = 4
    while c1 < l1:
        if data[s1:e1] == ",3+d":
            output = output + "a"
        if data[s1:e1] == "`z*^":
            output = output + "b"
        if data[s1:e1] == "CTe6":
            output = output + "c"
        if data[s1:e1] == "q9Xi":
            output = output + "d"
        if data[s1:e1] == "[kW9":
            output = output + "e"
        if data[s1:e1] == "5=F3":
            output = output + "f"
        if data[s1:e1] == "8:'o":
            output = output + "g"
        if data[s1:e1] == "uf$n":
            output = output + "h"
        if data[s1:e1] == "6I]6":
            output = output + "i"
        if data[s1:e1] == "Yyj*":
            output = output + "j"
        if data[s1:e1] == "-_?b":
            output = output + "k"
        if data[s1:e1] == "!SG8":
            output = output + "l"
        if data[s1:e1] == "!{h?":
            output = output + "m"
        if data[s1:e1] == "uEl6":
            output = output + "n"
        if data[s1:e1] == "Nl~O":
            output = output + "o"
        if data[s1:e1] == "aP@z":
            output = output + "p"
        if data[s1:e1] == "]3gg":
            output = output + "q"
        if data[s1:e1] == "aM%i":
            output = output + "r"
        if data[s1:e1] == "'%Wq":
            output = output + "s"
        if data[s1:e1] == "E7Ue":
            output = output + "t"
        if data[s1:e1] == "#w.P":
            output = output + "u"
        if data[s1:e1] == "WlLp":
            output = output + "v"
        if data[s1:e1] == "R8.-":
            output = output + "w"
        if data[s1:e1] == "/Ire":
            output = output + "x"
        if data[s1:e1] == "V@)J":
            output = output + "y"
        if data[s1:e1] == "J.~P":
            output = output + "z"
        if data[s1:e1] == "DByu":
            output = output + "A"
        if data[s1:e1] == "He]L":
            output = output + "B"
        if data[s1:e1] == "?$(/":
            output = output + "C"
        if data[s1:e1] == "1}`4":
            output = output + "D"
        if data[s1:e1] == "-Go{":
            output = output + "E"
        if data[s1:e1] == "dJ0<":
            output = output + "F"
        if data[s1:e1] == "'Q=o":
            output = output + "G"
        if data[s1:e1] == "S&0V":
            output = output + "H"
        if data[s1:e1] == "U]av":
            output = output + "I"
        if data[s1:e1] == "c Zw":
            output = output + "J"
        if data[s1:e1] == "s}^Y":
            output = output + "K"
        if data[s1:e1] == "hM=r":
            output = output + "L"
        if data[s1:e1] == "MVJ@":
            output = output + "M"
        if data[s1:e1] == "phBv":
            output = output + "N"
        if data[s1:e1] == "ANB%":
            output = output + "O"
        if data[s1:e1] == "YSDx":
            output = output + "P"
        if data[s1:e1] == "}m:E":
            output = output + "Q"
        if data[s1:e1] == "Uv#8":
            output = output + "R"
        if data[s1:e1] == "(*9x":
            output = output + "S"
        if data[s1:e1] == "yTis":
            output = output + "T"
        if data[s1:e1] == "q?,5":
            output = output + "U"
        if data[s1:e1] == "bczv":
            output = output + "V"
        if data[s1:e1] == "F>X2":
            output = output + "W"
        if data[s1:e1] == "M4sC":
            output = output + "X"
        if data[s1:e1] == "!Fot":
            output = output + "Y"
        if data[s1:e1] == " DW3":
            output = output + "Z"
        if data[s1:e1] == "<H^m":
            output = output + "1"
        if data[s1:e1] == "~'nO":
            output = output + "2"
        if data[s1:e1] == "4YxP":
            output = output + "3"
        if data[s1:e1] == "lGRU":
            output = output + "4"
        if data[s1:e1] == ">)FO":
            output = output + "5"
        if data[s1:e1] == "27/5":
            output = output + "6"
        if data[s1:e1] == "NE:(":
            output = output + "7"
        if data[s1:e1] == "5>Hr":
            output = output + "8"
        if data[s1:e1] == "mZH%":
            output = output + "9"
        if data[s1:e1] == "r&XT":
            output = output + "0"
        if data[s1:e1] == "zwLi":
            output = output + "`"
        if data[s1:e1] == "._R2":
            output = output + "!"
        if data[s1:e1] == "NjBC":
            output = output + "'"
        if data[s1:e1] == "Qm[V":
            output = output + "$"
        if data[s1:e1] == "Kcn7":
            output = output + "%"
        if data[s1:e1] == ">{b ":
            output = output + "^"
        if data[s1:e1] == ")$47":
            output = output + "&"
        if data[s1:e1] == "DK)R":
            output = output + "*"
        if data[s1:e1] == "1(@<":
            output = output + "("
        if data[s1:e1] == "[kAZ":
            output = output + ")"
        if data[s1:e1] == "0~jS":
            output = output + "_"
        if data[s1:e1] == "Gs-p":
            output = output + "+"
        if data[s1:e1] == "ud`Q":
            output = output + "-"
        if data[s1:e1] == "$#}c":
            output = output + "="
        if data[s1:e1] == "K^!g":
            output = output + "{"
        if data[s1:e1] == "#xnk":
            output = output + "["
        if data[s1:e1] == "hI'K":
            output = output + "]"
        if data[s1:e1] == "O_X9":
            output = output + "}"
        if data[s1:e1] == "fb=2":
            output = output + ":"
        if data[s1:e1] == "&{1f":
            output = output + "'"
        if data[s1:e1] == "ZtLj":
            output = output + "@"
        if data[s1:e1] == "'C&*":
            output = output + "#"
        if data[s1:e1] == "a[:T":
            output = output + "~"
        if data[s1:e1] == "+`/,":
            output = output + "/"
        if data[s1:e1] == ",Qp'":
            output = output + "?"
        if data[s1:e1] == "I1 +":
            output = output + "."
        if data[s1:e1] == "+0<A":
            output = output + ">"
        if data[s1:e1] == "w'f_":
            output = output + ","
        if data[s1:e1] == "dqty":
            output = output + "<"
        if data[s1:e1] == "gtkA":
            output = output + " "
        s1 = s1 + 4
        e1 = e1 + 4
        c1 = c1 + 4
        if data[s1:e1] == "nR/d":
            output = output + "a"
        if data[s1:e1] == "yD{V":
            output = output + "b"
        if data[s1:e1] == "G+1+":
            output = output + "c"
        if data[s1:e1] == "3e:R":
            output = output + "d"
        if data[s1:e1] == "0}))":
            output = output + "e"
        if data[s1:e1] == "HqrU":
            output = output + "f"
        if data[s1:e1] == ">F98":
            output = output + "g"
        if data[s1:e1] == "Dxt~":
            output = output + "h"
        if data[s1:e1] == "3#7L":
            output = output + "i"
        if data[s1:e1] == ",&mv":
            output = output + "j"
        if data[s1:e1] == "56B3":
            output = output + "k"
        if data[s1:e1] == "gQ)p":
            output = output + "l"
        if data[s1:e1] == "Ek[w":
            output = output + "m"
        if data[s1:e1] == ":bHR":
            output = output + "n"
        if data[s1:e1] == "'E'=":
            output = output + "o"
        if data[s1:e1] == "{yTG":
            output = output + "p"
        if data[s1:e1] == "X]DS":
            output = output + "q"
        if data[s1:e1] == "s!aa":
            output = output + "r"
        if data[s1:e1] == "r]`2":
            output = output + "s"
        if data[s1:e1] == "uIPh":
            output = output + "t"
        if data[s1:e1] == "9Kug":
            output = output + "u"
        if data[s1:e1] == "<Z4D":
            output = output + "v"
        if data[s1:e1] == "u2OP":
            output = output + "w"
        if data[s1:e1] == "8x O":
            output = output + "x"
        if data[s1:e1] == ", *p":
            output = output + "y"
        if data[s1:e1] == "X}6$":
            output = output + "z"
        if data[s1:e1] == "Qgb.":
            output = output + "A"
        if data[s1:e1] == "70<]":
            output = output + "B"
        if data[s1:e1] == "'kpl":
            output = output + "C"
        if data[s1:e1] == "5yvW":
            output = output + "D"
        if data[s1:e1] == "Cizs":
            output = output + "E"
        if data[s1:e1] == "Fy,h":
            output = output + "F"
        if data[s1:e1] == "d7_~":
            output = output + "G"
        if data[s1:e1] == "/G~R":
            output = output + "H"
        if data[s1:e1] == "v'dz":
            output = output + "I"
        if data[s1:e1] == ":~^M":
            output = output + "J"
        if data[s1:e1] == "f:Ek":
            output = output + "K"
        if data[s1:e1] == "L^xG":
            output = output + "L"
        if data[s1:e1] == "=.m9":
            output = output + "M"
        if data[s1:e1] == "Y{C-":
            output = output + "N"
        if data[s1:e1] == "th$?":
            output = output + "O"
        if data[s1:e1] == "(tf$":
            output = output + "P"
        if data[s1:e1] == "&Z0$":
            output = output + "Q"
        if data[s1:e1] == "(N24":
            output = output + "R"
        if data[s1:e1] == "Kcf-":
            output = output + "S"
        if data[s1:e1] == "IPKx":
            output = output + "T"
        if data[s1:e1] == "Na_b":
            output = output + "U"
        if data[s1:e1] == "8wu(":
            output = output + "V"
        if data[s1:e1] == "JZYj":
            output = output + "W"
        if data[s1:e1] == "T'q4":
            output = output + "X"
        if data[s1:e1] == "dkH#":
            output = output + "Y"
        if data[s1:e1] == "%c1[":
            output = output + "Z"
        if data[s1:e1] == ".MV,":
            output = output + "1"
        if data[s1:e1] == "U>m>":
            output = output + "2"
        if data[s1:e1] == "jelg":
            output = output + "3"
        if data[s1:e1] == "*CnT":
            output = output + "4"
        if data[s1:e1] == "W1c{":
            output = output + "5"
        if data[s1:e1] == "@?ic":
            output = output + "6"
        if data[s1:e1] == "4I8H":
            output = output + "7"
        if data[s1:e1] == "oaVE":
            output = output + "8"
        if data[s1:e1] == "e-=<":
            output = output + "9"
        if data[s1:e1] == "(I^b":
            output = output + "0"
        if data[s1:e1] == "w#. ":
            output = output + "`"
        if data[s1:e1] == "Kf3_":
            output = output + "!"
        if data[s1:e1] == "+Jz=":
            output = output + "'"
        if data[s1:e1] == "-'[l":
            output = output + "$"
        if data[s1:e1] == "AhwP":
            output = output + "%"
        if data[s1:e1] == "Qz7J":
            output = output + "^"
        if data[s1:e1] == "j!ML":
            output = output + "&"
        if data[s1:e1] == "`*%o":
            output = output + "*"
        if data[s1:e1] == "2/ '":
            output = output + "("
        if data[s1:e1] == "?eNO":
            output = output + ")"
        if data[s1:e1] == "<}p*":
            output = output + "_"
        if data[s1:e1] == "SJ+B":
            output = output + "+"
        if data[s1:e1] == "SA`q":
            output = output + "-"
        if data[s1:e1] == "?StX":
            output = output + "="
        if data[s1:e1] == "r6T`":
            output = output + "{"
        if data[s1:e1] == "&LF%":
            output = output + "["
        if data[s1:e1] == "s#YU":
            output = output + "]"
        if data[s1:e1] == "]Zso":
            output = output + "}"
        if data[s1:e1] == "Q_}j":
            output = output + ":"
        if data[s1:e1] == "WUX!":
            output = output + "'"
        if data[s1:e1] == "9NA5":
            output = output + "@"
        if data[s1:e1] == "qo!n":
            output = output + "#"
        if data[s1:e1] == "nlVi":
            output = output + "~"
        if data[s1:e1] == "B[mW":
            output = output + "/"
        if data[s1:e1] == ">O'@":
            output = output + "?"
        if data[s1:e1] == "F@Y@":
            output = output + "."
        if data[s1:e1] == "AM^i":
            output = output + ">"
        if data[s1:e1] == "%0Cv":
            output = output + ","
        if data[s1:e1] == "/rB)":
            output = output + "<"
        if data[s1:e1] == "&561":
            output = output + " "
        s1 = s1 + 4
        e1 = e1 + 4
        c1 = c1 + 4
        if data[s1:e1] == "qyQb":
            output = output + "a"
        if data[s1:e1] == "i/SV":
            output = output + "b"
        if data[s1:e1] == "gHY1":
            output = output + "c"
        if data[s1:e1] == "/++^":
            output = output + "d"
        if data[s1:e1] == "x,n6":
            output = output + "e"
        if data[s1:e1] == "!=Sk":
            output = output + "f"
        if data[s1:e1] == "F'$e":
            output = output + "g"
        if data[s1:e1] == ",_t ":
            output = output + "h"
        if data[s1:e1] == "HTX'":
            output = output + "i"
        if data[s1:e1] == "MW#o":
            output = output + "j"
        if data[s1:e1] == "+Mk5":
            output = output + "k"
        if data[s1:e1] == "c^X(":
            output = output + "l"
        if data[s1:e1] == "~u_a":
            output = output + "m"
        if data[s1:e1] == "zmqW":
            output = output + "n"
        if data[s1:e1] == "c3By":
            output = output + "o"
        if data[s1:e1] == "a'mP":
            output = output + "p"
        if data[s1:e1] == "[JtK":
            output = output + "q"
        if data[s1:e1] == "<j~s":
            output = output + "r"
        if data[s1:e1] == "ZF-%":
            output = output + "s"
        if data[s1:e1] == "GCaj":
            output = output + "t"
        if data[s1:e1] == "ms/8":
            output = output + "u"
        if data[s1:e1] == "4NP{":
            output = output + "v"
        if data[s1:e1] == "=PZx":
            output = output + "w"
        if data[s1:e1] == "O]%y":
            output = output + "x"
        if data[s1:e1] == "_W!E":
            output = output + "y"
        if data[s1:e1] == "zo>O":
            output = output + "z"
        if data[s1:e1] == "&hT#":
            output = output + "A"
        if data[s1:e1] == "Fb'9":
            output = output + "B"
        if data[s1:e1] == "KGl/":
            output = output + "C"
        if data[s1:e1] == "9MkI":
            output = output + "D"
        if data[s1:e1] == "$lp}":
            output = output + "E"
        if data[s1:e1] == "2Ae?":
            output = output + "F"
        if data[s1:e1] == "M{?l":
            output = output + "G"
        if data[s1:e1] == "w8.7":
            output = output + "H"
        if data[s1:e1] == "))X9":
            output = output + "I"
        if data[s1:e1] == "+Kft":
            output = output + "J"
        if data[s1:e1] == "C`O*":
            output = output + "K"
        if data[s1:e1] == "h'v0":
            output = output + "L"
        if data[s1:e1] == "`26h":
            output = output + "M"
        if data[s1:e1] == "'YQz":
            output = output + "N"
        if data[s1:e1] == "tS7B":
            output = output + "O"
        if data[s1:e1] == "UJCN":
            output = output + "P"
        if data[s1:e1] == "6ugD":
            output = output + "Q"
        if data[s1:e1] == "&(DT":
            output = output + "R"
        if data[s1:e1] == "pw5-":
            output = output + "S"
        if data[s1:e1] == "G}d4":
            output = output + "T"
        if data[s1:e1] == "LDN*":
            output = output + "U"
        if data[s1:e1] == "ieRV":
            output = output + "V"
        if data[s1:e1] == "Br[*":
            output = output + "W"
        if data[s1:e1] == "}`)K":
            output = output + "X"
        if data[s1:e1] == "xI@s":
            output = output + "Y"
        if data[s1:e1] == "fZnP":
            output = output + "Z"
        if data[s1:e1] == "kWeU":
            output = output + "1"
        if data[s1:e1] == "mA7Y":
            output = output + "2"
        if data[s1:e1] == ":[_8":
            output = output + "3"
        if data[s1:e1] == "UA17":
            output = output + "4"
        if data[s1:e1] == "&Fb2":
            output = output + "5"
        if data[s1:e1] == "6nxT":
            output = output + "6"
        if data[s1:e1] == "l.]R":
            output = output + "7"
        if data[s1:e1] == " ,-u":
            output = output + "8"
        if data[s1:e1] == " *i<":
            output = output + "9"
        if data[s1:e1] == "L!#w":
            output = output + "0"
        if data[s1:e1] == "L-Vr":
            output = output + "`"
        if data[s1:e1] == "pIwH":
            output = output + "!"
        if data[s1:e1] == ":BGd":
            output = output + "'"
        if data[s1:e1] == "4%oq":
            output = output + "$"
        if data[s1:e1] == "{hQQ":
            output = output + "%"
        if data[s1:e1] == "1a3@":
            output = output + "^"
        if data[s1:e1] == "OZzr":
            output = output + "&"
        if data[s1:e1] == "]>f{":
            output = output + "*"
        if data[s1:e1] == "v1#E":
            output = output + "("
        if data[s1:e1] == "0(XJ":
            output = output + ")"
        if data[s1:e1] == "$u3=":
            output = output + "_"
        if data[s1:e1] == "r}&A":
            output = output + "+"
        if data[s1:e1] == "NRf'":
            output = output + "-"
        if data[s1:e1] == ")`RS":
            output = output + "="
        if data[s1:e1] == "o!'?":
            output = output + "{"
        if data[s1:e1] == "s3~^":
            output = output + "["
        if data[s1:e1] == "J<i,":
            output = output + "]"
        if data[s1:e1] == "2%5.":
            output = output + "}"
        if data[s1:e1] == "?b]<":
            output = output + ":"
        if data[s1:e1] == ":0^g":
            output = output + "'"
        if data[s1:e1] == "n.cj":
            output = output + "@"
        if data[s1:e1] == "9dc>":
            output = output + "#"
        if data[s1:e1] == "vvE~":
            output = output + "~"
        if data[s1:e1] == "0[qg":
            output = output + "/"
        if data[s1:e1] == "y=CL":
            output = output + "?"
        if data[s1:e1] == "HYV4":
            output = output + "."
        if data[s1:e1] == "U$>D":
            output = output + ">"
        if data[s1:e1] == "5p8@":
            output = output + ","
        if data[s1:e1] == "dI: ":
            output = output + "<"
        if data[s1:e1] == "@E(j":
            output = output + " "
        s1 = s1 + 4
        e1 = e1 + 4
        c1 = c1 + 4
        if data[s1:e1] == "-z00":
            output = output + "a"
        if data[s1:e1] == "^JL4":
            output = output + "b"
        if data[s1:e1] == "D5u3":
            output = output + "c"
        if data[s1:e1] == "wYu3":
            output = output + "d"
        if data[s1:e1] == "3f-~":
            output = output + "e"
        if data[s1:e1] == "ZZ8(":
            output = output + "f"
        if data[s1:e1] == "?341":
            output = output + "g"
        if data[s1:e1] == "'m?/":
            output = output + "h"
        if data[s1:e1] == "t]#y":
            output = output + "i"
        if data[s1:e1] == "6M1q":
            output = output + "j"
        if data[s1:e1] == "DWu_":
            output = output + "k"
        if data[s1:e1] == "i}U'":
            output = output + "l"
        if data[s1:e1] == "z9CS":
            output = output + "m"
        if data[s1:e1] == "OPtG":
            output = output + "n"
        if data[s1:e1] == "gvIj":
            output = output + "o"
        if data[s1:e1] == "'c:^":
            output = output + "p"
        if data[s1:e1] == "x.}*":
            output = output + "q"
        if data[s1:e1] == "ewkc":
            output = output + "r"
        if data[s1:e1] == "y]>y":
            output = output + "s"
        if data[s1:e1] == ">xbl":
            output = output + "t"
        if data[s1:e1] == "AG,&":
            output = output + "u"
        if data[s1:e1] == "NY.'":
            output = output + "v"
        if data[s1:e1] == "A}Fa":
            output = output + "w"
        if data[s1:e1] == "AQ9S":
            output = output + "x"
        if data[s1:e1] == "6oU2":
            output = output + "y"
        if data[s1:e1] == "TqBq":
            output = output + "z"
        if data[s1:e1] == "V!eN":
            output = output + "A"
        if data[s1:e1] == "=%C`":
            output = output + "B"
        if data[s1:e1] == "_fs#":
            output = output + "C"
        if data[s1:e1] == "r2U5":
            output = output + "D"
        if data[s1:e1] == "pmmx":
            output = output + "E"
        if data[s1:e1] == " srv":
            output = output + "F"
        if data[s1:e1] == "'ogJ":
            output = output + "G"
        if data[s1:e1] == "+K#$":
            output = output + "H"
        if data[s1:e1] == "el`!":
            output = output + "I"
        if data[s1:e1] == "I<&<":
            output = output + "J"
        if data[s1:e1] == "8efV":
            output = output + "K"
        if data[s1:e1] == "ubwK":
            output = output + "L"
        if data[s1:e1] == "7>@S":
            output = output + "M"
        if data[s1:e1] == "7(1'":
            output = output + "N"
        if data[s1:e1] == "Zp`T":
            output = output + "O"
        if data[s1:e1] == "*y$*":
            output = output + "P"
        if data[s1:e1] == "7ER{":
            output = output + "Q"
        if data[s1:e1] == "jDW%":
            output = output + "R"
        if data[s1:e1] == "zw~M":
            output = output + "S"
        if data[s1:e1] == "@]6~":
            output = output + "T"
        if data[s1:e1] == "vJ%A":
            output = output + "U"
        if data[s1:e1] == "k>W/":
            output = output + "V"
        if data[s1:e1] == "kVSX":
            output = output + "W"
        if data[s1:e1] == "BQ$*":
            output = output + "X"
        if data[s1:e1] == "C:Xq":
            output = output + "Y"
        if data[s1:e1] == "a^$B":
            output = output + "Z"
        if data[s1:e1] == "-P5H":
            output = output + "1"
        if data[s1:e1] == "hYP#":
            output = output + "2"
        if data[s1:e1] == "8T_F":
            output = output + "3"
        if data[s1:e1] == ":Y= ":
            output = output + "4"
        if data[s1:e1] == "_f)<":
            output = output + "5"
        if data[s1:e1] == "p~]0":
            output = output + "6"
        if data[s1:e1] == "d%zl":
            output = output + "7"
        if data[s1:e1] == "M2,[":
            output = output + "8"
        if data[s1:e1] == "}ZhH":
            output = output + "9"
        if data[s1:e1] == "EL4N":
            output = output + "0"
        if data[s1:e1] == "rt R":
            output = output + "`"
        if data[s1:e1] == "t FG":
            output = output + "!"
        if data[s1:e1] == "^[0/":
            output = output + "'"
        if data[s1:e1] == "hN2E":
            output = output + "$"
        if data[s1:e1] == "j)so":
            output = output + "%"
        if data[s1:e1] == "P)b/":
            output = output + "^"
        if data[s1:e1] == "JVWH":
            output = output + "&"
        if data[s1:e1] == "p5{G":
            output = output + "*"
        if data[s1:e1] == "Rid.":
            output = output + "("
        if data[s1:e1] == "vn+K":
            output = output + ")"
        if data[s1:e1] == "iIH!":
            output = output + "_"
        if data[s1:e1] == "XcOQ":
            output = output + "+"
        if data[s1:e1] == "K?o)":
            output = output + "-"
        if data[s1:e1] == "jgk7":
            output = output + "="
        if data[s1:e1] == "@Ox(":
            output = output + "{"
        if data[s1:e1] == ",d(B":
            output = output + "["
        if data[s1:e1] == "8s<`":
            output = output + "]"
        if data[s1:e1] == "{c6F":
            output = output + "}"
        if data[s1:e1] == "b.+=":
            output = output + ":"
        if data[s1:e1] == "l[{[":
            output = output + "'"
        if data[s1:e1] == "?-a&":
            output = output + "@"
        if data[s1:e1] == "M:L9":
            output = output + "#"
        if data[s1:e1] == "C=Em":
            output = output + "~"
        if data[s1:e1] == "+Xn1":
            output = output + "/"
        if data[s1:e1] == "@Q'L":
            output = output + "?"
        if data[s1:e1] == "dUTi":
            output = output + "."
        if data[s1:e1] == "h'nI":
            output = output + ">"
        if data[s1:e1] == "94R!":
            output = output + ","
        if data[s1:e1] == "Dagn":
            output = output + "<"
        if data[s1:e1] == "&Or,":
            output = output + " "
        s1 = s1 + 4
        e1 = e1 + 4
        c1 = c1 + 4
elif leng == 16:
    e1 = 16
    while c1 < l1:
        if data[s1:e1] == "TC{emM1>ALJH<`Lt":
            output = output + "a"
        if data[s1:e1] == "Z9 *m' jx1z~H-+t":
            output = output + "b"
        if data[s1:e1] == "%bQ:LTWwgDzLE=X&":
            output = output + "c"
        if data[s1:e1] == "'$(PFba`gg-ek~TJ":
            output = output + "d"
        if data[s1:e1] == "yQ!Te YWm$Gy2uv@":
            output = output + "e"
        if data[s1:e1] == "0<Y[5u&tuPuPCL)y":
            output = output + "f"
        if data[s1:e1] == "Ff1r0(:K72Db,PT1":
            output = output + "g"
        if data[s1:e1] == ">G6fGyodR~8ZY/+q":
            output = output + "h"
        if data[s1:e1] == "NH@yUg'MDZ5YC!w^":
            output = output + "i"
        if data[s1:e1] == "'+{a$$h,w77.H>3?":
            output = output + "j"
        if data[s1:e1] == "kNN's'=2-MixM_bi":
            output = output + "k"
        if data[s1:e1] == "bn,9C+Bu>6lwJ41S":
            output = output + "l"
        if data[s1:e1] == "v3,(V6~^<?re'aWj":
            output = output + "m"
        if data[s1:e1] == "(H<^pWf8iPUY+3OR":
            output = output + "n"
        if data[s1:e1] == "-*Yq#t#M )GE's{Q":
            output = output + "o"
        if data[s1:e1] == "sUx3Hb[la,,k$(Ig":
            output = output + "p"
        if data[s1:e1] == "D@1jdAnEeFf#ge2v":
            output = output + "q"
        if data[s1:e1] == "9z9{rm,rFvU,ZX]Q":
            output = output + "r"
        if data[s1:e1] == "{[(D+HDux*!Oos+c":
            output = output + "s"
        if data[s1:e1] == "d/yu.wLldMz]Pf{G":
            output = output + "t"
        if data[s1:e1] == "ozC%E5rx'r(K[sx4":
            output = output + "u"
        if data[s1:e1] == "]Ej=x^56iMTCcIOl":
            output = output + "v"
        if data[s1:e1] == "p%P3Nn#BiDLn}GA0":
            output = output + "w"
        if data[s1:e1] == "cQB?)lF1etk@-`]Z":
            output = output + "x"
        if data[s1:e1] == "oAxo>3[]F{=<t/+Y":
            output = output + "y"
        if data[s1:e1] == "o/hJt?iN#v3/pu@j":
            output = output + "z"
        if data[s1:e1] == "t?jWhGzwUzTX{n9h":
            output = output + "A"
        if data[s1:e1] == "I.$zQc#R6jE[Q4S}":
            output = output + "B"
        if data[s1:e1] == "'&1cB9pou.8fgJ&^":
            output = output + "C"
        if data[s1:e1] == "GIMq]z_'Q:XBd+/R":
            output = output + "D"
        if data[s1:e1] == "GvN7Iv]80}*ZoA.K":
            output = output + "E"
        if data[s1:e1] == "P-.!>{ q=/yI=2qU":
            output = output + "F"
        if data[s1:e1] == "JBKi5WJQkX(E&#1C":
            output = output + "G"
        if data[s1:e1] == "9.XW_}A+_G[mL7*w":
            output = output + "H"
        if data[s1:e1] == ":K%^R_R&1_!y&?69":
            output = output + "I"
        if data[s1:e1] == "]L8_~it!FEUYst#c":
            output = output + "J"
        if data[s1:e1] == "xero(Rowc#*][ude":
            output = output + "K"
        if data[s1:e1] == "n0*no=Vx~GqCD'fl":
            output = output + "L"
        if data[s1:e1] == "IEqw6lfApI4N:g>X":
            output = output + "M"
        if data[s1:e1] == "1[75~L4K%s@3R>gR":
            output = output + "N"
        if data[s1:e1] == "vIxPC,pkqU<8'fHK":
            output = output + "O"
        if data[s1:e1] == "YNx'1UO3)Dk)?z?R":
            output = output + "P"
        if data[s1:e1] == "<2Vn=dEW-Karg,Q'":
            output = output + "Q"
        if data[s1:e1] == "Oro_)&<MmUbh$d!h":
            output = output + "R"
        if data[s1:e1] == "mszc:2WHZ>eLWcWW":
            output = output + "S"
        if data[s1:e1] == "s`_wfAc/4nQauqut":
            output = output + "T"
        if data[s1:e1] == "9l@j3(Z+b$4~.uiO":
            output = output + "U"
        if data[s1:e1] == "H&9QC!d'~c/h!Y&a":
            output = output + "V"
        if data[s1:e1] == "L#^F0K{ xsCSe2yV":
            output = output + "W"
        if data[s1:e1] == "6<`IQ:Vj{%k+5605":
            output = output + "X"
        if data[s1:e1] == "%p@Xm:2ez'xPT'2}":
            output = output + "Y"
        if data[s1:e1] == "T%4~F5R/S}hgW`yv":
            output = output + "Z"
        if data[s1:e1] == "-)z7U>$K{o'kEts>":
            output = output + "1"
        if data[s1:e1] == "@uhx``Vg'6(jX*_f":
            output = output + "2"
        if data[s1:e1] == "m@Y<<_}*]1[*5%dn":
            output = output + "3"
        if data[s1:e1] == "(XyDRT%la+AX(pNO":
            output = output + "4"
        if data[s1:e1] == "aBm03%NS viqZ/r ":
            output = output + "5"
        if data[s1:e1] == "]sc4N%K2 Y(Z'H9X":
            output = output + "6"
        if data[s1:e1] == "N^D#Kh w?:D(=b$7":
            output = output + "7"
        if data[s1:e1] == "6hFSPPhI }qvP3Q[":
            output = output + "8"
        if data[s1:e1] == "Vfj<Jpyp5.!'%EBV":
            output = output + "9"
        if data[s1:e1] == "`R-@4J5TZj>DacLs":
            output = output + "0"
        if data[s1:e1] == "dN{8,4 ed=6]C:gJ":
            output = output + "`"
        if data[s1:e1] == "7=A9`[iHKQo}BjGh":
            output = output + "!"
        if data[s1:e1] == "Wykn&'R,{r!S7zn:":
            output = output + "'"
        if data[s1:e1] == "lX0$,i.?-7F^h FZ":
            output = output + "$"
        if data[s1:e1] == "fR{>)T?.l.w:&G78":
            output = output + "%"
        if data[s1:e1] == "p[6^naiIqH}rm$,&":
            output = output + "^"
        if data[s1:e1] == "JAOnF)lfW^/*M=U1":
            output = output + "&"
        if data[s1:e1] == "@GJ}8aS+8Ci`3f5x":
            output = output + "*"
        if data[s1:e1] == "`?#ZVN~TPUs+_'qS":
            output = output + "("
        if data[s1:e1] == "SUYc)jV-!qE0Loz9":
            output = output + ")"
        if data[s1:e1] == "!/^O@p5eP}c5~b3B":
            output = output + "_"
        if data[s1:e1] == "rkZB.k1jw*SZUDJb":
            output = output + "+"
        if data[s1:e1] == "4_zlbc)K3:B7T%QF":
            output = output + "-"
        if data[s1:e1] == "9#J=%?Ft-)0GYv2p":
            output = output + "="
        if data[s1:e1] == "/'8aUC_h''}Mda8M":
            output = output + "{"
        if data[s1:e1] == "M}K.gV8!klnS$2*:":
            output = output + "["
        if data[s1:e1] == "Rm vT)5B>y:VZ0SJ":
            output = output + "]"
        if data[s1:e1] == "1y*~PH=+E_>Xd#Bu":
            output = output + "}"
        if data[s1:e1] == "_or-LY<Xp] s8)9B":
            output = output + ":"
        if data[s1:e1] == "kCA`kL?NNHOd?('O":
            output = output + "'"
        if data[s1:e1] == "F/mteOA}HgA^[OE~":
            output = output + "@"
        if data[s1:e1] == "lhX2a9k`Vm4f42>`":
            output = output + "#"
        if data[s1:e1] == "$bqltJSwvbSOwb$m":
            output = output + "~"
        if data[s1:e1] == "'4BC/<-=j^I'!?][":
            output = output + "/"
        if data[s1:e1] == ".6~bMV}*)7S.Ms~0":
            output = output + "?"
        if data[s1:e1] == "'AIi6VY3VDa4T&O&":
            output = output + "."
        if data[s1:e1] == "r8&<Dmq@t0v^$)n,":
            output = output + ">"
        if data[s1:e1] == "7id!@ vK%]E^,w@2":
            output = output + ","
        if data[s1:e1] == "`#:0eIrW--A{I]p7":
            output = output + "<"
        if data[s1:e1] == "pM*g80y#6u'OG<=[":
            output = output + " "
        s1 = s1 + 1
        e1 = e1 + 1
        c1 = c1 + 1
        if data[s1:e1] == "&mYzFJ<alZg76bJu":
            output = output + "a"
        if data[s1:e1] == "<KXB~}##SK=<J_JB":
            output = output + "b"
        if data[s1:e1] == "AlItG2aLnaM1zMw^":
            output = output + "c"
        if data[s1:e1] == "e!8(cYtEqEx(esHL":
            output = output + "d"
        if data[s1:e1] == "PYrVn@39SRFs?Q@v":
            output = output + "e"
        if data[s1:e1] == ")m_w%n*gT`FMF<5a":
            output = output + "f"
        if data[s1:e1] == ">o&Cky!4IQL&309c":
            output = output + "g"
        if data[s1:e1] == "KbMoy6gl^+PP<YwU":
            output = output + "h"
        if data[s1:e1] == "l66_-g4'''d'0Ar:":
            output = output + "i"
        if data[s1:e1] == "4B}Xu$-H.oO5Wj_c":
            output = output + "j"
        if data[s1:e1] == "+u~'$6dIW1m~1kjj":
            output = output + "k"
        if data[s1:e1] == ",bdw.Y0,>bC%~]xv":
            output = output + "l"
        if data[s1:e1] == "'Hj!,}1Bz/% nt`W":
            output = output + "m"
        if data[s1:e1] == "A$F[_)'n)]q.2Yr)":
            output = output + "n"
        if data[s1:e1] == "XFw0ay,0-F>V8Rk3":
            output = output + "o"
        if data[s1:e1] == "Nn{9V3m'`o%AK<5C":
            output = output + "p"
        if data[s1:e1] == "qeVc:N`@pWJW@GHM":
            output = output + "q"
        if data[s1:e1] == "g+oxaqUima<}S`-P":
            output = output + "r"
        if data[s1:e1] == "g+%!dCK4N[xRk^W2":
            output = output + "s"
        if data[s1:e1] == "((^Tp0upeqP/4N.v":
            output = output + "t"
        if data[s1:e1] == "uh,e`ME_=p&v_A!/":
            output = output + "u"
        if data[s1:e1] == "fZ:!)zD01_>=L}75":
            output = output + "v"
        if data[s1:e1] == "{K*Mjf_KeS3ii5Ry":
            output = output + "w"
        if data[s1:e1] == "Q#Kl8>m0E4P&cgQW":
            output = output + "x"
        if data[s1:e1] == "q'LB'f?t(U-D&nWK":
            output = output + "y"
        if data[s1:e1] == "Gqj'-mMYTY M!+/l":
            output = output + "z"
        if data[s1:e1] == "sI=zi.As%E_R $Y?":
            output = output + "A"
        if data[s1:e1] == "('[b!3!hSO~7rmLN":
            output = output + "B"
        if data[s1:e1] == "{R2T8'Z?)UG[O*F{":
            output = output + "C"
        if data[s1:e1] == "pXIzr&Wg?E6<)O2N":
            output = output + "D"
        if data[s1:e1] == "OLtPg#S0Jg6'v2]I":
            output = output + "E"
        if data[s1:e1] == "k.,V3 =]:Nb'3`#B":
            output = output + "F"
        if data[s1:e1] == "RGlC2,aInJl#_#RU":
            output = output + "G"
        if data[s1:e1] == "'w'gIMR^21s7hyaG":
            output = output + "H"
        if data[s1:e1] == ">hN{ `AXXD]7kXSK":
            output = output + "I"
        if data[s1:e1] == "TB!Ps yNus~[S$i-":
            output = output + "J"
        if data[s1:e1] == "*`81[D!MDQMQvX2w":
            output = output + "K"
        if data[s1:e1] == "jA6,F/5k7MV#}HAS":
            output = output + "L"
        if data[s1:e1] == "O[z*W)zct]kN]j.f":
            output = output + "M"
        if data[s1:e1] == "c*}=Q.jXV>lmi@y?":
            output = output + "N"
        if data[s1:e1] == "5*t{:[6)8&zTo1Q)":
            output = output + "O"
        if data[s1:e1] == "HW'c),sTXu(C/hb_":
            output = output + "P"
        if data[s1:e1] == "Yi%!@l0?eFVO9_yf":
            output = output + "Q"
        if data[s1:e1] == "v%g6vt$iu wr~hT0":
            output = output + "R"
        if data[s1:e1] == "'HXI~-:f6/q.+W~5":
            output = output + "S"
        if data[s1:e1] == "75ja:yi~Be<) //4":
            output = output + "T"
        if data[s1:e1] == "/m%JaE?]HkhUYmiU":
            output = output + "U"
        if data[s1:e1] == "s@hq}&db'wr}9G/^":
            output = output + "V"
        if data[s1:e1] == "EDZ$lA w]@:8s8K8":
            output = output + "W"
        if data[s1:e1] == ",EQ,*,X}Ap( HR %":
            output = output + "X"
        if data[s1:e1] == ".zth& E^Ej:>a(n3":
            output = output + "Y"
        if data[s1:e1] == "AXZ*v4J+l'm=z&4{":
            output = output + "Z"
        if data[s1:e1] == "6b6~{g-~cdP*7@Ga":
            output = output + "1"
        if data[s1:e1] == "@(wQcBz/Ih[oJUu(":
            output = output + "2"
        if data[s1:e1] == "H9[V>`W^n3f/P[k#":
            output = output + "3"
        if data[s1:e1] == "qViZb(=iW7O#2^>x":
            output = output + "4"
        if data[s1:e1] == "9%epq=/FH'k?+{Jx":
            output = output + "5"
        if data[s1:e1] == "ch8}`?r:%28G182a":
            output = output + "6"
        if data[s1:e1] == "fU_DIR]wn%TKdo`B":
            output = output + "7"
        if data[s1:e1] == "+TuQ2yj eKdEd$+=":
            output = output + "8"
        if data[s1:e1] == "t1x4fJD@w.fNxkwa":
            output = output + "9"
        if data[s1:e1] == "$N!8W$16QZAOYF@W":
            output = output + "0"
        if data[s1:e1] == ")BUdeFiR`Nkc-E'>":
            output = output + "`"
        if data[s1:e1] == "/G4yHvg$Q}bO627@":
            output = output + "!"
        if data[s1:e1] == "vbl)pPLZ>Z&C>x9}":
            output = output + "'"
        if data[s1:e1] == "ZopPq{^S&rg']o[Q":
            output = output + "$"
        if data[s1:e1] == "]sOs(pX[G~cK<=uO":
            output = output + "%"
        if data[s1:e1] == "UtO}M=P3oB52~S+!":
            output = output + "^"
        if data[s1:e1] == "eVu?fnR>*@=d`x'S":
            output = output + "&"
        if data[s1:e1] == ":LZDD/Ef{`t 73x8":
            output = output + "*"
        if data[s1:e1] == "L>_Zk^tLly:Z<[^J":
            output = output + "("
        if data[s1:e1] == "CB--{.iiC<TmV,,8":
            output = output + ")"
        if data[s1:e1] == "UppH4w,FqRRD=9Bb":
            output = output + "_"
        if data[s1:e1] == "<-p#%n@*yM_9^K:'":
            output = output + "+"
        if data[s1:e1] == "OX P7+g^k7h>1z{e":
            output = output + "-"
        if data[s1:e1] == "v'mCirIC-EpY^PhY":
            output = output + "="
        if data[s1:e1] == "dtqo&*=?'vaC9Nz!":
            output = output + "{"
        if data[s1:e1] == "#XGhoIc3+T{xUnCr":
            output = output + "["
        if data[s1:e1] == "B5rL7^o$7x#(tAd2":
            output = output + "]"
        if data[s1:e1] == "9*}Jju']4IxQccTh":
            output = output + "}"
        if data[s1:e1] == "Dd1rJ#G<jZf&54<$":
            output = output + ":"
        if data[s1:e1] == "-pv-sCZ]d}zK'[H:":
            output = output + "'"
        if data[s1:e1] == "D]#.,s+9(NfFdR9$":
            output = output + "@"
        if data[s1:e1] == "(#1?AwVIxGO+mux!":
            output = output + "#"
        if data[s1:e1] == "{Hv0tnV$3'. r+9z":
            output = output + "~"
        if data[s1:e1] == "JbVy5YSy&54$:eBF":
            output = output + "/"
        if data[s1:e1] == "?feC`*qV7*Tn?P3~":
            output = output + "?"
        if data[s1:e1] == "4{lO0T6r5mU=L[qf":
            output = output + "."
        if data[s1:e1] == "So1oMEG.9LT3j0Le":
            output = output + ">"
        if data[s1:e1] == "Dup:hbD]l)G?sA05":
            output = output + ","
        if data[s1:e1] == "Sj%LkU0YI1DQ8C~H":
            output = output + "<"
        if data[s1:e1] == ".<sr@yvZNS%u'bU)":
            output = output + " "
        s1 = s1 + 1
        e1 = e1 + 1
        c1 = c1 + 1
        if data[s1:e1] == "X]1V7dN=bD9'DYrU":
            output = output + "a"
        if data[s1:e1] == "R^~ch$.-[vryRU@-":
            output = output + "b"
        if data[s1:e1] == "z!T qdwGiy1)B4kO":
            output = output + "c"
        if data[s1:e1] == "I7#[{aH^vdxp~0wf":
            output = output + "d"
        if data[s1:e1] == "qcTHOm(dB/7@Vfbe":
            output = output + "e"
        if data[s1:e1] == "F:%!f#`@MMmI(yK'":
            output = output + "f"
        if data[s1:e1] == "UB0P0eQ7R_[YX.x ":
            output = output + "g"
        if data[s1:e1] == "WRHY}V#y5,a.EB=7":
            output = output + "h"
        if data[s1:e1] == "5'rIDk?yez=Fn`m!":
            output = output + "i"
        if data[s1:e1] == "`f~WobEXT'[&C-,7":
            output = output + "j"
        if data[s1:e1] == "xzr]=?5qKNAG*O.N":
            output = output + "k"
        if data[s1:e1] == "~=gX4%%-'o{zF`5I":
            output = output + "l"
        if data[s1:e1] == "JhMJb6R6:mgs]?%X":
            output = output + "m"
        if data[s1:e1] == "Yz`yZJ&a>(~O9'7+":
            output = output + "n"
        if data[s1:e1] == ":'K#,8]It>Zav&2F":
            output = output + "o"
        if data[s1:e1] == "46I}s1A]Yr<S$)qQ":
            output = output + "p"
        if data[s1:e1] == "viv@T4mAGLF3J9pA":
            output = output + "q"
        if data[s1:e1] == "dP'g_mvoZ+ mUDjl":
            output = output + "r"
        if data[s1:e1] == "sJI@Ul[!N(!>DE4y":
            output = output + "s"
        if data[s1:e1] == "Q'V<h_*ua/'8Qy1D":
            output = output + "t"
        if data[s1:e1] == "iI,Bu2'EOSzeA?=t":
            output = output + "u"
        if data[s1:e1] == "!X{r]3BQi1BD6`3_":
            output = output + "v"
        if data[s1:e1] == "Z1bgz}p@Q?C^VLTR":
            output = output + "w"
        if data[s1:e1] == "_tidaKL^xd%CNriq":
            output = output + "x"
        if data[s1:e1] == "zk[!-)NRPlna_,!H":
            output = output + "y"
        if data[s1:e1] == "tbmY>:%(}QShNBy.":
            output = output + "z"
        if data[s1:e1] == "n(6#GV:ckT*&psX,":
            output = output + "A"
        if data[s1:e1] == "{Z+d.*G(C30ab2`6":
            output = output + "B"
        if data[s1:e1] == "GsM:^wHk0,_+I*E.":
            output = output + "C"
        if data[s1:e1] == "8qcE/$b*i~K)`}9}":
            output = output + "D"
        if data[s1:e1] == "zWz^^,nL_tCV9PWx":
            output = output + "E"
        if data[s1:e1] == "VF`s<a`JU7D>LY.1":
            output = output + "F"
        if data[s1:e1] == "84lQ4M'RxkNmEH)>":
            output = output + "G"
        if data[s1:e1] == "GxwbtIU&#H<C3i*'":
            output = output + "H"
        if data[s1:e1] == "APJ7m+c9c1sw8dMf":
            output = output + "I"
        if data[s1:e1] == "Vw0c]5#6t1X~gp7f":
            output = output + "J"
        if data[s1:e1] == ")__9ls8<vL ghhoG":
            output = output + "K"
        if data[s1:e1] == "TeX/5uT7nEL4JZNU":
            output = output + "L"
        if data[s1:e1] == "oXw>F%gS&m4AIG38":
            output = output + "M"
        if data[s1:e1] == "ef~Hnor-C7[nR>hW":
            output = output + "N"
        if data[s1:e1] == "dreQtX2V<F%iw&9~":
            output = output + "O"
        if data[s1:e1] == "krc'!^+Pw81?JG+T":
            output = output + "P"
        if data[s1:e1] == "-)Wg9$L/$b$*J6Pl":
            output = output + "Q"
        if data[s1:e1] == "2DGOf)sfZmWtyTa{":
            output = output + "R"
        if data[s1:e1] == "h4[shug+]Z?%5Swq":
            output = output + "S"
        if data[s1:e1] == "LTMYC<3e}*cdK Sq":
            output = output + "T"
        if data[s1:e1] == "cA0[-b$2#)HsI`p=":
            output = output + "U"
        if data[s1:e1] == "L>a6jrtE~xk}=0D9":
            output = output + "V"
        if data[s1:e1] == "R@nKu9j)c'k.XRdj":
            output = output + "W"
        if data[s1:e1] == "EjV&'@G2Hx'N[2t?":
            output = output + "X"
        if data[s1:e1] == "k'9)GO{:I/4UP&$R":
            output = output + "Y"
        if data[s1:e1] == "qWL5gpaq]OkiVF_H":
            output = output + "Z"
        if data[s1:e1] == "%Jt=@e2pl:U8P<Ck":
            output = output + "1"
        if data[s1:e1] == "+cY,sDZ$u.Yeh5H:":
            output = output + "2"
        if data[s1:e1] == "l*#36/,f<g~-x%-(":
            output = output + "3"
        if data[s1:e1] == "N.l#0])+G&QKzQoS":
            output = output + "4"
        if data[s1:e1] == "J{>h^>$'p5Ynw^l ":
            output = output + "5"
        if data[s1:e1] == "#%ZnztmyugKSa9vi":
            output = output + "6"
        if data[s1:e1] == "`!W=Eu7f@3H`^(yb":
            output = output + "7"
        if data[s1:e1] == "5hQ<$aB2=pu!BS$S":
            output = output + "8"
        if data[s1:e1] == "BozuKFWPYX gM-!6":
            output = output + "9"
        if data[s1:e1] == " o=r(#su1fmSqiih":
            output = output + "0"
        if data[s1:e1] == "Fr}oIWc=U]bjv/'_":
            output = output + "`"
        if data[s1:e1] == "]AEnj(b]!(AK2$D/":
            output = output + "!"
        if data[s1:e1] == "[sEHZ0Eh7cySxPc~":
            output = output + "'"
        if data[s1:e1] == "`{A0Pjt.KN& v-%:":
            output = output + "$"
        if data[s1:e1] == "A-CsMZy6t>o13jJi":
            output = output + "%"
        if data[s1:e1] == "/ }${{~wUD[/fu?Y":
            output = output + "^"
        if data[s1:e1] == "8(+gBl/jTMRXdurp":
            output = output + "&"
        if data[s1:e1] == "wY[?~6Z.n.}=?vJV":
            output = output + "*"
        if data[s1:e1] == "dOXeNMTx=W&v3M4>":
            output = output + "("
        if data[s1:e1] == "o*BS%6,K8'3_2ZQ'":
            output = output + ")"
        if data[s1:e1] == "W)F#{+*EjuOM@^@l":
            output = output + "_"
        if data[s1:e1] == "0k{TNVD0<bdUC+Vj":
            output = output + "+"
        if data[s1:e1] == ".f)^Ip5(814HRc:m":
            output = output + "-"
        if data[s1:e1] == "}Bf2OuneKwn-U7xr":
            output = output + "="
        if data[s1:e1] == "8U)peC2A@KeMSO$}":
            output = output + "{"
        if data[s1:e1] == "u{ZOe,zpLDz'wak3":
            output = output + "["
        if data[s1:e1] == "^e8qROoFIF38!5Uq":
            output = output + "]"
        if data[s1:e1] == "Mty!Pg?C?9N4C:R(":
            output = output + "}"
        if data[s1:e1] == "Ho%l0> },Xlr<?B_":
            output = output + ":"
        if data[s1:e1] == "gE(]-LCl'A,>LPbM":
            output = output + "'"
        if data[s1:e1] == "a9AF6AlPTD*& 'B2":
            output = output + "@"
        if data[s1:e1] == "!<L]W/[3 <<&}Wnk":
            output = output + "#"
        if data[s1:e1] == ":'O1xZ'wiJ3:`i%8":
            output = output + "~"
        if data[s1:e1] == "k5#Ljv2o9 1q[h=O":
            output = output + "/"
        if data[s1:e1] == "/+5?vQq @#.N'}&q":
            output = output + "?"
        if data[s1:e1] == "^'sm`h@YyY'[ n6{":
            output = output + "."
        if data[s1:e1] == "p{&7*oQfQ)p>VG?j":
            output = output + ">"
        if data[s1:e1] == "$:0]J4xdTv0K,G+'":
            output = output + ","
        if data[s1:e1] == "-P*_x/SWSzj*,+/v":
            output = output + "<"
        if data[s1:e1] == "{_^1jC~:5#'<4@~F":
            output = output + " "
        s1 = s1 + 1
        e1 = e1 + 1
        c1 = c1 + 1
        if data[s1:e1] == "u3j/CdB_3/tMU/>9":
            output = output + "a"
        if data[s1:e1] == "Dl!!8R#@Er&rL&*m":
            output = output + "b"
        if data[s1:e1] == "TLcuMu.Xj iIoq`-":
            output = output + "c"
        if data[s1:e1] == "Z%tRl{.KMg$Lw2Q7":
            output = output + "d"
        if data[s1:e1] == "~-?Pt$0'[~>T' vy":
            output = output + "e"
        if data[s1:e1] == ",$g'ZVX!g('[gX6S":
            output = output + "f"
        if data[s1:e1] == "r79P8MrY7N5HqU $":
            output = output + "g"
        if data[s1:e1] == "^BpZ#1g*z1z6y*o&":
            output = output + "h"
        if data[s1:e1] == "8_q%Lwx( ,I0+JjM":
            output = output + "i"
        if data[s1:e1] == "0,pVvRp*9u:,mICI":
            output = output + "j"
        if data[s1:e1] == "a5:]KoZBH0ZY`(BO":
            output = output + "k"
        if data[s1:e1] == ">iuHQar0k`S2T(Ju":
            output = output + "l"
        if data[s1:e1] == "VG#olvLi%%aEY7tk":
            output = output + "m"
        if data[s1:e1] == "jL0:Fd#AU#8[B1z@":
            output = output + "n"
        if data[s1:e1] == "Yu=e`H@u,MXAek[A":
            output = output + "o"
        if data[s1:e1] == "-M7  ~K[]3s`8Rd^":
            output = output + "p"
        if data[s1:e1] == "[MIR]vf^G]<.`*!S":
            output = output + "q"
        if data[s1:e1] == ">G7MWqwU2O_.hY4=":
            output = output + "r"
        if data[s1:e1] == "J^xd}PAC6&*WT]5_":
            output = output + "s"
        if data[s1:e1] == "S2LMj+kJ_bIr4opW":
            output = output + "t"
        if data[s1:e1] == "!ChlX{B4p#lU'^sC":
            output = output + "u"
        if data[s1:e1] == "*'Ed36@Q-n3pt1fA":
            output = output + "v"
        if data[s1:e1] == "xcQNKMwS{HGB9K`3":
            output = output + "w"
        if data[s1:e1] == "wm}lOxZRh=Tq>w}%":
            output = output + "x"
        if data[s1:e1] == "/ dF-!#t6eV?qIkF":
            output = output + "y"
        if data[s1:e1] == "rFRR2[wH(:7O+8Z.":
            output = output + "z"
        if data[s1:e1] == ":0r&zCLQ,}5=D!!]":
            output = output + "A"
        if data[s1:e1] == "V@7@X~~sHFYCr83U":
            output = output + "B"
        if data[s1:e1] == "_<&}yG,'d $o-O+g":
            output = output + "C"
        if data[s1:e1] == "t~lMw@u$v!asiy]g":
            output = output + "D"
        if data[s1:e1] == "Sk18X/.>/LvT+z:n":
            output = output + "E"
        if data[s1:e1] == "Ak@i.j b'=@<aU4:":
            output = output + "F"
        if data[s1:e1] == "@3+&G:'b*NwoTb2`":
            output = output + "G"
        if data[s1:e1] == "t9HlZ'N=k_z}4i$#":
            output = output + "H"
        if data[s1:e1] == "'g{QP?L<cK%9O/oZ":
            output = output + "I"
        if data[s1:e1] == "NcFn+/'KiAxsqZeP":
            output = output + "J"
        if data[s1:e1] == "}W/o,sVn=&2G-w=>":
            output = output + "K"
        if data[s1:e1] == "0kzzqf05{{<:#(j6":
            output = output + "L"
        if data[s1:e1] == "O_Nk9zaUP%WYpgM)":
            output = output + "M"
        if data[s1:e1] == "=qBrK8DO1,13Og~o":
            output = output + "N"
        if data[s1:e1] == "!eVDB?W)(aJ)9U3B":
            output = output + "O"
        if data[s1:e1] == "fa%vKxX{Aqv+gbyt":
            output = output + "P"
        if data[s1:e1] == "MZDhRnnC?l$(&xOe":
            output = output + "Q"
        if data[s1:e1] == ":kV[YK/W5<J*e#`p":
            output = output + "R"
        if data[s1:e1] == "C33YW*10hR>T=/+D":
            output = output + "S"
        if data[s1:e1] == "`./$]apmBl6(7e)J":
            output = output + "T"
        if data[s1:e1] == "E?rQfP^5$0y{KJn4":
            output = output + "U"
        if data[s1:e1] == "1LcTFCcy]4D.}jXb":
            output = output + "V"
        if data[s1:e1] == "^u5O{5sRvEA)BG:(":
            output = output + "W"
        if data[s1:e1] == "s !?8c'Xz+JLilt(":
            output = output + "X"
        if data[s1:e1] == "9&Q{r,b5gAOe3.V^":
            output = output + "Y"
        if data[s1:e1] == "PF[9p,T6?1*N+@i`":
            output = output + "Z"
        if data[s1:e1] == "QlWw/'')'AC'>f?,":
            output = output + "1"
        if data[s1:e1] == "aBXDtI1r3n9vwyjg":
            output = output + "2"
        if data[s1:e1] == "c)=E.r6-4175Byq ":
            output = output + "3"
        if data[s1:e1] == "&&546D<:NSPN>vkN":
            output = output + "4"
        if data[s1:e1] == "l@lQ<kiQRQYSFw+0":
            output = output + "5"
        if data[s1:e1] == ")bnA=A'7*z$iCMD~":
            output = output + "6"
        if data[s1:e1] == "/ia+O]3V<Y>R:J:y":
            output = output + "7"
        if data[s1:e1] == "S8}oc??$K.2v'<Y$":
            output = output + "8"
        if data[s1:e1] == "'q<:5Ci+-J51^S#h":
            output = output + "9"
        if data[s1:e1] == "2m?~:G)qghHHwa's":
            output = output + "0"
        if data[s1:e1] == "j6{dl!n^s'Hz^WXs":
            output = output + "`"
        if data[s1:e1] == "VmB)fc-j0dhW9H^9":
            output = output + "!"
        if data[s1:e1] == "~xbNWHI00]7Ssh!U":
            output = output + "'"
        if data[s1:e1] == "xr_W#>~WVoJ7pbj*":
            output = output + "$"
        if data[s1:e1] == "E'Xn!zQc-CxRW'~h":
            output = output + "%"
        if data[s1:e1] == "F4K{z%.JYID5}*H}":
            output = output + "^"
        if data[s1:e1] == "=>NVat0[Idm$8fpq":
            output = output + "&"
        if data[s1:e1] == "e7ufbGX<h>bRX{V9":
            output = output + "*"
        if data[s1:e1] == "+@ZWI1E?Fp%?m%>~":
            output = output + "("
        if data[s1:e1] == "Z[cu24GQ_~4[_bEx":
            output = output + ")"
        if data[s1:e1] == "vvL{A}=JsY#GTu3f":
            output = output + "_"
        if data[s1:e1] == "mI](F-4FNaEuACP'":
            output = output + "+"
        if data[s1:e1] == "GX@)P&%}%{^hsRJf":
            output = output + "-"
        if data[s1:e1] == "HcIpn2TihU8xtkY-":
            output = output + "="
        if data[s1:e1] == "+eN-Txy_E<UmU$in":
            output = output + "{"
        if data[s1:e1] == "I#.hEvr6DEfc>~Q`":
            output = output + "["
        if data[s1:e1] == "1'v_,&s8zKPd?Mws":
            output = output + "]"
        if data[s1:e1] == ",NE''yP4Z(^/Fq`L":
            output = output + "}"
        if data[s1:e1] == "GL=1jjd)UpS''C[-":
            output = output + ":"
        if data[s1:e1] == "_<-zd#oe}pOZd)b_":
            output = output + "'"
        if data[s1:e1] == "2Td]mo{!Oxey<6l]":
            output = output + "@"
        if data[s1:e1] == "nh9L'j2)7(6f%[m}":
            output = output + "#"
        if data[s1:e1] == "dZ%ge`cS8o&}U Sb":
            output = output + "~"
        if data[s1:e1] == "7*y~58kw.m2<V[@E":
            output = output + "/"
        if data[s1:e1] == "yuJ,tcxA*DODYS.f":
            output = output + "?"
        if data[s1:e1] == "x?IPFmfF6B$ty^42":
            output = output + "."
        if data[s1:e1] == "iDmVn%2Q' 6e^ T(":
            output = output + ">"
        if data[s1:e1] == ")H@heUmD_Ng4a!(E":
            output = output + ","
        if data[s1:e1] == "Sf]=aqot#GTbukK`":
            output = output + "<"
        if data[s1:e1] == "[,P 9]K nP/j&G`)":
            output = output + " "
        s1 = s1 + 1
        e1 = e1 + 1
        c1 = c1 + 1
    print(output)
elif leng == 64:
    e1 = 64
    while c1 < l1:
        if data[s1:e1] == "u1*Gt?fd[#~t$2j<NGx.o2&i0_CUZ`3cfR.Lv5L+yOV&Ii{.by#3:c+5'P01#)3_":
            output = output + "a"
        if data[s1:e1] == "^ko'ph%uzs.b.WGWA{^WWtyr(Rxs{XAM(yE29_Hu,eM1Ng#ncl~'8I IPoZ!9yKJ":
            output = output + "b"
        if data[s1:e1] == "*z#Zb>tmt'6a!Ky*#0aMk#ma JPSsg69G*~OQ6</OKX>.xABb:k/9e<]hi H^Md)":
            output = output + "c"
        if data[s1:e1] == "*yAk5%ILJFwB?bzDz1<X> 8]eR-P0#alQk4`*vgTL&iqKx[c7/@~-qbn%Ul8XV&n":
            output = output + "d"
        if data[s1:e1] == "`0oZn,]a)H!vWPk_@#mJcG>ONnAFb)fzBm=GYU=B<=2FsvfvC2{PGM[`'sDI&+B)":
            output = output + "e"
        if data[s1:e1] == "rg'u=uVy$c'X668[y~LewEcZ+ Zo+Os{8_f9Pjj%)y?'B2OI-7Rd[OE7ad:9JGV{":
            output = output + "f"
        if data[s1:e1] == "Ot!3+=X=ICp>:^ `g~TSfd(C`~L0&.c66D'!8/JjL-K[4<i>S}q@:=ohNF~<D}eD":
            output = output + "g"
        if data[s1:e1] == "pg<%lB9E5b=SJ/1<#Z}ao@z(zf`HWs~LB_V*_x@6o'r06(X@~AF.!F,o02~5K5C9":
            output = output + "h"
        if data[s1:e1] == "1NJ(?v4Gqe_@$J}Z5aX'3b%cv'q~'V$azjK}9Bf>QJ1s/AH{GVQ5!O RBPg/?}SS":
            output = output + "i"
        if data[s1:e1] == "tFGH}<z(sqTAI#7Fmv-jRb&J+P' vd8xGEKIP^AH2']V:Lh1CA`N]MW?<si^!gav":
            output = output + "j"
        if data[s1:e1] == "'Uo'i(9=Iv18-WdT03RD$>xFpH,-B8lQfM#9zUG^<zHHT77Oe)*:m1NfBcr(oGh$":
            output = output + "k"
        if data[s1:e1] == "#$K,]A]yR`[GU`?&$O%$Ky)`Dg9#GkvH-cxK*V_PL9rw},wsOIoQ(]1zYn(@OQK0":
            output = output + "l"
        if data[s1:e1] == "roPd&%@<2Kf,,RlR5mbw{&GTN4n:igNHX+4a&U5Vo=I[~mpcTiwC+'h2iF$!s+Ak":
            output = output + "m"
        if data[s1:e1] == "W@SY,&tP'))]jF}(W+ui]K{3UUBCgQ%jV]xCyA^~m7l)}#[9X[Q<.n- K{`8x^om":
            output = output + "n"
        if data[s1:e1] == "N)?-vQ8fBs7.]8Zco_WOQ*CRNK{=_zj37YfD(hbhU=j9`c.)Mx& mPw$o{$KH'YE":
            output = output + "o"
        if data[s1:e1] == "7'wtWqACX]E1OP8q{{<6N=#KcXb^:h(:d6tST/4hZ[u= m4yCi(41qUZhjVExNX9":
            output = output + "p"
        if data[s1:e1] == "x&F?3Insb.xT'&u4hcbO-jNYb6_']?*CIG<e/nPt%4,ax&.@11 LR/usWHvo7}>v":
            output = output + "q"
        if data[s1:e1] == "(<@<Pppdw:=BC#a7:*'Cv'l+/+4maAey)jSK>lU*j.cy'rze4cU,=m!) 9>x()}%":
            output = output + "r"
        if data[s1:e1] == "HZ'jb@Kt,H@0F@'k7GeMNgr{Cro_?&Ei}UkG#*=0R>ww{LaXX2^%[#FQ/5o+13NI":
            output = output + "s"
        if data[s1:e1] == "SDd9XAJ#m]nsL!-+nww~0+*`M:Zol'!f2hH3/f70aYQ%$(_q~&.(^mS[h?GecntU":
            output = output + "t"
        if data[s1:e1] == "KuNQ)PQQ(2R*+P3Gj1Ok:4J7l2:RK}&U I):n6hM=n*.D'IB}E1{Sg2_Fxu75!Xe":
            output = output + "u"
        if data[s1:e1] == "}fc+foRUt7-.`0tAw?jlA.p[,q&K'[F3ZcvjB6E9,ClTXk'f/RNq/i$B>Y&Knlaj":
            output = output + "v"
        if data[s1:e1] == "7urMcAdHNedQ7}Vn7[6.2scz2P%Q/wD+2LmUG3p=/fVV0T`9/Hl&lRmeoN=%hWgJ":
            output = output + "w"
        if data[s1:e1] == "ug*f38sR2n'hWt}^27?>>weX%EKJ@<3FW<G^v?xzatx=8v}'m@FXw(*7cc'0T'0R":
            output = output + "x"
        if data[s1:e1] == "d!`@nX9Yi5JC_ZO7~GyCH>U_y_vAfM@PJEW)K[!m:'a~%2RC$q>bLx_T<+vT %M4":
            output = output + "y"
        if data[s1:e1] == "P,CtyWeWhX%-%Y#xvhr,M'%38eI(0%3!l-mW`mZT=-LCFmi'f8^=nX@~stHqnknK":
            output = output + "z"
        if data[s1:e1] == "2[797 $Vn'P5I~e%'Mub1#Qn7R:56Cf?gd:}u%E_wfEK&vqjL^naaE-glDlIT0/$":
            output = output + "A"
        if data[s1:e1] == "U-WLw_'7/9gGg-]v?4RFg8TM&6%wp9qW@D1Xp~5SpQb@'c<RN.0%^@ipsr&!ND'M":
            output = output + "B"
        if data[s1:e1] == "^~0cQ@9ZY^N^D Xb9f2n s/(VE#uw--jZ~2UYWgg*bv6')h+}1W`@up'V1n2F!*a":
            output = output + "C"
        if data[s1:e1] == "lA3%3!Ju,UU,~/A[[,l?,W-xr'J/CER[FY&R@K9pzG#k4R0_nxoaVx.{_q1q%E/>":
            output = output + "D"
        if data[s1:e1] == "?)q=^ySldTrk/ Eym2Lt &Ou!,_e^(vV8.-r%LtBUqIl<E-F{Fm'71!H=RK'&}%V":
            output = output + "E"
        if data[s1:e1] == "}bZDB'{ycri&gjm'uv5`B_VI]jo_Agy17F*}M'3N:]pbh0:71.J{puJ<$NlO4]#`":
            output = output + "F"
        if data[s1:e1] == "T,HXgr-L=^3M-xqVI'lA^c#vINh({F#>!Rc]4iC{?D7e5}83gI7f?<J9S.M,3#_8":
            output = output + "G"
        if data[s1:e1] == "KZ'kve<,RyIt> &iJ'bTy<X]:8QeI(zf)_/3zrvA%Y-3kb4#gNk~ss53VoQ=T$&t":
            output = output + "H"
        if data[s1:e1] == "=6g52Kl)MSi2[0CvHY[+5f2iQK2Yg)+LbgnxYOgXL=jT<3b'h76Q[4{5z'Cws/MS":
            output = output + "I"
        if data[s1:e1] == "kTEHrI>It'O?2raKO- X:?8+9x~:{Ls'h'~H'7OkZ!2SOrA}{3 m'!YDAiAUk_Bf":
            output = output + "J"
        if data[s1:e1] == "H-ok}0XL>-hEW7RJl5r8Dk:o=z.28j-P/'i^ q]bV39@Pb5S558s5`zn-LYZ+'Vb":
            output = output + "K"
        if data[s1:e1] == "N$$uZvlQ1,uqc#!l]x}K 0Cp%}{nz08B*Do%mceYT`=~-*  G5lVS^n,k*In+_@v":
            output = output + "L"
        if data[s1:e1] == "s`*TorB8%0vVI,l'+h)snJ`--]p'ja_Ug?RjHdvJqakJ+S:X8'O,[4``x[P'pMca":
            output = output + "M"
        if data[s1:e1] == "z$yw UsGP=4NBgt/0rO4)(~@pe8Y9~5>3c=.ezT0~f!!1r7CB:wVPuGaVGF[=h_U":
            output = output + "N"
        if data[s1:e1] == "]#)UR=V^-h4?~*'+]wNJ%j?<(#OGN1DwF db4.6'+YP0i'6e_aEJb$K$=z_'RDy0":
            output = output + "O"
        if data[s1:e1] == "dFL+c[OD]]IGYEm [`Om24@]f$0{4^U&6Nd`F,e*{}Do}_eJitz&6izDI70':!_O":
            output = output + "P"
        if data[s1:e1] == "}/Op<Zp7dV@S{S'E^Y4PdbRih+}E8jlv>pM9fbAPaNaXg/I%kPyV#Bts3.u}>L4'":
            output = output + "Q"
        if data[s1:e1] == "U3~_+ttfrQ1q)!Wf[?jK%M8OuY07v$RrVdt?/C3Uh3,YXC3jaN5=LrzDf!$r*+*=":
            output = output + "R"
        if data[s1:e1] == "f-#a<?jMXnea>W$,$rb?7a?QEk/tg>!MN'fQI6^9zOOqNKf}~0NK6)Jaxh(yZL2Y":
            output = output + "S"
        if data[s1:e1] == "wBu#D(k=SE^0xxigg n>*B`2CO't/F@rlR9('Yxw)k.'x.Kg+Meo<-}gmkTjsk&F":
            output = output + "T"
        if data[s1:e1] == "D'hordB`!b]7xv(PcWDZ-Vjw}EQ?5IuPm=uown%9`j?JCxh35W2:HU4z7pFsF`[^":
            output = output + "U"
        if data[s1:e1] == "`c.tz[}~,`]s-}qW>hWC ]~r_CH$P#G5#G4`vt?1y'WA&97ckAv2orW~krIckhD~":
            output = output + "V"
        if data[s1:e1] == "pAC<=4'0Ds7N+uN~`K,NFk,1k61LWic)<+S8hT:Su4[{9,@#{^2SJ3}+-{/Ja%R*":
            output = output + "W"
        if data[s1:e1] == ">-cC@!o$'TABF.m6AcEh,eZy:F`as-d7IjCsO*[-}8=/)Hy5fF+cn<C]rJg/aDhU":
            output = output + "X"
        if data[s1:e1] == "f$!@T7'rEBOho_Hp^<4YnXyQ)RWY,Wj:-km]kI8&k3N7'PL4(kR+uqxL6CAG2#y'":
            output = output + "Y"
        if data[s1:e1] == "kKH(q^lBRgS+Ye*e,Iiho^Gib+3Ek&5bGxmoFT.(qxX[4Gb.$TY^Lo?a[J]7A{k]":
            output = output + "Z"
        if data[s1:e1] == "j<{KKOz`>m(`]Jm,@hkkz5@XHQGZuuh55>:Ld4VXEhf`fobhi7h 8RN[Hgn9(!j`":
            output = output + "1"
        if data[s1:e1] == "1'9B%f9>]maN/>[/E@!gVulL9zpG-P'er_Txs(!7(1VcD*u(G IX6HLHl1rH6B~T":
            output = output + "2"
        if data[s1:e1] == "MyBZi24pp-P]#{}#lD85RVP8##d2$aW4>d_^ep>zd0(]W.kLfZk*1QR$KY1Og0N~":
            output = output + "3"
        if data[s1:e1] == "~Md}??{YPTsY]wsmtriuzQ`Vv*???@*ef #0yY#8TmQ{iD*y=p#bC>/'Y*N+LgnD":
            output = output + "4"
        if data[s1:e1] == "m'zEYYp(PO+6Knvd}=pCqcGruQ2.Bb'?lL@+t:^Mp1H&wTCOvmD?u^BA@AttMPZ%":
            output = output + "5"
        if data[s1:e1] == "4N5&zY'#F<MF<z4S~'iu)60uOI]4E`%xm:y&UqQ__e JT)A{E]%L.j3Sefu`@:)5":
            output = output + "6"
        if data[s1:e1] == "dmrJeLEy1^)7{Szu6TbGZ/5f-cOp0OA@o}Up:&/ M3xL2cWJk!(nXI9K[A8t@{:Q":
            output = output + "7"
        if data[s1:e1] == "eoZu'@g=<4&}YSI[9b1DXz2Uw[R1h1ecd'N&.j3DgM'*?Q~_Z3QNQ^/{r{S){KlY":
            output = output + "8"
        if data[s1:e1] == "tHh.> n#ig =dLK98>WC:NUqHtR:F](~zFM[q&m_AjGMnNM zM4J:2M$Bh0P<&k4":
            output = output + "9"
        if data[s1:e1] == "rHDe:&+0dq5Df_t..e%cECq#/fVM2+6>Rpw$ser2^wN28m7bE*)TW'GT]4u<i=fz":
            output = output + "0"
        if data[s1:e1] == "Uz$1l.[GpeX$%T&3Go+Md]UBb#),Y6yr)5)X~o*0E'6?aPpbH!$?@vhc'ZHGHnQp":
            output = output + "`"
        if data[s1:e1] == "RE@&wO649l@qnT?'btpapj/fC7q@Jz><qyYO`Q [:9&%cSfCg05+ydz+^[6]S>:F":
            output = output + "!"
        if data[s1:e1] == "jptY%W$wJhcZ<v8w%}NC_jVv3 l_}uO#le_SgUsQ,MS:JTp'AI,PSVE!'[?6[gr#":
            output = output + "'"
        if data[s1:e1] == "r*Ial#S=LSZi{Rh'Z(=ccEoT^/k'm Z$^J]SJPHa:%BPpEQJVio>5Cnye:QUs2ux":
            output = output + "$"
        if data[s1:e1] == "cSF6Xan!SwxwZ&F?K{>M/=)4`R4H&1>KJt^z@[ebb 9SCL*#d90ds68yV}fcl =%":
            output = output + "%"
        if data[s1:e1] == "%%o+8gpP)0jo@:Ll*Z1mDY9-8r)qjvwbM-Z=8rAgD%F<L9L Z?WN(y8gl^#NI'ox":
            output = output + "^"
        if data[s1:e1] == "d~mhA8=A1T$3TYoq:lkf3@d6+DDMA/El .3R X1 xCZqQ?QxwbN`m3a?Wd65otpA":
            output = output + "&"
        if data[s1:e1] == "b&Lf=^tX6wq# f29}Tui~nI0Bt/m).2S$<$<P1Q!4q'k5JIyo_5PpoY6x.`^wxr#":
            output = output + "*"
        if data[s1:e1] == " #j=dui!E+On_Q)eUiFVE'uAK}&:d<aV&:jr9p*a'^lB,O(-[*k6I~~Tzr+3< R6":
            output = output + "("
        if data[s1:e1] == "!i?rG:lM2jwZ ' (H~!~D<HwnW7.BS:T-8uh^OYk'^T'*aQ8-5v,L*iXIH=BLI`d":
            output = output + ")"
        if data[s1:e1] == "$T9!`vlEPo<{Vu1M{.V~gn0SwiBJ.EHv_5LfC:/Lg`T(4`8O&N(iUt,J,3#{!E'R":
            output = output + "_"
        if data[s1:e1] == "8BMRW3lme`>MTHBV{KLtJ_tz u(d&~kvI@}>.H-/Pd4:0 4+z<h-dwsdEUjwup`Y":
            output = output + "+"
        if data[s1:e1] == ":<I2dzeD0#/TQ8W46wMyI5UL0OJs`s8xNt1ZKDwZC7SpXm?5OmyS:[bGGpQq_).s":
            output = output + "-"
        if data[s1:e1] == "Lq>iR^sw?DZ@brLSEiBfxU7=Gfs3FBBR<g.hqh.RyorX[sgCavxc@*MGg8^K4m1Z":
            output = output + "="
        if data[s1:e1] == "Jj7dWNS?Z>#Zw)j'69%b]BW3@)PFbi1$WTl+Sm%A'Kt&?!pEL~.+:<qFWx,.3H,y":
            output = output + "{"
        if data[s1:e1] == "IQ.rOUOJX+<tZ!vcezC&>V9 6qeLekE^^7!'*3BP(bqB9]/WYA9<0RF$f#P[Wxf`":
            output = output + "["
        if data[s1:e1] == "rMFG'd09CB.S !t yQ4PSig[9CJF`6X,^[EuAMGAkQM0l*iC)EyuX>$x,Uxh,aHM":
            output = output + "]"
        if data[s1:e1] == "{O22!eE`wulPnXa=~Cu-vgRUvHL6GAkb]9zFYuMQ'Ul%S,!GR^qZ4-Sx]+q=>z/t":
            output = output + "}"
        if data[s1:e1] == "_3<@]}74D,:L$,Or_P_w.YgH&,-,P!.qjOG5NB~a*QI{i]FEA2iO$uV}:4t+0,}t":
            output = output + ":"
        if data[s1:e1] == "a(g_qD.^5~8z]dS<TP:d$KYX%VQY20?I2@)U[K]W1Z`x,j6ozAd> ~+a[5n6lDm1":
            output = output + "'"
        if data[s1:e1] == "o.wv1{nNZhc/k!vyB$O{<FsU}hDi1/ei>AyZ(iK%zb3iAoDeVCnmjH/sE4Y&J(Dz":
            output = output + "@"
        if data[s1:e1] == "r[]S&nokFp%{Y$RE,sUy!vFBEc% Y8mkz_0T3*a43Wu0^CD}3b?>hUPrc]$x)21>":
            output = output + "#"
        if data[s1:e1] == ",#Cu2/wxriil}-r{7B2HX57(,GD$TQIvb0Zn%KA>h4=XDravs7lJBh]6w*e{a*W!":
            output = output + "~"
        if data[s1:e1] == "mdd'[IsU>q>*TB$VDisUG*CyJm6L])@yznzq,Zt-XH'e[X5gjy]6qJy<X!:_[8p{":
            output = output + "/"
        if data[s1:e1] == "?dKKN&ys%'{hl>MMKDqWP]OSsa#1n`U)x$2yyD{y6XI&d)?(q w3)Ml??}a`hT/{":
            output = output + "?"
        if data[s1:e1] == "]5)~()k3~pv=)oVTsMTsv!~fWj6AV{sHNQnS+f`j)VU$Rp}pa.X?$Zd@wV'}/(Sx":
            output = output + "."
        if data[s1:e1] == "YXi=U}G:%Wte(nv8@s'Zd%R{5(HAY<!@VF@ pU`/=7m9A5FDm)1cA*eUI_xloSXx":
            output = output + ">"
        if data[s1:e1] == "}]6nqBq)_>1{Jw5.wt0E>-5te6-vU9'HBYK_$jWNsb.=HuMY<wV^km8uWd)-[a~S":
            output = output + ","
        if data[s1:e1] == "6ywI*S1o-$J8dXC*8PNZOWc(p'9kp,98qOF~s!F4^:*Dz}_'P7Ie>&Yjl[<QJqY'":
            output = output + "<"
        if data[s1:e1] == "'TZ/+>$p!Fq,!jGA[6V*GDtJQ'V[(Q^/?5W2jRoLZ d/1.UM1B!Z@ptc(f+$4iVj":
            output = output + " "
        s1 = s1 + 64
        e1 = e1 + 64
        c1 = c1 + 64
        if data[s1:e1] == "'sq7?r6>XKoX,9RCRX%N&i[ _) 5>F-+=25C%G39Y4J>'Y['gVzM6_Q6mA&gaT:o":
            output = output + "a"
        if data[s1:e1] == "('Ih,t#/aH*9+N]/}FBw=0-qgLv?pvOCrDZXqw34@~^N?}:4OS ~_w)MG04n.@JA":
            output = output + "b"
        if data[s1:e1] == "{)HyPe?yLG!Alj>w:Cd4{5<8*h#6y%wPuLbi/sDMgW'#(A:rvt4C<2(t2xm'R/4-":
            output = output + "c"
        if data[s1:e1] == "IEV`It9FV+hEiEH(s?J*NU,6kzu9.K3*^sR#n3:jJDi}iqM4!D$uWrMS!2}]4)fr":
            output = output + "d"
        if data[s1:e1] == "F D[qnD-YqhlRU*_v)%Qjl1GNF^Yk?Bk6',57k5D2Fa(1@o{zWjq'6t]!Jz:krxw":
            output = output + "e"
        if data[s1:e1] == "8W&Xxedz>e3@9D-Reql:)Y?6vy!t+( DX8DSdvB(U*G<d{Q3yxfzizN2zb2O={I9":
            output = output + "f"
        if data[s1:e1] == "AV&)'ZeZ{/E`zQ>qE55pM9oFkv&{i'#<1,LzI(S/isx%XQ/EX272+8qwMp3yWm{p":
            output = output + "g"
        if data[s1:e1] == "c<LWEK,#/p1}K1UTqp4GfoWC}g!gzC4Dfp#MgP~gf1@UR L_<X%2Q7Q#B5=7Ot1 ":
            output = output + "h"
        if data[s1:e1] == "I%ADWc1d'(o3[oWcf5Phr.*wS{e>(yVEE9voy#r7ku9cO&*(Y>.Az9'qiQ)_GaL?":
            output = output + "i"
        if data[s1:e1] == "bh]w+0!sXK9r8A,8A%G I={'pwHm3uATJ>'9dZZF!~>uxTzY`@#<[1CC4#KZq*VX":
            output = output + "j"
        if data[s1:e1] == "eVR=k[MNNnWS$xpl,^@U%2YfL*hnV=83sfFoy[VAzB}(MWXV]odF6jF9gq0+A]@Y":
            output = output + "k"
        if data[s1:e1] == "W4QB~]F~NA9HDK&/y@?2dO(=-,zT2sl'Y06[_E,MHi3<>{$]msxcmBm,J%}XQcHR":
            output = output + "l"
        if data[s1:e1] == "!F<I&{GB{.'VKy-'r7+51SE){vh^lR>>'8A`+o>+yi:HMEiR2L@?An=GP::6s3uG":
            output = output + "m"
        if data[s1:e1] == "%G3q4S{[K0W E'}KKaPI]W`.tjl*p,Qc8ZC6X._~!6U`B'nhcLq5R*#^1mp{Pjz[":
            output = output + "n"
        if data[s1:e1] == "To#2(/~5T0SSWcHHdV.f@?^Tlot0mODIhT[TC-@yOs/c-T_8B!JgbDg6I]dY@{U1":
            output = output + "o"
        if data[s1:e1] == "=<^yUm=d{<sy?H?aNu,OWu?>bdb!BCHwB1o?{80M)inV!E=MO%s8*Hk#Y['g7XwC":
            output = output + "p"
        if data[s1:e1] == "R')8EaY,m).137t@.OpT~lolG@N]i1H[IE7DLL?{y'#qjZON_gsJt+'$cy)!q+,#":
            output = output + "q"
        if data[s1:e1] == "V$9LSV)v}j> BaoV1JgZV+Shh8$X7WOws#'Tc&(H&/z34#tDEdoyh$:B/HMagFZy":
            output = output + "r"
        if data[s1:e1] == "5Kj}Y%Zxgm&XNI#9i)Uu5?]'B%Awny]H&:w)<hEoX%H/'Fe-w(,)TU`PseBP}X b":
            output = output + "s"
        if data[s1:e1] == "kSB`KN<H?*yds0Zz68(8&B'hy/'-I@9W=tVt4-}TjbRBOW.xdQy,U/`+b%2I)}0+":
            output = output + "t"
        if data[s1:e1] == "dGLDJRBlbuvo5R. [^^s[cD$k>u2%LOnlVLy/*w9C70T C@x'muu.W)BOVJK i*l":
            output = output + "u"
        if data[s1:e1] == "MD>w]Z9]GR@?a$f -h{ly_/:J{{E%ZznN8Qt&2UURfEQD}:cVE^(YF=RVb$c391q":
            output = output + "v"
        if data[s1:e1] == "h^%sP1@HxdtCYe[OvHGd%+*sWsG.9:e1ah8FR#vj/l<d/GMB+$CDn'ja'u+J~6<j":
            output = output + "w"
        if data[s1:e1] == "gt$KVbX,-4ex07gK!q3aTrQ}*F4OxmOE)tPzj?K-'W&H}*&CyhN]ZANz{#5N%H<x":
            output = output + "x"
        if data[s1:e1] == "VA=AW]q6)T!9~`r1egHL+.7Kh9(yXs*32!P)OaTmAb+52mBup0/!1t&]fbfNIPbO":
            output = output + "y"
        if data[s1:e1] == "Fp_cCg_mx-m7MaOfTh1`Ue*3iM9='97f=>4ub+jSdv9q=-vJ,d+L{G7))I8T'-@0":
            output = output + "z"
        if data[s1:e1] == "3:Y/_ $)+(C^EY[lcl= rM`vE1fIL1t:,'l'6Pb}.]vaULConErB{xb2,T%H8SW[":
            output = output + "A"
        if data[s1:e1] == "hiY>lkA0`JO W=Yc_7rD>Nu2+q(0xf'=P1zbp{p%_cFE8^(4GA0T^VDg3mQg'H*k":
            output = output + "B"
        if data[s1:e1] == ")G*S?Nrv:oB}inpY?wKnG,/ @K.PG.*b`v-*v`0aK*[QGI^UC&(A]e>rM+FQ0=ds":
            output = output + "C"
        if data[s1:e1] == "h?uO%VtWVjwj(MxHflh,ZIl0fQXtp9s?5CGA5b>#$ef*ss{'?8'-gwE[_:alo`1X":
            output = output + "D"
        if data[s1:e1] == "]=4:R&*`w**t^dW_q.b+pP1FRUIZX/Vv'FmD31'y%}aQT39>Nax)>4aFgji9c)''":
            output = output + "E"
        if data[s1:e1] == "?SD-~luI!vs1&Q'*@}}{8:plF),&7 =ji}y(yl0><Tfft()dGu0k%vXi2!_r$Y~.":
            output = output + "F"
        if data[s1:e1] == "cFj?Tn@%7c_FMA g1!+=J<=mtWnPk8G<xf{'xxAy6{m:i0-@n_D`S'NmISDh4kVh":
            output = output + "G"
        if data[s1:e1] == ":)i#Q0>aTP#NLD)U<+}oA<e<Jua.gY^u!W]9Zuv,ZtUT2VkRK=k@cipHae yZa2`":
            output = output + "H"
        if data[s1:e1] == "g<Z}1p#eRO4HVk{[CXZh8LK'<YU$~MBR!cH6 1TG_K^ACdU*m6]Jv4f6LS~xMXOR":
            output = output + "I"
        if data[s1:e1] == "O2HY{%WYLlrBo'/a7Rx[kuBkD+IhEFnKfJ<A%DiX@vxbM.l6ywINT ZP$va6e/'v":
            output = output + "J"
        if data[s1:e1] == "GAg?gmol89diBWzNP'^rtyPI>MV(In'0O&t'u-Ew-JF~~R ZX.DJghra!$G&c(-R":
            output = output + "K"
        if data[s1:e1] == "(`p3Rk_W'6&6re<4wSN&hwy)w66Qf8rX37xFL6r$B}`wz*nn`&)gvnF=aeLyVpH0":
            output = output + "L"
        if data[s1:e1] == "o3^XS4_'?q?]AO!5olWclwf.KND!PdWb+DCAPB#f2k!R0(_9QXhT`'rfwF<`7,HC":
            output = output + "M"
        if data[s1:e1] == "QmIu]TtPj[EYC@'oFAVtXPz)-r!7q!8sHc2*Omuot-3_v^$VKV>eG'$'+%MUB!OC":
            output = output + "N"
        if data[s1:e1] == "Y8*Nl@ueWJ_:]uGh$'n)WZO^-Xf&:I,r1Qf>n@SFV/OF 2m-BhvEuC{/V`sZ4dpt":
            output = output + "O"
        if data[s1:e1] == "r-/^ZQ{DCad`w.wBrLE[6C)8#Q^ZeS'igTdlG-}]'K:(Ji[^if2wn3e5}Y~~(LH=":
            output = output + "P"
        if data[s1:e1] == "ho25PI?CdUY552-qIO$AT1S^FZypk2(@@o0X]:73v@<O ?PA~xdH]X#_=NWCBr'Z":
            output = output + "Q"
        if data[s1:e1] == ",~+f:uyRxRRLzTrgYp6vKl]D2ZVSyV_.FN8Zx5b@HNfS6ks=89Tt5R3,.t'74X=>":
            output = output + "R"
        if data[s1:e1] == "#o`$3o4jQgC.2h98E2w}e5]59<5!X9FGN0a.<e~,/{eh*^0&c3$M`t]jca_V?@8t":
            output = output + "S"
        if data[s1:e1] == "`J^czF.+6u:bab7?USjuYrG!z']d,:ARV/Gv0WLjr%zAi+9BJ{~eGc]FMor4ajx]":
            output = output + "T"
        if data[s1:e1] == "1S)tj(~cpYNuN*'{<{$^[cF1MFlG5=XvjD~rtuN,s?2LWAT*rUWnA.IKJ&ti!<%m":
            output = output + "U"
        if data[s1:e1] == "cgi4kR*!P!~]M-?O-k?+F])^Ud]q!W09RjA '0^fCdHbRTnZ}t8mJ$:SvE~0hvE@":
            output = output + "V"
        if data[s1:e1] == "%Ks($.=?P rna^&hx0&N61[7)k?d`~H4SC.pq8&T>rm]wem+T^0Yu8_,3NF+/C'5":
            output = output + "W"
        if data[s1:e1] == "O(YZM4QpP8RoMS72-8.0e#Tv8Km@?.1>n8d.JI5&g&< 6ZWMZS)!<&:n/6xK#Qj~":
            output = output + "X"
        if data[s1:e1] == "jNae d1%)<i3s?'z/[c *bUv&,l)JZ7nLwvzIlaMUO8t]]vo4rT-k=G~ri=Wz=C4":
            output = output + "Y"
        if data[s1:e1] == "@!Ew_K{s%/l{el{_gszpkf05#oZ]`]1Ja?S!!&]+Oi(%p9r<ImeFGnS.:2xndlN[":
            output = output + "Z"
        if data[s1:e1] == "?Swf`*m>%sc,g43@w<Dp_kUw-:?YiiTD=1(75Fc(U-c.0IYoqB',Js3h'h</(`u/":
            output = output + "1"
        if data[s1:e1] == "m,DWFS~<{iRZwb=H,bX&[~X'QD/C>4FFvpT5u~38J5LkXew2qE=t3akI.)>d*eB@":
            output = output + "2"
        if data[s1:e1] == " -AzhU-'r`YI'5kh[lIp $IW^=/n'3/^+ENIN1f%gsG 0>edO ,QwWe]7Ho2rpIi":
            output = output + "3"
        if data[s1:e1] == ":LbR.0wb-1a:06YTMYeJk>KcM'x>0G'A7ukz%S>5NRhe ?UAu)qf mBLQP#wCtcd":
            output = output + "4"
        if data[s1:e1] == "7lH?k$jCpE3pg:'z5sp*?sJ]=k'jd'(K6tBOW+Leax^'Qzy n6Z%[n$4f#K9_.[v":
            output = output + "5"
        if data[s1:e1] == "k!mFaD_l$<x4R+I3W8V2<>O`Pc<Lie~<FtFJ Q:~YjqhPsQm#SEXQ7G@/`HtuQrS":
            output = output + "6"
        if data[s1:e1] == "L>Aj[*o:$#'u<f#M2fPaZQG''7kH7Hw7ktLYUx^qC :4&7`W<x]eL}hfPkfN~eoE":
            output = output + "7"
        if data[s1:e1] == "ja=']EQ6YKfgW]n%{:@Ii<1fOWA{d{ot+pXp#y)yBjJ}TP B5oNe:Z%nU?6lM}&<":
            output = output + "8"
        if data[s1:e1] == "/clu'A'<s=Y)AUV:g`8aO3*78q]27h+K th#M 6~lPMqbqVdk*Gg3:D=[:m^U4z~":
            output = output + "9"
        if data[s1:e1] == "'0p.-zYTHjvp``T`Bt43.sOVE`9]<T5!2LoePAcx+}IoY07cW^(U&/#J.zeb<jSw":
            output = output + "0"
        if data[s1:e1] == "}`Phjmf(Y9-aUu,JW~m1M$9R&/7f2LKU[EsL,#F_a_mVAO86JCwmZ(J_-c'pXYjl":
            output = output + "`"
        if data[s1:e1] == "5X,f-S!!*qp'=b^!cJS.2Jhm!M*9x(MA0Rj$vx3r/X'PiOiX<}uOsYmo2LJ-%~l$":
            output = output + "!"
        if data[s1:e1] == "wvzJZbmi&A~YAidMe&'(jE}RCZ}#bv6^M62HBO$k*$gmbE+xza%Oj2o%X^RUd1[l":
            output = output + "'"
        if data[s1:e1] == "6jDfi6n+p=<cA82pg[qb.BY%5_4GI'+wksSKR#e%}*@}~Ko!MqpZz&mGDt`v^!5I":
            output = output + "$"
        if data[s1:e1] == "'W4c <2q~Swu`BIU~#:ERG-?kdAS3yonk0]cSg_K*iNtFXav9tg}U5dwTy1$3H$O":
            output = output + "%"
        if data[s1:e1] == "C.u$^$PxneU/[r,x^dM($Q6'){)qMBYi14XV{.JCqRvVf!tg>5oL} OP!$sv.U/i":
            output = output + "^"
        if data[s1:e1] == "izfH}}+Ys{-5Ik-'GKlVxMvU6l9o%RHPP$G9/1qfjnI$*'#B^C`H$*qIrm9R+z@u":
            output = output + "&"
        if data[s1:e1] == ":>(_FpoPR/~QFlM=UT}bs!abdw(<qIt.h4 56GbTGNVODUk~1i`[K/Kr=wfah@R/":
            output = output + "*"
        if data[s1:e1] == "'SsYjfJ>{JQ0ykHBbHuK'mD)3=4,96+&qV6p5Yo0U[*'PSz5hL<$Ej8:9w^Hm2'a":
            output = output + "("
        if data[s1:e1] == "W(e]0CNVkLMfkr&zHk>c`Lyo'u?_IY?#>H^Q^T2<:x^1#}kF{,r8j,s2j-@ymxw^":
            output = output + ")"
        if data[s1:e1] == "9D$@)PD$pGDS*rE!yPr#,gn#[5t$~8Syfz{MXxU,M4/Qc4EBJ1Z{bqK3_0X'}cjr":
            output = output + "_"
        if data[s1:e1] == "w&DC~'%@@Sgn_[1D`K,Z3qIWToN':,V=XxCru*RBI>>)&%6EzL>gH0zl[s&^l`~&":
            output = output + "+"
        if data[s1:e1] == "4t8'Au'j)*[( BYsl7/tpnPL[B:#[p8Md}lWbr$zB%I!4@Yg(l9WjBw1>/2 qe n":
            output = output + "-"
        if data[s1:e1] == "xdnz{n-J59L_W?)OJ#@4Z-W$5zhQZjK%i2hFz}{^zh`77-9<!#T//KUq1~%x$SY@":
            output = output + "="
        if data[s1:e1] == "x1ZC `+rnhQ0+,)MqbqLZ*!m=/Rn*v$?cO{g61j:)^'s]AIdO[x'U.9'Es]?TH@h":
            output = output + "{"
        if data[s1:e1] == "-_EK7 A(}+bWJBsvIEV'Qnp{%`]_aTGAogq='Qb)3S8U'0X>b'X#PS_6P[):c>jZ":
            output = output + "["
        if data[s1:e1] == "uvhr!G5GVU,U'$@^_50[qIA}7'`Mi[e,PgY!+e4n~_y#}Unko4i_JC%Z[=^nt+Kq":
            output = output + "]"
        if data[s1:e1] == "~<Pn@Dzb.` eh6L,wrqU>O<cP+ pP8TD^fA=%XICya&`Sb[FyS@52gmPJu04,J0c":
            output = output + "}"
        if data[s1:e1] == "!1=$QR1q6]Y+%i(Qc7nTyK&hQs$%/r*KQ=_?_#r`k&'1!RQ8uN&/&rc4G@39a7Z'":
            output = output + ":"
        if data[s1:e1] == "[ggX,G~yTI57 :<CR<botpMaQSxCpjLzxi!j>`g3fB!DE=1k_?k`KVX,Z0ceDlX(":
            output = output + "'"
        if data[s1:e1] == "uxUH) ZP6`^QcXR4?vhkQl7]ZT_sumi~.>~HbD5,O`nKCU,3+y@:8Pv..eKn*zc:":
            output = output + "@"
        if data[s1:e1] == "=7au 5'l&Ube!#$ )QVa=8k3ipD*T2>6o>&>wi/D.5<8d#kxLc:'~HB4=d7@bC&O":
            output = output + "#"
        if data[s1:e1] == "O~.m>SBq:dd!sZ#{vs.72q(vYyLU-rkj,lX}P7~]}6F<J,XFNi_/K3U~D?ln.6Z ":
            output = output + "~"
        if data[s1:e1] == "`xS3fw.2-auf6aun^9DRtbb=sx>,^J(Zm8(13>}_[q?(~vw>[Nn~q#xNj)H.s1(E":
            output = output + "/"
        if data[s1:e1] == ")tU^{p'@$bi}y]V%[IaS{GE-vqo:5bzdyV:#CT[ep&zr`.J[96Z+FZJ+!?a:dN#7":
            output = output + "?"
        if data[s1:e1] == "-waD^'3N7Qc_iN:EvGWj&l%)Bo3.^T%''(}h{hkK[m]`0-0~=)Lm7Qi Be_Eg }4":
            output = output + "."
        if data[s1:e1] == "9KXo+G$MW}$fx__2?HN<p3,EpFm/xy#r@Ls.EQ5~@v+AV('o}V#}O8j}bR@+-u b":
            output = output + ">"
        if data[s1:e1] == "A*J5CB%p3'IINaEBu4_2[E-(9eyQRhoNO{n'>J-&%CY?Pl=V@$+BLP9Q&H0dve53":
            output = output + ","
        if data[s1:e1] == "(ed_O ykWt4NG4PCAMDc&*z%fyAJp-gD@6}J2xS/[8UN[MzZCL#0mj],G?SM:fg{":
            output = output + "<"
        if data[s1:e1] == "gM1Gu8mLO79L4gdyVY7CK{9[zK]]~0tL73dLK}?/87SNy:m$-JPFNbswz nENqb7":
            output = output + " "
        s1 = s1 + 64
        e1 = e1 + 64
        c1 = c1 + 64
        if data[s1:e1] == "Mg[ZIq(]-Sn!m3MNCNg^tL:)w8i(0U[ZNF0y_wkm/59'J:F~vBakr`:x-Su(e:%f":
            output = output + "a"
        if data[s1:e1] == "$'%]tpjm ?R{Vf#4o7~k)@tD&k/=8I#H}ENT6^#A8?sDiWI{ld'qvIhNr96~$k_&":
            output = output + "b"
        if data[s1:e1] == "nQiI_+[hLYg}'b+DcS't6O6L[g~1JiV8H'vb:>5)fBd7!iUZ)j3$f^'Z@}nxm4$p":
            output = output + "c"
        if data[s1:e1] == "fjMwo$lob(-y%4>2g[?-ktpziL9JP<DE0Z'M2k)Jql0%zE9_l)]2_0c6$2]d$4LG":
            output = output + "d"
        if data[s1:e1] == "r>-<RJmESr {S4VT,jlf)@E>h.Cc@$F{O9'm<yThy^b'S[X5Ybyt~<<E3bm][]'x":
            output = output + "e"
        if data[s1:e1] == "v==ZN)@kJiHP62+7E0sos.1%N.YO1,q8Tio:w[%rt[C~awcDqg-&tk!G)sjp&8uD":
            output = output + "f"
        if data[s1:e1] == "(Bxp+qTdGgrU<d87*mB<QRP,L@vV+k.u1x_jHds5kiM_^^96S<3?2Vld+Q6UMe>:":
            output = output + "g"
        if data[s1:e1] == "fgxFlJ#sdVZrQ8kB(->:sem#wd}eMP1_Fn:*i?P+Q(c>Aq2wg)8}'j'<5kHc[WxR":
            output = output + "h"
        if data[s1:e1] == "But}YBgtB*xoXr/VAV9~?rto76.l5G:R77QU?2z,7/?>g~ nk[Sge+menZ-$^{F,":
            output = output + "i"
        if data[s1:e1] == "Si`S`&%B>NAID[u4lad5AL%:.!v<[t-4 7?*Jvb42M{_+(3CQ>#Xg'I^AI$*ymN`":
            output = output + "j"
        if data[s1:e1] == "-HiHvs{`pR%Cq2{QC9{l)'6'{(olGcG$9XsF8,]5MOX($yi8'}Q&oE8`>e]fqrmc":
            output = output + "k"
        if data[s1:e1] == "#defBYmBB97(E0:Ct-t5B1?rcy.wD,~czb^asR$',Xf<<jGUt5_7Z6~fEs-5C~66":
            output = output + "l"
        if data[s1:e1] == "IjxZuH@7T,,$3K4~]#F4h0c5?X6zXK=Vm AGNTwlV*L`jNLcdz21g&5LpXg#Y4-1":
            output = output + "m"
        if data[s1:e1] == "p:u0KWHGzG,h3u7xdMWG]5{j&'`W}V-6{fiP.au97+kvw?/rfrpw3yU?3m0UV?<h":
            output = output + "n"
        if data[s1:e1] == " +^Oq@Xp?yz~ ii]O'{Xp`xqW>OMQwPUU7Lt?*+7NZQP0%0,74?Z^b=@>i.9/H78":
            output = output + "o"
        if data[s1:e1] == "%y'XFGM=Y9d:S7{^r&u(+$lLsF1WcUKOj--CE23oT&6rz5wa^0!`v9RoS?)&^tUS":
            output = output + "p"
        if data[s1:e1] == "fTm>E>zS%w9wrz*c_A8b>'nys8>F+x~[H!dn%{%a#a3%i Nxrn_80a`D%0(%NZRE":
            output = output + "q"
        if data[s1:e1] == "0AK'aJH>}c,e:,DO*wD9'dfY&(nCcnH^JOp~n[!4jPC8qFXXj)[[(K<Rg['zYD*X":
            output = output + "r"
        if data[s1:e1] == "Z,mgbZ#wLe2Q#t=zOAhBN'?7Mp~`~c'l#S@b~+!T^<Y++J-0yt(< ,-NkZh&nFDC":
            output = output + "s"
        if data[s1:e1] == "Vk>sLR>&6(2I~AS1r89W-^tG?cT!bC~at:0`q`O'fF ''9MG`hjUD<XDb'nDAA?j":
            output = output + "t"
        if data[s1:e1] == "+yFaOxu7q,_[.P3 P=G8ewlTcM+GH4'T&[ BA!Pb#MZH7! !:OMPh[6l*dkM'Bvs":
            output = output + "u"
        if data[s1:e1] == "gn{[C=''p3KJ=omwyA^a#e8T{QYnfZ-B^cI.Rj93RnkL]'g9isL1qg =JIWALe=A":
            output = output + "v"
        if data[s1:e1] == "KppBL1Tk6k_No^t%F^d[)}XLVY',9dtBIO/+ys.5F?ge rkI0p,681^4<n'}2[T[":
            output = output + "w"
        if data[s1:e1] == "^y .{y0&5M-I<AE~GFRpca8cEul$Jobh'oAIS1USyurU~tC`'^^ 8%ygg4UH#S5A":
            output = output + "x"
        if data[s1:e1] == "CQ1DlFgI)raD=n7zK&jQ9l pHV[?J3tk*k:ZK}zz1sF+q'#?0/ n@OeyvK!L0A$S":
            output = output + "y"
        if data[s1:e1] == "pN{CzfT*`P<,ENy8.ZwT<EF_3L!]wC!6H3yVcPI+R3b.rjX*D?>0??a![WEZTvA(":
            output = output + "z"
        if data[s1:e1] == "}HOu*z]WG/Y@p08B 6U62V~qa`CSaK)YlQTG{kX40+kYdWe0//2HZTI0`qj:}P+M":
            output = output + "A"
        if data[s1:e1] == "&i6]X4Z pH(Z{cRACG2)-fJ_8W~}9W[%+eM1v1sd8@uwbl-J$1_NT*y@op&_anWx":
            output = output + "B"
        if data[s1:e1] == ",txK=[atKV0%f#NG9/(/$eta>.#'&[P$zPPesb?t7Sg&/ /zDQ+JbM$,'16,,<9K":
            output = output + "C"
        if data[s1:e1] == "8r`'Jyu2&kxYb`f>e,1<S$:hM~LWAleQ4dQjHWQmi,mu:V*y6M{M[&iJO<%oCU:&":
            output = output + "D"
        if data[s1:e1] == "mGaJ*oCe Kc=6*:&Eu3g1AE'1jKz3$MtQ%rw~mD#i%N</RgtUB8OsO<TIk`Npvns":
            output = output + "E"
        if data[s1:e1] == "FBHk6uMCQdBZhI)<KturL5_B#boAJ@WC0%  y4$~{]RLNs3rZoexf5$%27=>`wmQ":
            output = output + "F"
        if data[s1:e1] == "K!FY}hoPvINn(2A'nC5&avL]76sC)wVxt@Wz}i@c#j:/P*C3vb:7xA]rQ]i7g)Tx":
            output = output + "G"
        if data[s1:e1] == "4?< /SNoU5jyY#!kolFx):ve/({'aJ^ygnDUWlCD19UH=*H``'oG.}@k[zxZnb.L":
            output = output + "H"
        if data[s1:e1] == "PN1xSK(h-V1(5@K)1#[Yl+}]>c':%[%EcN>*d0z8j_6w}5bg&bUV2Bg_hTh0K}=U":
            output = output + "I"
        if data[s1:e1] == "42>)I#2$r~]{BVR%cz],zXbv`vDp08n:mM3:wN}PkS]jRf~B3I?1f2s~g+mz4+iq":
            output = output + "J"
        if data[s1:e1] == "qGo?)od1lWrxW5^UnU3l&dbz3,/(V2=NSDED[}2fm}WM,g[-V7F2m?d<-9wkc'uB":
            output = output + "K"
        if data[s1:e1] == "N^Cr~wzZjCNsnY<0g!/{'n/K&u_XLOF5FI:4_^cd3ll`P0.9~I)T1UFEL4 PhK#y":
            output = output + "L"
        if data[s1:e1] == "YFU%'R+W?3LoTk?bx)0!uHJn*BZK/7.{22To}3:PD=1q9(}S,23hd (L<ZmV4%-U":
            output = output + "M"
        if data[s1:e1] == "ICPG&BL~d/bu0*n-~wNgXDZ,PyFL[)i,=Uc@>}-^lcn00R^}KLS)&me&g@y8Vs7/":
            output = output + "N"
        if data[s1:e1] == "*H)bQDxZ-,0 3Sf9Gh^q0Mgzylc,M~W#g<sT1Ww'K8<<C*i,d*rVm>yexl-WJj<7":
            output = output + "O"
        if data[s1:e1] == "HtcG=ioKu'@m,tgQ%zy'eRA!Jew.8fuvtQ@}(v4MSFcznrQQ#!-W$)Uvn fTOF0v":
            output = output + "P"
        if data[s1:e1] == "/W#57g&<=.l*PhK=^XQ:>UXf,WmF(uXKDG>q3b#Lb>E$md{~3d?gOmog}e+*9wMX":
            output = output + "Q"
        if data[s1:e1] == "'yzN!%y>3klYQ&wV)=!M^Z)`OlcGP7@2br_Grp{pxni7?v^#KFAC}3xV/,d1AtCl":
            output = output + "R"
        if data[s1:e1] == "3yCitEi^@@Fd#RW}Ram_&dfu>*]+Gj'~v'r&UqvpC<NSU:ON1A&Yum=+l`.Fvb0(":
            output = output + "S"
        if data[s1:e1] == ":f'b/lzzAVeC&U:7.&4_Djy/Y:EY/x.)5MP!sWb$<n/ =4<@_7yCjID],2w<,wVS":
            output = output + "T"
        if data[s1:e1] == "h7(iQho)[UmN<A~WHQk6s's'I-3h_=h{!P14{d_mbc%~N(Dz]H[MQa[K'Zf!D*lY":
            output = output + "U"
        if data[s1:e1] == "a$PLt!i=7>qdBIsH8Xf2f--*67>`n+X's7!O/*oe`ev{Fk ofC9+MQSR/Z^=@j@E":
            output = output + "V"
        if data[s1:e1] == "PlISi_98k^v4Tv]puXv66J!Gn}]l4WFg^kZ.N/dhur1<$I)MKhyV)BKuEdJJss%Q":
            output = output + "W"
        if data[s1:e1] == "a~pP~1OMg)-RUaH-o]QmhsOGB,T{FXHRV9*,e.DXQJ2YTdX x>{2C!QIDVDi'}}G":
            output = output + "X"
        if data[s1:e1] == "e2}o$76 >zwy'Qe!LpBj(LtzKxN596SD. S/Iu['6fGaR'#tUXhw_aKM.K^v'-z#":
            output = output + "Y"
        if data[s1:e1] == "ve!r:'!?}:pT&OL!4'FP,I/%gWvz1$:zB-gKCOh5$Kn#A%x7tr/oF2.a]yN32Ed7":
            output = output + "Z"
        if data[s1:e1] == "6B )o~ca&X3X'6K8 9}hW}%gAiy8y+O06G23`ViHG>3)QKZ`<bdi4I%9m.)$V&e4":
            output = output + "1"
        if data[s1:e1] == "YEEN>Vvd)VN{~ZEZuisgV}0?*qQ=iS-U-RI-(#fJM`{l*Yhx!Jw?l8+}a()b.k`L":
            output = output + "2"
        if data[s1:e1] == "5E/a[{thJ:=4YZ'_s[=j(mWRGxEB4__]Mk0d#^:!]k`9/ipXBm{OW$1VC$8y2TSD":
            output = output + "3"
        if data[s1:e1] == "6x.(y W%8_^ub$jy3Ia/oWi}*RF3Q 5h%VD~mZ-Ybwg~'.@oS@'FUpb:RC][:*c#":
            output = output + "4"
        if data[s1:e1] == "x_g8s(`Xq]]lB['1bx'WzUHqY^ `z+krgr0)V)3=xa9uKsRnO$i$+XkedW{oVF&#":
            output = output + "5"
        if data[s1:e1] == "izay'ikjo9=/R<hXXH4#N{nU}Tt@~w#Jn{T5^ETH9Q%NG:WU<:c@w44e>CAn=GqD":
            output = output + "6"
        if data[s1:e1] == "+q ,bPYu:U -eqrp'5oP?Q.RE=E5fCwH5p5/66SFS*kh3ri`rXwj,1=y?HK^'a=H":
            output = output + "7"
        if data[s1:e1] == "(v_'}{Ej'JTn'''a)2(><P+Im5+<*]aRPPk GVx:.1x::n.Z/cm`M$`~uLoI7s<)":
            output = output + "8"
        if data[s1:e1] == "S}'J'O:h(J>/-Se9 jsNU[D'7-pKtSfxs{^xc* y_l3@_/~:gRI8@z)}YtJD%.+J":
            output = output + "9"
        if data[s1:e1] == "O77X~g^5$cq]qHB$$.xK.Wq8j[1'tuUOAWqFP@Vn=izEG+8Wkx+BCI{v>2zlBto]":
            output = output + "0"
        if data[s1:e1] == "+jUqIEcR9($MlO_<?P`uJ09Sv@Uoe>ZXI%DNUBJ1@OuOJQj=+VJ5k))Cu>G9LhEr":
            output = output + "`"
        if data[s1:e1] == "-z[%nl1Pp?.Z}'V%:}`d2#wsTT!TrZzqFR3-2jL{?J@$Cd]=u*OEW='#IL36wGj4":
            output = output + "!"
        if data[s1:e1] == "Q*G+vv!'D5}QT_3'3'R8=(9P'V>yDlG''p2-b(uME.,BqLR)j3)u}tO3mD^HNlTB":
            output = output + "'"
        if data[s1:e1] == "3]JEWa=ZeA#8WG%L?>uDGa}uJkHR5b<<9kN:0ObX/pu(6i!MEj.evr/S[P+(bcRt":
            output = output + "$"
        if data[s1:e1] == "zYUZ2?[3`+Yhi_' t[V*)-ueW^!N1j'6~7x8ANh_iVfa7@<m>rRC+*$0zD5MsSkP":
            output = output + "%"
        if data[s1:e1] == "SR>'1jhC$,mgnJTC'.5=OB~GfKFyN7a!Cq5tB&WPF_+su=s+ARB:*o__&6#GT/5T":
            output = output + "^"
        if data[s1:e1] == "-i41'*zE}Mm^Rz([9@JI7K?ovkP.=ucH#ywvELbrat_7OpEj6Sr]h]w,MKX%G4py":
            output = output + "&"
        if data[s1:e1] == "cLEf`gQB?v!%W!$z6lRs9(.bM<%Q7AA`Vqm**Q!avT956Z~n-tAj$NvA>.`~FY(v":
            output = output + "*"
        if data[s1:e1] == "?`-6=R~]x@IAIrV 0AKEtM1lfaOg,^ta)4^w:b/=8HM/1tk?1J6#q=oH$n]HGhN*":
            output = output + "("
        if data[s1:e1] == ".EpN%Tx]TM1aMOEvd7&=<'s_2e1>U^Hl.i?'hp1n}f3DK{BL]pb5na9t'alcDUyA":
            output = output + ")"
        if data[s1:e1] == "7DMZXSaK.d5Ne61KRnIQ_i}:*YXXqUP&xq4~Lg?{o,.WVO7HpmJ!rUY0UVA2`q#k":
            output = output + "_"
        if data[s1:e1] == "v22 /(RfW)Y47JpA>hYbIy+ru^pX5z=G21P}bI'9EeIFz`k#aGGDiwqZ'$~+i@?X":
            output = output + "+"
        if data[s1:e1] == "Ie$%Fo!]rHi&@bLXk*5e(xuKDf&Jn8uWF/>)'>tsHY`M:#vy4C6c*h}s@'-o8]K#":
            output = output + "-"
        if data[s1:e1] == "@PQ{R.'`{_2!'^J,hr4iug#-@JBx$I3llI.[==Z Nn](X>cYbMxwwBe^d&.OyoRY":
            output = output + "="
        if data[s1:e1] == "Lc4@YVpo3Z(eTi_A'6,BI+@!fhsVh8$&mXv&c_Zj'Ld-*+[KJ! ,OaHG?[H}Of,I":
            output = output + "{"
        if data[s1:e1] == "ZJN#e(O,!N@euWlxYmF2iQ08FcPBV{<}1_O)Ov#*]+(q13Tv^0edrzYsvf.(P=2$":
            output = output + "["
        if data[s1:e1] == "9Hp6w^dG0i(=pTQmfJc3lhq8#]O6@Tph$jMh! YscC?$*x*6O2{<R54SYO}-ZHz$":
            output = output + "]"
        if data[s1:e1] == "UL2D#97,c<mwaeBqX!0Q`5gIfms%yx@!1*tLWYq?nVz~E]vhEc*4!!c$&0wDVS`]":
            output = output + "}"
        if data[s1:e1] == "SX5f5'YGJmsy?X!w .+=-9%E~A~E`# du<CR6%+_,PYpq2'mRRrC+.Fhf/) Axb_":
            output = output + ":"
        if data[s1:e1] == "fNz(Gock_j>Sz@=<a-*cM^'XJp6>Gv,@/YZP@,rBX%fV['3YlEOPUfI@O#t~qAaY":
            output = output + "'"
        if data[s1:e1] == "Lh8*!wd{8oIR pW9]H=4s4S_/$`pDkN8s>JQ_Mh.-'F/serT)HAm!$ K_V}-SuHY":
            output = output + "@"
        if data[s1:e1] == "wn5{?j0{xWoTZMZ~^+zk'}5FmSWS>lTug4n`GKNt0 @{?ELj3I*l&kq7QDfsp4C&":
            output = output + "#"
        if data[s1:e1] == "L>~d]dXAHKkYv=1S'a<599Xa.[JU/!/M[XoWD]GHEP!]8VTo.Eq5/M,r@,#@V<KG":
            output = output + "~"
        if data[s1:e1] == ")e(f:ZIk4Dj]8jz7UI [`t[`^w4PUaAoBvBYj.Fnb+&fy'qfySS5Tx&:w?TAJ<q-":
            output = output + "/"
        if data[s1:e1] == "1eYCOBltQ2A-DILDO`B#Ac5.Lxad^BQ&jR:Ch'Fz?7)m?Eqophqw,/FCj:ZQXX _":
            output = output + "?"
        if data[s1:e1] == "%`4?[4Db%v4j}W@U6YYFj%T#KK'oZRd uY:eEeu2{l6A]g3i{rehP])+E@$ T!qs":
            output = output + "."
        if data[s1:e1] == "ML]_3FSAHN^8fgbLmxr%jfS~9O@6,=104T0,/sPi=ZwL'WU>%J&-6]cbq8'qReFD":
            output = output + ">"
        if data[s1:e1] == "O?lL(Pp.4)rfc1o80/TB%'pq&hLh)'Uvd<!2u#^R599x8dKsx#o&N5_{.(jqm3[&":
            output = output + ","
        if data[s1:e1] == "('``'W9{~2<xr_PBeg{A%:kZKC*Y94u1Cr>b%nu)wAp57d[{ ]CRpbvKnwH/9aB/":
            output = output + "<"
        if data[s1:e1] == "`dC4QhU{0#{PG0]}QpqJ2Q f{_@0hgq}nOsY(m$ov&[(=>O :y8H!*7&2HapZ@in":
            output = output + " "
        s1 = s1 + 64
        e1 = e1 + 64
        c1 = c1 + 64
        if data[s1:e1] == "]d)c!$YLlX)kX:<u7/G>4<Q!]`#Arh0&xi^HZ9X:xkF~+Dpq0VsKqlh-}Pa1 uu^":
            output = output + "a"
        if data[s1:e1] == "D4u',-hHa4YW)_v=qiW+(M,JYw5kCKX,]8gKVfSL3B[=YxNuRJ2&=FATRK$QuE0n":
            output = output + "b"
        if data[s1:e1] == "6kHUN21Sj&YyQ~05e#4:{U+K&Vt i.*((_2EkmyjEV*!bFM=:FI6 $5~PbS]r,2%":
            output = output + "c"
        if data[s1:e1] == "Mmb`BA.sQ'3,trXg[D]mF3AIDa'pca'TkPdx$x{1S/0<EJjO,<RIpa<C2>gC:!9(":
            output = output + "d"
        if data[s1:e1] == "`WyywsSWc'`3&g$b$r<GX%L9d`g8>m<I]iSgBbTo%~vfYBAP7cfu4SN{O+$Z.@cE":
            output = output + "e"
        if data[s1:e1] == "MM8B)-[.$BMm#J(Iqy*?/ISYg#G{a,?mV)-zcnO-XV)N0_sp'OP~^Q@&}<?%!'UI":
            output = output + "f"
        if data[s1:e1] == " o k##X[gv~S<_?YYlb@Kq=pR{`~3hkOF:bHYzjnH]dafjs^obf?,v~N,F+_9mpd":
            output = output + "g"
        if data[s1:e1] == "O]K+eQSC)m7nv4Ko=2Y(k'Cu{0d^N !LnO5.4^='VLvQjXsWKz'bv 7~}MGkl_M'":
            output = output + "h"
        if data[s1:e1] == "x~h5F3o?sH[iI<DDin~y(9{G8L?[h.]*q5's=WeR$fZ4dZ$UXL(m8-^/l@&'6k7S":
            output = output + "i"
        if data[s1:e1] == "nx'U%-^&fwT5URIFnjA^r+5)X!5AyN%V:iHX'%-T{Ol5:lTaMTmxWDT!S`yDO0kW":
            output = output + "j"
        if data[s1:e1] == "[/xw7eK6ERz_wj&%Vop)B.WYvoA(/CpqtflYr4d[K99OK.cF@&G6GK9A}o8JO+_,":
            output = output + "k"
        if data[s1:e1] == "GP[Q,Zrx2eZK}uf0JZHMe3::x5piZVB%M@FWT`WI>oJhnFs@e,_Inhu2A#=fl=^h":
            output = output + "l"
        if data[s1:e1] == "u[YOImxVTG~5 &!*1?R50bVWsvQT`W=_Jf~0MXI1 ldyrB7'E#hJLF.g_{Po?P6]":
            output = output + "m"
        if data[s1:e1] == "9m5}pl)Sk^G/+48@k2-b=+opCCm]nCF`lyl/j2%5(/Nc2}az'*B1$EJ$DA +X?4U":
            output = output + "n"
        if data[s1:e1] == "]-D?`(XE7b8HP_MP3B+7@Kt<e%_-4%:mgb7<)EjDUX G#{z2'OE]Wk*.`}Yr5BAA":
            output = output + "o"
        if data[s1:e1] == "AmM xa'~b:/RZL1]8ROV`<I1((YpaL[8*v#mN^bSA:}bEo:iT^{H**)B$lUF.KRI":
            output = output + "p"
        if data[s1:e1] == "cl8MUPa9qlQwI$Zx^?D3MEz`z'9T7[MnU[:`^JT3JU`wbMcC5~{'Yd7`DxDSL*DG":
            output = output + "q"
        if data[s1:e1] == "li'(F5f-s',_kV#?5hg$>_l:c3F1jhM$ai^RG>vZB6&j3+0I'X5j4l@}9&aHhp^f":
            output = output + "r"
        if data[s1:e1] == "@5d:*88~^'QSF9PaJ1kV1dG#UF.>B5o%]Vu`2LZ1UI>U[9k0`&UKJZ+TI=G2T6OO":
            output = output + "s"
        if data[s1:e1] == "m!GV{:L,<=+<#mw_,94e=}E8PT:b-V&p72Zr4RMz0:/!P0mrGCBE+0/sHJ-6-K1d":
            output = output + "t"
        if data[s1:e1] == "!9]y]zF%W??KwDm:Uf}>Dh)>_{KEV+3qrYVk2~T%]eivCiTv?oS!4.<$0}K:l&6Q":
            output = output + "u"
        if data[s1:e1] == "ODdP6@GSx.:IXth_cqahE1}bv@701^2i 2gj'vdMz#THSmN:Pvoeubr,6wrR@v.v":
            output = output + "v"
        if data[s1:e1] == "Ec0L5ht/Flewx&'1D8Ala7v&^yO%W_TzDp?)Mz((l_i~`*(!gYcj~}#4 H+ys!['":
            output = output + "w"
        if data[s1:e1] == "'Ct33.*B<be9))q^-GzZqXB/p'~(j%]d'/oWn2xF/,Wo>y8Id{4m?Dc~(]}tKwj?":
            output = output + "x"
        if data[s1:e1] == "/RrU~d]&iiCfA:M`IYr@AeTtddKE.UkG*7C<PN+U!^u&RKQ@WA*P_SrK>]{<MG{=":
            output = output + "y"
        if data[s1:e1] == "Rl0=%5B)h{l!wJzu.UQBl3Ue/]B}k wKOJ*AKVJm*~Rk]A*:BrgCIySw_e1&Ou[#":
            output = output + "z"
        if data[s1:e1] == "GbEGxy9uS=v~m}TPYzp$1{!t$#o2s%}pjhQWHun,I/y-*# r[74Hc!y%/iB6IP e":
            output = output + "A"
        if data[s1:e1] == "3N={D<%$9Xs)7iu~K!eA}'~j.cv=%PZ>-8%,[8ut4-J&7T D['7IK!jUGK.'`GO=":
            output = output + "B"
        if data[s1:e1] == "+q?No<Qy#}6elN#6n1'2Am5zwd5r6e6yV.=X'[dv`wBc0wL_{qFZ`MN(RC50$Ke(":
            output = output + "C"
        if data[s1:e1] == "x/ST#G6Art?Dn57=czC^tbQDi>je3CoE2-j7ceC8O K't=P9F>xm&JM#c=7526C)":
            output = output + "D"
        if data[s1:e1] == "[N~CTh^s#0?.Z%KCGV)jwq3{kc/^5z&1%>1(lYg$m ?(Tsrcx^$W4cM~@a5tugdj":
            output = output + "E"
        if data[s1:e1] == "1^!8Pw+k~gS,^PQdBB~`UE<<b7_qly,o{v]NuI(%4g@a[1OgGWD2f~?>4OmAS/qk":
            output = output + "F"
        if data[s1:e1] == "*x*vcwxc 9Etsas4)&2IVjZXZk6W'tq2zcoblyd}H'8w8(x&E-HnN3CZWT8v@)qn":
            output = output + "G"
        if data[s1:e1] == "]C[''Lh'g/#Sn2Dr@=TVFlax'){uGP( 5h??+-'*Lqs~cdq9gao%pI@Ouu+=L,,d":
            output = output + "H"
        if data[s1:e1] == "_1'hD1q=bTTlH7)v[z`Rc&]P)a4 T'BlDVGhIb3dy^4Ar9/=Z0y4JMI'5s:@'U^z":
            output = output + "I"
        if data[s1:e1] == "@xG7Z}}*wT>g@+MX}?G`Z0^JA5g]}qr7z7Hag6Bqn+`Ep3ymka_gW1=7<M*pzp6%":
            output = output + "J"
        if data[s1:e1] == "@RW.j#!*N3)! 8NP-{4_'[L`h[{HP=$:BboGk 6+m/wweAS_d:%-bfv?g~@}HDr!":
            output = output + "K"
        if data[s1:e1] == "SPuE&X[+N25sza&g J#'am}?I@VB~*h2-}50~>bdU8HX?'S}B.{yO.9YC&)ngY1y":
            output = output + "L"
        if data[s1:e1] == "D)550&<@s3hx=.E<&#]{MeHfy~<9Qf]yl>EQWTx>Z_o3gHs{L~w>Sxw57TWGMoB$":
            output = output + "M"
        if data[s1:e1] == "iG]NMfe',<#h5cpC)Q71b} -.x/= NjX}zs%('Q<fHMKOTge8L{iINFNt%YNxXOw":
            output = output + "N"
        if data[s1:e1] == "~'Kntn+Nb`B'895mBzZ&)h1(>mJyZUK?qjpN]rlW)euC^m@AOt^3jyE>qC(Tse''":
            output = output + "O"
        if data[s1:e1] == "0/8 GoNUH+3Fp~!R9?:`HEu?:UWAzD>E?UchJ.Z/IxmV(#z)*os'eg!x!$IxXW:X":
            output = output + "P"
        if data[s1:e1] == "XN'Nj@ZC$kF'd.-pa-k8Sv8oDH4C6aWEZSz#~28Fd_Di0LDWzViXiz%0@rcNX2@-":
            output = output + "Q"
        if data[s1:e1] == "7-E-_Wv4>T<yXQjGN}Qq(Y&nsm~'sa' _hwn[KVY0lH0RD}vY<yKp4W}fi~3XoQ6":
            output = output + "R"
        if data[s1:e1] == "AY$ti)m]uQ,]kLA>9'6v'zFfA`(RFw*RPGW0v0=LB3p(6?JNoSJj{GM7S`f-a?7>":
            output = output + "S"
        if data[s1:e1] == "^?})aj}rejlrqPf&-fkYfE{FHJOj>y_BFkJH(Pc'dr.4J[}f]B-!wtRvQY0,tvvd":
            output = output + "T"
        if data[s1:e1] == "C@_TkNZ,~VDQe:LlXcv[.+5I4GWPj:q@8seSQISFE!&knG+%y9F_:70rvAZV'g.l":
            output = output + "U"
        if data[s1:e1] == "'h~,eDmY[e#A#=C#M{4f0 I2?Wot%CL~Z1>GzE19v1%`]S%sOI2?oklM][vwp-`A":
            output = output + "V"
        if data[s1:e1] == "tH(@R.)8,I*g`OVfWA%{2'4d>5^<<X.<=9>(tp'/&!NgGo}b(f,}amnE734Kt6&S":
            output = output + "W"
        if data[s1:e1] == "9oLdtPgZO{VB5 v]3vR}$f!'4(Oy}F32cO)LwP2T5(l4y6DRhM{SMs,VV{,kAAb~":
            output = output + "X"
        if data[s1:e1] == "(gmWyFx{xtR ya XK]az'O~Aj4tf]s1=Liabb76ff'27H'ol!d7Q-p_o,eu']}:~":
            output = output + "Y"
        if data[s1:e1] == "!YHEMTj#{^stna1sq-K)*?vw@n~^K- {hGlifF*#1qF.yAgWDeQ$~Hw{,Qq>w$3g":
            output = output + "Z"
        if data[s1:e1] == "Oc kt7^'Xje3)AD`S{_1Q@W#fW<i11=0-p2B=G&RAs.>)i-pVc0vJK2 69B5A{y6":
            output = output + "1"
        if data[s1:e1] == "Sq~D1]hzjQj: {Oo.8AhilY1`>N,t9p.t],2jF'[Ys]W~L E-=*i ,o9aX4Jn?s.":
            output = output + "2"
        if data[s1:e1] == "rX=nLSCI)5cCXIxh?Y[)3LK)}C!7gr>8.d-YtBq-KY5RviOpd`*L3Wi+t:>pJeW$":
            output = output + "3"
        if data[s1:e1] == "l#.MUz3dL>T!!JQE'T`poHtzPYj_VnFj%fWZps+R[P HXWF}k->HWMAM2pbQa6kZ":
            output = output + "4"
        if data[s1:e1] == "c0%QF[j,`~{+3A q<e:N>PSa?k}@[xu4zzed yr_&Z/W]f#?:OM*{zQJn'G=c6KJ":
            output = output + "5"
        if data[s1:e1] == "fGhSEJz5irQl#X<dOU^d/o/fBE5=<.6.[{v@`ue3&9.J^6wce:x4g$4k1K4E0NEq":
            output = output + "6"
        if data[s1:e1] == "xjpH,iDbI8T!iC<^g'ttfe'ELyTq$}K#m00ggY6%}H!no_{rxh8'6x2{_X*/P!vj":
            output = output + "7"
        if data[s1:e1] == "rLi_V&LVJ&W[-2'M$b083D_c***zqDhPJaprqg'#wbhwImj7A3Hv5<]sq1n+%5fM":
            output = output + "8"
        if data[s1:e1] == "*e*pU*HTZg%18q8++RYgl3tt'ZSQ3%*8IU%3*QR6,Z,R.Qb}S,BO^f4!Q-^L77/ ":
            output = output + "9"
        if data[s1:e1] == "E/@OucGK:C'Z@$'@L(=T9Q6+qe(&= z:i/{7>$Hor=n`bi}!~wa{Y^=0.6u'/MZ1":
            output = output + "0"
        if data[s1:e1] == "[$U=,wYh)PH[6:_/FpPA9dYl$OR}i&^R'e!u'Vcjd8s3Zi/v>Z1?`:F$6rmb&u6g":
            output = output + "`"
        if data[s1:e1] == "21*,(Ctp%,h7,Lud--/=}5vEqYL:TuPxJkjM{0({9PPd@6E:h]]9'V-n,@D+~7iO":
            output = output + "!"
        if data[s1:e1] == "+$CJ#klTMd7-P!n#mZvu5_:j}os^$,9XnP(G=&?'YgN$k['!khb92N'1'P0s4`nu":
            output = output + "'"
        if data[s1:e1] == "n`r@R<m4Ayyv6Urbyw@AY[]+lj6=okhUs3 IAeF0u3S>0nR'FJEn*8'=v-0m]{69":
            output = output + "$"
        if data[s1:e1] == "8`mDdxzhk<.+dDLU9dAhrZ',x3U_xJ%Nd=MVSaSk!f#.oQ/fmEbLDurZ@2WhDJUF":
            output = output + "%"
        if data[s1:e1] == "8QCFR0CZ!Q wtryL?YO=ff^L&=qKKJHu uVO=*@ZT{*oUfesO&`GR+r'bZl4RP!T":
            output = output + "^"
        if data[s1:e1] == "w@sGsU1p$`PZ Oe&LV6b5-hY,oY?D[l-yta*syNa'xl uG'cGz#6'.JO?J aE!68":
            output = output + "&"
        if data[s1:e1] == "<<$p^*PlJnPV2MLm*LL=}Ts1n$o/m3RZoN4D9B[yH8mMa&4.mo)qpn{O_cWrRfqZ":
            output = output + "*"
        if data[s1:e1] == "X_^_/IUy9V)#n3u z:(+? f>sT3vT]0%`!XmGG7=!o%&^J0G)NH9<9FkaAsU<z#C":
            output = output + "("
        if data[s1:e1] == "/Nrcqc3U~/xueIn/Ux@gGI)Oiq[>27 ~#vQug^KJECV$41IR%ZNdU{]]&W*QKJ$b":
            output = output + ")"
        if data[s1:e1] == "(yJeNS@(7bZW(JR=YK]kI1UX(_j&7YD2$b<.&#/I^W1v<1>(809fN<*Qi%utV>[ ":
            output = output + "_"
        if data[s1:e1] == "wBSr)NU-e=U9)LcpcO}3)rRN)Lh'nV`d3*r0Q*C/x%@%WCI~$#:7V8g!n89CR+)j":
            output = output + "+"
        if data[s1:e1] == "Og6sE+'b>xDksDOi^GXz<sXU8R]gI#A_<S 4BJ+#G+qYS'RzE2SLq*~LHUk_^pr+":
            output = output + "-"
        if data[s1:e1] == "%yIa>N7}@2gwO#GRo.q$x$4o>Jq]<VP(#v'Fb.u?^8la[nfX>SXi(nQSFt<ZUPK`":
            output = output + "="
        if data[s1:e1] == "<'kby+CAhd{[#p4&'VqN*VBt[pc1JDa'l?r6_-b]>'ivD: capJQ:2HA:c:}xoRI":
            output = output + "{"
        if data[s1:e1] == "TzYW2yzVk?bf5h@-y>?hlqC8OiP4l))_0~C33u'Kp':6SeV<!cw?#1(SxL:4O29J":
            output = output + "["
        if data[s1:e1] == "BH3BtejC$e7/%udzI`+$lTEpu.Lk4[,gARla@dE(TkO+AT)_Ca?ctzCO0JER,Fy*":
            output = output + "]"
        if data[s1:e1] == "rw%8'9R'L0ib*n(a2}~.b>!S' dT1RP)!d/K{'HTF@CsWQu2*XNS`.~/3kCTBiQ7":
            output = output + "}"
        if data[s1:e1] == "[j`M}[C=t!(8un9lvMzi`#Eb)wvjT:^%OM,6Y(_HmAt8<EVMht92hJ6,)?cgmt8g":
            output = output + ":"
        if data[s1:e1] == "}Bi>n$HHtcubM?ifwRU@OPDne'ao8{'p.15rk%U<9_9o%NaEQq7Mg'7.&qtw/)p(":
            output = output + "'"
        if data[s1:e1] == "tK>{YwXv!UCTpFrZa$ LHGQ-JZAa4<-=)P,#0[&/J?t=dp'f:$`$D^Qim]Iwf#OH":
            output = output + "@"
        if data[s1:e1] == "!8:S-jQUW^9ox5&Us&@S 6[NI@wX^'vm%3/+Ko~evD$_Whp[x+BP[fdMk,>xamfq":
            output = output + "#"
        if data[s1:e1] == "fFPs5sFc2vQVyqK+=j8245`9cU!CXB3BfIiBi^B,Y?utcX.tcM8.}@`)* R Nk9I":
            output = output + "~"
        if data[s1:e1] == "[S1On%<iY}g6B^v#y<:>zw!nap]xiC+:>AkN^q<[$FfQwC+/R`Qpmh(YINt#H+wQ":
            output = output + "/"
        if data[s1:e1] == "ynm{)FHaN<'o`*UIt:z-tB?cF!0g'j_j8/.e!5''zND:B#w]&)+?BU'E_(-{q2s4":
            output = output + "?"
        if data[s1:e1] == "#1R,4wJ9rZ8737s6LXG]a5HhqMHf1,Vkh5oxX3q?K`lu(1DXjQ]g[lez'sUuobYh":
            output = output + "."
        if data[s1:e1] == ",Lei70Ph^iwKZZos)@j/@]F-%dDcLHN!`K:mProiB>Ca8VRZh}Z42YV<bnm$(*&Y":
            output = output + ">"
        if data[s1:e1] == "1/76rp7y sRY,Xn_TK4+nn3W%-h_gnpx/dE9B]_mC0A$DyzfF>7Zx(1cVx@-z9uB":
            output = output + ","
        if data[s1:e1] == "H0kj@VGF,V~'3 L[UXpbMl5rSAPN1uuwXe+Uy6${,6W#&[ME&wL,G>+0ueLwPtzN":
            output = output + "<"
        if data[s1:e1] == ">/2+y.g6bgWC.?r2[.Fu^Xd*e[!%'z+t_9>R}%`z/Y4Hx2Lr/rsq<6EMI/iqBm$w":
            output = output + " "
        s1 = s1 + 64
        e1 = e1 + 64
        c1 = c1 + 64





#data3 = insert1
#key1 = insert7
#s3 = 0
#e3 = 51
#c3 = 0
#output3 = ""
#length = len(data3)
#while c3 < length:
#    temp = data3[s3:e3]
#    temp = int(temp) / key1
#    temp = str(temp)
#    s3 = s3 + 51
#    e3 = e3 + 51
#    c3 = c3 + 51
#    if len(temp) == 1:
#        temp = "00" + temp
#    if len(temp) == 2:
#        temp = "0" + temp
#    output3 = output3 + str(temp)
#output3 = insert1
#
#
#data4 = output3
#
#data4 = insert1
#
#key2 = insert5
#num1 = data4[0:3]
#num1 = int(num1)
#length = len(data4)
#data4 = data4[3:length]
#data4b = data4[num1:(num1+16)]
#data4 = data4[0:num1] + data4[(num1 + 16):length]

#data4b = str(data4b)
#key2 = str(key2)

#if data4b == key2:
#    data4 = data4
#else:
#    print("thief6")
#    data4 = "null"
#    exit()

#print " "
#print output3

#data3 = output3
#key1 = insert5
#s3 = 0
#e3 = 35
#c3 = 0
#output3 = ""
#length = len(data3)
#while c3 < length:
#    temp = data3[s3:e3]
#    if temp[0:35] == "00000000000000000000000000000000000":
#        temp = temp[35:35]
#    elif temp[0:34] == "0000000000000000000000000000000000":
#        temp = temp[34:35]
#    elif temp[0:33] == "000000000000000000000000000000000":
#        temp = temp[33:35]
#    elif temp[0:32] == "00000000000000000000000000000000":
#        temp = temp[32:35]
#    elif temp[0:31] == "0000000000000000000000000000000":
#        temp = temp[31:35]
#    elif temp[0:30] == "000000000000000000000000000000":
#        temp = temp[30:35]
#    elif temp[0:29] == "00000000000000000000000000000":
#        temp = temp[29:35]
#    elif temp[0:28] == "0000000000000000000000000000":
#        temp = temp[28:35]
#    elif temp[0:27] == "000000000000000000000000000":
#        temp = temp[27:35]
#    elif temp[0:26] == "00000000000000000000000000":
#        temp = temp[26:35]
#    elif temp[0:25] == "0000000000000000000000000":
#        temp = temp[25:35]
#    elif temp[0:24] == "000000000000000000000000":
#        temp = temp[24:35]
#    elif temp[0:23] == "00000000000000000000000":
#        temp = temp[23:35]
#    elif temp[0:22] == "0000000000000000000000":
#        temp = temp[22:35]
#    elif temp[0:21] == "000000000000000000000":
#        temp = temp[21:35]
#    elif temp[0:20] == "00000000000000000000":
#        temp = temp[20:35]
#    elif temp[0:19] == "0000000000000000000":
#        temp = temp[19:35]
#    elif temp[0:18] == "000000000000000000":
#        temp = temp[18:35]
#    elif temp[0:17] == "00000000000000000":
#        temp = temp[17:35]
#    elif temp[0:16] == "0000000000000000":
#        temp = temp[16:35]
#    elif temp[0:15] == "000000000000000":
#        temp = temp[15:35]
#    elif temp[0:14] == "00000000000000":
#        temp = temp[14:35]
#    elif temp[0:13] == "0000000000000":
#        temp = temp[13:35]
#    elif temp[0:12] == "000000000000":
#        temp = temp[12:35]
#    elif temp[0:11] == "00000000000":
#        temp = temp[11:35]
#    elif temp[0:10] == "0000000000":
#        temp = temp[10:35]
#    elif temp[0:9] == "000000000":
#        temp = temp[9:35]
##    elif temp[0:8] == "00000000":
 #       temp = temp[8:35]
 #   elif temp[0:7] == "0000000":
 #       temp = temp[7:35]
 #   elif temp[0:6] == "000000":
 #       temp = temp[6:35]
 ##   elif temp[0:5] == "00000":
  #      temp = temp[5:35]
   # elif temp[0:4] == "0000":
#        temp = temp[4:35]
#    elif temp[0:3] == "000":
#        temp = temp[3:35]
#    elif temp[0:2] == "00":
#        temp = temp[2:35]
#    elif temp[0:1] == "0":
#        temp = temp[1:35]
#    temp2 = int(temp) / int(key1)
#    s3 = s3 + 35
#    e3 = e3 + 35
#    c3 = c3 + 35
#    temp2 = str(temp2)
#    if len(temp2) == 1:
#        temp2 = "00" + temp2
#    if len(temp2) == 2:
#        temp2 = "0" + temp2
#    output3 = output3 + str(temp2)
#    
#print " "
#print output3    
    
data4 = output
key2 = str(insert5)
num1 = data4[0:3]
num1 = int(num1)
length = len(data4)
data4 = data4[3:length]
data4b = data4[num1:(num1+16)]
data4 = data4[0:num1] + data4[(num1 + 16):length]
if data4b != key2:
    print("thief4")
    data4 = "null"
    exit()
elif data4b == key2:
    data4 = data4

#print " "
#print data4
#
#print data4
#data3 = data4
#key1 = insert3
#s3 = 0
#e3 = 19
#c3 = 0
#output3 = ""
#length = len(data3)
#while c3 < length:
#    temp = data3[s3:e3]
#    if temp[0:18] == "000000000000000000":
#        temp = temp[18:19]
#    elif temp[0:17] == "00000000000000000":
#        temp = temp[17:19]
#    elif temp[0:16] == "0000000000000000":
#        temp = temp[16:19]
#    elif temp[0:15] == "000000000000000":
#        temp = temp[15:19]
#    elif temp[0:14] == "00000000000000":
#        temp = temp[14:19]
#    elif temp[0:13] == "0000000000000":
#        temp = temp[13:19]
#    elif temp[0:12] == "000000000000":
#        temp = temp[12:19]
#    elif temp[0:11] == "00000000000":
#        temp = temp[11:19]
#    elif temp[0:10] == "0000000000":
#        temp = temp[10:19]
#    elif temp[0:9] == "000000000":
#        temp = temp[9:19]
#    elif temp[0:8] == "00000000":
#        temp = temp[8:19]
#    elif temp[0:7] == "0000000":
#        temp = temp[7:19]
#    elif temp[0:6] == "000000":
#        temp = temp[6:19]
#    elif temp[0:5] == "00000":
#        temp = temp[5:19]
#    elif temp[0:4] == "0000":
#        temp = temp[4:19]
#    elif temp[0:3] == "000":
#        temp = temp[3:19]
#    elif temp[0:2] == "00":
#        temp = temp[2:19]
#    elif temp[0:1] == "0":
#        temp = temp[1:19]
#    temp2 = int(temp) / key1
#    s3 = s3 + 19
#    e3 = e3 + 19
#    c3 = c3 + 19
#    temp2 = str(temp2)
#    if len(temp2) == 1:
#        temp2 = "00" + temp2
#    if len(temp2) == 2:
#        temp2 = "0" + temp2
#    output3 = output3 + str(temp2)
#
#print output3
data2 = data4
s2 = 0
e2 = 3
c2 = 0
output2 = ""
length2 = len(data2)
while c2 < length2:
    temp1 = data2[s2:e2]
    if temp1[0:1] == "0":
        temp1 = temp1[1:3]
    elif temp1[0:2] == "00":
        temp1 = temp1[2:3]
    temp1 = int(temp1)
    temp2 = chr(temp1)
    temp3 = str(temp2)
    output2 = output2 + temp3
    s2 = s2 + 3
    e2 = e2 + 3
    c2 = c2 + 3

#print output2


data = output2
leng = insert2
s1 = 0
e1 = 1
c1 = 0
output = ""
l1 = len(data)
if leng == 1:
    while c1 < l1:
        if data[s1:e1] == ">":
            output = output + "a"
        if data[s1:e1] == "D":
            output = output + "b"
        if data[s1:e1] == "F":
            output = output + "c"
        if data[s1:e1] == "`":
            output = output + "d"
        if data[s1:e1] == "c":
            output = output + "e"
        if data[s1:e1] == "%":
            output = output + "f"
        if data[s1:e1] == ")":
            output = output + "g"
        if data[s1:e1] == "9":
            output = output + "h"
        if data[s1:e1] == "P":
            output = output + "i"
        if data[s1:e1] == "]":
            output = output + "j"
        if data[s1:e1] == "U":
            output = output + "k"
        if data[s1:e1] == "u":
            output = output + "l"
        if data[s1:e1] == "t":
            output = output + "m"
        if data[s1:e1] == "O":
            output = output + "n"
        if data[s1:e1] == "+":
            output = output + "o"
        if data[s1:e1] == "h":
            output = output + "p"
        if data[s1:e1] == "f":
            output = output + "q"
        if data[s1:e1] == "L":
            output = output + "r"
        if data[s1:e1] == "Z":
            output = output + "s"
        if data[s1:e1] == "V":
            output = output + "t"
        if data[s1:e1] == "[":
            output = output + "u"
        if data[s1:e1] == "W":
            output = output + "v"
        if data[s1:e1] == "_":
            output = output + "w"
        if data[s1:e1] == "8":
            output = output + "x"
        if data[s1:e1] == "~":
            output = output + "y"
        if data[s1:e1] == "/":
            output = output + "z"
        if data[s1:e1] == ",":
            output = output + "A"
        if data[s1:e1] == "C":
            output = output + "B"
        if data[s1:e1] == "R":
            output = output + "C"
        if data[s1:e1] == "H":
            output = output + "D"
        if data[s1:e1] == "2":
            output = output + "E"
        if data[s1:e1] == "k":
            output = output + "F"
        if data[s1:e1] == "b":
            output = output + "G"
        if data[s1:e1] == "!":
            output = output + "H"
        if data[s1:e1] == "I":
            output = output + "I"
        if data[s1:e1] == "3":
            output = output + "J"
        if data[s1:e1] == "m":
            output = output + "K"
        if data[s1:e1] == "#":
            output = output + "L"
        if data[s1:e1] == "N":
            output = output + "M"
        if data[s1:e1] == "X":
            output = output + "N"
        if data[s1:e1] == "r":
            output = output + "O"
        if data[s1:e1] == "0":
            output = output + "P"
        if data[s1:e1] == "1":
            output = output + "Q"
        if data[s1:e1] == "{":
            output = output + "R"
        if data[s1:e1] == "i":
            output = output + "S"
        if data[s1:e1] == "G":
            output = output + "T"
        if data[s1:e1] == "&":
            output = output + "U"
        if data[s1:e1] == "K":
            output = output + "V"
        if data[s1:e1] == "g":
            output = output + "W"
        if data[s1:e1] == "6":
            output = output + "X"
        if data[s1:e1] == "4":
            output = output + "Y"
        if data[s1:e1] == "<":
            output = output + "Z"
        if data[s1:e1] == "T":
            output = output + "1"
        if data[s1:e1] == "5":
            output = output + "2"
        if data[s1:e1] == "s":
            output = output + "3"
        if data[s1:e1] == "v":
            output = output + "4"
        if data[s1:e1] == "=":
            output = output + "5"
        if data[s1:e1] == "?":
            output = output + "6"
        if data[s1:e1] == "@":
            output = output + "7"
        if data[s1:e1] == "x":
            output = output + "8"
        if data[s1:e1] == "y":
            output = output + "9"
        if data[s1:e1] == "^":
            output = output + "0"
        if data[s1:e1] == "S":
            output = output + "`"
        if data[s1:e1] == "Y":
            output = output + "!"
        if data[s1:e1] == "'":
            output = output + "'"
        if data[s1:e1] == "(":
            output = output + "$"
        if data[s1:e1] == "d":
            output = output + "%"
        if data[s1:e1] == "7":
            output = output + "^"
        if data[s1:e1] == "B":
            output = output + "&"
        if data[s1:e1] == "'":
            output = output + "*"
        if data[s1:e1] == "n":
            output = output + "("
        if data[s1:e1] == " ":
            output = output + ")"
        if data[s1:e1] == "w":
            output = output + "_"
        if data[s1:e1] == "A":
            output = output + "+"
        if data[s1:e1] == "J":
            output = output + "-"
        if data[s1:e1] == "j":
            output = output + "="
        if data[s1:e1] == ":":
            output = output + "{"
        if data[s1:e1] == "z":
            output = output + "["
        if data[s1:e1] == "Q":
            output = output + "]"
        if data[s1:e1] == "$":
            output = output + "}"
        if data[s1:e1] == ".":
            output = output + ":"
        if data[s1:e1] == "q":
            output = output + "'"
        if data[s1:e1] == "l":
            output = output + "@"
        if data[s1:e1] == "p":
            output = output + "#"
        if data[s1:e1] == "M":
            output = output + "~"
        if data[s1:e1] == "e":
            output = output + "/"
        if data[s1:e1] == "-":
            output = output + "?"
        if data[s1:e1] == "}":
            output = output + "."
        if data[s1:e1] == "E":
            output = output + ">"
        if data[s1:e1] == "a":
            output = output + ","
        if data[s1:e1] == "*":
            output = output + "<"
        if data[s1:e1] == "o":
            output = output + " "
        s1 = s1 + 1
        e1 = e1 + 1
        c1 = c1 + 1
        if data[s1:e1] == "1":
            output = output + "a"
        if data[s1:e1] == "2":
            output = output + "b"
        if data[s1:e1] == "h":
            output = output + "c"
        if data[s1:e1] == "P":
            output = output + "d"
        if data[s1:e1] == "<":
            output = output + "e"
        if data[s1:e1] == "]":
            output = output + "f"
        if data[s1:e1] == "T":
            output = output + "g"
        if data[s1:e1] == "J":
            output = output + "h"
        if data[s1:e1] == "c":
            output = output + "i"
        if data[s1:e1] == "^":
            output = output + "j"
        if data[s1:e1] == ",":
            output = output + "k"
        if data[s1:e1] == " ":
            output = output + "l"
        if data[s1:e1] == "v":
            output = output + "m"
        if data[s1:e1] == "(":
            output = output + "n"
        if data[s1:e1] == "j":
            output = output + "o"
        if data[s1:e1] == "`":
            output = output + "p"
        if data[s1:e1] == "+":
            output = output + "q"
        if data[s1:e1] == "9":
            output = output + "r"
        if data[s1:e1] == "/":
            output = output + "s"
        if data[s1:e1] == ">":
            output = output + "t"
        if data[s1:e1] == "f":
            output = output + "u"
        if data[s1:e1] == "e":
            output = output + "v"
        if data[s1:e1] == "[":
            output = output + "w"
        if data[s1:e1] == "'":
            output = output + "x"
        if data[s1:e1] == "n":
            output = output + "y"
        if data[s1:e1] == "X":
            output = output + "z"
        if data[s1:e1] == "u":
            output = output + "A"
        if data[s1:e1] == "4":
            output = output + "B"
        if data[s1:e1] == "m":
            output = output + "C"
        if data[s1:e1] == "6":
            output = output + "D"
        if data[s1:e1] == "G":
            output = output + "E"
        if data[s1:e1] == "b":
            output = output + "F"
        if data[s1:e1] == "3":
            output = output + "G"
        if data[s1:e1] == "%":
            output = output + "H"
        if data[s1:e1] == "S":
            output = output + "I"
        if data[s1:e1] == ".":
            output = output + "J"
        if data[s1:e1] == "p":
            output = output + "K"
        if data[s1:e1] == "@":
            output = output + "L"
        if data[s1:e1] == "$":
            output = output + "M"
        if data[s1:e1] == "l":
            output = output + "N"
        if data[s1:e1] == "?":
            output = output + "O"
        if data[s1:e1] == "Q":
            output = output + "P"
        if data[s1:e1] == "W":
            output = output + "Q"
        if data[s1:e1] == "H":
            output = output + "R"
        if data[s1:e1] == "{":
            output = output + "S"
        if data[s1:e1] == "K":
            output = output + "T"
        if data[s1:e1] == "L":
            output = output + "U"
        if data[s1:e1] == "w":
            output = output + "V"
        if data[s1:e1] == "&":
            output = output + "W"
        if data[s1:e1] == ":":
            output = output + "X"
        if data[s1:e1] == "~":
            output = output + "Y"
        if data[s1:e1] == "k":
            output = output + "Z"
        if data[s1:e1] == "I":
            output = output + "1"
        if data[s1:e1] == "M":
            output = output + "2"
        if data[s1:e1] == "_":
            output = output + "3"
        if data[s1:e1] == "q":
            output = output + "4"
        if data[s1:e1] == "a":
            output = output + "5"
        if data[s1:e1] == "g":
            output = output + "6"
        if data[s1:e1] == "D":
            output = output + "7"
        if data[s1:e1] == "E":
            output = output + "8"
        if data[s1:e1] == "U":
            output = output + "9"
        if data[s1:e1] == "*":
            output = output + "0"
        if data[s1:e1] == "r":
            output = output + "`"
        if data[s1:e1] == "0":
            output = output + "!"
        if data[s1:e1] == "'":
            output = output + "'"
        if data[s1:e1] == "=":
            output = output + "$"
        if data[s1:e1] == ")":
            output = output + "%"
        if data[s1:e1] == "N":
            output = output + "^"
        if data[s1:e1] == "8":
            output = output + "&"
        if data[s1:e1] == "Y":
            output = output + "*"
        if data[s1:e1] == "F":
            output = output + "("
        if data[s1:e1] == "t":
            output = output + ")"
        if data[s1:e1] == "B":
            output = output + "_"
        if data[s1:e1] == "o":
            output = output + "+"
        if data[s1:e1] == "d":
            output = output + "-"
        if data[s1:e1] == "C":
            output = output + "="
        if data[s1:e1] == "-":
            output = output + "{"
        if data[s1:e1] == "x":
            output = output + "["
        if data[s1:e1] == "R":
            output = output + "]"
        if data[s1:e1] == "i":
            output = output + "}"
        if data[s1:e1] == "7":
            output = output + ":"
        if data[s1:e1] == "V":
            output = output + "'"
        if data[s1:e1] == "s":
            output = output + "@"
        if data[s1:e1] == "#":
            output = output + "#"
        if data[s1:e1] == "z":
            output = output + "~"
        if data[s1:e1] == "!":
            output = output + "/"
        if data[s1:e1] == "y":
            output = output + "?"
        if data[s1:e1] == "A":
            output = output + "."
        if data[s1:e1] == "}":
            output = output + ">"
        if data[s1:e1] == "5":
            output = output + ","
        if data[s1:e1] == "Z":
            output = output + "<"
        if data[s1:e1] == "O":
            output = output + " "
        s1 = s1 + 1
        e1 = e1 + 1
        c1 = c1 + 1
        if data[s1:e1] == "0":
            output = output + "a"
        if data[s1:e1] == "D":
            output = output + "b"
        if data[s1:e1] == "+":
            output = output + "c"
        if data[s1:e1] == "*":
            output = output + "d"
        if data[s1:e1] == "9":
            output = output + "e"
        if data[s1:e1] == "l":
            output = output + "f"
        if data[s1:e1] == "i":
            output = output + "g"
        if data[s1:e1] == "y":
            output = output + "h"
        if data[s1:e1] == "Q":
            output = output + "i"
        if data[s1:e1] == "U":
            output = output + "j"
        if data[s1:e1] == "[":
            output = output + "k"
        if data[s1:e1] == "t":
            output = output + "l"
        if data[s1:e1] == "Z":
            output = output + "m"
        if data[s1:e1] == "$":
            output = output + "n"
        if data[s1:e1] == "!":
            output = output + "o"
        if data[s1:e1] == "<":
            output = output + "p"
        if data[s1:e1] == "'":
            output = output + "q"
        if data[s1:e1] == "]":
            output = output + "r"
        if data[s1:e1] == "1":
            output = output + "s"
        if data[s1:e1] == "O":
            output = output + "t"
        if data[s1:e1] == "u":
            output = output + "u"
        if data[s1:e1] == " ":
            output = output + "v"
        if data[s1:e1] == "2":
            output = output + "w"
        if data[s1:e1] == "^":
            output = output + "x"
        if data[s1:e1] == "c":
            output = output + "y"
        if data[s1:e1] == "g":
            output = output + "z"
        if data[s1:e1] == "x":
            output = output + "A"
        if data[s1:e1] == "k":
            output = output + "B"
        if data[s1:e1] == "d":
            output = output + "C"
        if data[s1:e1] == ")":
            output = output + "D"
        if data[s1:e1] == "}":
            output = output + "E"
        if data[s1:e1] == "C":
            output = output + "F"
        if data[s1:e1] == ">":
            output = output + "G"
        if data[s1:e1] == "J":
            output = output + "H"
        if data[s1:e1] == "F":
            output = output + "I"
        if data[s1:e1] == "&":
            output = output + "J"
        if data[s1:e1] == "L":
            output = output + "K"
        if data[s1:e1] == "j":
            output = output + "L"
        if data[s1:e1] == "%":
            output = output + "M"
        if data[s1:e1] == "T":
            output = output + "N"
        if data[s1:e1] == "?":
            output = output + "O"
        if data[s1:e1] == "p":
            output = output + "P"
        if data[s1:e1] == "K":
            output = output + "Q"
        if data[s1:e1] == "{":
            output = output + "R"
        if data[s1:e1] == "'":
            output = output + "S"
        if data[s1:e1] == "(":
            output = output + "T"
        if data[s1:e1] == "#":
            output = output + "U"
        if data[s1:e1] == "o":
            output = output + "V"
        if data[s1:e1] == "-":
            output = output + "W"
        if data[s1:e1] == "N":
            output = output + "X"
        if data[s1:e1] == "P":
            output = output + "Y"
        if data[s1:e1] == "W":
            output = output + "Z"
        if data[s1:e1] == "s":
            output = output + "1"
        if data[s1:e1] == "/":
            output = output + "2"
        if data[s1:e1] == ".":
            output = output + "3"
        if data[s1:e1] == "z":
            output = output + "4"
        if data[s1:e1] == "3":
            output = output + "5"
        if data[s1:e1] == "8":
            output = output + "6"
        if data[s1:e1] == ":":
            output = output + "7"
        if data[s1:e1] == "B":
            output = output + "8"
        if data[s1:e1] == "R":
            output = output + "9"
        if data[s1:e1] == "X":
            output = output + "0"
        if data[s1:e1] == "_":
            output = output + "`"
        if data[s1:e1] == "4":
            output = output + "!"
        if data[s1:e1] == "f":
            output = output + "'"
        if data[s1:e1] == "e":
            output = output + "$"
        if data[s1:e1] == "r":
            output = output + "%"
        if data[s1:e1] == "n":
            output = output + "^"
        if data[s1:e1] == "h":
            output = output + "&"
        if data[s1:e1] == "m":
            output = output + "*"
        if data[s1:e1] == "7":
            output = output + "("
        if data[s1:e1] == "E":
            output = output + ")"
        if data[s1:e1] == "5":
            output = output + "_"
        if data[s1:e1] == "H":
            output = output + "+"
        if data[s1:e1] == "V":
            output = output + "-"
        if data[s1:e1] == "b":
            output = output + "="
        if data[s1:e1] == "M":
            output = output + "{"
        if data[s1:e1] == "w":
            output = output + "["
        if data[s1:e1] == "v":
            output = output + "]"
        if data[s1:e1] == "A":
            output = output + "}"
        if data[s1:e1] == "@":
            output = output + ":"
        if data[s1:e1] == "a":
            output = output + "'"
        if data[s1:e1] == "Y":
            output = output + "@"
        if data[s1:e1] == "6":
            output = output + "#"
        if data[s1:e1] == "=":
            output = output + "~"
        if data[s1:e1] == "~":
            output = output + "/"
        if data[s1:e1] == "`":
            output = output + "?"
        if data[s1:e1] == "G":
            output = output + "."
        if data[s1:e1] == "I":
            output = output + ">"
        if data[s1:e1] == "S":
            output = output + ","
        if data[s1:e1] == "q":
            output = output + "<"
        if data[s1:e1] == ",":
            output = output + " "
        s1 = s1 + 1
        e1 = e1 + 1
        c1 = c1 + 1
        if data[s1:e1] == "$":
            output = output + "a"
        if data[s1:e1] == "~":
            output = output + "b"
        if data[s1:e1] == ">":
            output = output + "c"
        if data[s1:e1] == "L":
            output = output + "d"
        if data[s1:e1] == "X":
            output = output + "e"
        if data[s1:e1] == "2":
            output = output + "f"
        if data[s1:e1] == "}":
            output = output + "g"
        if data[s1:e1] == "'":
            output = output + "h"
        if data[s1:e1] == "m":
            output = output + "i"
        if data[s1:e1] == "8":
            output = output + "j"
        if data[s1:e1] == "r":
            output = output + "k"
        if data[s1:e1] == "i":
            output = output + "l"
        if data[s1:e1] == "`":
            output = output + "m"
        if data[s1:e1] == "G":
            output = output + "n"
        if data[s1:e1] == "e":
            output = output + "o"
        if data[s1:e1] == "o":
            output = output + "p"
        if data[s1:e1] == "@":
            output = output + "q"
        if data[s1:e1] == "S":
            output = output + "r"
        if data[s1:e1] == "Z":
            output = output + "s"
        if data[s1:e1] == "?":
            output = output + "t"
        if data[s1:e1] == "g":
            output = output + "u"
        if data[s1:e1] == "Y":
            output = output + "v"
        if data[s1:e1] == "t":
            output = output + "w"
        if data[s1:e1] == "y":
            output = output + "x"
        if data[s1:e1] == "q":
            output = output + "y"
        if data[s1:e1] == "h":
            output = output + "z"
        if data[s1:e1] == "v":
            output = output + "A"
        if data[s1:e1] == "'":
            output = output + "B"
        if data[s1:e1] == "H":
            output = output + "C"
        if data[s1:e1] == "*":
            output = output + "D"
        if data[s1:e1] == "4":
            output = output + "E"
        if data[s1:e1] == "u":
            output = output + "F"
        if data[s1:e1] == "1":
            output = output + "G"
        if data[s1:e1] == "J":
            output = output + "H"
        if data[s1:e1] == "p":
            output = output + "I"
        if data[s1:e1] == "^":
            output = output + "J"
        if data[s1:e1] == "_":
            output = output + "K"
        if data[s1:e1] == "I":
            output = output + "L"
        if data[s1:e1] == "{":
            output = output + "M"
        if data[s1:e1] == "=":
            output = output + "N"
        if data[s1:e1] == ",":
            output = output + "O"
        if data[s1:e1] == "N":
            output = output + "P"
        if data[s1:e1] == "E":
            output = output + "Q"
        if data[s1:e1] == "B":
            output = output + "R"
        if data[s1:e1] == "0":
            output = output + "S"
        if data[s1:e1] == "k":
            output = output + "T"
        if data[s1:e1] == "/":
            output = output + "U"
        if data[s1:e1] == " ":
            output = output + "V"
        if data[s1:e1] == "c":
            output = output + "W"
        if data[s1:e1] == "+":
            output = output + "X"
        if data[s1:e1] == "C":
            output = output + "Y"
        if data[s1:e1] == ":":
            output = output + "Z"
        if data[s1:e1] == "V":
            output = output + "1"
        if data[s1:e1] == "n":
            output = output + "2"
        if data[s1:e1] == "]":
            output = output + "3"
        if data[s1:e1] == "z":
            output = output + "4"
        if data[s1:e1] == "b":
            output = output + "5"
        if data[s1:e1] == "%":
            output = output + "6"
        if data[s1:e1] == "-":
            output = output + "7"
        if data[s1:e1] == "a":
            output = output + "8"
        if data[s1:e1] == "l":
            output = output + "9"
        if data[s1:e1] == "s":
            output = output + "0"
        if data[s1:e1] == "6":
            output = output + "`"
        if data[s1:e1] == "R":
            output = output + "!"
        if data[s1:e1] == "5":
            output = output + "'"
        if data[s1:e1] == "O":
            output = output + "$"
        if data[s1:e1] == "K":
            output = output + "%"
        if data[s1:e1] == "F":
            output = output + "^"
        if data[s1:e1] == "Q":
            output = output + "&"
        if data[s1:e1] == "D":
            output = output + "*"
        if data[s1:e1] == "A":
            output = output + "("
        if data[s1:e1] == "x":
            output = output + ")"
        if data[s1:e1] == "d":
            output = output + "_"
        if data[s1:e1] == ")":
            output = output + "+"
        if data[s1:e1] == "<":
            output = output + "-"
        if data[s1:e1] == ".":
            output = output + "="
        if data[s1:e1] == "M":
            output = output + "{"
        if data[s1:e1] == "[":
            output = output + "["
        if data[s1:e1] == "P":
            output = output + "]"
        if data[s1:e1] == "7":
            output = output + "}"
        if data[s1:e1] == "U":
            output = output + ":"
        if data[s1:e1] == "9":
            output = output + "'"
        if data[s1:e1] == "j":
            output = output + "@"
        if data[s1:e1] == "&":
            output = output + "#"
        if data[s1:e1] == "T":
            output = output + "~"
        if data[s1:e1] == "3":
            output = output + "/"
        if data[s1:e1] == "W":
            output = output + "?"
        if data[s1:e1] == "f":
            output = output + "."
        if data[s1:e1] == "#":
            output = output + ">"
        if data[s1:e1] == "w":
            output = output + ","
        if data[s1:e1] == "(":
            output = output + "<"
        if data[s1:e1] == "!":
            output = output + " "
        s1 = s1 + 1
        e1 = e1 + 1
        c1 = c1 + 1
elif leng == 4:
    e1 = 4
    while c1 < l1:
        if data[s1:e1] == ",3+d":
            output = output + "a"
        if data[s1:e1] == "`z*^":
            output = output + "b"
        if data[s1:e1] == "CTe6":
            output = output + "c"
        if data[s1:e1] == "q9Xi":
            output = output + "d"
        if data[s1:e1] == "[kW9":
            output = output + "e"
        if data[s1:e1] == "5=F3":
            output = output + "f"
        if data[s1:e1] == "8:'o":
            output = output + "g"
        if data[s1:e1] == "uf$n":
            output = output + "h"
        if data[s1:e1] == "6I]6":
            output = output + "i"
        if data[s1:e1] == "Yyj*":
            output = output + "j"
        if data[s1:e1] == "-_?b":
            output = output + "k"
        if data[s1:e1] == "!SG8":
            output = output + "l"
        if data[s1:e1] == "!{h?":
            output = output + "m"
        if data[s1:e1] == "uEl6":
            output = output + "n"
        if data[s1:e1] == "Nl~O":
            output = output + "o"
        if data[s1:e1] == "aP@z":
            output = output + "p"
        if data[s1:e1] == "]3gg":
            output = output + "q"
        if data[s1:e1] == "aM%i":
            output = output + "r"
        if data[s1:e1] == "'%Wq":
            output = output + "s"
        if data[s1:e1] == "E7Ue":
            output = output + "t"
        if data[s1:e1] == "#w.P":
            output = output + "u"
        if data[s1:e1] == "WlLp":
            output = output + "v"
        if data[s1:e1] == "R8.-":
            output = output + "w"
        if data[s1:e1] == "/Ire":
            output = output + "x"
        if data[s1:e1] == "V@)J":
            output = output + "y"
        if data[s1:e1] == "J.~P":
            output = output + "z"
        if data[s1:e1] == "DByu":
            output = output + "A"
        if data[s1:e1] == "He]L":
            output = output + "B"
        if data[s1:e1] == "?$(/":
            output = output + "C"
        if data[s1:e1] == "1}`4":
            output = output + "D"
        if data[s1:e1] == "-Go{":
            output = output + "E"
        if data[s1:e1] == "dJ0<":
            output = output + "F"
        if data[s1:e1] == "'Q=o":
            output = output + "G"
        if data[s1:e1] == "S&0V":
            output = output + "H"
        if data[s1:e1] == "U]av":
            output = output + "I"
        if data[s1:e1] == "c Zw":
            output = output + "J"
        if data[s1:e1] == "s}^Y":
            output = output + "K"
        if data[s1:e1] == "hM=r":
            output = output + "L"
        if data[s1:e1] == "MVJ@":
            output = output + "M"
        if data[s1:e1] == "phBv":
            output = output + "N"
        if data[s1:e1] == "ANB%":
            output = output + "O"
        if data[s1:e1] == "YSDx":
            output = output + "P"
        if data[s1:e1] == "}m:E":
            output = output + "Q"
        if data[s1:e1] == "Uv#8":
            output = output + "R"
        if data[s1:e1] == "(*9x":
            output = output + "S"
        if data[s1:e1] == "yTis":
            output = output + "T"
        if data[s1:e1] == "q?,5":
            output = output + "U"
        if data[s1:e1] == "bczv":
            output = output + "V"
        if data[s1:e1] == "F>X2":
            output = output + "W"
        if data[s1:e1] == "M4sC":
            output = output + "X"
        if data[s1:e1] == "!Fot":
            output = output + "Y"
        if data[s1:e1] == " DW3":
            output = output + "Z"
        if data[s1:e1] == "<H^m":
            output = output + "1"
        if data[s1:e1] == "~'nO":
            output = output + "2"
        if data[s1:e1] == "4YxP":
            output = output + "3"
        if data[s1:e1] == "lGRU":
            output = output + "4"
        if data[s1:e1] == ">)FO":
            output = output + "5"
        if data[s1:e1] == "27/5":
            output = output + "6"
        if data[s1:e1] == "NE:(":
            output = output + "7"
        if data[s1:e1] == "5>Hr":
            output = output + "8"
        if data[s1:e1] == "mZH%":
            output = output + "9"
        if data[s1:e1] == "r&XT":
            output = output + "0"
        if data[s1:e1] == "zwLi":
            output = output + "`"
        if data[s1:e1] == "._R2":
            output = output + "!"
        if data[s1:e1] == "NjBC":
            output = output + "'"
        if data[s1:e1] == "Qm[V":
            output = output + "$"
        if data[s1:e1] == "Kcn7":
            output = output + "%"
        if data[s1:e1] == ">{b ":
            output = output + "^"
        if data[s1:e1] == ")$47":
            output = output + "&"
        if data[s1:e1] == "DK)R":
            output = output + "*"
        if data[s1:e1] == "1(@<":
            output = output + "("
        if data[s1:e1] == "[kAZ":
            output = output + ")"
        if data[s1:e1] == "0~jS":
            output = output + "_"
        if data[s1:e1] == "Gs-p":
            output = output + "+"
        if data[s1:e1] == "ud`Q":
            output = output + "-"
        if data[s1:e1] == "$#}c":
            output = output + "="
        if data[s1:e1] == "K^!g":
            output = output + "{"
        if data[s1:e1] == "#xnk":
            output = output + "["
        if data[s1:e1] == "hI'K":
            output = output + "]"
        if data[s1:e1] == "O_X9":
            output = output + "}"
        if data[s1:e1] == "fb=2":
            output = output + ":"
        if data[s1:e1] == "&{1f":
            output = output + "'"
        if data[s1:e1] == "ZtLj":
            output = output + "@"
        if data[s1:e1] == "'C&*":
            output = output + "#"
        if data[s1:e1] == "a[:T":
            output = output + "~"
        if data[s1:e1] == "+`/,":
            output = output + "/"
        if data[s1:e1] == ",Qp'":
            output = output + "?"
        if data[s1:e1] == "I1 +":
            output = output + "."
        if data[s1:e1] == "+0<A":
            output = output + ">"
        if data[s1:e1] == "w'f_":
            output = output + ","
        if data[s1:e1] == "dqty":
            output = output + "<"
        if data[s1:e1] == "gtkA":
            output = output + " "
        s1 = s1 + 4
        e1 = e1 + 4
        c1 = c1 + 4
        if data[s1:e1] == "nR/d":
            output = output + "a"
        if data[s1:e1] == "yD{V":
            output = output + "b"
        if data[s1:e1] == "G+1+":
            output = output + "c"
        if data[s1:e1] == "3e:R":
            output = output + "d"
        if data[s1:e1] == "0}))":
            output = output + "e"
        if data[s1:e1] == "HqrU":
            output = output + "f"
        if data[s1:e1] == ">F98":
            output = output + "g"
        if data[s1:e1] == "Dxt~":
            output = output + "h"
        if data[s1:e1] == "3#7L":
            output = output + "i"
        if data[s1:e1] == ",&mv":
            output = output + "j"
        if data[s1:e1] == "56B3":
            output = output + "k"
        if data[s1:e1] == "gQ)p":
            output = output + "l"
        if data[s1:e1] == "Ek[w":
            output = output + "m"
        if data[s1:e1] == ":bHR":
            output = output + "n"
        if data[s1:e1] == "'E'=":
            output = output + "o"
        if data[s1:e1] == "{yTG":
            output = output + "p"
        if data[s1:e1] == "X]DS":
            output = output + "q"
        if data[s1:e1] == "s!aa":
            output = output + "r"
        if data[s1:e1] == "r]`2":
            output = output + "s"
        if data[s1:e1] == "uIPh":
            output = output + "t"
        if data[s1:e1] == "9Kug":
            output = output + "u"
        if data[s1:e1] == "<Z4D":
            output = output + "v"
        if data[s1:e1] == "u2OP":
            output = output + "w"
        if data[s1:e1] == "8x O":
            output = output + "x"
        if data[s1:e1] == ", *p":
            output = output + "y"
        if data[s1:e1] == "X}6$":
            output = output + "z"
        if data[s1:e1] == "Qgb.":
            output = output + "A"
        if data[s1:e1] == "70<]":
            output = output + "B"
        if data[s1:e1] == "'kpl":
            output = output + "C"
        if data[s1:e1] == "5yvW":
            output = output + "D"
        if data[s1:e1] == "Cizs":
            output = output + "E"
        if data[s1:e1] == "Fy,h":
            output = output + "F"
        if data[s1:e1] == "d7_~":
            output = output + "G"
        if data[s1:e1] == "/G~R":
            output = output + "H"
        if data[s1:e1] == "v'dz":
            output = output + "I"
        if data[s1:e1] == ":~^M":
            output = output + "J"
        if data[s1:e1] == "f:Ek":
            output = output + "K"
        if data[s1:e1] == "L^xG":
            output = output + "L"
        if data[s1:e1] == "=.m9":
            output = output + "M"
        if data[s1:e1] == "Y{C-":
            output = output + "N"
        if data[s1:e1] == "th$?":
            output = output + "O"
        if data[s1:e1] == "(tf$":
            output = output + "P"
        if data[s1:e1] == "&Z0$":
            output = output + "Q"
        if data[s1:e1] == "(N24":
            output = output + "R"
        if data[s1:e1] == "Kcf-":
            output = output + "S"
        if data[s1:e1] == "IPKx":
            output = output + "T"
        if data[s1:e1] == "Na_b":
            output = output + "U"
        if data[s1:e1] == "8wu(":
            output = output + "V"
        if data[s1:e1] == "JZYj":
            output = output + "W"
        if data[s1:e1] == "T'q4":
            output = output + "X"
        if data[s1:e1] == "dkH#":
            output = output + "Y"
        if data[s1:e1] == "%c1[":
            output = output + "Z"
        if data[s1:e1] == ".MV,":
            output = output + "1"
        if data[s1:e1] == "U>m>":
            output = output + "2"
        if data[s1:e1] == "jelg":
            output = output + "3"
        if data[s1:e1] == "*CnT":
            output = output + "4"
        if data[s1:e1] == "W1c{":
            output = output + "5"
        if data[s1:e1] == "@?ic":
            output = output + "6"
        if data[s1:e1] == "4I8H":
            output = output + "7"
        if data[s1:e1] == "oaVE":
            output = output + "8"
        if data[s1:e1] == "e-=<":
            output = output + "9"
        if data[s1:e1] == "(I^b":
            output = output + "0"
        if data[s1:e1] == "w#. ":
            output = output + "`"
        if data[s1:e1] == "Kf3_":
            output = output + "!"
        if data[s1:e1] == "+Jz=":
            output = output + "'"
        if data[s1:e1] == "-'[l":
            output = output + "$"
        if data[s1:e1] == "AhwP":
            output = output + "%"
        if data[s1:e1] == "Qz7J":
            output = output + "^"
        if data[s1:e1] == "j!ML":
            output = output + "&"
        if data[s1:e1] == "`*%o":
            output = output + "*"
        if data[s1:e1] == "2/ '":
            output = output + "("
        if data[s1:e1] == "?eNO":
            output = output + ")"
        if data[s1:e1] == "<}p*":
            output = output + "_"
        if data[s1:e1] == "SJ+B":
            output = output + "+"
        if data[s1:e1] == "SA`q":
            output = output + "-"
        if data[s1:e1] == "?StX":
            output = output + "="
        if data[s1:e1] == "r6T`":
            output = output + "{"
        if data[s1:e1] == "&LF%":
            output = output + "["
        if data[s1:e1] == "s#YU":
            output = output + "]"
        if data[s1:e1] == "]Zso":
            output = output + "}"
        if data[s1:e1] == "Q_}j":
            output = output + ":"
        if data[s1:e1] == "WUX!":
            output = output + "'"
        if data[s1:e1] == "9NA5":
            output = output + "@"
        if data[s1:e1] == "qo!n":
            output = output + "#"
        if data[s1:e1] == "nlVi":
            output = output + "~"
        if data[s1:e1] == "B[mW":
            output = output + "/"
        if data[s1:e1] == ">O'@":
            output = output + "?"
        if data[s1:e1] == "F@Y@":
            output = output + "."
        if data[s1:e1] == "AM^i":
            output = output + ">"
        if data[s1:e1] == "%0Cv":
            output = output + ","
        if data[s1:e1] == "/rB)":
            output = output + "<"
        if data[s1:e1] == "&561":
            output = output + " "
        s1 = s1 + 4
        e1 = e1 + 4
        c1 = c1 + 4
        if data[s1:e1] == "qyQb":
            output = output + "a"
        if data[s1:e1] == "i/SV":
            output = output + "b"
        if data[s1:e1] == "gHY1":
            output = output + "c"
        if data[s1:e1] == "/++^":
            output = output + "d"
        if data[s1:e1] == "x,n6":
            output = output + "e"
        if data[s1:e1] == "!=Sk":
            output = output + "f"
        if data[s1:e1] == "F'$e":
            output = output + "g"
        if data[s1:e1] == ",_t ":
            output = output + "h"
        if data[s1:e1] == "HTX'":
            output = output + "i"
        if data[s1:e1] == "MW#o":
            output = output + "j"
        if data[s1:e1] == "+Mk5":
            output = output + "k"
        if data[s1:e1] == "c^X(":
            output = output + "l"
        if data[s1:e1] == "~u_a":
            output = output + "m"
        if data[s1:e1] == "zmqW":
            output = output + "n"
        if data[s1:e1] == "c3By":
            output = output + "o"
        if data[s1:e1] == "a'mP":
            output = output + "p"
        if data[s1:e1] == "[JtK":
            output = output + "q"
        if data[s1:e1] == "<j~s":
            output = output + "r"
        if data[s1:e1] == "ZF-%":
            output = output + "s"
        if data[s1:e1] == "GCaj":
            output = output + "t"
        if data[s1:e1] == "ms/8":
            output = output + "u"
        if data[s1:e1] == "4NP{":
            output = output + "v"
        if data[s1:e1] == "=PZx":
            output = output + "w"
        if data[s1:e1] == "O]%y":
            output = output + "x"
        if data[s1:e1] == "_W!E":
            output = output + "y"
        if data[s1:e1] == "zo>O":
            output = output + "z"
        if data[s1:e1] == "&hT#":
            output = output + "A"
        if data[s1:e1] == "Fb'9":
            output = output + "B"
        if data[s1:e1] == "KGl/":
            output = output + "C"
        if data[s1:e1] == "9MkI":
            output = output + "D"
        if data[s1:e1] == "$lp}":
            output = output + "E"
        if data[s1:e1] == "2Ae?":
            output = output + "F"
        if data[s1:e1] == "M{?l":
            output = output + "G"
        if data[s1:e1] == "w8.7":
            output = output + "H"
        if data[s1:e1] == "))X9":
            output = output + "I"
        if data[s1:e1] == "+Kft":
            output = output + "J"
        if data[s1:e1] == "C`O*":
            output = output + "K"
        if data[s1:e1] == "h'v0":
            output = output + "L"
        if data[s1:e1] == "`26h":
            output = output + "M"
        if data[s1:e1] == "'YQz":
            output = output + "N"
        if data[s1:e1] == "tS7B":
            output = output + "O"
        if data[s1:e1] == "UJCN":
            output = output + "P"
        if data[s1:e1] == "6ugD":
            output = output + "Q"
        if data[s1:e1] == "&(DT":
            output = output + "R"
        if data[s1:e1] == "pw5-":
            output = output + "S"
        if data[s1:e1] == "G}d4":
            output = output + "T"
        if data[s1:e1] == "LDN*":
            output = output + "U"
        if data[s1:e1] == "ieRV":
            output = output + "V"
        if data[s1:e1] == "Br[*":
            output = output + "W"
        if data[s1:e1] == "}`)K":
            output = output + "X"
        if data[s1:e1] == "xI@s":
            output = output + "Y"
        if data[s1:e1] == "fZnP":
            output = output + "Z"
        if data[s1:e1] == "kWeU":
            output = output + "1"
        if data[s1:e1] == "mA7Y":
            output = output + "2"
        if data[s1:e1] == ":[_8":
            output = output + "3"
        if data[s1:e1] == "UA17":
            output = output + "4"
        if data[s1:e1] == "&Fb2":
            output = output + "5"
        if data[s1:e1] == "6nxT":
            output = output + "6"
        if data[s1:e1] == "l.]R":
            output = output + "7"
        if data[s1:e1] == " ,-u":
            output = output + "8"
        if data[s1:e1] == " *i<":
            output = output + "9"
        if data[s1:e1] == "L!#w":
            output = output + "0"
        if data[s1:e1] == "L-Vr":
            output = output + "`"
        if data[s1:e1] == "pIwH":
            output = output + "!"
        if data[s1:e1] == ":BGd":
            output = output + "'"
        if data[s1:e1] == "4%oq":
            output = output + "$"
        if data[s1:e1] == "{hQQ":
            output = output + "%"
        if data[s1:e1] == "1a3@":
            output = output + "^"
        if data[s1:e1] == "OZzr":
            output = output + "&"
        if data[s1:e1] == "]>f{":
            output = output + "*"
        if data[s1:e1] == "v1#E":
            output = output + "("
        if data[s1:e1] == "0(XJ":
            output = output + ")"
        if data[s1:e1] == "$u3=":
            output = output + "_"
        if data[s1:e1] == "r}&A":
            output = output + "+"
        if data[s1:e1] == "NRf'":
            output = output + "-"
        if data[s1:e1] == ")`RS":
            output = output + "="
        if data[s1:e1] == "o!'?":
            output = output + "{"
        if data[s1:e1] == "s3~^":
            output = output + "["
        if data[s1:e1] == "J<i,":
            output = output + "]"
        if data[s1:e1] == "2%5.":
            output = output + "}"
        if data[s1:e1] == "?b]<":
            output = output + ":"
        if data[s1:e1] == ":0^g":
            output = output + "'"
        if data[s1:e1] == "n.cj":
            output = output + "@"
        if data[s1:e1] == "9dc>":
            output = output + "#"
        if data[s1:e1] == "vvE~":
            output = output + "~"
        if data[s1:e1] == "0[qg":
            output = output + "/"
        if data[s1:e1] == "y=CL":
            output = output + "?"
        if data[s1:e1] == "HYV4":
            output = output + "."
        if data[s1:e1] == "U$>D":
            output = output + ">"
        if data[s1:e1] == "5p8@":
            output = output + ","
        if data[s1:e1] == "dI: ":
            output = output + "<"
        if data[s1:e1] == "@E(j":
            output = output + " "
        s1 = s1 + 4
        e1 = e1 + 4
        c1 = c1 + 4
        if data[s1:e1] == "-z00":
            output = output + "a"
        if data[s1:e1] == "^JL4":
            output = output + "b"
        if data[s1:e1] == "D5u3":
            output = output + "c"
        if data[s1:e1] == "wYu3":
            output = output + "d"
        if data[s1:e1] == "3f-~":
            output = output + "e"
        if data[s1:e1] == "ZZ8(":
            output = output + "f"
        if data[s1:e1] == "?341":
            output = output + "g"
        if data[s1:e1] == "'m?/":
            output = output + "h"
        if data[s1:e1] == "t]#y":
            output = output + "i"
        if data[s1:e1] == "6M1q":
            output = output + "j"
        if data[s1:e1] == "DWu_":
            output = output + "k"
        if data[s1:e1] == "i}U'":
            output = output + "l"
        if data[s1:e1] == "z9CS":
            output = output + "m"
        if data[s1:e1] == "OPtG":
            output = output + "n"
        if data[s1:e1] == "gvIj":
            output = output + "o"
        if data[s1:e1] == "'c:^":
            output = output + "p"
        if data[s1:e1] == "x.}*":
            output = output + "q"
        if data[s1:e1] == "ewkc":
            output = output + "r"
        if data[s1:e1] == "y]>y":
            output = output + "s"
        if data[s1:e1] == ">xbl":
            output = output + "t"
        if data[s1:e1] == "AG,&":
            output = output + "u"
        if data[s1:e1] == "NY.'":
            output = output + "v"
        if data[s1:e1] == "A}Fa":
            output = output + "w"
        if data[s1:e1] == "AQ9S":
            output = output + "x"
        if data[s1:e1] == "6oU2":
            output = output + "y"
        if data[s1:e1] == "TqBq":
            output = output + "z"
        if data[s1:e1] == "V!eN":
            output = output + "A"
        if data[s1:e1] == "=%C`":
            output = output + "B"
        if data[s1:e1] == "_fs#":
            output = output + "C"
        if data[s1:e1] == "r2U5":
            output = output + "D"
        if data[s1:e1] == "pmmx":
            output = output + "E"
        if data[s1:e1] == " srv":
            output = output + "F"
        if data[s1:e1] == "'ogJ":
            output = output + "G"
        if data[s1:e1] == "+K#$":
            output = output + "H"
        if data[s1:e1] == "el`!":
            output = output + "I"
        if data[s1:e1] == "I<&<":
            output = output + "J"
        if data[s1:e1] == "8efV":
            output = output + "K"
        if data[s1:e1] == "ubwK":
            output = output + "L"
        if data[s1:e1] == "7>@S":
            output = output + "M"
        if data[s1:e1] == "7(1'":
            output = output + "N"
        if data[s1:e1] == "Zp`T":
            output = output + "O"
        if data[s1:e1] == "*y$*":
            output = output + "P"
        if data[s1:e1] == "7ER{":
            output = output + "Q"
        if data[s1:e1] == "jDW%":
            output = output + "R"
        if data[s1:e1] == "zw~M":
            output = output + "S"
        if data[s1:e1] == "@]6~":
            output = output + "T"
        if data[s1:e1] == "vJ%A":
            output = output + "U"
        if data[s1:e1] == "k>W/":
            output = output + "V"
        if data[s1:e1] == "kVSX":
            output = output + "W"
        if data[s1:e1] == "BQ$*":
            output = output + "X"
        if data[s1:e1] == "C:Xq":
            output = output + "Y"
        if data[s1:e1] == "a^$B":
            output = output + "Z"
        if data[s1:e1] == "-P5H":
            output = output + "1"
        if data[s1:e1] == "hYP#":
            output = output + "2"
        if data[s1:e1] == "8T_F":
            output = output + "3"
        if data[s1:e1] == ":Y= ":
            output = output + "4"
        if data[s1:e1] == "_f)<":
            output = output + "5"
        if data[s1:e1] == "p~]0":
            output = output + "6"
        if data[s1:e1] == "d%zl":
            output = output + "7"
        if data[s1:e1] == "M2,[":
            output = output + "8"
        if data[s1:e1] == "}ZhH":
            output = output + "9"
        if data[s1:e1] == "EL4N":
            output = output + "0"
        if data[s1:e1] == "rt R":
            output = output + "`"
        if data[s1:e1] == "t FG":
            output = output + "!"
        if data[s1:e1] == "^[0/":
            output = output + "'"
        if data[s1:e1] == "hN2E":
            output = output + "$"
        if data[s1:e1] == "j)so":
            output = output + "%"
        if data[s1:e1] == "P)b/":
            output = output + "^"
        if data[s1:e1] == "JVWH":
            output = output + "&"
        if data[s1:e1] == "p5{G":
            output = output + "*"
        if data[s1:e1] == "Rid.":
            output = output + "("
        if data[s1:e1] == "vn+K":
            output = output + ")"
        if data[s1:e1] == "iIH!":
            output = output + "_"
        if data[s1:e1] == "XcOQ":
            output = output + "+"
        if data[s1:e1] == "K?o)":
            output = output + "-"
        if data[s1:e1] == "jgk7":
            output = output + "="
        if data[s1:e1] == "@Ox(":
            output = output + "{"
        if data[s1:e1] == ",d(B":
            output = output + "["
        if data[s1:e1] == "8s<`":
            output = output + "]"
        if data[s1:e1] == "{c6F":
            output = output + "}"
        if data[s1:e1] == "b.+=":
            output = output + ":"
        if data[s1:e1] == "l[{[":
            output = output + "'"
        if data[s1:e1] == "?-a&":
            output = output + "@"
        if data[s1:e1] == "M:L9":
            output = output + "#"
        if data[s1:e1] == "C=Em":
            output = output + "~"
        if data[s1:e1] == "+Xn1":
            output = output + "/"
        if data[s1:e1] == "@Q'L":
            output = output + "?"
        if data[s1:e1] == "dUTi":
            output = output + "."
        if data[s1:e1] == "h'nI":
            output = output + ">"
        if data[s1:e1] == "94R!":
            output = output + ","
        if data[s1:e1] == "Dagn":
            output = output + "<"
        if data[s1:e1] == "&Or,":
            output = output + " "
        s1 = s1 + 4
        e1 = e1 + 4
        c1 = c1 + 4
elif leng == 16:
    e1 = 16
    while c1 < l1:
        if data[s1:e1] == "TC{emM1>ALJH<`Lt":
            output = output + "a"
        if data[s1:e1] == "Z9 *m' jx1z~H-+t":
            output = output + "b"
        if data[s1:e1] == "%bQ:LTWwgDzLE=X&":
            output = output + "c"
        if data[s1:e1] == "'$(PFba`gg-ek~TJ":
            output = output + "d"
        if data[s1:e1] == "yQ!Te YWm$Gy2uv@":
            output = output + "e"
        if data[s1:e1] == "0<Y[5u&tuPuPCL)y":
            output = output + "f"
        if data[s1:e1] == "Ff1r0(:K72Db,PT1":
            output = output + "g"
        if data[s1:e1] == ">G6fGyodR~8ZY/+q":
            output = output + "h"
        if data[s1:e1] == "NH@yUg'MDZ5YC!w^":
            output = output + "i"
        if data[s1:e1] == "'+{a$$h,w77.H>3?":
            output = output + "j"
        if data[s1:e1] == "kNN's'=2-MixM_bi":
            output = output + "k"
        if data[s1:e1] == "bn,9C+Bu>6lwJ41S":
            output = output + "l"
        if data[s1:e1] == "v3,(V6~^<?re'aWj":
            output = output + "m"
        if data[s1:e1] == "(H<^pWf8iPUY+3OR":
            output = output + "n"
        if data[s1:e1] == "-*Yq#t#M )GE's{Q":
            output = output + "o"
        if data[s1:e1] == "sUx3Hb[la,,k$(Ig":
            output = output + "p"
        if data[s1:e1] == "D@1jdAnEeFf#ge2v":
            output = output + "q"
        if data[s1:e1] == "9z9{rm,rFvU,ZX]Q":
            output = output + "r"
        if data[s1:e1] == "{[(D+HDux*!Oos+c":
            output = output + "s"
        if data[s1:e1] == "d/yu.wLldMz]Pf{G":
            output = output + "t"
        if data[s1:e1] == "ozC%E5rx'r(K[sx4":
            output = output + "u"
        if data[s1:e1] == "]Ej=x^56iMTCcIOl":
            output = output + "v"
        if data[s1:e1] == "p%P3Nn#BiDLn}GA0":
            output = output + "w"
        if data[s1:e1] == "cQB?)lF1etk@-`]Z":
            output = output + "x"
        if data[s1:e1] == "oAxo>3[]F{=<t/+Y":
            output = output + "y"
        if data[s1:e1] == "o/hJt?iN#v3/pu@j":
            output = output + "z"
        if data[s1:e1] == "t?jWhGzwUzTX{n9h":
            output = output + "A"
        if data[s1:e1] == "I.$zQc#R6jE[Q4S}":
            output = output + "B"
        if data[s1:e1] == "'&1cB9pou.8fgJ&^":
            output = output + "C"
        if data[s1:e1] == "GIMq]z_'Q:XBd+/R":
            output = output + "D"
        if data[s1:e1] == "GvN7Iv]80}*ZoA.K":
            output = output + "E"
        if data[s1:e1] == "P-.!>{ q=/yI=2qU":
            output = output + "F"
        if data[s1:e1] == "JBKi5WJQkX(E&#1C":
            output = output + "G"
        if data[s1:e1] == "9.XW_}A+_G[mL7*w":
            output = output + "H"
        if data[s1:e1] == ":K%^R_R&1_!y&?69":
            output = output + "I"
        if data[s1:e1] == "]L8_~it!FEUYst#c":
            output = output + "J"
        if data[s1:e1] == "xero(Rowc#*][ude":
            output = output + "K"
        if data[s1:e1] == "n0*no=Vx~GqCD'fl":
            output = output + "L"
        if data[s1:e1] == "IEqw6lfApI4N:g>X":
            output = output + "M"
        if data[s1:e1] == "1[75~L4K%s@3R>gR":
            output = output + "N"
        if data[s1:e1] == "vIxPC,pkqU<8'fHK":
            output = output + "O"
        if data[s1:e1] == "YNx'1UO3)Dk)?z?R":
            output = output + "P"
        if data[s1:e1] == "<2Vn=dEW-Karg,Q'":
            output = output + "Q"
        if data[s1:e1] == "Oro_)&<MmUbh$d!h":
            output = output + "R"
        if data[s1:e1] == "mszc:2WHZ>eLWcWW":
            output = output + "S"
        if data[s1:e1] == "s`_wfAc/4nQauqut":
            output = output + "T"
        if data[s1:e1] == "9l@j3(Z+b$4~.uiO":
            output = output + "U"
        if data[s1:e1] == "H&9QC!d'~c/h!Y&a":
            output = output + "V"
        if data[s1:e1] == "L#^F0K{ xsCSe2yV":
            output = output + "W"
        if data[s1:e1] == "6<`IQ:Vj{%k+5605":
            output = output + "X"
        if data[s1:e1] == "%p@Xm:2ez'xPT'2}":
            output = output + "Y"
        if data[s1:e1] == "T%4~F5R/S}hgW`yv":
            output = output + "Z"
        if data[s1:e1] == "-)z7U>$K{o'kEts>":
            output = output + "1"
        if data[s1:e1] == "@uhx``Vg'6(jX*_f":
            output = output + "2"
        if data[s1:e1] == "m@Y<<_}*]1[*5%dn":
            output = output + "3"
        if data[s1:e1] == "(XyDRT%la+AX(pNO":
            output = output + "4"
        if data[s1:e1] == "aBm03%NS viqZ/r ":
            output = output + "5"
        if data[s1:e1] == "]sc4N%K2 Y(Z'H9X":
            output = output + "6"
        if data[s1:e1] == "N^D#Kh w?:D(=b$7":
            output = output + "7"
        if data[s1:e1] == "6hFSPPhI }qvP3Q[":
            output = output + "8"
        if data[s1:e1] == "Vfj<Jpyp5.!'%EBV":
            output = output + "9"
        if data[s1:e1] == "`R-@4J5TZj>DacLs":
            output = output + "0"
        if data[s1:e1] == "dN{8,4 ed=6]C:gJ":
            output = output + "`"
        if data[s1:e1] == "7=A9`[iHKQo}BjGh":
            output = output + "!"
        if data[s1:e1] == "Wykn&'R,{r!S7zn:":
            output = output + "'"
        if data[s1:e1] == "lX0$,i.?-7F^h FZ":
            output = output + "$"
        if data[s1:e1] == "fR{>)T?.l.w:&G78":
            output = output + "%"
        if data[s1:e1] == "p[6^naiIqH}rm$,&":
            output = output + "^"
        if data[s1:e1] == "JAOnF)lfW^/*M=U1":
            output = output + "&"
        if data[s1:e1] == "@GJ}8aS+8Ci`3f5x":
            output = output + "*"
        if data[s1:e1] == "`?#ZVN~TPUs+_'qS":
            output = output + "("
        if data[s1:e1] == "SUYc)jV-!qE0Loz9":
            output = output + ")"
        if data[s1:e1] == "!/^O@p5eP}c5~b3B":
            output = output + "_"
        if data[s1:e1] == "rkZB.k1jw*SZUDJb":
            output = output + "+"
        if data[s1:e1] == "4_zlbc)K3:B7T%QF":
            output = output + "-"
        if data[s1:e1] == "9#J=%?Ft-)0GYv2p":
            output = output + "="
        if data[s1:e1] == "/'8aUC_h''}Mda8M":
            output = output + "{"
        if data[s1:e1] == "M}K.gV8!klnS$2*:":
            output = output + "["
        if data[s1:e1] == "Rm vT)5B>y:VZ0SJ":
            output = output + "]"
        if data[s1:e1] == "1y*~PH=+E_>Xd#Bu":
            output = output + "}"
        if data[s1:e1] == "_or-LY<Xp] s8)9B":
            output = output + ":"
        if data[s1:e1] == "kCA`kL?NNHOd?('O":
            output = output + "'"
        if data[s1:e1] == "F/mteOA}HgA^[OE~":
            output = output + "@"
        if data[s1:e1] == "lhX2a9k`Vm4f42>`":
            output = output + "#"
        if data[s1:e1] == "$bqltJSwvbSOwb$m":
            output = output + "~"
        if data[s1:e1] == "'4BC/<-=j^I'!?][":
            output = output + "/"
        if data[s1:e1] == ".6~bMV}*)7S.Ms~0":
            output = output + "?"
        if data[s1:e1] == "'AIi6VY3VDa4T&O&":
            output = output + "."
        if data[s1:e1] == "r8&<Dmq@t0v^$)n,":
            output = output + ">"
        if data[s1:e1] == "7id!@ vK%]E^,w@2":
            output = output + ","
        if data[s1:e1] == "`#:0eIrW--A{I]p7":
            output = output + "<"
        if data[s1:e1] == "pM*g80y#6u'OG<=[":
            output = output + " "
        s1 = s1 + 1
        e1 = e1 + 1
        c1 = c1 + 1
        if data[s1:e1] == "&mYzFJ<alZg76bJu":
            output = output + "a"
        if data[s1:e1] == "<KXB~}##SK=<J_JB":
            output = output + "b"
        if data[s1:e1] == "AlItG2aLnaM1zMw^":
            output = output + "c"
        if data[s1:e1] == "e!8(cYtEqEx(esHL":
            output = output + "d"
        if data[s1:e1] == "PYrVn@39SRFs?Q@v":
            output = output + "e"
        if data[s1:e1] == ")m_w%n*gT`FMF<5a":
            output = output + "f"
        if data[s1:e1] == ">o&Cky!4IQL&309c":
            output = output + "g"
        if data[s1:e1] == "KbMoy6gl^+PP<YwU":
            output = output + "h"
        if data[s1:e1] == "l66_-g4'''d'0Ar:":
            output = output + "i"
        if data[s1:e1] == "4B}Xu$-H.oO5Wj_c":
            output = output + "j"
        if data[s1:e1] == "+u~'$6dIW1m~1kjj":
            output = output + "k"
        if data[s1:e1] == ",bdw.Y0,>bC%~]xv":
            output = output + "l"
        if data[s1:e1] == "'Hj!,}1Bz/% nt`W":
            output = output + "m"
        if data[s1:e1] == "A$F[_)'n)]q.2Yr)":
            output = output + "n"
        if data[s1:e1] == "XFw0ay,0-F>V8Rk3":
            output = output + "o"
        if data[s1:e1] == "Nn{9V3m'`o%AK<5C":
            output = output + "p"
        if data[s1:e1] == "qeVc:N`@pWJW@GHM":
            output = output + "q"
        if data[s1:e1] == "g+oxaqUima<}S`-P":
            output = output + "r"
        if data[s1:e1] == "g+%!dCK4N[xRk^W2":
            output = output + "s"
        if data[s1:e1] == "((^Tp0upeqP/4N.v":
            output = output + "t"
        if data[s1:e1] == "uh,e`ME_=p&v_A!/":
            output = output + "u"
        if data[s1:e1] == "fZ:!)zD01_>=L}75":
            output = output + "v"
        if data[s1:e1] == "{K*Mjf_KeS3ii5Ry":
            output = output + "w"
        if data[s1:e1] == "Q#Kl8>m0E4P&cgQW":
            output = output + "x"
        if data[s1:e1] == "q'LB'f?t(U-D&nWK":
            output = output + "y"
        if data[s1:e1] == "Gqj'-mMYTY M!+/l":
            output = output + "z"
        if data[s1:e1] == "sI=zi.As%E_R $Y?":
            output = output + "A"
        if data[s1:e1] == "('[b!3!hSO~7rmLN":
            output = output + "B"
        if data[s1:e1] == "{R2T8'Z?)UG[O*F{":
            output = output + "C"
        if data[s1:e1] == "pXIzr&Wg?E6<)O2N":
            output = output + "D"
        if data[s1:e1] == "OLtPg#S0Jg6'v2]I":
            output = output + "E"
        if data[s1:e1] == "k.,V3 =]:Nb'3`#B":
            output = output + "F"
        if data[s1:e1] == "RGlC2,aInJl#_#RU":
            output = output + "G"
        if data[s1:e1] == "'w'gIMR^21s7hyaG":
            output = output + "H"
        if data[s1:e1] == ">hN{ `AXXD]7kXSK":
            output = output + "I"
        if data[s1:e1] == "TB!Ps yNus~[S$i-":
            output = output + "J"
        if data[s1:e1] == "*`81[D!MDQMQvX2w":
            output = output + "K"
        if data[s1:e1] == "jA6,F/5k7MV#}HAS":
            output = output + "L"
        if data[s1:e1] == "O[z*W)zct]kN]j.f":
            output = output + "M"
        if data[s1:e1] == "c*}=Q.jXV>lmi@y?":
            output = output + "N"
        if data[s1:e1] == "5*t{:[6)8&zTo1Q)":
            output = output + "O"
        if data[s1:e1] == "HW'c),sTXu(C/hb_":
            output = output + "P"
        if data[s1:e1] == "Yi%!@l0?eFVO9_yf":
            output = output + "Q"
        if data[s1:e1] == "v%g6vt$iu wr~hT0":
            output = output + "R"
        if data[s1:e1] == "'HXI~-:f6/q.+W~5":
            output = output + "S"
        if data[s1:e1] == "75ja:yi~Be<) //4":
            output = output + "T"
        if data[s1:e1] == "/m%JaE?]HkhUYmiU":
            output = output + "U"
        if data[s1:e1] == "s@hq}&db'wr}9G/^":
            output = output + "V"
        if data[s1:e1] == "EDZ$lA w]@:8s8K8":
            output = output + "W"
        if data[s1:e1] == ",EQ,*,X}Ap( HR %":
            output = output + "X"
        if data[s1:e1] == ".zth& E^Ej:>a(n3":
            output = output + "Y"
        if data[s1:e1] == "AXZ*v4J+l'm=z&4{":
            output = output + "Z"
        if data[s1:e1] == "6b6~{g-~cdP*7@Ga":
            output = output + "1"
        if data[s1:e1] == "@(wQcBz/Ih[oJUu(":
            output = output + "2"
        if data[s1:e1] == "H9[V>`W^n3f/P[k#":
            output = output + "3"
        if data[s1:e1] == "qViZb(=iW7O#2^>x":
            output = output + "4"
        if data[s1:e1] == "9%epq=/FH'k?+{Jx":
            output = output + "5"
        if data[s1:e1] == "ch8}`?r:%28G182a":
            output = output + "6"
        if data[s1:e1] == "fU_DIR]wn%TKdo`B":
            output = output + "7"
        if data[s1:e1] == "+TuQ2yj eKdEd$+=":
            output = output + "8"
        if data[s1:e1] == "t1x4fJD@w.fNxkwa":
            output = output + "9"
        if data[s1:e1] == "$N!8W$16QZAOYF@W":
            output = output + "0"
        if data[s1:e1] == ")BUdeFiR`Nkc-E'>":
            output = output + "`"
        if data[s1:e1] == "/G4yHvg$Q}bO627@":
            output = output + "!"
        if data[s1:e1] == "vbl)pPLZ>Z&C>x9}":
            output = output + "'"
        if data[s1:e1] == "ZopPq{^S&rg']o[Q":
            output = output + "$"
        if data[s1:e1] == "]sOs(pX[G~cK<=uO":
            output = output + "%"
        if data[s1:e1] == "UtO}M=P3oB52~S+!":
            output = output + "^"
        if data[s1:e1] == "eVu?fnR>*@=d`x'S":
            output = output + "&"
        if data[s1:e1] == ":LZDD/Ef{`t 73x8":
            output = output + "*"
        if data[s1:e1] == "L>_Zk^tLly:Z<[^J":
            output = output + "("
        if data[s1:e1] == "CB--{.iiC<TmV,,8":
            output = output + ")"
        if data[s1:e1] == "UppH4w,FqRRD=9Bb":
            output = output + "_"
        if data[s1:e1] == "<-p#%n@*yM_9^K:'":
            output = output + "+"
        if data[s1:e1] == "OX P7+g^k7h>1z{e":
            output = output + "-"
        if data[s1:e1] == "v'mCirIC-EpY^PhY":
            output = output + "="
        if data[s1:e1] == "dtqo&*=?'vaC9Nz!":
            output = output + "{"
        if data[s1:e1] == "#XGhoIc3+T{xUnCr":
            output = output + "["
        if data[s1:e1] == "B5rL7^o$7x#(tAd2":
            output = output + "]"
        if data[s1:e1] == "9*}Jju']4IxQccTh":
            output = output + "}"
        if data[s1:e1] == "Dd1rJ#G<jZf&54<$":
            output = output + ":"
        if data[s1:e1] == "-pv-sCZ]d}zK'[H:":
            output = output + "'"
        if data[s1:e1] == "D]#.,s+9(NfFdR9$":
            output = output + "@"
        if data[s1:e1] == "(#1?AwVIxGO+mux!":
            output = output + "#"
        if data[s1:e1] == "{Hv0tnV$3'. r+9z":
            output = output + "~"
        if data[s1:e1] == "JbVy5YSy&54$:eBF":
            output = output + "/"
        if data[s1:e1] == "?feC`*qV7*Tn?P3~":
            output = output + "?"
        if data[s1:e1] == "4{lO0T6r5mU=L[qf":
            output = output + "."
        if data[s1:e1] == "So1oMEG.9LT3j0Le":
            output = output + ">"
        if data[s1:e1] == "Dup:hbD]l)G?sA05":
            output = output + ","
        if data[s1:e1] == "Sj%LkU0YI1DQ8C~H":
            output = output + "<"
        if data[s1:e1] == ".<sr@yvZNS%u'bU)":
            output = output + " "
        s1 = s1 + 1
        e1 = e1 + 1
        c1 = c1 + 1
        if data[s1:e1] == "X]1V7dN=bD9'DYrU":
            output = output + "a"
        if data[s1:e1] == "R^~ch$.-[vryRU@-":
            output = output + "b"
        if data[s1:e1] == "z!T qdwGiy1)B4kO":
            output = output + "c"
        if data[s1:e1] == "I7#[{aH^vdxp~0wf":
            output = output + "d"
        if data[s1:e1] == "qcTHOm(dB/7@Vfbe":
            output = output + "e"
        if data[s1:e1] == "F:%!f#`@MMmI(yK'":
            output = output + "f"
        if data[s1:e1] == "UB0P0eQ7R_[YX.x ":
            output = output + "g"
        if data[s1:e1] == "WRHY}V#y5,a.EB=7":
            output = output + "h"
        if data[s1:e1] == "5'rIDk?yez=Fn`m!":
            output = output + "i"
        if data[s1:e1] == "`f~WobEXT'[&C-,7":
            output = output + "j"
        if data[s1:e1] == "xzr]=?5qKNAG*O.N":
            output = output + "k"
        if data[s1:e1] == "~=gX4%%-'o{zF`5I":
            output = output + "l"
        if data[s1:e1] == "JhMJb6R6:mgs]?%X":
            output = output + "m"
        if data[s1:e1] == "Yz`yZJ&a>(~O9'7+":
            output = output + "n"
        if data[s1:e1] == ":'K#,8]It>Zav&2F":
            output = output + "o"
        if data[s1:e1] == "46I}s1A]Yr<S$)qQ":
            output = output + "p"
        if data[s1:e1] == "viv@T4mAGLF3J9pA":
            output = output + "q"
        if data[s1:e1] == "dP'g_mvoZ+ mUDjl":
            output = output + "r"
        if data[s1:e1] == "sJI@Ul[!N(!>DE4y":
            output = output + "s"
        if data[s1:e1] == "Q'V<h_*ua/'8Qy1D":
            output = output + "t"
        if data[s1:e1] == "iI,Bu2'EOSzeA?=t":
            output = output + "u"
        if data[s1:e1] == "!X{r]3BQi1BD6`3_":
            output = output + "v"
        if data[s1:e1] == "Z1bgz}p@Q?C^VLTR":
            output = output + "w"
        if data[s1:e1] == "_tidaKL^xd%CNriq":
            output = output + "x"
        if data[s1:e1] == "zk[!-)NRPlna_,!H":
            output = output + "y"
        if data[s1:e1] == "tbmY>:%(}QShNBy.":
            output = output + "z"
        if data[s1:e1] == "n(6#GV:ckT*&psX,":
            output = output + "A"
        if data[s1:e1] == "{Z+d.*G(C30ab2`6":
            output = output + "B"
        if data[s1:e1] == "GsM:^wHk0,_+I*E.":
            output = output + "C"
        if data[s1:e1] == "8qcE/$b*i~K)`}9}":
            output = output + "D"
        if data[s1:e1] == "zWz^^,nL_tCV9PWx":
            output = output + "E"
        if data[s1:e1] == "VF`s<a`JU7D>LY.1":
            output = output + "F"
        if data[s1:e1] == "84lQ4M'RxkNmEH)>":
            output = output + "G"
        if data[s1:e1] == "GxwbtIU&#H<C3i*'":
            output = output + "H"
        if data[s1:e1] == "APJ7m+c9c1sw8dMf":
            output = output + "I"
        if data[s1:e1] == "Vw0c]5#6t1X~gp7f":
            output = output + "J"
        if data[s1:e1] == ")__9ls8<vL ghhoG":
            output = output + "K"
        if data[s1:e1] == "TeX/5uT7nEL4JZNU":
            output = output + "L"
        if data[s1:e1] == "oXw>F%gS&m4AIG38":
            output = output + "M"
        if data[s1:e1] == "ef~Hnor-C7[nR>hW":
            output = output + "N"
        if data[s1:e1] == "dreQtX2V<F%iw&9~":
            output = output + "O"
        if data[s1:e1] == "krc'!^+Pw81?JG+T":
            output = output + "P"
        if data[s1:e1] == "-)Wg9$L/$b$*J6Pl":
            output = output + "Q"
        if data[s1:e1] == "2DGOf)sfZmWtyTa{":
            output = output + "R"
        if data[s1:e1] == "h4[shug+]Z?%5Swq":
            output = output + "S"
        if data[s1:e1] == "LTMYC<3e}*cdK Sq":
            output = output + "T"
        if data[s1:e1] == "cA0[-b$2#)HsI`p=":
            output = output + "U"
        if data[s1:e1] == "L>a6jrtE~xk}=0D9":
            output = output + "V"
        if data[s1:e1] == "R@nKu9j)c'k.XRdj":
            output = output + "W"
        if data[s1:e1] == "EjV&'@G2Hx'N[2t?":
            output = output + "X"
        if data[s1:e1] == "k'9)GO{:I/4UP&$R":
            output = output + "Y"
        if data[s1:e1] == "qWL5gpaq]OkiVF_H":
            output = output + "Z"
        if data[s1:e1] == "%Jt=@e2pl:U8P<Ck":
            output = output + "1"
        if data[s1:e1] == "+cY,sDZ$u.Yeh5H:":
            output = output + "2"
        if data[s1:e1] == "l*#36/,f<g~-x%-(":
            output = output + "3"
        if data[s1:e1] == "N.l#0])+G&QKzQoS":
            output = output + "4"
        if data[s1:e1] == "J{>h^>$'p5Ynw^l ":
            output = output + "5"
        if data[s1:e1] == "#%ZnztmyugKSa9vi":
            output = output + "6"
        if data[s1:e1] == "`!W=Eu7f@3H`^(yb":
            output = output + "7"
        if data[s1:e1] == "5hQ<$aB2=pu!BS$S":
            output = output + "8"
        if data[s1:e1] == "BozuKFWPYX gM-!6":
            output = output + "9"
        if data[s1:e1] == " o=r(#su1fmSqiih":
            output = output + "0"
        if data[s1:e1] == "Fr}oIWc=U]bjv/'_":
            output = output + "`"
        if data[s1:e1] == "]AEnj(b]!(AK2$D/":
            output = output + "!"
        if data[s1:e1] == "[sEHZ0Eh7cySxPc~":
            output = output + "'"
        if data[s1:e1] == "`{A0Pjt.KN& v-%:":
            output = output + "$"
        if data[s1:e1] == "A-CsMZy6t>o13jJi":
            output = output + "%"
        if data[s1:e1] == "/ }${{~wUD[/fu?Y":
            output = output + "^"
        if data[s1:e1] == "8(+gBl/jTMRXdurp":
            output = output + "&"
        if data[s1:e1] == "wY[?~6Z.n.}=?vJV":
            output = output + "*"
        if data[s1:e1] == "dOXeNMTx=W&v3M4>":
            output = output + "("
        if data[s1:e1] == "o*BS%6,K8'3_2ZQ'":
            output = output + ")"
        if data[s1:e1] == "W)F#{+*EjuOM@^@l":
            output = output + "_"
        if data[s1:e1] == "0k{TNVD0<bdUC+Vj":
            output = output + "+"
        if data[s1:e1] == ".f)^Ip5(814HRc:m":
            output = output + "-"
        if data[s1:e1] == "}Bf2OuneKwn-U7xr":
            output = output + "="
        if data[s1:e1] == "8U)peC2A@KeMSO$}":
            output = output + "{"
        if data[s1:e1] == "u{ZOe,zpLDz'wak3":
            output = output + "["
        if data[s1:e1] == "^e8qROoFIF38!5Uq":
            output = output + "]"
        if data[s1:e1] == "Mty!Pg?C?9N4C:R(":
            output = output + "}"
        if data[s1:e1] == "Ho%l0> },Xlr<?B_":
            output = output + ":"
        if data[s1:e1] == "gE(]-LCl'A,>LPbM":
            output = output + "'"
        if data[s1:e1] == "a9AF6AlPTD*& 'B2":
            output = output + "@"
        if data[s1:e1] == "!<L]W/[3 <<&}Wnk":
            output = output + "#"
        if data[s1:e1] == ":'O1xZ'wiJ3:`i%8":
            output = output + "~"
        if data[s1:e1] == "k5#Ljv2o9 1q[h=O":
            output = output + "/"
        if data[s1:e1] == "/+5?vQq @#.N'}&q":
            output = output + "?"
        if data[s1:e1] == "^'sm`h@YyY'[ n6{":
            output = output + "."
        if data[s1:e1] == "p{&7*oQfQ)p>VG?j":
            output = output + ">"
        if data[s1:e1] == "$:0]J4xdTv0K,G+'":
            output = output + ","
        if data[s1:e1] == "-P*_x/SWSzj*,+/v":
            output = output + "<"
        if data[s1:e1] == "{_^1jC~:5#'<4@~F":
            output = output + " "
        s1 = s1 + 1
        e1 = e1 + 1
        c1 = c1 + 1
        if data[s1:e1] == "u3j/CdB_3/tMU/>9":
            output = output + "a"
        if data[s1:e1] == "Dl!!8R#@Er&rL&*m":
            output = output + "b"
        if data[s1:e1] == "TLcuMu.Xj iIoq`-":
            output = output + "c"
        if data[s1:e1] == "Z%tRl{.KMg$Lw2Q7":
            output = output + "d"
        if data[s1:e1] == "~-?Pt$0'[~>T' vy":
            output = output + "e"
        if data[s1:e1] == ",$g'ZVX!g('[gX6S":
            output = output + "f"
        if data[s1:e1] == "r79P8MrY7N5HqU $":
            output = output + "g"
        if data[s1:e1] == "^BpZ#1g*z1z6y*o&":
            output = output + "h"
        if data[s1:e1] == "8_q%Lwx( ,I0+JjM":
            output = output + "i"
        if data[s1:e1] == "0,pVvRp*9u:,mICI":
            output = output + "j"
        if data[s1:e1] == "a5:]KoZBH0ZY`(BO":
            output = output + "k"
        if data[s1:e1] == ">iuHQar0k`S2T(Ju":
            output = output + "l"
        if data[s1:e1] == "VG#olvLi%%aEY7tk":
            output = output + "m"
        if data[s1:e1] == "jL0:Fd#AU#8[B1z@":
            output = output + "n"
        if data[s1:e1] == "Yu=e`H@u,MXAek[A":
            output = output + "o"
        if data[s1:e1] == "-M7  ~K[]3s`8Rd^":
            output = output + "p"
        if data[s1:e1] == "[MIR]vf^G]<.`*!S":
            output = output + "q"
        if data[s1:e1] == ">G7MWqwU2O_.hY4=":
            output = output + "r"
        if data[s1:e1] == "J^xd}PAC6&*WT]5_":
            output = output + "s"
        if data[s1:e1] == "S2LMj+kJ_bIr4opW":
            output = output + "t"
        if data[s1:e1] == "!ChlX{B4p#lU'^sC":
            output = output + "u"
        if data[s1:e1] == "*'Ed36@Q-n3pt1fA":
            output = output + "v"
        if data[s1:e1] == "xcQNKMwS{HGB9K`3":
            output = output + "w"
        if data[s1:e1] == "wm}lOxZRh=Tq>w}%":
            output = output + "x"
        if data[s1:e1] == "/ dF-!#t6eV?qIkF":
            output = output + "y"
        if data[s1:e1] == "rFRR2[wH(:7O+8Z.":
            output = output + "z"
        if data[s1:e1] == ":0r&zCLQ,}5=D!!]":
            output = output + "A"
        if data[s1:e1] == "V@7@X~~sHFYCr83U":
            output = output + "B"
        if data[s1:e1] == "_<&}yG,'d $o-O+g":
            output = output + "C"
        if data[s1:e1] == "t~lMw@u$v!asiy]g":
            output = output + "D"
        if data[s1:e1] == "Sk18X/.>/LvT+z:n":
            output = output + "E"
        if data[s1:e1] == "Ak@i.j b'=@<aU4:":
            output = output + "F"
        if data[s1:e1] == "@3+&G:'b*NwoTb2`":
            output = output + "G"
        if data[s1:e1] == "t9HlZ'N=k_z}4i$#":
            output = output + "H"
        if data[s1:e1] == "'g{QP?L<cK%9O/oZ":
            output = output + "I"
        if data[s1:e1] == "NcFn+/'KiAxsqZeP":
            output = output + "J"
        if data[s1:e1] == "}W/o,sVn=&2G-w=>":
            output = output + "K"
        if data[s1:e1] == "0kzzqf05{{<:#(j6":
            output = output + "L"
        if data[s1:e1] == "O_Nk9zaUP%WYpgM)":
            output = output + "M"
        if data[s1:e1] == "=qBrK8DO1,13Og~o":
            output = output + "N"
        if data[s1:e1] == "!eVDB?W)(aJ)9U3B":
            output = output + "O"
        if data[s1:e1] == "fa%vKxX{Aqv+gbyt":
            output = output + "P"
        if data[s1:e1] == "MZDhRnnC?l$(&xOe":
            output = output + "Q"
        if data[s1:e1] == ":kV[YK/W5<J*e#`p":
            output = output + "R"
        if data[s1:e1] == "C33YW*10hR>T=/+D":
            output = output + "S"
        if data[s1:e1] == "`./$]apmBl6(7e)J":
            output = output + "T"
        if data[s1:e1] == "E?rQfP^5$0y{KJn4":
            output = output + "U"
        if data[s1:e1] == "1LcTFCcy]4D.}jXb":
            output = output + "V"
        if data[s1:e1] == "^u5O{5sRvEA)BG:(":
            output = output + "W"
        if data[s1:e1] == "s !?8c'Xz+JLilt(":
            output = output + "X"
        if data[s1:e1] == "9&Q{r,b5gAOe3.V^":
            output = output + "Y"
        if data[s1:e1] == "PF[9p,T6?1*N+@i`":
            output = output + "Z"
        if data[s1:e1] == "QlWw/'')'AC'>f?,":
            output = output + "1"
        if data[s1:e1] == "aBXDtI1r3n9vwyjg":
            output = output + "2"
        if data[s1:e1] == "c)=E.r6-4175Byq ":
            output = output + "3"
        if data[s1:e1] == "&&546D<:NSPN>vkN":
            output = output + "4"
        if data[s1:e1] == "l@lQ<kiQRQYSFw+0":
            output = output + "5"
        if data[s1:e1] == ")bnA=A'7*z$iCMD~":
            output = output + "6"
        if data[s1:e1] == "/ia+O]3V<Y>R:J:y":
            output = output + "7"
        if data[s1:e1] == "S8}oc??$K.2v'<Y$":
            output = output + "8"
        if data[s1:e1] == "'q<:5Ci+-J51^S#h":
            output = output + "9"
        if data[s1:e1] == "2m?~:G)qghHHwa's":
            output = output + "0"
        if data[s1:e1] == "j6{dl!n^s'Hz^WXs":
            output = output + "`"
        if data[s1:e1] == "VmB)fc-j0dhW9H^9":
            output = output + "!"
        if data[s1:e1] == "~xbNWHI00]7Ssh!U":
            output = output + "'"
        if data[s1:e1] == "xr_W#>~WVoJ7pbj*":
            output = output + "$"
        if data[s1:e1] == "E'Xn!zQc-CxRW'~h":
            output = output + "%"
        if data[s1:e1] == "F4K{z%.JYID5}*H}":
            output = output + "^"
        if data[s1:e1] == "=>NVat0[Idm$8fpq":
            output = output + "&"
        if data[s1:e1] == "e7ufbGX<h>bRX{V9":
            output = output + "*"
        if data[s1:e1] == "+@ZWI1E?Fp%?m%>~":
            output = output + "("
        if data[s1:e1] == "Z[cu24GQ_~4[_bEx":
            output = output + ")"
        if data[s1:e1] == "vvL{A}=JsY#GTu3f":
            output = output + "_"
        if data[s1:e1] == "mI](F-4FNaEuACP'":
            output = output + "+"
        if data[s1:e1] == "GX@)P&%}%{^hsRJf":
            output = output + "-"
        if data[s1:e1] == "HcIpn2TihU8xtkY-":
            output = output + "="
        if data[s1:e1] == "+eN-Txy_E<UmU$in":
            output = output + "{"
        if data[s1:e1] == "I#.hEvr6DEfc>~Q`":
            output = output + "["
        if data[s1:e1] == "1'v_,&s8zKPd?Mws":
            output = output + "]"
        if data[s1:e1] == ",NE''yP4Z(^/Fq`L":
            output = output + "}"
        if data[s1:e1] == "GL=1jjd)UpS''C[-":
            output = output + ":"
        if data[s1:e1] == "_<-zd#oe}pOZd)b_":
            output = output + "'"
        if data[s1:e1] == "2Td]mo{!Oxey<6l]":
            output = output + "@"
        if data[s1:e1] == "nh9L'j2)7(6f%[m}":
            output = output + "#"
        if data[s1:e1] == "dZ%ge`cS8o&}U Sb":
            output = output + "~"
        if data[s1:e1] == "7*y~58kw.m2<V[@E":
            output = output + "/"
        if data[s1:e1] == "yuJ,tcxA*DODYS.f":
            output = output + "?"
        if data[s1:e1] == "x?IPFmfF6B$ty^42":
            output = output + "."
        if data[s1:e1] == "iDmVn%2Q' 6e^ T(":
            output = output + ">"
        if data[s1:e1] == ")H@heUmD_Ng4a!(E":
            output = output + ","
        if data[s1:e1] == "Sf]=aqot#GTbukK`":
            output = output + "<"
        if data[s1:e1] == "[,P 9]K nP/j&G`)":
            output = output + " "
        s1 = s1 + 1
        e1 = e1 + 1
        c1 = c1 + 1
    print(output)
elif leng == 64:
    e1 = 64
    while c1 < l1:
        if data[s1:e1] == "u1*Gt?fd[#~t$2j<NGx.o2&i0_CUZ`3cfR.Lv5L+yOV&Ii{.by#3:c+5'P01#)3_":
            output = output + "a"
        if data[s1:e1] == "^ko'ph%uzs.b.WGWA{^WWtyr(Rxs{XAM(yE29_Hu,eM1Ng#ncl~'8I IPoZ!9yKJ":
            output = output + "b"
        if data[s1:e1] == "*z#Zb>tmt'6a!Ky*#0aMk#ma JPSsg69G*~OQ6</OKX>.xABb:k/9e<]hi H^Md)":
            output = output + "c"
        if data[s1:e1] == "*yAk5%ILJFwB?bzDz1<X> 8]eR-P0#alQk4`*vgTL&iqKx[c7/@~-qbn%Ul8XV&n":
            output = output + "d"
        if data[s1:e1] == "`0oZn,]a)H!vWPk_@#mJcG>ONnAFb)fzBm=GYU=B<=2FsvfvC2{PGM[`'sDI&+B)":
            output = output + "e"
        if data[s1:e1] == "rg'u=uVy$c'X668[y~LewEcZ+ Zo+Os{8_f9Pjj%)y?'B2OI-7Rd[OE7ad:9JGV{":
            output = output + "f"
        if data[s1:e1] == "Ot!3+=X=ICp>:^ `g~TSfd(C`~L0&.c66D'!8/JjL-K[4<i>S}q@:=ohNF~<D}eD":
            output = output + "g"
        if data[s1:e1] == "pg<%lB9E5b=SJ/1<#Z}ao@z(zf`HWs~LB_V*_x@6o'r06(X@~AF.!F,o02~5K5C9":
            output = output + "h"
        if data[s1:e1] == "1NJ(?v4Gqe_@$J}Z5aX'3b%cv'q~'V$azjK}9Bf>QJ1s/AH{GVQ5!O RBPg/?}SS":
            output = output + "i"
        if data[s1:e1] == "tFGH}<z(sqTAI#7Fmv-jRb&J+P' vd8xGEKIP^AH2']V:Lh1CA`N]MW?<si^!gav":
            output = output + "j"
        if data[s1:e1] == "'Uo'i(9=Iv18-WdT03RD$>xFpH,-B8lQfM#9zUG^<zHHT77Oe)*:m1NfBcr(oGh$":
            output = output + "k"
        if data[s1:e1] == "#$K,]A]yR`[GU`?&$O%$Ky)`Dg9#GkvH-cxK*V_PL9rw},wsOIoQ(]1zYn(@OQK0":
            output = output + "l"
        if data[s1:e1] == "roPd&%@<2Kf,,RlR5mbw{&GTN4n:igNHX+4a&U5Vo=I[~mpcTiwC+'h2iF$!s+Ak":
            output = output + "m"
        if data[s1:e1] == "W@SY,&tP'))]jF}(W+ui]K{3UUBCgQ%jV]xCyA^~m7l)}#[9X[Q<.n- K{`8x^om":
            output = output + "n"
        if data[s1:e1] == "N)?-vQ8fBs7.]8Zco_WOQ*CRNK{=_zj37YfD(hbhU=j9`c.)Mx& mPw$o{$KH'YE":
            output = output + "o"
        if data[s1:e1] == "7'wtWqACX]E1OP8q{{<6N=#KcXb^:h(:d6tST/4hZ[u= m4yCi(41qUZhjVExNX9":
            output = output + "p"
        if data[s1:e1] == "x&F?3Insb.xT'&u4hcbO-jNYb6_']?*CIG<e/nPt%4,ax&.@11 LR/usWHvo7}>v":
            output = output + "q"
        if data[s1:e1] == "(<@<Pppdw:=BC#a7:*'Cv'l+/+4maAey)jSK>lU*j.cy'rze4cU,=m!) 9>x()}%":
            output = output + "r"
        if data[s1:e1] == "HZ'jb@Kt,H@0F@'k7GeMNgr{Cro_?&Ei}UkG#*=0R>ww{LaXX2^%[#FQ/5o+13NI":
            output = output + "s"
        if data[s1:e1] == "SDd9XAJ#m]nsL!-+nww~0+*`M:Zol'!f2hH3/f70aYQ%$(_q~&.(^mS[h?GecntU":
            output = output + "t"
        if data[s1:e1] == "KuNQ)PQQ(2R*+P3Gj1Ok:4J7l2:RK}&U I):n6hM=n*.D'IB}E1{Sg2_Fxu75!Xe":
            output = output + "u"
        if data[s1:e1] == "}fc+foRUt7-.`0tAw?jlA.p[,q&K'[F3ZcvjB6E9,ClTXk'f/RNq/i$B>Y&Knlaj":
            output = output + "v"
        if data[s1:e1] == "7urMcAdHNedQ7}Vn7[6.2scz2P%Q/wD+2LmUG3p=/fVV0T`9/Hl&lRmeoN=%hWgJ":
            output = output + "w"
        if data[s1:e1] == "ug*f38sR2n'hWt}^27?>>weX%EKJ@<3FW<G^v?xzatx=8v}'m@FXw(*7cc'0T'0R":
            output = output + "x"
        if data[s1:e1] == "d!`@nX9Yi5JC_ZO7~GyCH>U_y_vAfM@PJEW)K[!m:'a~%2RC$q>bLx_T<+vT %M4":
            output = output + "y"
        if data[s1:e1] == "P,CtyWeWhX%-%Y#xvhr,M'%38eI(0%3!l-mW`mZT=-LCFmi'f8^=nX@~stHqnknK":
            output = output + "z"
        if data[s1:e1] == "2[797 $Vn'P5I~e%'Mub1#Qn7R:56Cf?gd:}u%E_wfEK&vqjL^naaE-glDlIT0/$":
            output = output + "A"
        if data[s1:e1] == "U-WLw_'7/9gGg-]v?4RFg8TM&6%wp9qW@D1Xp~5SpQb@'c<RN.0%^@ipsr&!ND'M":
            output = output + "B"
        if data[s1:e1] == "^~0cQ@9ZY^N^D Xb9f2n s/(VE#uw--jZ~2UYWgg*bv6')h+}1W`@up'V1n2F!*a":
            output = output + "C"
        if data[s1:e1] == "lA3%3!Ju,UU,~/A[[,l?,W-xr'J/CER[FY&R@K9pzG#k4R0_nxoaVx.{_q1q%E/>":
            output = output + "D"
        if data[s1:e1] == "?)q=^ySldTrk/ Eym2Lt &Ou!,_e^(vV8.-r%LtBUqIl<E-F{Fm'71!H=RK'&}%V":
            output = output + "E"
        if data[s1:e1] == "}bZDB'{ycri&gjm'uv5`B_VI]jo_Agy17F*}M'3N:]pbh0:71.J{puJ<$NlO4]#`":
            output = output + "F"
        if data[s1:e1] == "T,HXgr-L=^3M-xqVI'lA^c#vINh({F#>!Rc]4iC{?D7e5}83gI7f?<J9S.M,3#_8":
            output = output + "G"
        if data[s1:e1] == "KZ'kve<,RyIt> &iJ'bTy<X]:8QeI(zf)_/3zrvA%Y-3kb4#gNk~ss53VoQ=T$&t":
            output = output + "H"
        if data[s1:e1] == "=6g52Kl)MSi2[0CvHY[+5f2iQK2Yg)+LbgnxYOgXL=jT<3b'h76Q[4{5z'Cws/MS":
            output = output + "I"
        if data[s1:e1] == "kTEHrI>It'O?2raKO- X:?8+9x~:{Ls'h'~H'7OkZ!2SOrA}{3 m'!YDAiAUk_Bf":
            output = output + "J"
        if data[s1:e1] == "H-ok}0XL>-hEW7RJl5r8Dk:o=z.28j-P/'i^ q]bV39@Pb5S558s5`zn-LYZ+'Vb":
            output = output + "K"
        if data[s1:e1] == "N$$uZvlQ1,uqc#!l]x}K 0Cp%}{nz08B*Do%mceYT`=~-*  G5lVS^n,k*In+_@v":
            output = output + "L"
        if data[s1:e1] == "s`*TorB8%0vVI,l'+h)snJ`--]p'ja_Ug?RjHdvJqakJ+S:X8'O,[4``x[P'pMca":
            output = output + "M"
        if data[s1:e1] == "z$yw UsGP=4NBgt/0rO4)(~@pe8Y9~5>3c=.ezT0~f!!1r7CB:wVPuGaVGF[=h_U":
            output = output + "N"
        if data[s1:e1] == "]#)UR=V^-h4?~*'+]wNJ%j?<(#OGN1DwF db4.6'+YP0i'6e_aEJb$K$=z_'RDy0":
            output = output + "O"
        if data[s1:e1] == "dFL+c[OD]]IGYEm [`Om24@]f$0{4^U&6Nd`F,e*{}Do}_eJitz&6izDI70':!_O":
            output = output + "P"
        if data[s1:e1] == "}/Op<Zp7dV@S{S'E^Y4PdbRih+}E8jlv>pM9fbAPaNaXg/I%kPyV#Bts3.u}>L4'":
            output = output + "Q"
        if data[s1:e1] == "U3~_+ttfrQ1q)!Wf[?jK%M8OuY07v$RrVdt?/C3Uh3,YXC3jaN5=LrzDf!$r*+*=":
            output = output + "R"
        if data[s1:e1] == "f-#a<?jMXnea>W$,$rb?7a?QEk/tg>!MN'fQI6^9zOOqNKf}~0NK6)Jaxh(yZL2Y":
            output = output + "S"
        if data[s1:e1] == "wBu#D(k=SE^0xxigg n>*B`2CO't/F@rlR9('Yxw)k.'x.Kg+Meo<-}gmkTjsk&F":
            output = output + "T"
        if data[s1:e1] == "D'hordB`!b]7xv(PcWDZ-Vjw}EQ?5IuPm=uown%9`j?JCxh35W2:HU4z7pFsF`[^":
            output = output + "U"
        if data[s1:e1] == "`c.tz[}~,`]s-}qW>hWC ]~r_CH$P#G5#G4`vt?1y'WA&97ckAv2orW~krIckhD~":
            output = output + "V"
        if data[s1:e1] == "pAC<=4'0Ds7N+uN~`K,NFk,1k61LWic)<+S8hT:Su4[{9,@#{^2SJ3}+-{/Ja%R*":
            output = output + "W"
        if data[s1:e1] == ">-cC@!o$'TABF.m6AcEh,eZy:F`as-d7IjCsO*[-}8=/)Hy5fF+cn<C]rJg/aDhU":
            output = output + "X"
        if data[s1:e1] == "f$!@T7'rEBOho_Hp^<4YnXyQ)RWY,Wj:-km]kI8&k3N7'PL4(kR+uqxL6CAG2#y'":
            output = output + "Y"
        if data[s1:e1] == "kKH(q^lBRgS+Ye*e,Iiho^Gib+3Ek&5bGxmoFT.(qxX[4Gb.$TY^Lo?a[J]7A{k]":
            output = output + "Z"
        if data[s1:e1] == "j<{KKOz`>m(`]Jm,@hkkz5@XHQGZuuh55>:Ld4VXEhf`fobhi7h 8RN[Hgn9(!j`":
            output = output + "1"
        if data[s1:e1] == "1'9B%f9>]maN/>[/E@!gVulL9zpG-P'er_Txs(!7(1VcD*u(G IX6HLHl1rH6B~T":
            output = output + "2"
        if data[s1:e1] == "MyBZi24pp-P]#{}#lD85RVP8##d2$aW4>d_^ep>zd0(]W.kLfZk*1QR$KY1Og0N~":
            output = output + "3"
        if data[s1:e1] == "~Md}??{YPTsY]wsmtriuzQ`Vv*???@*ef #0yY#8TmQ{iD*y=p#bC>/'Y*N+LgnD":
            output = output + "4"
        if data[s1:e1] == "m'zEYYp(PO+6Knvd}=pCqcGruQ2.Bb'?lL@+t:^Mp1H&wTCOvmD?u^BA@AttMPZ%":
            output = output + "5"
        if data[s1:e1] == "4N5&zY'#F<MF<z4S~'iu)60uOI]4E`%xm:y&UqQ__e JT)A{E]%L.j3Sefu`@:)5":
            output = output + "6"
        if data[s1:e1] == "dmrJeLEy1^)7{Szu6TbGZ/5f-cOp0OA@o}Up:&/ M3xL2cWJk!(nXI9K[A8t@{:Q":
            output = output + "7"
        if data[s1:e1] == "eoZu'@g=<4&}YSI[9b1DXz2Uw[R1h1ecd'N&.j3DgM'*?Q~_Z3QNQ^/{r{S){KlY":
            output = output + "8"
        if data[s1:e1] == "tHh.> n#ig =dLK98>WC:NUqHtR:F](~zFM[q&m_AjGMnNM zM4J:2M$Bh0P<&k4":
            output = output + "9"
        if data[s1:e1] == "rHDe:&+0dq5Df_t..e%cECq#/fVM2+6>Rpw$ser2^wN28m7bE*)TW'GT]4u<i=fz":
            output = output + "0"
        if data[s1:e1] == "Uz$1l.[GpeX$%T&3Go+Md]UBb#),Y6yr)5)X~o*0E'6?aPpbH!$?@vhc'ZHGHnQp":
            output = output + "`"
        if data[s1:e1] == "RE@&wO649l@qnT?'btpapj/fC7q@Jz><qyYO`Q [:9&%cSfCg05+ydz+^[6]S>:F":
            output = output + "!"
        if data[s1:e1] == "jptY%W$wJhcZ<v8w%}NC_jVv3 l_}uO#le_SgUsQ,MS:JTp'AI,PSVE!'[?6[gr#":
            output = output + "'"
        if data[s1:e1] == "r*Ial#S=LSZi{Rh'Z(=ccEoT^/k'm Z$^J]SJPHa:%BPpEQJVio>5Cnye:QUs2ux":
            output = output + "$"
        if data[s1:e1] == "cSF6Xan!SwxwZ&F?K{>M/=)4`R4H&1>KJt^z@[ebb 9SCL*#d90ds68yV}fcl =%":
            output = output + "%"
        if data[s1:e1] == "%%o+8gpP)0jo@:Ll*Z1mDY9-8r)qjvwbM-Z=8rAgD%F<L9L Z?WN(y8gl^#NI'ox":
            output = output + "^"
        if data[s1:e1] == "d~mhA8=A1T$3TYoq:lkf3@d6+DDMA/El .3R X1 xCZqQ?QxwbN`m3a?Wd65otpA":
            output = output + "&"
        if data[s1:e1] == "b&Lf=^tX6wq# f29}Tui~nI0Bt/m).2S$<$<P1Q!4q'k5JIyo_5PpoY6x.`^wxr#":
            output = output + "*"
        if data[s1:e1] == " #j=dui!E+On_Q)eUiFVE'uAK}&:d<aV&:jr9p*a'^lB,O(-[*k6I~~Tzr+3< R6":
            output = output + "("
        if data[s1:e1] == "!i?rG:lM2jwZ ' (H~!~D<HwnW7.BS:T-8uh^OYk'^T'*aQ8-5v,L*iXIH=BLI`d":
            output = output + ")"
        if data[s1:e1] == "$T9!`vlEPo<{Vu1M{.V~gn0SwiBJ.EHv_5LfC:/Lg`T(4`8O&N(iUt,J,3#{!E'R":
            output = output + "_"
        if data[s1:e1] == "8BMRW3lme`>MTHBV{KLtJ_tz u(d&~kvI@}>.H-/Pd4:0 4+z<h-dwsdEUjwup`Y":
            output = output + "+"
        if data[s1:e1] == ":<I2dzeD0#/TQ8W46wMyI5UL0OJs`s8xNt1ZKDwZC7SpXm?5OmyS:[bGGpQq_).s":
            output = output + "-"
        if data[s1:e1] == "Lq>iR^sw?DZ@brLSEiBfxU7=Gfs3FBBR<g.hqh.RyorX[sgCavxc@*MGg8^K4m1Z":
            output = output + "="
        if data[s1:e1] == "Jj7dWNS?Z>#Zw)j'69%b]BW3@)PFbi1$WTl+Sm%A'Kt&?!pEL~.+:<qFWx,.3H,y":
            output = output + "{"
        if data[s1:e1] == "IQ.rOUOJX+<tZ!vcezC&>V9 6qeLekE^^7!'*3BP(bqB9]/WYA9<0RF$f#P[Wxf`":
            output = output + "["
        if data[s1:e1] == "rMFG'd09CB.S !t yQ4PSig[9CJF`6X,^[EuAMGAkQM0l*iC)EyuX>$x,Uxh,aHM":
            output = output + "]"
        if data[s1:e1] == "{O22!eE`wulPnXa=~Cu-vgRUvHL6GAkb]9zFYuMQ'Ul%S,!GR^qZ4-Sx]+q=>z/t":
            output = output + "}"
        if data[s1:e1] == "_3<@]}74D,:L$,Or_P_w.YgH&,-,P!.qjOG5NB~a*QI{i]FEA2iO$uV}:4t+0,}t":
            output = output + ":"
        if data[s1:e1] == "a(g_qD.^5~8z]dS<TP:d$KYX%VQY20?I2@)U[K]W1Z`x,j6ozAd> ~+a[5n6lDm1":
            output = output + "'"
        if data[s1:e1] == "o.wv1{nNZhc/k!vyB$O{<FsU}hDi1/ei>AyZ(iK%zb3iAoDeVCnmjH/sE4Y&J(Dz":
            output = output + "@"
        if data[s1:e1] == "r[]S&nokFp%{Y$RE,sUy!vFBEc% Y8mkz_0T3*a43Wu0^CD}3b?>hUPrc]$x)21>":
            output = output + "#"
        if data[s1:e1] == ",#Cu2/wxriil}-r{7B2HX57(,GD$TQIvb0Zn%KA>h4=XDravs7lJBh]6w*e{a*W!":
            output = output + "~"
        if data[s1:e1] == "mdd'[IsU>q>*TB$VDisUG*CyJm6L])@yznzq,Zt-XH'e[X5gjy]6qJy<X!:_[8p{":
            output = output + "/"
        if data[s1:e1] == "?dKKN&ys%'{hl>MMKDqWP]OSsa#1n`U)x$2yyD{y6XI&d)?(q w3)Ml??}a`hT/{":
            output = output + "?"
        if data[s1:e1] == "]5)~()k3~pv=)oVTsMTsv!~fWj6AV{sHNQnS+f`j)VU$Rp}pa.X?$Zd@wV'}/(Sx":
            output = output + "."
        if data[s1:e1] == "YXi=U}G:%Wte(nv8@s'Zd%R{5(HAY<!@VF@ pU`/=7m9A5FDm)1cA*eUI_xloSXx":
            output = output + ">"
        if data[s1:e1] == "}]6nqBq)_>1{Jw5.wt0E>-5te6-vU9'HBYK_$jWNsb.=HuMY<wV^km8uWd)-[a~S":
            output = output + ","
        if data[s1:e1] == "6ywI*S1o-$J8dXC*8PNZOWc(p'9kp,98qOF~s!F4^:*Dz}_'P7Ie>&Yjl[<QJqY'":
            output = output + "<"
        if data[s1:e1] == "'TZ/+>$p!Fq,!jGA[6V*GDtJQ'V[(Q^/?5W2jRoLZ d/1.UM1B!Z@ptc(f+$4iVj":
            output = output + " "
        s1 = s1 + 64
        e1 = e1 + 64
        c1 = c1 + 64
        if data[s1:e1] == "'sq7?r6>XKoX,9RCRX%N&i[ _) 5>F-+=25C%G39Y4J>'Y['gVzM6_Q6mA&gaT:o":
            output = output + "a"
        if data[s1:e1] == "('Ih,t#/aH*9+N]/}FBw=0-qgLv?pvOCrDZXqw34@~^N?}:4OS ~_w)MG04n.@JA":
            output = output + "b"
        if data[s1:e1] == "{)HyPe?yLG!Alj>w:Cd4{5<8*h#6y%wPuLbi/sDMgW'#(A:rvt4C<2(t2xm'R/4-":
            output = output + "c"
        if data[s1:e1] == "IEV`It9FV+hEiEH(s?J*NU,6kzu9.K3*^sR#n3:jJDi}iqM4!D$uWrMS!2}]4)fr":
            output = output + "d"
        if data[s1:e1] == "F D[qnD-YqhlRU*_v)%Qjl1GNF^Yk?Bk6',57k5D2Fa(1@o{zWjq'6t]!Jz:krxw":
            output = output + "e"
        if data[s1:e1] == "8W&Xxedz>e3@9D-Reql:)Y?6vy!t+( DX8DSdvB(U*G<d{Q3yxfzizN2zb2O={I9":
            output = output + "f"
        if data[s1:e1] == "AV&)'ZeZ{/E`zQ>qE55pM9oFkv&{i'#<1,LzI(S/isx%XQ/EX272+8qwMp3yWm{p":
            output = output + "g"
        if data[s1:e1] == "c<LWEK,#/p1}K1UTqp4GfoWC}g!gzC4Dfp#MgP~gf1@UR L_<X%2Q7Q#B5=7Ot1 ":
            output = output + "h"
        if data[s1:e1] == "I%ADWc1d'(o3[oWcf5Phr.*wS{e>(yVEE9voy#r7ku9cO&*(Y>.Az9'qiQ)_GaL?":
            output = output + "i"
        if data[s1:e1] == "bh]w+0!sXK9r8A,8A%G I={'pwHm3uATJ>'9dZZF!~>uxTzY`@#<[1CC4#KZq*VX":
            output = output + "j"
        if data[s1:e1] == "eVR=k[MNNnWS$xpl,^@U%2YfL*hnV=83sfFoy[VAzB}(MWXV]odF6jF9gq0+A]@Y":
            output = output + "k"
        if data[s1:e1] == "W4QB~]F~NA9HDK&/y@?2dO(=-,zT2sl'Y06[_E,MHi3<>{$]msxcmBm,J%}XQcHR":
            output = output + "l"
        if data[s1:e1] == "!F<I&{GB{.'VKy-'r7+51SE){vh^lR>>'8A`+o>+yi:HMEiR2L@?An=GP::6s3uG":
            output = output + "m"
        if data[s1:e1] == "%G3q4S{[K0W E'}KKaPI]W`.tjl*p,Qc8ZC6X._~!6U`B'nhcLq5R*#^1mp{Pjz[":
            output = output + "n"
        if data[s1:e1] == "To#2(/~5T0SSWcHHdV.f@?^Tlot0mODIhT[TC-@yOs/c-T_8B!JgbDg6I]dY@{U1":
            output = output + "o"
        if data[s1:e1] == "=<^yUm=d{<sy?H?aNu,OWu?>bdb!BCHwB1o?{80M)inV!E=MO%s8*Hk#Y['g7XwC":
            output = output + "p"
        if data[s1:e1] == "R')8EaY,m).137t@.OpT~lolG@N]i1H[IE7DLL?{y'#qjZON_gsJt+'$cy)!q+,#":
            output = output + "q"
        if data[s1:e1] == "V$9LSV)v}j> BaoV1JgZV+Shh8$X7WOws#'Tc&(H&/z34#tDEdoyh$:B/HMagFZy":
            output = output + "r"
        if data[s1:e1] == "5Kj}Y%Zxgm&XNI#9i)Uu5?]'B%Awny]H&:w)<hEoX%H/'Fe-w(,)TU`PseBP}X b":
            output = output + "s"
        if data[s1:e1] == "kSB`KN<H?*yds0Zz68(8&B'hy/'-I@9W=tVt4-}TjbRBOW.xdQy,U/`+b%2I)}0+":
            output = output + "t"
        if data[s1:e1] == "dGLDJRBlbuvo5R. [^^s[cD$k>u2%LOnlVLy/*w9C70T C@x'muu.W)BOVJK i*l":
            output = output + "u"
        if data[s1:e1] == "MD>w]Z9]GR@?a$f -h{ly_/:J{{E%ZznN8Qt&2UURfEQD}:cVE^(YF=RVb$c391q":
            output = output + "v"
        if data[s1:e1] == "h^%sP1@HxdtCYe[OvHGd%+*sWsG.9:e1ah8FR#vj/l<d/GMB+$CDn'ja'u+J~6<j":
            output = output + "w"
        if data[s1:e1] == "gt$KVbX,-4ex07gK!q3aTrQ}*F4OxmOE)tPzj?K-'W&H}*&CyhN]ZANz{#5N%H<x":
            output = output + "x"
        if data[s1:e1] == "VA=AW]q6)T!9~`r1egHL+.7Kh9(yXs*32!P)OaTmAb+52mBup0/!1t&]fbfNIPbO":
            output = output + "y"
        if data[s1:e1] == "Fp_cCg_mx-m7MaOfTh1`Ue*3iM9='97f=>4ub+jSdv9q=-vJ,d+L{G7))I8T'-@0":
            output = output + "z"
        if data[s1:e1] == "3:Y/_ $)+(C^EY[lcl= rM`vE1fIL1t:,'l'6Pb}.]vaULConErB{xb2,T%H8SW[":
            output = output + "A"
        if data[s1:e1] == "hiY>lkA0`JO W=Yc_7rD>Nu2+q(0xf'=P1zbp{p%_cFE8^(4GA0T^VDg3mQg'H*k":
            output = output + "B"
        if data[s1:e1] == ")G*S?Nrv:oB}inpY?wKnG,/ @K.PG.*b`v-*v`0aK*[QGI^UC&(A]e>rM+FQ0=ds":
            output = output + "C"
        if data[s1:e1] == "h?uO%VtWVjwj(MxHflh,ZIl0fQXtp9s?5CGA5b>#$ef*ss{'?8'-gwE[_:alo`1X":
            output = output + "D"
        if data[s1:e1] == "]=4:R&*`w**t^dW_q.b+pP1FRUIZX/Vv'FmD31'y%}aQT39>Nax)>4aFgji9c)''":
            output = output + "E"
        if data[s1:e1] == "?SD-~luI!vs1&Q'*@}}{8:plF),&7 =ji}y(yl0><Tfft()dGu0k%vXi2!_r$Y~.":
            output = output + "F"
        if data[s1:e1] == "cFj?Tn@%7c_FMA g1!+=J<=mtWnPk8G<xf{'xxAy6{m:i0-@n_D`S'NmISDh4kVh":
            output = output + "G"
        if data[s1:e1] == ":)i#Q0>aTP#NLD)U<+}oA<e<Jua.gY^u!W]9Zuv,ZtUT2VkRK=k@cipHae yZa2`":
            output = output + "H"
        if data[s1:e1] == "g<Z}1p#eRO4HVk{[CXZh8LK'<YU$~MBR!cH6 1TG_K^ACdU*m6]Jv4f6LS~xMXOR":
            output = output + "I"
        if data[s1:e1] == "O2HY{%WYLlrBo'/a7Rx[kuBkD+IhEFnKfJ<A%DiX@vxbM.l6ywINT ZP$va6e/'v":
            output = output + "J"
        if data[s1:e1] == "GAg?gmol89diBWzNP'^rtyPI>MV(In'0O&t'u-Ew-JF~~R ZX.DJghra!$G&c(-R":
            output = output + "K"
        if data[s1:e1] == "(`p3Rk_W'6&6re<4wSN&hwy)w66Qf8rX37xFL6r$B}`wz*nn`&)gvnF=aeLyVpH0":
            output = output + "L"
        if data[s1:e1] == "o3^XS4_'?q?]AO!5olWclwf.KND!PdWb+DCAPB#f2k!R0(_9QXhT`'rfwF<`7,HC":
            output = output + "M"
        if data[s1:e1] == "QmIu]TtPj[EYC@'oFAVtXPz)-r!7q!8sHc2*Omuot-3_v^$VKV>eG'$'+%MUB!OC":
            output = output + "N"
        if data[s1:e1] == "Y8*Nl@ueWJ_:]uGh$'n)WZO^-Xf&:I,r1Qf>n@SFV/OF 2m-BhvEuC{/V`sZ4dpt":
            output = output + "O"
        if data[s1:e1] == "r-/^ZQ{DCad`w.wBrLE[6C)8#Q^ZeS'igTdlG-}]'K:(Ji[^if2wn3e5}Y~~(LH=":
            output = output + "P"
        if data[s1:e1] == "ho25PI?CdUY552-qIO$AT1S^FZypk2(@@o0X]:73v@<O ?PA~xdH]X#_=NWCBr'Z":
            output = output + "Q"
        if data[s1:e1] == ",~+f:uyRxRRLzTrgYp6vKl]D2ZVSyV_.FN8Zx5b@HNfS6ks=89Tt5R3,.t'74X=>":
            output = output + "R"
        if data[s1:e1] == "#o`$3o4jQgC.2h98E2w}e5]59<5!X9FGN0a.<e~,/{eh*^0&c3$M`t]jca_V?@8t":
            output = output + "S"
        if data[s1:e1] == "`J^czF.+6u:bab7?USjuYrG!z']d,:ARV/Gv0WLjr%zAi+9BJ{~eGc]FMor4ajx]":
            output = output + "T"
        if data[s1:e1] == "1S)tj(~cpYNuN*'{<{$^[cF1MFlG5=XvjD~rtuN,s?2LWAT*rUWnA.IKJ&ti!<%m":
            output = output + "U"
        if data[s1:e1] == "cgi4kR*!P!~]M-?O-k?+F])^Ud]q!W09RjA '0^fCdHbRTnZ}t8mJ$:SvE~0hvE@":
            output = output + "V"
        if data[s1:e1] == "%Ks($.=?P rna^&hx0&N61[7)k?d`~H4SC.pq8&T>rm]wem+T^0Yu8_,3NF+/C'5":
            output = output + "W"
        if data[s1:e1] == "O(YZM4QpP8RoMS72-8.0e#Tv8Km@?.1>n8d.JI5&g&< 6ZWMZS)!<&:n/6xK#Qj~":
            output = output + "X"
        if data[s1:e1] == "jNae d1%)<i3s?'z/[c *bUv&,l)JZ7nLwvzIlaMUO8t]]vo4rT-k=G~ri=Wz=C4":
            output = output + "Y"
        if data[s1:e1] == "@!Ew_K{s%/l{el{_gszpkf05#oZ]`]1Ja?S!!&]+Oi(%p9r<ImeFGnS.:2xndlN[":
            output = output + "Z"
        if data[s1:e1] == "?Swf`*m>%sc,g43@w<Dp_kUw-:?YiiTD=1(75Fc(U-c.0IYoqB',Js3h'h</(`u/":
            output = output + "1"
        if data[s1:e1] == "m,DWFS~<{iRZwb=H,bX&[~X'QD/C>4FFvpT5u~38J5LkXew2qE=t3akI.)>d*eB@":
            output = output + "2"
        if data[s1:e1] == " -AzhU-'r`YI'5kh[lIp $IW^=/n'3/^+ENIN1f%gsG 0>edO ,QwWe]7Ho2rpIi":
            output = output + "3"
        if data[s1:e1] == ":LbR.0wb-1a:06YTMYeJk>KcM'x>0G'A7ukz%S>5NRhe ?UAu)qf mBLQP#wCtcd":
            output = output + "4"
        if data[s1:e1] == "7lH?k$jCpE3pg:'z5sp*?sJ]=k'jd'(K6tBOW+Leax^'Qzy n6Z%[n$4f#K9_.[v":
            output = output + "5"
        if data[s1:e1] == "k!mFaD_l$<x4R+I3W8V2<>O`Pc<Lie~<FtFJ Q:~YjqhPsQm#SEXQ7G@/`HtuQrS":
            output = output + "6"
        if data[s1:e1] == "L>Aj[*o:$#'u<f#M2fPaZQG''7kH7Hw7ktLYUx^qC :4&7`W<x]eL}hfPkfN~eoE":
            output = output + "7"
        if data[s1:e1] == "ja=']EQ6YKfgW]n%{:@Ii<1fOWA{d{ot+pXp#y)yBjJ}TP B5oNe:Z%nU?6lM}&<":
            output = output + "8"
        if data[s1:e1] == "/clu'A'<s=Y)AUV:g`8aO3*78q]27h+K th#M 6~lPMqbqVdk*Gg3:D=[:m^U4z~":
            output = output + "9"
        if data[s1:e1] == "'0p.-zYTHjvp``T`Bt43.sOVE`9]<T5!2LoePAcx+}IoY07cW^(U&/#J.zeb<jSw":
            output = output + "0"
        if data[s1:e1] == "}`Phjmf(Y9-aUu,JW~m1M$9R&/7f2LKU[EsL,#F_a_mVAO86JCwmZ(J_-c'pXYjl":
            output = output + "`"
        if data[s1:e1] == "5X,f-S!!*qp'=b^!cJS.2Jhm!M*9x(MA0Rj$vx3r/X'PiOiX<}uOsYmo2LJ-%~l$":
            output = output + "!"
        if data[s1:e1] == "wvzJZbmi&A~YAidMe&'(jE}RCZ}#bv6^M62HBO$k*$gmbE+xza%Oj2o%X^RUd1[l":
            output = output + "'"
        if data[s1:e1] == "6jDfi6n+p=<cA82pg[qb.BY%5_4GI'+wksSKR#e%}*@}~Ko!MqpZz&mGDt`v^!5I":
            output = output + "$"
        if data[s1:e1] == "'W4c <2q~Swu`BIU~#:ERG-?kdAS3yonk0]cSg_K*iNtFXav9tg}U5dwTy1$3H$O":
            output = output + "%"
        if data[s1:e1] == "C.u$^$PxneU/[r,x^dM($Q6'){)qMBYi14XV{.JCqRvVf!tg>5oL} OP!$sv.U/i":
            output = output + "^"
        if data[s1:e1] == "izfH}}+Ys{-5Ik-'GKlVxMvU6l9o%RHPP$G9/1qfjnI$*'#B^C`H$*qIrm9R+z@u":
            output = output + "&"
        if data[s1:e1] == ":>(_FpoPR/~QFlM=UT}bs!abdw(<qIt.h4 56GbTGNVODUk~1i`[K/Kr=wfah@R/":
            output = output + "*"
        if data[s1:e1] == "'SsYjfJ>{JQ0ykHBbHuK'mD)3=4,96+&qV6p5Yo0U[*'PSz5hL<$Ej8:9w^Hm2'a":
            output = output + "("
        if data[s1:e1] == "W(e]0CNVkLMfkr&zHk>c`Lyo'u?_IY?#>H^Q^T2<:x^1#}kF{,r8j,s2j-@ymxw^":
            output = output + ")"
        if data[s1:e1] == "9D$@)PD$pGDS*rE!yPr#,gn#[5t$~8Syfz{MXxU,M4/Qc4EBJ1Z{bqK3_0X'}cjr":
            output = output + "_"
        if data[s1:e1] == "w&DC~'%@@Sgn_[1D`K,Z3qIWToN':,V=XxCru*RBI>>)&%6EzL>gH0zl[s&^l`~&":
            output = output + "+"
        if data[s1:e1] == "4t8'Au'j)*[( BYsl7/tpnPL[B:#[p8Md}lWbr$zB%I!4@Yg(l9WjBw1>/2 qe n":
            output = output + "-"
        if data[s1:e1] == "xdnz{n-J59L_W?)OJ#@4Z-W$5zhQZjK%i2hFz}{^zh`77-9<!#T//KUq1~%x$SY@":
            output = output + "="
        if data[s1:e1] == "x1ZC `+rnhQ0+,)MqbqLZ*!m=/Rn*v$?cO{g61j:)^'s]AIdO[x'U.9'Es]?TH@h":
            output = output + "{"
        if data[s1:e1] == "-_EK7 A(}+bWJBsvIEV'Qnp{%`]_aTGAogq='Qb)3S8U'0X>b'X#PS_6P[):c>jZ":
            output = output + "["
        if data[s1:e1] == "uvhr!G5GVU,U'$@^_50[qIA}7'`Mi[e,PgY!+e4n~_y#}Unko4i_JC%Z[=^nt+Kq":
            output = output + "]"
        if data[s1:e1] == "~<Pn@Dzb.` eh6L,wrqU>O<cP+ pP8TD^fA=%XICya&`Sb[FyS@52gmPJu04,J0c":
            output = output + "}"
        if data[s1:e1] == "!1=$QR1q6]Y+%i(Qc7nTyK&hQs$%/r*KQ=_?_#r`k&'1!RQ8uN&/&rc4G@39a7Z'":
            output = output + ":"
        if data[s1:e1] == "[ggX,G~yTI57 :<CR<botpMaQSxCpjLzxi!j>`g3fB!DE=1k_?k`KVX,Z0ceDlX(":
            output = output + "'"
        if data[s1:e1] == "uxUH) ZP6`^QcXR4?vhkQl7]ZT_sumi~.>~HbD5,O`nKCU,3+y@:8Pv..eKn*zc:":
            output = output + "@"
        if data[s1:e1] == "=7au 5'l&Ube!#$ )QVa=8k3ipD*T2>6o>&>wi/D.5<8d#kxLc:'~HB4=d7@bC&O":
            output = output + "#"
        if data[s1:e1] == "O~.m>SBq:dd!sZ#{vs.72q(vYyLU-rkj,lX}P7~]}6F<J,XFNi_/K3U~D?ln.6Z ":
            output = output + "~"
        if data[s1:e1] == "`xS3fw.2-auf6aun^9DRtbb=sx>,^J(Zm8(13>}_[q?(~vw>[Nn~q#xNj)H.s1(E":
            output = output + "/"
        if data[s1:e1] == ")tU^{p'@$bi}y]V%[IaS{GE-vqo:5bzdyV:#CT[ep&zr`.J[96Z+FZJ+!?a:dN#7":
            output = output + "?"
        if data[s1:e1] == "-waD^'3N7Qc_iN:EvGWj&l%)Bo3.^T%''(}h{hkK[m]`0-0~=)Lm7Qi Be_Eg }4":
            output = output + "."
        if data[s1:e1] == "9KXo+G$MW}$fx__2?HN<p3,EpFm/xy#r@Ls.EQ5~@v+AV('o}V#}O8j}bR@+-u b":
            output = output + ">"
        if data[s1:e1] == "A*J5CB%p3'IINaEBu4_2[E-(9eyQRhoNO{n'>J-&%CY?Pl=V@$+BLP9Q&H0dve53":
            output = output + ","
        if data[s1:e1] == "(ed_O ykWt4NG4PCAMDc&*z%fyAJp-gD@6}J2xS/[8UN[MzZCL#0mj],G?SM:fg{":
            output = output + "<"
        if data[s1:e1] == "gM1Gu8mLO79L4gdyVY7CK{9[zK]]~0tL73dLK}?/87SNy:m$-JPFNbswz nENqb7":
            output = output + " "
        s1 = s1 + 64
        e1 = e1 + 64
        c1 = c1 + 64
        if data[s1:e1] == "Mg[ZIq(]-Sn!m3MNCNg^tL:)w8i(0U[ZNF0y_wkm/59'J:F~vBakr`:x-Su(e:%f":
            output = output + "a"
        if data[s1:e1] == "$'%]tpjm ?R{Vf#4o7~k)@tD&k/=8I#H}ENT6^#A8?sDiWI{ld'qvIhNr96~$k_&":
            output = output + "b"
        if data[s1:e1] == "nQiI_+[hLYg}'b+DcS't6O6L[g~1JiV8H'vb:>5)fBd7!iUZ)j3$f^'Z@}nxm4$p":
            output = output + "c"
        if data[s1:e1] == "fjMwo$lob(-y%4>2g[?-ktpziL9JP<DE0Z'M2k)Jql0%zE9_l)]2_0c6$2]d$4LG":
            output = output + "d"
        if data[s1:e1] == "r>-<RJmESr {S4VT,jlf)@E>h.Cc@$F{O9'm<yThy^b'S[X5Ybyt~<<E3bm][]'x":
            output = output + "e"
        if data[s1:e1] == "v==ZN)@kJiHP62+7E0sos.1%N.YO1,q8Tio:w[%rt[C~awcDqg-&tk!G)sjp&8uD":
            output = output + "f"
        if data[s1:e1] == "(Bxp+qTdGgrU<d87*mB<QRP,L@vV+k.u1x_jHds5kiM_^^96S<3?2Vld+Q6UMe>:":
            output = output + "g"
        if data[s1:e1] == "fgxFlJ#sdVZrQ8kB(->:sem#wd}eMP1_Fn:*i?P+Q(c>Aq2wg)8}'j'<5kHc[WxR":
            output = output + "h"
        if data[s1:e1] == "But}YBgtB*xoXr/VAV9~?rto76.l5G:R77QU?2z,7/?>g~ nk[Sge+menZ-$^{F,":
            output = output + "i"
        if data[s1:e1] == "Si`S`&%B>NAID[u4lad5AL%:.!v<[t-4 7?*Jvb42M{_+(3CQ>#Xg'I^AI$*ymN`":
            output = output + "j"
        if data[s1:e1] == "-HiHvs{`pR%Cq2{QC9{l)'6'{(olGcG$9XsF8,]5MOX($yi8'}Q&oE8`>e]fqrmc":
            output = output + "k"
        if data[s1:e1] == "#defBYmBB97(E0:Ct-t5B1?rcy.wD,~czb^asR$',Xf<<jGUt5_7Z6~fEs-5C~66":
            output = output + "l"
        if data[s1:e1] == "IjxZuH@7T,,$3K4~]#F4h0c5?X6zXK=Vm AGNTwlV*L`jNLcdz21g&5LpXg#Y4-1":
            output = output + "m"
        if data[s1:e1] == "p:u0KWHGzG,h3u7xdMWG]5{j&'`W}V-6{fiP.au97+kvw?/rfrpw3yU?3m0UV?<h":
            output = output + "n"
        if data[s1:e1] == " +^Oq@Xp?yz~ ii]O'{Xp`xqW>OMQwPUU7Lt?*+7NZQP0%0,74?Z^b=@>i.9/H78":
            output = output + "o"
        if data[s1:e1] == "%y'XFGM=Y9d:S7{^r&u(+$lLsF1WcUKOj--CE23oT&6rz5wa^0!`v9RoS?)&^tUS":
            output = output + "p"
        if data[s1:e1] == "fTm>E>zS%w9wrz*c_A8b>'nys8>F+x~[H!dn%{%a#a3%i Nxrn_80a`D%0(%NZRE":
            output = output + "q"
        if data[s1:e1] == "0AK'aJH>}c,e:,DO*wD9'dfY&(nCcnH^JOp~n[!4jPC8qFXXj)[[(K<Rg['zYD*X":
            output = output + "r"
        if data[s1:e1] == "Z,mgbZ#wLe2Q#t=zOAhBN'?7Mp~`~c'l#S@b~+!T^<Y++J-0yt(< ,-NkZh&nFDC":
            output = output + "s"
        if data[s1:e1] == "Vk>sLR>&6(2I~AS1r89W-^tG?cT!bC~at:0`q`O'fF ''9MG`hjUD<XDb'nDAA?j":
            output = output + "t"
        if data[s1:e1] == "+yFaOxu7q,_[.P3 P=G8ewlTcM+GH4'T&[ BA!Pb#MZH7! !:OMPh[6l*dkM'Bvs":
            output = output + "u"
        if data[s1:e1] == "gn{[C=''p3KJ=omwyA^a#e8T{QYnfZ-B^cI.Rj93RnkL]'g9isL1qg =JIWALe=A":
            output = output + "v"
        if data[s1:e1] == "KppBL1Tk6k_No^t%F^d[)}XLVY',9dtBIO/+ys.5F?ge rkI0p,681^4<n'}2[T[":
            output = output + "w"
        if data[s1:e1] == "^y .{y0&5M-I<AE~GFRpca8cEul$Jobh'oAIS1USyurU~tC`'^^ 8%ygg4UH#S5A":
            output = output + "x"
        if data[s1:e1] == "CQ1DlFgI)raD=n7zK&jQ9l pHV[?J3tk*k:ZK}zz1sF+q'#?0/ n@OeyvK!L0A$S":
            output = output + "y"
        if data[s1:e1] == "pN{CzfT*`P<,ENy8.ZwT<EF_3L!]wC!6H3yVcPI+R3b.rjX*D?>0??a![WEZTvA(":
            output = output + "z"
        if data[s1:e1] == "}HOu*z]WG/Y@p08B 6U62V~qa`CSaK)YlQTG{kX40+kYdWe0//2HZTI0`qj:}P+M":
            output = output + "A"
        if data[s1:e1] == "&i6]X4Z pH(Z{cRACG2)-fJ_8W~}9W[%+eM1v1sd8@uwbl-J$1_NT*y@op&_anWx":
            output = output + "B"
        if data[s1:e1] == ",txK=[atKV0%f#NG9/(/$eta>.#'&[P$zPPesb?t7Sg&/ /zDQ+JbM$,'16,,<9K":
            output = output + "C"
        if data[s1:e1] == "8r`'Jyu2&kxYb`f>e,1<S$:hM~LWAleQ4dQjHWQmi,mu:V*y6M{M[&iJO<%oCU:&":
            output = output + "D"
        if data[s1:e1] == "mGaJ*oCe Kc=6*:&Eu3g1AE'1jKz3$MtQ%rw~mD#i%N</RgtUB8OsO<TIk`Npvns":
            output = output + "E"
        if data[s1:e1] == "FBHk6uMCQdBZhI)<KturL5_B#boAJ@WC0%  y4$~{]RLNs3rZoexf5$%27=>`wmQ":
            output = output + "F"
        if data[s1:e1] == "K!FY}hoPvINn(2A'nC5&avL]76sC)wVxt@Wz}i@c#j:/P*C3vb:7xA]rQ]i7g)Tx":
            output = output + "G"
        if data[s1:e1] == "4?< /SNoU5jyY#!kolFx):ve/({'aJ^ygnDUWlCD19UH=*H``'oG.}@k[zxZnb.L":
            output = output + "H"
        if data[s1:e1] == "PN1xSK(h-V1(5@K)1#[Yl+}]>c':%[%EcN>*d0z8j_6w}5bg&bUV2Bg_hTh0K}=U":
            output = output + "I"
        if data[s1:e1] == "42>)I#2$r~]{BVR%cz],zXbv`vDp08n:mM3:wN}PkS]jRf~B3I?1f2s~g+mz4+iq":
            output = output + "J"
        if data[s1:e1] == "qGo?)od1lWrxW5^UnU3l&dbz3,/(V2=NSDED[}2fm}WM,g[-V7F2m?d<-9wkc'uB":
            output = output + "K"
        if data[s1:e1] == "N^Cr~wzZjCNsnY<0g!/{'n/K&u_XLOF5FI:4_^cd3ll`P0.9~I)T1UFEL4 PhK#y":
            output = output + "L"
        if data[s1:e1] == "YFU%'R+W?3LoTk?bx)0!uHJn*BZK/7.{22To}3:PD=1q9(}S,23hd (L<ZmV4%-U":
            output = output + "M"
        if data[s1:e1] == "ICPG&BL~d/bu0*n-~wNgXDZ,PyFL[)i,=Uc@>}-^lcn00R^}KLS)&me&g@y8Vs7/":
            output = output + "N"
        if data[s1:e1] == "*H)bQDxZ-,0 3Sf9Gh^q0Mgzylc,M~W#g<sT1Ww'K8<<C*i,d*rVm>yexl-WJj<7":
            output = output + "O"
        if data[s1:e1] == "HtcG=ioKu'@m,tgQ%zy'eRA!Jew.8fuvtQ@}(v4MSFcznrQQ#!-W$)Uvn fTOF0v":
            output = output + "P"
        if data[s1:e1] == "/W#57g&<=.l*PhK=^XQ:>UXf,WmF(uXKDG>q3b#Lb>E$md{~3d?gOmog}e+*9wMX":
            output = output + "Q"
        if data[s1:e1] == "'yzN!%y>3klYQ&wV)=!M^Z)`OlcGP7@2br_Grp{pxni7?v^#KFAC}3xV/,d1AtCl":
            output = output + "R"
        if data[s1:e1] == "3yCitEi^@@Fd#RW}Ram_&dfu>*]+Gj'~v'r&UqvpC<NSU:ON1A&Yum=+l`.Fvb0(":
            output = output + "S"
        if data[s1:e1] == ":f'b/lzzAVeC&U:7.&4_Djy/Y:EY/x.)5MP!sWb$<n/ =4<@_7yCjID],2w<,wVS":
            output = output + "T"
        if data[s1:e1] == "h7(iQho)[UmN<A~WHQk6s's'I-3h_=h{!P14{d_mbc%~N(Dz]H[MQa[K'Zf!D*lY":
            output = output + "U"
        if data[s1:e1] == "a$PLt!i=7>qdBIsH8Xf2f--*67>`n+X's7!O/*oe`ev{Fk ofC9+MQSR/Z^=@j@E":
            output = output + "V"
        if data[s1:e1] == "PlISi_98k^v4Tv]puXv66J!Gn}]l4WFg^kZ.N/dhur1<$I)MKhyV)BKuEdJJss%Q":
            output = output + "W"
        if data[s1:e1] == "a~pP~1OMg)-RUaH-o]QmhsOGB,T{FXHRV9*,e.DXQJ2YTdX x>{2C!QIDVDi'}}G":
            output = output + "X"
        if data[s1:e1] == "e2}o$76 >zwy'Qe!LpBj(LtzKxN596SD. S/Iu['6fGaR'#tUXhw_aKM.K^v'-z#":
            output = output + "Y"
        if data[s1:e1] == "ve!r:'!?}:pT&OL!4'FP,I/%gWvz1$:zB-gKCOh5$Kn#A%x7tr/oF2.a]yN32Ed7":
            output = output + "Z"
        if data[s1:e1] == "6B )o~ca&X3X'6K8 9}hW}%gAiy8y+O06G23`ViHG>3)QKZ`<bdi4I%9m.)$V&e4":
            output = output + "1"
        if data[s1:e1] == "YEEN>Vvd)VN{~ZEZuisgV}0?*qQ=iS-U-RI-(#fJM`{l*Yhx!Jw?l8+}a()b.k`L":
            output = output + "2"
        if data[s1:e1] == "5E/a[{thJ:=4YZ'_s[=j(mWRGxEB4__]Mk0d#^:!]k`9/ipXBm{OW$1VC$8y2TSD":
            output = output + "3"
        if data[s1:e1] == "6x.(y W%8_^ub$jy3Ia/oWi}*RF3Q 5h%VD~mZ-Ybwg~'.@oS@'FUpb:RC][:*c#":
            output = output + "4"
        if data[s1:e1] == "x_g8s(`Xq]]lB['1bx'WzUHqY^ `z+krgr0)V)3=xa9uKsRnO$i$+XkedW{oVF&#":
            output = output + "5"
        if data[s1:e1] == "izay'ikjo9=/R<hXXH4#N{nU}Tt@~w#Jn{T5^ETH9Q%NG:WU<:c@w44e>CAn=GqD":
            output = output + "6"
        if data[s1:e1] == "+q ,bPYu:U -eqrp'5oP?Q.RE=E5fCwH5p5/66SFS*kh3ri`rXwj,1=y?HK^'a=H":
            output = output + "7"
        if data[s1:e1] == "(v_'}{Ej'JTn'''a)2(><P+Im5+<*]aRPPk GVx:.1x::n.Z/cm`M$`~uLoI7s<)":
            output = output + "8"
        if data[s1:e1] == "S}'J'O:h(J>/-Se9 jsNU[D'7-pKtSfxs{^xc* y_l3@_/~:gRI8@z)}YtJD%.+J":
            output = output + "9"
        if data[s1:e1] == "O77X~g^5$cq]qHB$$.xK.Wq8j[1'tuUOAWqFP@Vn=izEG+8Wkx+BCI{v>2zlBto]":
            output = output + "0"
        if data[s1:e1] == "+jUqIEcR9($MlO_<?P`uJ09Sv@Uoe>ZXI%DNUBJ1@OuOJQj=+VJ5k))Cu>G9LhEr":
            output = output + "`"
        if data[s1:e1] == "-z[%nl1Pp?.Z}'V%:}`d2#wsTT!TrZzqFR3-2jL{?J@$Cd]=u*OEW='#IL36wGj4":
            output = output + "!"
        if data[s1:e1] == "Q*G+vv!'D5}QT_3'3'R8=(9P'V>yDlG''p2-b(uME.,BqLR)j3)u}tO3mD^HNlTB":
            output = output + "'"
        if data[s1:e1] == "3]JEWa=ZeA#8WG%L?>uDGa}uJkHR5b<<9kN:0ObX/pu(6i!MEj.evr/S[P+(bcRt":
            output = output + "$"
        if data[s1:e1] == "zYUZ2?[3`+Yhi_' t[V*)-ueW^!N1j'6~7x8ANh_iVfa7@<m>rRC+*$0zD5MsSkP":
            output = output + "%"
        if data[s1:e1] == "SR>'1jhC$,mgnJTC'.5=OB~GfKFyN7a!Cq5tB&WPF_+su=s+ARB:*o__&6#GT/5T":
            output = output + "^"
        if data[s1:e1] == "-i41'*zE}Mm^Rz([9@JI7K?ovkP.=ucH#ywvELbrat_7OpEj6Sr]h]w,MKX%G4py":
            output = output + "&"
        if data[s1:e1] == "cLEf`gQB?v!%W!$z6lRs9(.bM<%Q7AA`Vqm**Q!avT956Z~n-tAj$NvA>.`~FY(v":
            output = output + "*"
        if data[s1:e1] == "?`-6=R~]x@IAIrV 0AKEtM1lfaOg,^ta)4^w:b/=8HM/1tk?1J6#q=oH$n]HGhN*":
            output = output + "("
        if data[s1:e1] == ".EpN%Tx]TM1aMOEvd7&=<'s_2e1>U^Hl.i?'hp1n}f3DK{BL]pb5na9t'alcDUyA":
            output = output + ")"
        if data[s1:e1] == "7DMZXSaK.d5Ne61KRnIQ_i}:*YXXqUP&xq4~Lg?{o,.WVO7HpmJ!rUY0UVA2`q#k":
            output = output + "_"
        if data[s1:e1] == "v22 /(RfW)Y47JpA>hYbIy+ru^pX5z=G21P}bI'9EeIFz`k#aGGDiwqZ'$~+i@?X":
            output = output + "+"
        if data[s1:e1] == "Ie$%Fo!]rHi&@bLXk*5e(xuKDf&Jn8uWF/>)'>tsHY`M:#vy4C6c*h}s@'-o8]K#":
            output = output + "-"
        if data[s1:e1] == "@PQ{R.'`{_2!'^J,hr4iug#-@JBx$I3llI.[==Z Nn](X>cYbMxwwBe^d&.OyoRY":
            output = output + "="
        if data[s1:e1] == "Lc4@YVpo3Z(eTi_A'6,BI+@!fhsVh8$&mXv&c_Zj'Ld-*+[KJ! ,OaHG?[H}Of,I":
            output = output + "{"
        if data[s1:e1] == "ZJN#e(O,!N@euWlxYmF2iQ08FcPBV{<}1_O)Ov#*]+(q13Tv^0edrzYsvf.(P=2$":
            output = output + "["
        if data[s1:e1] == "9Hp6w^dG0i(=pTQmfJc3lhq8#]O6@Tph$jMh! YscC?$*x*6O2{<R54SYO}-ZHz$":
            output = output + "]"
        if data[s1:e1] == "UL2D#97,c<mwaeBqX!0Q`5gIfms%yx@!1*tLWYq?nVz~E]vhEc*4!!c$&0wDVS`]":
            output = output + "}"
        if data[s1:e1] == "SX5f5'YGJmsy?X!w .+=-9%E~A~E`# du<CR6%+_,PYpq2'mRRrC+.Fhf/) Axb_":
            output = output + ":"
        if data[s1:e1] == "fNz(Gock_j>Sz@=<a-*cM^'XJp6>Gv,@/YZP@,rBX%fV['3YlEOPUfI@O#t~qAaY":
            output = output + "'"
        if data[s1:e1] == "Lh8*!wd{8oIR pW9]H=4s4S_/$`pDkN8s>JQ_Mh.-'F/serT)HAm!$ K_V}-SuHY":
            output = output + "@"
        if data[s1:e1] == "wn5{?j0{xWoTZMZ~^+zk'}5FmSWS>lTug4n`GKNt0 @{?ELj3I*l&kq7QDfsp4C&":
            output = output + "#"
        if data[s1:e1] == "L>~d]dXAHKkYv=1S'a<599Xa.[JU/!/M[XoWD]GHEP!]8VTo.Eq5/M,r@,#@V<KG":
            output = output + "~"
        if data[s1:e1] == ")e(f:ZIk4Dj]8jz7UI [`t[`^w4PUaAoBvBYj.Fnb+&fy'qfySS5Tx&:w?TAJ<q-":
            output = output + "/"
        if data[s1:e1] == "1eYCOBltQ2A-DILDO`B#Ac5.Lxad^BQ&jR:Ch'Fz?7)m?Eqophqw,/FCj:ZQXX _":
            output = output + "?"
        if data[s1:e1] == "%`4?[4Db%v4j}W@U6YYFj%T#KK'oZRd uY:eEeu2{l6A]g3i{rehP])+E@$ T!qs":
            output = output + "."
        if data[s1:e1] == "ML]_3FSAHN^8fgbLmxr%jfS~9O@6,=104T0,/sPi=ZwL'WU>%J&-6]cbq8'qReFD":
            output = output + ">"
        if data[s1:e1] == "O?lL(Pp.4)rfc1o80/TB%'pq&hLh)'Uvd<!2u#^R599x8dKsx#o&N5_{.(jqm3[&":
            output = output + ","
        if data[s1:e1] == "('``'W9{~2<xr_PBeg{A%:kZKC*Y94u1Cr>b%nu)wAp57d[{ ]CRpbvKnwH/9aB/":
            output = output + "<"
        if data[s1:e1] == "`dC4QhU{0#{PG0]}QpqJ2Q f{_@0hgq}nOsY(m$ov&[(=>O :y8H!*7&2HapZ@in":
            output = output + " "
        s1 = s1 + 64
        e1 = e1 + 64
        c1 = c1 + 64
        if data[s1:e1] == "]d)c!$YLlX)kX:<u7/G>4<Q!]`#Arh0&xi^HZ9X:xkF~+Dpq0VsKqlh-}Pa1 uu^":
            output = output + "a"
        if data[s1:e1] == "D4u',-hHa4YW)_v=qiW+(M,JYw5kCKX,]8gKVfSL3B[=YxNuRJ2&=FATRK$QuE0n":
            output = output + "b"
        if data[s1:e1] == "6kHUN21Sj&YyQ~05e#4:{U+K&Vt i.*((_2EkmyjEV*!bFM=:FI6 $5~PbS]r,2%":
            output = output + "c"
        if data[s1:e1] == "Mmb`BA.sQ'3,trXg[D]mF3AIDa'pca'TkPdx$x{1S/0<EJjO,<RIpa<C2>gC:!9(":
            output = output + "d"
        if data[s1:e1] == "`WyywsSWc'`3&g$b$r<GX%L9d`g8>m<I]iSgBbTo%~vfYBAP7cfu4SN{O+$Z.@cE":
            output = output + "e"
        if data[s1:e1] == "MM8B)-[.$BMm#J(Iqy*?/ISYg#G{a,?mV)-zcnO-XV)N0_sp'OP~^Q@&}<?%!'UI":
            output = output + "f"
        if data[s1:e1] == " o k##X[gv~S<_?YYlb@Kq=pR{`~3hkOF:bHYzjnH]dafjs^obf?,v~N,F+_9mpd":
            output = output + "g"
        if data[s1:e1] == "O]K+eQSC)m7nv4Ko=2Y(k'Cu{0d^N !LnO5.4^='VLvQjXsWKz'bv 7~}MGkl_M'":
            output = output + "h"
        if data[s1:e1] == "x~h5F3o?sH[iI<DDin~y(9{G8L?[h.]*q5's=WeR$fZ4dZ$UXL(m8-^/l@&'6k7S":
            output = output + "i"
        if data[s1:e1] == "nx'U%-^&fwT5URIFnjA^r+5)X!5AyN%V:iHX'%-T{Ol5:lTaMTmxWDT!S`yDO0kW":
            output = output + "j"
        if data[s1:e1] == "[/xw7eK6ERz_wj&%Vop)B.WYvoA(/CpqtflYr4d[K99OK.cF@&G6GK9A}o8JO+_,":
            output = output + "k"
        if data[s1:e1] == "GP[Q,Zrx2eZK}uf0JZHMe3::x5piZVB%M@FWT`WI>oJhnFs@e,_Inhu2A#=fl=^h":
            output = output + "l"
        if data[s1:e1] == "u[YOImxVTG~5 &!*1?R50bVWsvQT`W=_Jf~0MXI1 ldyrB7'E#hJLF.g_{Po?P6]":
            output = output + "m"
        if data[s1:e1] == "9m5}pl)Sk^G/+48@k2-b=+opCCm]nCF`lyl/j2%5(/Nc2}az'*B1$EJ$DA +X?4U":
            output = output + "n"
        if data[s1:e1] == "]-D?`(XE7b8HP_MP3B+7@Kt<e%_-4%:mgb7<)EjDUX G#{z2'OE]Wk*.`}Yr5BAA":
            output = output + "o"
        if data[s1:e1] == "AmM xa'~b:/RZL1]8ROV`<I1((YpaL[8*v#mN^bSA:}bEo:iT^{H**)B$lUF.KRI":
            output = output + "p"
        if data[s1:e1] == "cl8MUPa9qlQwI$Zx^?D3MEz`z'9T7[MnU[:`^JT3JU`wbMcC5~{'Yd7`DxDSL*DG":
            output = output + "q"
        if data[s1:e1] == "li'(F5f-s',_kV#?5hg$>_l:c3F1jhM$ai^RG>vZB6&j3+0I'X5j4l@}9&aHhp^f":
            output = output + "r"
        if data[s1:e1] == "@5d:*88~^'QSF9PaJ1kV1dG#UF.>B5o%]Vu`2LZ1UI>U[9k0`&UKJZ+TI=G2T6OO":
            output = output + "s"
        if data[s1:e1] == "m!GV{:L,<=+<#mw_,94e=}E8PT:b-V&p72Zr4RMz0:/!P0mrGCBE+0/sHJ-6-K1d":
            output = output + "t"
        if data[s1:e1] == "!9]y]zF%W??KwDm:Uf}>Dh)>_{KEV+3qrYVk2~T%]eivCiTv?oS!4.<$0}K:l&6Q":
            output = output + "u"
        if data[s1:e1] == "ODdP6@GSx.:IXth_cqahE1}bv@701^2i 2gj'vdMz#THSmN:Pvoeubr,6wrR@v.v":
            output = output + "v"
        if data[s1:e1] == "Ec0L5ht/Flewx&'1D8Ala7v&^yO%W_TzDp?)Mz((l_i~`*(!gYcj~}#4 H+ys!['":
            output = output + "w"
        if data[s1:e1] == "'Ct33.*B<be9))q^-GzZqXB/p'~(j%]d'/oWn2xF/,Wo>y8Id{4m?Dc~(]}tKwj?":
            output = output + "x"
        if data[s1:e1] == "/RrU~d]&iiCfA:M`IYr@AeTtddKE.UkG*7C<PN+U!^u&RKQ@WA*P_SrK>]{<MG{=":
            output = output + "y"
        if data[s1:e1] == "Rl0=%5B)h{l!wJzu.UQBl3Ue/]B}k wKOJ*AKVJm*~Rk]A*:BrgCIySw_e1&Ou[#":
            output = output + "z"
        if data[s1:e1] == "GbEGxy9uS=v~m}TPYzp$1{!t$#o2s%}pjhQWHun,I/y-*# r[74Hc!y%/iB6IP e":
            output = output + "A"
        if data[s1:e1] == "3N={D<%$9Xs)7iu~K!eA}'~j.cv=%PZ>-8%,[8ut4-J&7T D['7IK!jUGK.'`GO=":
            output = output + "B"
        if data[s1:e1] == "+q?No<Qy#}6elN#6n1'2Am5zwd5r6e6yV.=X'[dv`wBc0wL_{qFZ`MN(RC50$Ke(":
            output = output + "C"
        if data[s1:e1] == "x/ST#G6Art?Dn57=czC^tbQDi>je3CoE2-j7ceC8O K't=P9F>xm&JM#c=7526C)":
            output = output + "D"
        if data[s1:e1] == "[N~CTh^s#0?.Z%KCGV)jwq3{kc/^5z&1%>1(lYg$m ?(Tsrcx^$W4cM~@a5tugdj":
            output = output + "E"
        if data[s1:e1] == "1^!8Pw+k~gS,^PQdBB~`UE<<b7_qly,o{v]NuI(%4g@a[1OgGWD2f~?>4OmAS/qk":
            output = output + "F"
        if data[s1:e1] == "*x*vcwxc 9Etsas4)&2IVjZXZk6W'tq2zcoblyd}H'8w8(x&E-HnN3CZWT8v@)qn":
            output = output + "G"
        if data[s1:e1] == "]C[''Lh'g/#Sn2Dr@=TVFlax'){uGP( 5h??+-'*Lqs~cdq9gao%pI@Ouu+=L,,d":
            output = output + "H"
        if data[s1:e1] == "_1'hD1q=bTTlH7)v[z`Rc&]P)a4 T'BlDVGhIb3dy^4Ar9/=Z0y4JMI'5s:@'U^z":
            output = output + "I"
        if data[s1:e1] == "@xG7Z}}*wT>g@+MX}?G`Z0^JA5g]}qr7z7Hag6Bqn+`Ep3ymka_gW1=7<M*pzp6%":
            output = output + "J"
        if data[s1:e1] == "@RW.j#!*N3)! 8NP-{4_'[L`h[{HP=$:BboGk 6+m/wweAS_d:%-bfv?g~@}HDr!":
            output = output + "K"
        if data[s1:e1] == "SPuE&X[+N25sza&g J#'am}?I@VB~*h2-}50~>bdU8HX?'S}B.{yO.9YC&)ngY1y":
            output = output + "L"
        if data[s1:e1] == "D)550&<@s3hx=.E<&#]{MeHfy~<9Qf]yl>EQWTx>Z_o3gHs{L~w>Sxw57TWGMoB$":
            output = output + "M"
        if data[s1:e1] == "iG]NMfe',<#h5cpC)Q71b} -.x/= NjX}zs%('Q<fHMKOTge8L{iINFNt%YNxXOw":
            output = output + "N"
        if data[s1:e1] == "~'Kntn+Nb`B'895mBzZ&)h1(>mJyZUK?qjpN]rlW)euC^m@AOt^3jyE>qC(Tse''":
            output = output + "O"
        if data[s1:e1] == "0/8 GoNUH+3Fp~!R9?:`HEu?:UWAzD>E?UchJ.Z/IxmV(#z)*os'eg!x!$IxXW:X":
            output = output + "P"
        if data[s1:e1] == "XN'Nj@ZC$kF'd.-pa-k8Sv8oDH4C6aWEZSz#~28Fd_Di0LDWzViXiz%0@rcNX2@-":
            output = output + "Q"
        if data[s1:e1] == "7-E-_Wv4>T<yXQjGN}Qq(Y&nsm~'sa' _hwn[KVY0lH0RD}vY<yKp4W}fi~3XoQ6":
            output = output + "R"
        if data[s1:e1] == "AY$ti)m]uQ,]kLA>9'6v'zFfA`(RFw*RPGW0v0=LB3p(6?JNoSJj{GM7S`f-a?7>":
            output = output + "S"
        if data[s1:e1] == "^?})aj}rejlrqPf&-fkYfE{FHJOj>y_BFkJH(Pc'dr.4J[}f]B-!wtRvQY0,tvvd":
            output = output + "T"
        if data[s1:e1] == "C@_TkNZ,~VDQe:LlXcv[.+5I4GWPj:q@8seSQISFE!&knG+%y9F_:70rvAZV'g.l":
            output = output + "U"
        if data[s1:e1] == "'h~,eDmY[e#A#=C#M{4f0 I2?Wot%CL~Z1>GzE19v1%`]S%sOI2?oklM][vwp-`A":
            output = output + "V"
        if data[s1:e1] == "tH(@R.)8,I*g`OVfWA%{2'4d>5^<<X.<=9>(tp'/&!NgGo}b(f,}amnE734Kt6&S":
            output = output + "W"
        if data[s1:e1] == "9oLdtPgZO{VB5 v]3vR}$f!'4(Oy}F32cO)LwP2T5(l4y6DRhM{SMs,VV{,kAAb~":
            output = output + "X"
        if data[s1:e1] == "(gmWyFx{xtR ya XK]az'O~Aj4tf]s1=Liabb76ff'27H'ol!d7Q-p_o,eu']}:~":
            output = output + "Y"
        if data[s1:e1] == "!YHEMTj#{^stna1sq-K)*?vw@n~^K- {hGlifF*#1qF.yAgWDeQ$~Hw{,Qq>w$3g":
            output = output + "Z"
        if data[s1:e1] == "Oc kt7^'Xje3)AD`S{_1Q@W#fW<i11=0-p2B=G&RAs.>)i-pVc0vJK2 69B5A{y6":
            output = output + "1"
        if data[s1:e1] == "Sq~D1]hzjQj: {Oo.8AhilY1`>N,t9p.t],2jF'[Ys]W~L E-=*i ,o9aX4Jn?s.":
            output = output + "2"
        if data[s1:e1] == "rX=nLSCI)5cCXIxh?Y[)3LK)}C!7gr>8.d-YtBq-KY5RviOpd`*L3Wi+t:>pJeW$":
            output = output + "3"
        if data[s1:e1] == "l#.MUz3dL>T!!JQE'T`poHtzPYj_VnFj%fWZps+R[P HXWF}k->HWMAM2pbQa6kZ":
            output = output + "4"
        if data[s1:e1] == "c0%QF[j,`~{+3A q<e:N>PSa?k}@[xu4zzed yr_&Z/W]f#?:OM*{zQJn'G=c6KJ":
            output = output + "5"
        if data[s1:e1] == "fGhSEJz5irQl#X<dOU^d/o/fBE5=<.6.[{v@`ue3&9.J^6wce:x4g$4k1K4E0NEq":
            output = output + "6"
        if data[s1:e1] == "xjpH,iDbI8T!iC<^g'ttfe'ELyTq$}K#m00ggY6%}H!no_{rxh8'6x2{_X*/P!vj":
            output = output + "7"
        if data[s1:e1] == "rLi_V&LVJ&W[-2'M$b083D_c***zqDhPJaprqg'#wbhwImj7A3Hv5<]sq1n+%5fM":
            output = output + "8"
        if data[s1:e1] == "*e*pU*HTZg%18q8++RYgl3tt'ZSQ3%*8IU%3*QR6,Z,R.Qb}S,BO^f4!Q-^L77/ ":
            output = output + "9"
        if data[s1:e1] == "E/@OucGK:C'Z@$'@L(=T9Q6+qe(&= z:i/{7>$Hor=n`bi}!~wa{Y^=0.6u'/MZ1":
            output = output + "0"
        if data[s1:e1] == "[$U=,wYh)PH[6:_/FpPA9dYl$OR}i&^R'e!u'Vcjd8s3Zi/v>Z1?`:F$6rmb&u6g":
            output = output + "`"
        if data[s1:e1] == "21*,(Ctp%,h7,Lud--/=}5vEqYL:TuPxJkjM{0({9PPd@6E:h]]9'V-n,@D+~7iO":
            output = output + "!"
        if data[s1:e1] == "+$CJ#klTMd7-P!n#mZvu5_:j}os^$,9XnP(G=&?'YgN$k['!khb92N'1'P0s4`nu":
            output = output + "'"
        if data[s1:e1] == "n`r@R<m4Ayyv6Urbyw@AY[]+lj6=okhUs3 IAeF0u3S>0nR'FJEn*8'=v-0m]{69":
            output = output + "$"
        if data[s1:e1] == "8`mDdxzhk<.+dDLU9dAhrZ',x3U_xJ%Nd=MVSaSk!f#.oQ/fmEbLDurZ@2WhDJUF":
            output = output + "%"
        if data[s1:e1] == "8QCFR0CZ!Q wtryL?YO=ff^L&=qKKJHu uVO=*@ZT{*oUfesO&`GR+r'bZl4RP!T":
            output = output + "^"
        if data[s1:e1] == "w@sGsU1p$`PZ Oe&LV6b5-hY,oY?D[l-yta*syNa'xl uG'cGz#6'.JO?J aE!68":
            output = output + "&"
        if data[s1:e1] == "<<$p^*PlJnPV2MLm*LL=}Ts1n$o/m3RZoN4D9B[yH8mMa&4.mo)qpn{O_cWrRfqZ":
            output = output + "*"
        if data[s1:e1] == "X_^_/IUy9V)#n3u z:(+? f>sT3vT]0%`!XmGG7=!o%&^J0G)NH9<9FkaAsU<z#C":
            output = output + "("
        if data[s1:e1] == "/Nrcqc3U~/xueIn/Ux@gGI)Oiq[>27 ~#vQug^KJECV$41IR%ZNdU{]]&W*QKJ$b":
            output = output + ")"
        if data[s1:e1] == "(yJeNS@(7bZW(JR=YK]kI1UX(_j&7YD2$b<.&#/I^W1v<1>(809fN<*Qi%utV>[ ":
            output = output + "_"
        if data[s1:e1] == "wBSr)NU-e=U9)LcpcO}3)rRN)Lh'nV`d3*r0Q*C/x%@%WCI~$#:7V8g!n89CR+)j":
            output = output + "+"
        if data[s1:e1] == "Og6sE+'b>xDksDOi^GXz<sXU8R]gI#A_<S 4BJ+#G+qYS'RzE2SLq*~LHUk_^pr+":
            output = output + "-"
        if data[s1:e1] == "%yIa>N7}@2gwO#GRo.q$x$4o>Jq]<VP(#v'Fb.u?^8la[nfX>SXi(nQSFt<ZUPK`":
            output = output + "="
        if data[s1:e1] == "<'kby+CAhd{[#p4&'VqN*VBt[pc1JDa'l?r6_-b]>'ivD: capJQ:2HA:c:}xoRI":
            output = output + "{"
        if data[s1:e1] == "TzYW2yzVk?bf5h@-y>?hlqC8OiP4l))_0~C33u'Kp':6SeV<!cw?#1(SxL:4O29J":
            output = output + "["
        if data[s1:e1] == "BH3BtejC$e7/%udzI`+$lTEpu.Lk4[,gARla@dE(TkO+AT)_Ca?ctzCO0JER,Fy*":
            output = output + "]"
        if data[s1:e1] == "rw%8'9R'L0ib*n(a2}~.b>!S' dT1RP)!d/K{'HTF@CsWQu2*XNS`.~/3kCTBiQ7":
            output = output + "}"
        if data[s1:e1] == "[j`M}[C=t!(8un9lvMzi`#Eb)wvjT:^%OM,6Y(_HmAt8<EVMht92hJ6,)?cgmt8g":
            output = output + ":"
        if data[s1:e1] == "}Bi>n$HHtcubM?ifwRU@OPDne'ao8{'p.15rk%U<9_9o%NaEQq7Mg'7.&qtw/)p(":
            output = output + "'"
        if data[s1:e1] == "tK>{YwXv!UCTpFrZa$ LHGQ-JZAa4<-=)P,#0[&/J?t=dp'f:$`$D^Qim]Iwf#OH":
            output = output + "@"
        if data[s1:e1] == "!8:S-jQUW^9ox5&Us&@S 6[NI@wX^'vm%3/+Ko~evD$_Whp[x+BP[fdMk,>xamfq":
            output = output + "#"
        if data[s1:e1] == "fFPs5sFc2vQVyqK+=j8245`9cU!CXB3BfIiBi^B,Y?utcX.tcM8.}@`)* R Nk9I":
            output = output + "~"
        if data[s1:e1] == "[S1On%<iY}g6B^v#y<:>zw!nap]xiC+:>AkN^q<[$FfQwC+/R`Qpmh(YINt#H+wQ":
            output = output + "/"
        if data[s1:e1] == "ynm{)FHaN<'o`*UIt:z-tB?cF!0g'j_j8/.e!5''zND:B#w]&)+?BU'E_(-{q2s4":
            output = output + "?"
        if data[s1:e1] == "#1R,4wJ9rZ8737s6LXG]a5HhqMHf1,Vkh5oxX3q?K`lu(1DXjQ]g[lez'sUuobYh":
            output = output + "."
        if data[s1:e1] == ",Lei70Ph^iwKZZos)@j/@]F-%dDcLHN!`K:mProiB>Ca8VRZh}Z42YV<bnm$(*&Y":
            output = output + ">"
        if data[s1:e1] == "1/76rp7y sRY,Xn_TK4+nn3W%-h_gnpx/dE9B]_mC0A$DyzfF>7Zx(1cVx@-z9uB":
            output = output + ","
        if data[s1:e1] == "H0kj@VGF,V~'3 L[UXpbMl5rSAPN1uuwXe+Uy6${,6W#&[ME&wL,G>+0ueLwPtzN":
            output = output + "<"
        if data[s1:e1] == ">/2+y.g6bgWC.?r2[.Fu^Xd*e[!%'z+t_9>R}%`z/Y4Hx2Lr/rsq<6EMI/iqBm$w":
            output = output + " "
        s1 = s1 + 64
        e1 = e1 + 64
        c1 = c1 + 64
print(output)