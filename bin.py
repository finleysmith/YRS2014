import binascii
import sys
def main():
    binary = True                  #Record past letter.
    output = ''                     #The output string.
    last = ''
    count = 0
    #message = raw_input('Enter message: ')        #Input message
    message = sys.argv[1]
    for i in message:                                   #For each character in message:
        if i != '0' and i != '1' and i != ' ':                #If not binary, run text to binary.
            binary = False
    
    #for i in message:
    #    count = count + 1 
    #    if i == '!':
    #        #message[count] = ' '
    #        message = message.replace('!', '_')
            
    #for i in message:
    #    count++
    #    if i == '%' or i == '2' or i == '0':
    #        if len(last) == 3 and last == '%20':
    #            counti = count - 3
                
    
    
    
    if binary == True:                                  #If the string entered was binary:
        last = ''                                           #Variable to record last character.
        message = message  + ' '                            #Add a space to the end of message.
        #n = (raw_input('Enter binary for conversion here: ')) + ' ' 
        #n = sys.argv[0] + ' '
        for i in message:                             #For each character in message:
            if i == '0' or i == '1':                #If it's a 1 or a 0:
                last = last + i                         #Add it to last.
            else:                                   #Otherwise:
                if last != '':                          #If last is not empty:
                    mi = 0
                    mi = int(last,2)                        #Save last as an int.
                    last = ''                               #Clear last.
                    output = output + binascii.unhexlify('%x' % mi) #Convert the binary to hexidecimal to characters, then add to string.
                else:                                       #If last is empty:
                    output = output + ' '
    else:                                   #If message entered was text:
        mlength = len(message)                  #Save the length of the message.
        for i in message:                       #For each character in message:
            try:
                ordi = ord(i)                       #convert to ascii integer
                bini = (bin(ordi)[2:].zfill(8))     #convert integer to binary string
                output = output + bini + ' '        #add that to output
            except:
                print('Failed to convert.')
    print(output)
if __name__ == '__main__':
    main()