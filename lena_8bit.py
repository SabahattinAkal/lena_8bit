import cv2
import numpy as np 
img= cv2.imread("lena.png")

x=256
y=256
img[x,y]=0
img[x-1,y]=0
img[x,y+1]=0
img[x+1,y]=0
img[x,y-1]=0
img[x-1,y-1]=0
img[x+1,y+1]=0
img[x-1,y+1]=0
img[x+1,y-1]=0

cv2.imshow("lena_pixel",img)
cv2.waitKey()