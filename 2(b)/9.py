import cv2
import math
import numpy as np

cameramanimg = cv2.imread("../cameraman.tif")
cameramanimg = cv2.cvtColor(cameramanimg,cv2.COLOR_BGR2GRAY)	#convert to gray 

row = cameramanimg.shape[0]
col = cameramanimg.shape[1]

newImage = np.ndarray((row,col))
newImage1 = np.ndarray((row,col))


for i in range(row):
	for j in range(col):
		newImage[i][j] = 1*(cameramanimg[i][j]/255)**0.2

for i in range(row):
	for j in range(col):
		newImage1[i][j] = 1*(cameramanimg[i][j]/255)**(1/0.2)

cv2.imshow("Original image",cameramanimg)
cv2.imshow("c=1 image",newImage)
cv2.imshow("c=2 image",newImage1)
cv2.waitKey(0)