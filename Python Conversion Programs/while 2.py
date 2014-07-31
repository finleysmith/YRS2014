data2 = raw_input("Please enter data to be encrypted")
s2 = 0
e2 = 1
c2 = 0
output2 = ""
length2 = len(data2)
while c2 < length2:
    temp1 = data2[s2:e2]
    temp2 = ord(temp1)
    temp3 = str(temp2)
    lengtht = len(temp3)
    if lengtht == 1:
        temp3 = "00" + temp3
    elif lengtht == 2:
        temp3 = "0" + temp3
    output2 = output2 + temp3
    s2 = s2 + 1
    e2 = e2 + 1
    c2 = c2 + 1
print(output2)