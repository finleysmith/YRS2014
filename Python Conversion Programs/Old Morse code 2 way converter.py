#This is the old morse code converter that can convert entered text to Morse, or entered Morse to text. 
#However, the new version is much better at returning Morse to text as there are no spaces between the text.
#The only advantage that this version has is that it can sometimes convert both text and morse at the same time.
#Despite this, I would highly reccomend using the new version to convert between Morse and Text.

#Text -> Morse  &   Morse -> Text   &   Text+Morse -> Morse+Text.

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

        '.-' : 'a',    '-...' : 'b',  '-.-.' : 'c',
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
    past_lt = ''                    #Record past letter.
    output = ''                     #The output string.
    message = raw_input('Enter message: ').lower() + ' '        #Message to lower case.
    for i in message:                               #For each character in message:
        if i == '.' or i == '-':                #If . or - , add to past letter
            past_lt = past_lt + i
        elif i in MORSE:                        #If recognised, add character to output.
            output = output + MORSE[i] + ' '
            past_lt = ' '
        elif i == ' ' or i == '':               #If space or empty:
            if past_lt != '':                       #If past letter is not empty:
                if past_lt in MORSE:                    #If past letter is registered in MORSE
                    output = output + MORSE[past_lt] + ' ' #Add character, clear past letter
                    past_lt = ''
                else:
                    output = output + ' ' #Otherwise add an empty space to output.
                    past_lt = ' '
            else:
                output = output + ' ' #If special character add empty space
                past_lt = ''
        else:
            output = output + ' ' #Else add empty space.
            past_lt = ' '
        #print (past_lt)
    print (output)

if __name__ == '__main__':
    main()