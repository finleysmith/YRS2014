#This is the old version of the image to text converter. It only works if it converts images that were made
#by the old text to imge converter. I would highly reccomend using the new version which uses ascii.

#Image made by old text to image converter  ->   text

import Image

CHARACTERS ={1 : 'a',  2 : 'b',  3 : 'c',
             4 : 'd',  5 : 'e',  6 : 'f',
             7 : 'g',  8 : 'h',  9 : 'i',
             10: 'j', 11 : 'k', 12 : 'l',
             13: 'm', 14 : 'n', 15 : 'o',
             16: 'p', 17 : 'q', 18 : 'r',
             19: 's', 20 : 't', 21 : 'u',
             22: 'v', 23 : 'w', 24 : 'x',
             25: 'y', 26 : 'z',

             27: '0', 28 : '1', 29 : '2',
             30: '3', 31 : '4', 32 : '5',
             33: '6', 34 : '7', 35 : '8',
             36: '9', 0 : ' '
             }

def main():
    output = ''
    RGBvals = []
    input = raw_input("Enter image URL/link here \n (include.filetype) \n i.e D:\images\image1.png: ")
    try:
        img = Image.open(input)

        for x in xrange(img.size[0]):
             for y in xrange(img.size[1]):
                 r,g,b = img.getpixel((x,y))
                 RGBvals.append(r)
                 RGBvals.append(g)
                 RGBvals.append(b)
        for i in RGBvals:
            if i in CHARACTERS:
                output = output + CHARACTERS[i]
            else:
                output = output + ' '
        print output
    except:
        print('Failed to open image.')

if __name__ == '__main__':
    main()