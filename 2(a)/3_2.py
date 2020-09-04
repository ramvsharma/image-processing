import cv2
import numpy as np

cameramanimg = cv2.imread("../cameraman.tif")
cameramanimg = cv2.cvtColor(cameramanimg,cv2.COLOR_BGR2GRAY)	#convert to gray 

row = cameramanimg.shape[0]
col = cameramanimg.shape[1]

newImage1 = np.ndarray((row,col), dtype=np.uint8)
newImage2 = np.ndarray((row,col), dtype=np.uint8)
newImage3 = np.ndarray((row,col), dtype=np.uint8)
newImage4 = np.ndarray((row,col), dtype=np.uint8)

for i in range(row):
	for j in range(col):
		newImage1[i][j] = (cameramanimg[i][j])**(1/float(0.8))
		newImage2[i][j] = (cameramanimg[i][j])**(1/float(0.9))
		newImage3[i][j] = (cameramanimg[i][j])**(1/float(1.1))
		newImage4[i][j] = (cameramanimg[i][j])**(1/float(1.2))

cv2.imshow("Original image",cameramanimg)
cv2.imshow("0.8 image",newImage1)
cv2.imshow("0.9 image",newImage2)
cv2.imshow("1.1 image",newImage3)
cv2.imshow("1.2 image",newImage4)
cv2.waitKey(0)