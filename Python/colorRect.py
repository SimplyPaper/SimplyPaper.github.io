from PIL import Image
import itertools


def colorInsideR (imageName, coordinateTopLeft, coordinateBLeft, coordinateTopRight):
    im = Image.open(imageName)
    pix = im.load()
    RArr = []
    GArr = []
    BArr = []
    for x in range(coordinateTopLeft, coordinateBLeft):
        for y in range(coordinateTopLeft, coordinateTopRight):
            RArr.append(pix[y,x][0])
            GArr.append(pix[y,x][1])
            BArr.append(pix[y,x][2])
            
    CombinedArry = [RArr, GArr, BArr]

    for i,j,k in itertools.izip(RArr[:], GArr[:], BArr[:]):
        if (i > 245 & j > 245 & k > 245):
            RArr.remove(i)
            GArr.remove(j)
            BArr.remove(k)
        
   
    Red = reduce(lambda x, y: x + y,RArr) / len(RArr)
    Green = reduce(lambda x, y: x + y,GArr) / len(GArr)
    Blue = reduce(lambda x, y: x + y,BArr) / len(BArr)
    
    ColorArr = [Red, Green, Blue]
    return ColorArr
            

    