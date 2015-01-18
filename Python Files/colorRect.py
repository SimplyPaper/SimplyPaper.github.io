#from PIL import Image
#import itertools
import numpy as np
import cv2


def colorInsideR (imageName, coordinateLeft, coordinateRight, coordinateTop, coordinateB):
    #im = Image.open(imageName)
    #pix = im.load()
    
    img = cv2.imread(imageName)
    
    RArr = []
    GArr = []
    BArr = []
    for x in range(coordinateTop, coordinateB):
        for y in range(coordinateLeft, coordinateRight):
            RArr.append(img[x][y][0])
            GArr.append(img[x][y][1])
            BArr.append(img[x][y][2])
            
    #CombinedArry = [RArr, GArr, BArr]  
    
    Rfinal = []
    Bfinal = []
    Gfinal = []
    
    for i in range(len(RArr)):
        if RArr[i] < 245:
            Rfinal.append(RArr[i])
    for i in range(len(GArr)):
        if GArr[i] < 245:
            Gfinal.append(GArr[i])
    for i in range(len(BArr)):
        if BArr[i] < 245:
            Bfinal.append(BArr[i])
    
    '''
    for i,j,k in itertools.izip(RArr[:], GArr[:], BArr[:]):
        if (i > 230 | j > 230 | k > 230):
            print i
            RArr.remove(i)
            GArr.remove(j)
            BArr.remove(k)
    '''
    
   
    Red = reduce(lambda x, y: x + y,Rfinal) / len(Rfinal)
    Green = reduce(lambda x, y: x + y,Gfinal) / len(Gfinal)
    Blue = reduce(lambda x, y: x + y,Bfinal) / len(Bfinal)
    
    ColorArr = [Red, Green, Blue]
    return ColorArr

def getRGB(imageName, coordinateLeft, coordinateRight, coordinateTop, coordinateB):
    RGB = colorInsideR('2rect.jpg', coordinateLeft, coordinateRight, coordinateTop, coordinateB)
    return RGB