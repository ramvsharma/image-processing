import cv2
import numpy as np

a = np.ones((64,64))
for i in range(64):
	j =0
	while j<64:
		a[i][j] = 0
		j+= 2

for j in range(32,64):
	i=0
	while i<32:
		a[i][j] = 0
		a[i+32][j-32] = 0
		i += 2

cv2.imshow("C",a)
cv2.waitKey(0)