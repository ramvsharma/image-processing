import cv2
import numpy as np

img = cv2.imread("cameraman.png")
print(img.shape)

C11 = img[:128,:128,:]
cv2.imshow("C11",C11)

C12 = img[128:,:128,:]
cv2.imshow("C12",C12)

C21 = img[:128,128:,:]
cv2.imshow("C21",C21)

C22 = img[128:,128:,:]
cv2.imshow("C22",C22)

cv2.waitKey(0)