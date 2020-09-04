import cv2
import numpy as np

cameramanimg = cv2.imread("../cameraman.tif")

grayImage = cv2.cvtColor(cameramanimg, cv2.COLOR_BGR2GRAY) 
row = grayImage.shape[0]
col = grayImage.shape[1]

arr = np.zeros(256,dtype=np.uint32)

for i in range(row):
	for j in range(col):
		arr[grayImage[i][j]] +=1

for i in range(1,len(arr)):
	arr[i] += arr[i-1]

for i in range(len(arr)):
	arr[i] = (arr[i]*255)/(row*col)

newImage = np.ndarray((row,col),dtype=np.uint8)
for i in range(row):
	for j in range(col):
		newImage[i][j] = arr[grayImage[i][j]]

cv2.imshow("or",grayImage)
cv2.imshow("ddd",newImage)
cv2.waitKey(0)

print(arr)