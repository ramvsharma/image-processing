import cv2
import math
import numpy as np

cameramanimg = cv2.imread("../cameraman.tif")

row = cameramanimg.shape[0]
col = cameramanimg.shape[1]

newImage = np.ndarray((col,row,3))
newImage1 = np.ndarray((col,row,3))


for i in range(row):
	for j in range(col):
		newImage[i][j] = 1*(cameramanimg[i][j][0]/255)**0.1

for i in range(row):
	for j in range(col):
		newImage1[i][j] = 1*(cameramanimg[i][j][0]/255)**(1/2.5)

cv2.imshow("Original image",cameramanimg)
cv2.imshow("c=1 image",newImage)
cv2.imshow("c=2 image",newImage1)
cv2.waitKey(0)