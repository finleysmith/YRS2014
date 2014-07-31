#This converter will recieve an image URL or link, then record the RGB values of each pixel, and convert these
#to characters using ascii.

#Image -> Text

import Image        #Import the image library
def main():
    output = ''         #The output string, starts empty.
    RGBvals = []        #A list that will contain lists of RGB values.
    input1 = raw_input("Enter image URL/link here \n (include.filetype) \n i.e D:\images\image1.png: ")
    try:
        img = Image.open(input1)        #Try to open the image

        for x in xrange(img.size[0]):       #For each pixel:
             for y in xrange(img.size[1]):
                 r,g,b = img.getpixel((x,y))    #Get the RGB values as integers
                 RGBvals.append(r)              #And save them to RGBvals
                 RGBvals.append(g)
                 RGBvals.append(b)
             #print(RGBvals) #DEBUG
        for i in RGBvals:               #For each character in RGBvals:
            output = output + chr(i)        #Convert the integers to characters using ascii and add to output.
        print output                    #Print the output.
    except:
        print('Failed to open image.')  #If it fails, tell the user it failed.
    
if __name__ == '__main__':
    main()