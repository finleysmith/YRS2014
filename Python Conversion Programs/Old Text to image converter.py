#This is the old text to image converter. I would highly reccomend using the new version instead as it uses
#ascii, meaning it will could with similar programs and has all 256 characters entered. This version doesn't.

#Text   ->  Image

import Image

CHARACTERS ={'a': 1,    'b': 2,   'c': 3,
             'd': 4,    'e': 5,   'f': 6,
             'g': 7,    'h': 8,   'i': 9,
             'j': 10,   'k': 11,  'l': 12,
             'm': 13,   'n': 14,  'o': 15,
             'p': 16,   'q': 17,  'r': 18,
             's': 19,   't': 20,  'u': 21,
             'v': 22,   'w': 23,  'x': 24,
             'y': 25,   'z': 26,

             '0': 27,  '1': 28,  '2': 29,
             '3': 30,  '4': 31,  '5': 32,
             '6': 33,  '7': 34,  '8': 35,
             '9': 36,  ' ': 0,
             }

def main():
    output = []             #The output list
    got3 = []               #A check to see if there are any more characters after assigning all RGB values
    RGBvals = []            #A list containing lists containing RGB values.
    message = raw_input('Enter message: ').lower()          #Enter text & convert to lower case.
    mlength = len(message)                  #Save the length of the message.
    last = []                               #Part of the got3 check.

    for i in message:           #For each character in message
        if i in CHARACTERS:         #If recognised by CHARACRERS dictionary:
            output.append(CHARACTERS[i])        #Add value to output list.
        else:
            output.append(0)        #If character is not recognised, add a 0 (space)

    for j in output:            #For each character in output
        if len(got3) == 3:      #If the got3 list contains 3 items, add them to RGB values as a list.
            RGBvals.append([got3[0],got3[1],got3[2]])
            got3 = [j]
        else:                   #Otherwise add the character to got3.
            got3.append(j)

    if len(got3)!= 0:           #If the length of got 3 is not zero (so not all characters have been assigned to RGBvals):
        if len(got3) == 1:          #Add the value to RGBvals and add zeros if there are no other characters.
            last = [got3[0],0,0]
            RGBvals.append([last[0],last[1],last[2]])
        elif len(got3) == 2:
            last = [got3[0],got3[1],0]
            RGBvals.append([last[0],last[1],last[2]])
        elif len(got3) == 3:
            last = [got3[0],got3[1],got3[2]]
            RGBvals.append([last[0],last[1],last[2]])
    #print output        #DEBUG
    #print got3          #DEBUG
    #print RGBvals       #DEBUG
    #print len(RGBvals)  #DEBUG
    xlen = (len(RGBvals)%600)       #The width of the image is the number of pixels modulo by 600 (600 is max image length)
    ylen = 1 + (len(RGBvals)/600)   #The height of the image is the number of pixels divide by 500, +1.
    #print (xlen, ylen) #DEBUG
    img = Image.new("RGB",(xlen,ylen),(0,0,0))      #Create a new image of size xlen, ylen, white.
    for x in xrange(xlen):                          #For each pixel:
        for y in xrange(ylen):
            img.putpixel((x,y),(RGBvals[x][0],RGBvals[x][1],RGBvals[x][2])) #Assign the colour to the corrseponding list of RGB values from RGBvals.
    image_save = raw_input("Enter the URL where you would like to save the image \n i.e: C:\images\imagename.png")
    image_type = raw_input('Enter the file type you want it saved as /n i.e PNG, etc.')
    try:
        img.save(image_save,image_type)         #Save the image to my memory stick.
    except:
        print('Failed to save image.')

    #img2 = Image.open("D:\imagetest1.png") #DEBUG, Just so it prints the RGB values for each pixel.
    #for x in xrange(img.size[0]):
    #    for y in xrange(img.size[1]):
    #        r,g,b = img.getpixel((x,y))
    #        print (r,g,b)

    #img.save("D:\image2.png","PNG")

if __name__ == '__main__':
    main()