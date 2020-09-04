import cv2
import numpy as np
import math


cameramanimg = cv2.imread("../cameraman.tif")
cameramanimg = cv2.cvtColor(cameramanimg,cv2.COLOR_BGR2GRAY)	#convert to gray 

row = cameramanimg.shape[0]
col = cameramanimg.shape[1]

cv2.imshow("Original",cameramanimg)

bit = 1

newImage = np.ndarray((row,col),dtype=np.uint8)

for k in range(8):
	for i in range(row):
		for j in range(col):
			if (bit & cameramanimg[i][j]):
				newImage[i][j] = 255
			else:
				newImage[i][j] = 0	
	if k==0:
		cv2.imshow("bit0",newImage)
	elif k==1:
		cv2.imshow("bit1",newImage)
	elif k==2:
		cv2.imshow("bit2",newImage)
	elif k==3:
		cv2.imshow("bit3",newImage)
	elif k==4:
		cv2.imshow("bit4",newImage)
	elif k==5:
		cv2.imshow("bit5",newImage)
	elif k==6:
		cv2.imshow("bit6",newImage)
	else:
		cv2.imshow("bit7",newImage)

	bit *= 2



cv2.waitKey(0)