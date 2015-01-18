import numpy as np
import cv2
from matplotlib import pyplot as plt
import heapq

img = cv2.imread('color.jpg')
#edges = cv2.Canny(img,100,200)
#plt.subplot(121),plt.imshow(edges,cmap = 'gray')
#plt.title('Edge Image'), plt.xticks([]), plt.yticks([])


#imgray = img
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.subplot(121),plt.imshow(imgray,cmap = 'gray')
plt.title('Grayscale Image'), plt.xticks([]), plt.yticks([])


#ret,thresh = cv2.threshold(imgray,230,255,cv2.THRESH_BINARY)
#th3 = cv2.adaptiveThreshold(imgray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,8)


# Otsu's thresholding after Gaussian filtering
imgray = cv2.adaptiveThreshold(imgray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,8)
blur = cv2.GaussianBlur(imgray,(5,5),0.5)
#plt.subplot(122),plt.imshow(blur,cmap = 'gray')
#plt.title('Blurred image'), plt.xticks([]), plt.yticks([])


ret3,th3 = cv2.threshold(blur,127, 255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

#corners = cv2.goodFeaturesToTrack(th3,8,0.03,50)
#corners = np.int0(corners)

#for i in corners:
#    x,y = i.ravel()
#    cv2.circle(th3,(x,y),20,255,-1)

#plt.imshow(th3),plt.show()


contours, hierarchy = cv2.findContours(th3,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(th3, contours, -1, (0,255,0), 3)
plt.subplot(122),plt.imshow(th3,cmap = 'gray')
plt.title('Contours'), plt.xticks([]), plt.yticks([])

areas = [cv2.contourArea(c) for c in contours]
res = heapq.nlargest(10, areas)

'''
approx_contours=[]
for cnt in contours:
    approx = cv2.approxPolyDP(cnt,0.125*cv2.arcLength(cnt,True),True)
    print len(approx)
    approx_contours.append(approx)
'''









