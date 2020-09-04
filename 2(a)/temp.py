import cv2
import numpy as np

cameramanimg = cv2.imread("../cameraman.tif")

row = cameramanimg.shape[0]
col = cameramanimg.shape[1]

newImage = np.ndarray((col,row,3))
cv2.imshow("Original image",cameramanimg)
powValue = 0.1
while powValue<=2.0:
	for i in range(row):
		for j in range(col):
			newImage[i][j] = (cameramanimg[i][j]/255)**(1/float(powValue))
	cv2.imshow("abc"+str(powValue),newImage)
	powValue += 0.1
cv2.waitKey(0)