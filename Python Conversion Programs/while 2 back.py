data2 = raw_input("Please enter data to be decrypted: ")
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
print(output2)