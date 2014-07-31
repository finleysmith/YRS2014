#This converter recieves an input string from the user (just 1s, 0s and spaces), and converts each character 
#to alphanumeric characters. Then it prints the output string.

#Binary -> Text

import binascii                             #import the binary ascii module.
def main():
    output = ''                             #the output string
    last = ''                               #record the last character.
    #n = (raw_input('Enter binary for conversion here: ')) + ' ' #input binary
    n = sys.argv[0] + ' '
    for i in n:                             #for each character in binary:
        if i == '0' or i == '1':                #If it's a 1 or a 0:
            last = last + i                         #Add it to last.
        else:                                   #Otherwise:
            if last != '':                          #If last is not empty:
                ni = 0
                ni = int(last,2)                        #Save last as an int.
                last = ''                               #Clear last.
                output = output + binascii.unhexlify('%x' % ni) #Convert the binary to hexidecimal to characters, then add to string.
            else:                                   #If last is empty:
                output = output + ' '                   #Add an empty space to output.
    print(output)                           #Print output.

if __name__ == '__main__':
    main()