import cv2
import numpy as np

a = np.ones((16,16))
for i in range(16):
	j =0
	while j<16:
		a[i][j] = 0
		a[j][i] = 0
		j+= 2

cv2.imshow("B",a)
cv2.waitKey(0)