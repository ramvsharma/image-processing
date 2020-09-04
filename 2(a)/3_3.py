import cv2
import math
import numpy as np

cameramanimg = cv2.imread("../cameraman.tif")
cameramanimg = cv2.cvtColor(cameramanimg,cv2.COLOR_BGR2GRAY)	#convert to gray 

row = cameramanimg.shape[0]
col = cameramanimg.shape[1]

newImage1 = np.ndarray((row,col))
newImage2 = np.ndarray((row,col))
newImage3 = np.ndarray((row,col))

for i in range(row):
	for j in range(col):
		pixel = cameramanimg[i][j]/255
		newImage1[i][j] = 1*math.log(1 + pixel)
		newImage2[i][j] = 2*math.log(1 + pixel)
		newImage3[i][j] = 3*math.log(1 + pixel)

cv2.imshow("Original image",cameramanimg)
cv2.imshow("c=1 image",newImage1)
cv2.imshow("c=2 image",newImage2)
cv2.imshow("c=3 image",newImage3)
cv2.waitKey(0)