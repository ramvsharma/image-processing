import cv2
import numpy as np

img = cv2.imread("cameraman.png")

newImage = np.zeros((260,260,3))

C11 = img[:128,:128,:]
cv2.imshow("C11",C11)

C12 = img[128:,:128,:]
cv2.imshow("C12",C12)

C21 = img[:128,128:,:]
cv2.imshow("C21",C21)

C22 = img[128:,128:,:]
cv2.imshow("C22",C22)


newImage[:128,:128,:] = C11/255;
newImage[130:258,:128,:] = C12/255;
newImage[:128,130:258,:] = C21/255;
newImage[130:258,130:258,:] = C22/255;


cv2.imshow("Combined",newImage)

cv2.waitKey(0)