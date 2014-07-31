#This converter will recognise whether the string entered is Morse (ony .s -s and spaces), or text.
#If it is text, it will convert to Morse. If it is Morse, it will convert to text.
#Note there are no special characters in Morse, so they will be replaced with spaces in the conversion.

#Text -> Morse  &   Morse -> Text
import sys
MORSE2 = ['.','-',' ']
MORSE ={'a': '.-',     'b': '-...',   'c': '-.-.',
        'd': '-..',    'e': '.',      'f': '..-.',
        'g': '--.',    'h': '....',   'i': '..',
        'j': '.---',   'k': '-.-',    'l': '.-..',
        'm': '--',     'n': '-.',     'o': '---',
        'p': '.--.',   'q': '--.-',   'r': '.-.',
     	's': '...',    't': '-',      'u': '..-',
        'v': '...-',   'w': '.--',    'x': '-..-',
        'y': '-.--',   'z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.',
        }

MORSE3={'.-' : 'a',    '-...' : 'b',  '-.-.' : 'c',
        '-..' : 'd',   '.' : 'e',     '..-.' : 'f',
        '--.' : 'g',   '....' : 'h',  '..' : 'i',
        '.---' : 'j',  '-.-' : 'k',   '.-..' : 'l',
        '--' : 'm',    '-.' : 'n',    '---' : 'o',
        '.--.' : 'p',  '--.-' : 'q',  '.-.' : 'r',
        '...' : 's',   '-' : 't',     '..-' : 'u',
        '...-' : 'v',  '.--' : 'w',   '-..-' : 'x',
        '-.--' : 'y',  '--..' : 'z',

        '-----' : '0', '.----' : '1', '..---' : '2',
        '...--' : '3', '....-' : '4', '.....' : '5',
        '-....' : '6', '--...' : '7', '---..' : '8',
        '----.' : '9'
        }

def main():
    binary = True                  #Record past letter.
    output = ''                     #The output string.
    morse = ''
    message = sys.argv[1]
    
    message = message.lower() + ' '
    #message = raw_input('Enter message: ').lower() + ' '        #Message to lower case.
    for i in message:                                   #For each character in message:
        if i != '.' and i != '-' and i != ' ':                #If not binary, run text to binary.
            binary = False
    if binary == True:                          #If binary,
        message2 = message.split(" ")           #Look for spaces and add the characters between the spaces to a list.
        #print (message2)           #DEBUG
        for i in message2:                      #For each character:
            i = i[1:]                            #Remove the first character (u)
        for i in message2:                      #For each character:
            if i in MORSE3:                      #If the character string is recognised:
                output = output + MORSE3[i]      #Add it's character value to the output string
            else:
                output = output + ' '           #If it's not recognised, add a space.
    else:
        for i in message:               #If it's not binary, then it must be characters, so for each character:
            if i in MORSE:              #If it's recognised, add it's value to the output string
                output = output + MORSE[i] + ' '
            else:
                output = output + ' '       #Otherwise add a space
    print(output)                   #Print the output string.

if __name__ == '__main__':
    main()