#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jamie
#
# Created:     29/07/2014
# Copyright:   (c) Jamie 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
data3 = raw_input("please enter data")
key1 = input("key")
s3 = 0
e3 = 3
c3 = 0
output3 = ""
length = len(data3)
while c3 < length:
    temp = int(data3[s3:e3])
    temp1 = temp * key1
    temp3 = str(temp1)
    s3 = s3 + 3
    e3 = e3 + 3
    c3 = c3 + 3
    length33 = len(temp3)
    if length33 == 0:
        temp3 = "0000000000000000000"
    elif length33 == 1:
        temp3 = "000000000000000000" + temp3
    elif length33 == 2:
        temp3 = "00000000000000000" + temp3
    elif length33 == 3:
        temp3 = "0000000000000000" + temp3
    elif length33 == 4:
        temp3 = "000000000000000" + temp3
    elif length33 == 5:
        temp3 = "00000000000000" + temp3
    elif length33 == 6:
        temp3 = "0000000000000" + temp3
    elif length33 == 7:
        temp3 = "000000000000" + temp3
    elif length33 == 8:
        temp3 = "00000000000" + temp3
    elif length33 == 9:
        temp3 = "0000000000" + temp3
    elif length33 == 10:
        temp3 = "000000000" + temp3
    elif length33 == 11:
        temp3 = "00000000" + temp3
    elif length33 == 12:
        temp3 = "0000000" + temp3
    elif length33 == 13:
        temp3 = "000000" + temp3
    elif length33 == 14:
        temp3 = "00000" + temp3
    elif length33 == 15:
        temp3 = "0000" + temp3
    elif length33 == 16:
        temp3 = "000" + temp3
    elif length33 == 17:
        temp3 = "00" + temp3
    elif length33 == 18:
        temp3 = "0" + temp3
    output3 = output3 + str(temp3)
print(output3)