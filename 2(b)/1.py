import cv2
import numpy as np

cameramanimg = cv2.imread("../cameraman.tif")





grayImage = cv2.cvtColor(cameramanimg, cv2.COLOR_BGR2GRAY) 
row = grayImage.shape[0]
col = grayImage.shape[1]

a = 256		#min
b = 0		#max

for i in range(row):
	for j in range(col):
		if a > grayImage[i][j]:
			a = grayImage[i][j]
		if b < grayImage[i][j]:
			b = grayImage[i][j]
# arr = np.array([0,0,0,0,0,0,0,0,0,0,0])
# for i in range(row):
# 	for j in range(col):
# 		currentPixelValue = grayImage[i][j] *10 // 255
# 		arr[currentPixelValue] += 1

newimage = np.ndarray((row,col,1),np.uint8)


#  using formula   s = (r-c)*(b-a)/(d-a) + a

c = 0
d = 2 - 1

for i in range(row):
	for j in range(col):
		newimage[i][j] = (grayImage[i][j]-c)*(b-a)//(d-c) + a

cv2.imshow("Original image",cameramanimg)
cv2.imshow("Rotated",grayImage)
cv2.imshow("newimage",newimage)
print(newimage)
cv2.waitKey(0)