import cv2
import math
import numpy as np

cameramanimg = cv2.imread("../cameraman.tif")

row = cameramanimg.shape[0]
col = cameramanimg.shape[1]

newImage1 = np.ndarray((col,row,3))
newImage2 = np.ndarray((col,row,3))
newImage3 = np.ndarray((col,row,3))

for i in range(row):
	for j in range(col):
		pixel = cameramanimg[i][j][0]/255
		newImage1[i][j] = 1*math.log(1 + pixel)
		newImage2[i][j] = 2*math.log(1 + pixel)
		newImage3[i][j] = 3*math.log(1 + pixel)

cv2.imshow("Original image",cameramanimg)
cv2.imshow("c=1 image",newImage1)
cv2.imshow("c=2 image",newImage2)
cv2.imshow("c=3 image",newImage3)
cv2.waitKey(0)