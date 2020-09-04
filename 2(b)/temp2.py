import cv2
import numpy as np
import math


cameramanimg = cv2.imread("../cameraman.tif")
cameramanimg = cv2.cvtColor(cameramanimg,cv2.COLOR_BGR2GRAY)	#convert to gray 

row = cameramanimg.shape[0]
col = cameramanimg.shape[1]

bit = 4

newImage = np.ndarray((row,col),dtype=np.uint8)

for i in range(row):
	for j in range(col):
		if (bit & cameramanimg[i][j]):
			newImage[i][j] = 255
		else:
			newImage[i][j] = 0	

cv2.imshow("bit7",newImage)

cv2.waitKey(0)