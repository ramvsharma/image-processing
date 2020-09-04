import cv2
import random
import numpy as np


A = np.zeros((512,512))

for i in range(512):
	for j in range(512):
		A[i][j] = random.random()


cv2.imshow("B",A)
cv2.waitKey(0)