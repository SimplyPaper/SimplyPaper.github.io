# -*- coding: utf-8 -*-
"""
Canny Edge Detection
"""


#Detect Edges
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('sample_image.png',0)
edges = cv2.Canny(img,100,200)


plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()

'''
actual_edgesx = []
actual_edgesy = []
for index1 in range(len(edges)):
    new = []
    for index2 in range(len(edges[0])):
        if edges[index1][index2] > 0:
            actual_edgesx.append(index1)
            actual_edgesy.append(index2)
            
actual_edges = np.array([actual_edgesx, actual_edgesy])

width = 0
lenth = 0

for index in range(len(actual_edges[0])-1):
    if actual_edges[0][index] == actual_edges[0][index+1] && actual_edges[0][index] > 10:
        lenth = lenth + 1
'''    

'''
    for index1 in range(len(actual_edges)):
        if actual_edges[index1] = actual_edges[index+1]:
            countUpX = countUpX + 1
        
'''
    
            
        

#Detect Corners
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#corners = cv2.goodFeaturesToTrack(gray,4,0.01,10)
#corners = np.int0(corners)

#for i in corners:
#    x,y = i.ravel()
#    cv2.circle(img,(x,y),3,255,-1)

#plt.imshow(img),plt.show()