#This converter will recieve a string, convert the characters into ascii integers, take these in groups of 3
#and assign these to a list, then use these values as RGB values to construct an image. It will then ask for
#where to save the image and what file type to save it as. Converts text to images.

#Text -> Image

import Image
def main():
    output = []             #The output list
    got3 = []               #A check to see if there are any more characters after assigning all RGB values
    RGBvals = []            #A list containing lists containing RGB values.
    message = raw_input('Enter message: ') #Enter text.
    mlength = len(message)                  #Save the length of the message.
    last = []                               #Part of the got3 check.

    for i in message:           #For each character in message
        output.append(ord(i))       #Add its ascii value to output string.

    for j in output:            #For each character in output:
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
    try:                                        #Try to save the image.
        img.save(image_save,image_type)         #Save the image.
    except:
        print('Failed to save image.')          #Otherwise, tell the user it failed.

if __name__ == '__main__':
    main()