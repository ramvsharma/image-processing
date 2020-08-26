import cv2
import numpy as np

img = cv2.imread("cameraman.png")

newImage = np.ones((256,256,3))

x = img[:128,:128,:]

cv2.imshow("Ram",x)
cv2.waitKey(0)