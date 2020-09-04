import cv2
import numpy as np

cameramanimg = cv2.imread("../cameraman.tif")

row = cameramanimg.shape[0]
col = cameramanimg.shape[1]

newImage = np.ndarray((col,row,3))

for i in range(row):
	for j in range(col):
		newImage[col-j-1][i] = cameramanimg[i][j]/255

cv2.imshow("Original image",cameramanimg)
cv2.imshow("Rotated image",newImage)
cv2.waitKey(0)