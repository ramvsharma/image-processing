import cv2
import numpy as np


radius = 50
c_x = 128
c_y = 128

cameramanimg = cv2.imread("cameraman.png")

for i in range(256):
	for j in range(256):
		if (i-c_x)*(i-c_x) + (j-c_y)*(j-c_y)   > radius*radius:
			cameramanimg[i][j] = 127
		


cv2.imshow("Circular part of cameraman image",cameramanimg)
cv2.waitKey(0)