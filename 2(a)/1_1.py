import cv2
import numpy as np

cameramanimg = cv2.imread("../cameraman.tif")
cameramanimg = cv2.cvtColor(cameramanimg,cv2.COLOR_BGR2GRAY)	#convert to gray 

row = cameramanimg.shape[0]
col = cameramanimg.shape[1]

rotatedImage = np.ndarray((col,row),dtype=np.uint8)

for i in range(row):
	for j in range(col):
		rotatedImage[col-j-1][i] = cameramanimg[i][j]

cv2.imshow("Original image",cameramanimg)
cv2.imshow("Rotated image",rotatedImage)
cv2.waitKey(0)