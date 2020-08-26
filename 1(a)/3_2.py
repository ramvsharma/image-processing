import cv2
import numpy as np


circle = np.zeros((256,256))

radius = 50
c_x = 128
c_y = 128
for i in range(256):
	for j in range(256):
		if (i-c_x)*(i-c_x) + (j-c_y)*(j-c_y)   <= radius*radius:
			circle[i][j] = 255

cv2.imshow("Circle",circle)
cv2.waitKey(0)