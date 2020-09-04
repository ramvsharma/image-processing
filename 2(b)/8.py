import cv2
import numpy as np
import math


cameramanimg = cv2.imread("../cameraman.tif")
cameramanimg = cv2.cvtColor(cameramanimg,cv2.COLOR_BGR2GRAY)	#convert to gray 

row = cameramanimg.shape[0]
col = cameramanimg.shape[1]

logTransformImage = np.ndarray((row,col))
inverseLogtransformImage = np.ndarray((row,col))
squareImage = np.ndarray((row,col))
squareRootImage = np.ndarray((row,col))
negativeImage = np.ndarray((row,col))

for i in range(row):
	for j in range(col):
		currentPixel = cameramanimg[i][j]/255
		logTransformImage[i][j] = math.log(1+ currentPixel)
		inverseLogtransformImage[i][j] = 1 - logTransformImage[i][j]
		squareImage[i][j] = currentPixel * currentPixel
		squareRootImage[i][j] = math.sqrt(currentPixel)
		negativeImage[i][j] = 1 - currentPixel



cv2.imshow("2",inverseLogtransformImage)
cv2.imshow("3",squareImage)
cv2.imshow("4",squareRootImage)
cv2.imshow("5",negativeImage)
cv2.waitKey(0)

