import cv2
import numpy as np

cameramanimg = cv2.imread("../cameraman.tif")
cameramanimg = cv2.cvtColor(cameramanimg,cv2.COLOR_BGR2GRAY)	#convert to gray 

row = cameramanimg.shape[0]
col = cameramanimg.shape[1]

negativeImage = np.ndarray((row,col),dtype = np.uint8)

for i in range(row):
	for j in range(col):
		negativeImage[i][j] = 255 - cameramanimg[i][j]

cv2.imshow("Original image",cameramanimg)
cv2.imshow("Negative image",negativeImage)
cv2.waitKey(0)