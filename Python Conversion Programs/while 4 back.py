#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jamie
#
# Created:     30/07/2014
# Copyright:   (c) Jamie 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
data4 = raw_input("please enter data")
key2 = raw_input("key")
num1 = data4[0:3]
num1 = int(num1)
length = len(data4)
data4 = data4[3:length]
data4b = data4[num1:(num1+16)]
data4 = data4[0:num1] + data4[(num1 + 16):length]
if data4b != key2:
    print("go fuck your self thief")
    data4 = "null"
    exit()
elif data4b == key2:
    print data4