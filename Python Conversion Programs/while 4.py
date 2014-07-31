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
length = len(data4) / 2
length3 = len(data4)
if length >= 1000:
    length = 999
elif len(str(length)) == 1:
    length = "00" + str(length)
elif len(str(length)) == 2:
    length = "0" + str(length)
length = str(length)
length2 = int(length)
output4 = length + data4[0:length2] + key2 + data4[length2:length3]
print(output4)