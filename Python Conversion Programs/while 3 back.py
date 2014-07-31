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
e3 = 19
c3 = 0
output3 = ""
length = len(data3)
while c3 < length:
    temp = data3[s3:e3]
    if temp[0:18] == "000000000000000000":
        temp = temp[18:19]
    elif temp[0:17] == "00000000000000000":
        temp = temp[17:19]
    elif temp[0:16] == "0000000000000000":
        temp = temp[16:19]
    elif temp[0:15] == "000000000000000":
        temp = temp[15:19]
    elif temp[0:14] == "00000000000000":
        temp = temp[14:19]
    elif temp[0:13] == "0000000000000":
        temp = temp[13:19]
    elif temp[0:12] == "000000000000":
        temp = temp[12:19]
    elif temp[0:11] == "00000000000":
        temp = temp[11:19]
    elif temp[0:10] == "0000000000":
        temp = temp[10:19]
    elif temp[0:9] == "000000000":
        temp = temp[9:19]
    elif temp[0:8] == "00000000":
        temp = temp[8:19]
    elif temp[0:7] == "0000000":
        temp = temp[7:19]
    elif temp[0:6] == "000000":
        temp = temp[6:19]
    elif temp[0:5] == "00000":
        temp = temp[5:19]
    elif temp[0:4] == "0000":
        temp = temp[4:19]
    elif temp[0:3] == "000":
        temp = temp[3:19]
    elif temp[0:2] == "00":
        temp = temp[2:19]
    elif temp[0:1] == "0":
        temp = temp[1:19]
    temp2 = int(temp) / key1
    s3 = s3 + 19
    e3 = e3 + 19
    c3 = c3 + 19
    temp2 = str(temp2)
    if len(temp2) == 1:
        temp2 = "00" + temp2
    if len(temp2) == 2:
        temp2 = "0" + temp2
    output3 = output3 + str(temp2)
print(output3)