#This converter recieves an input string from the user, and converts each character first to ascii, then to
#binary. Then it prints the output string.

#Text   ->  Binary

def main():
    output = ''             #The output string
    #message = raw_input('Enter message to convert to binary : ')         #Enter text to convert
    message = sys.argv[0]
    mlength = len(message)                  #Save the length of the message.
    for i in message:                       #For each character in message
        try:
            ordi = ord(i)                       #convert to ascii integer
            bini = (bin(ordi)[2:].zfill(8))     #convert integer to binary string
            output = output + bini + ' '        #add that to output
        except:
            print('Failed to convert.')         #If process fails, tell the user.
    print (output)                          #print output

if __name__ == '__main__':
    main()