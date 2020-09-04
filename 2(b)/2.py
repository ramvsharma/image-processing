import cv2
import numpy as np
from matplotlib import pyplot as plt 

cameramanimg = cv2.imread("../cameraman.tif")


# histo = cv2.calcHist(cameramanimg,[0],None,[256],[0,256])

# plt.plot(histo)
# plt.show()
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
arr = []
for i in range(row):
	for j in range(col):
		arr.append(grayImage[i][j])

binList =[]
for i in range(256):
	binList.append(i)

fig, ax = plt.subplots() 
ax.hist(arr,bins = binList)
ax.set_title("Original image")
ax.set_xlabel("Gray level")
ax.set_ylabel("No. of Graylevel present")
newimage = np.ndarray((row,col,1),np.uint8)


#  using formula   s = (r-c)*(b-a)/(d-a) + a

c = 0
d = 1024 - 1

for i in range(row):
	for j in range(col):
		newimage[i][j] = ((grayImage[i][j]-c)*(b-a))/(d-c) + a

cv2.imshow("Original image",cameramanimg)
cv2.imshow("Rotated",grayImage)
cv2.imshow("newimage",newimage)

brr = []
for i in range(row):
	for j in range(col): 
		brr.append(newimage[i][j][0])
fig1, bx = plt.subplots() 
bx.hist(brr,bins = binList)
bx.set_title("newimage")
bx.set_xlabel("Gray level")
bx.set_ylabel("No. of Graylevel present")
plt.show() 


cv2.waitKey(0)