import cv2
import random
import numpy as np


img = np.zeros((512,512))

for i in range(512):
	for j in range(512):
		img[i][j] = random.randint(0,256)

print(img)

cv2.imshow("a",img)
cv2.waitKey(0)