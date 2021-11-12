import cv2 as cv
import sys
import numpy as np

img = cv.imread('lighthouse.jpg',0)


if img is None:
    sys.exit("Could not read the image.")
img = cv.resize(img, (0, 0), None, .5, .5)
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img = cv.GaussianBlur(img ,(3,3),0)

edges1 = cv.Canny(img,100,200)
edges2 = cv.Canny(img,0,500)
edges3 = cv.Canny(img,200,255)

sobelx = cv.Sobel(img,cv.CV_64F,1,0,ksize=7)  # x
# sobelx = cv.GaussianBlur(sobelx ,(7,7),0)
sobely = cv.Sobel(img,cv.CV_64F,0,1,ksize=7) # y
# sobely = cv.GaussianBlur(sobely ,(7,7),0)
sobelxy = cv.Sobel(img,cv.CV_64F,1,1,ksize=7) # xy
# sobelxy = cv.GaussianBlur(sobelxy ,(7,7),0)

numpy_canny = np.vstack((edges1,edges2,edges3))
numpy_sobel = np.vstack((sobelx,sobely,sobelxy))
cv.imshow('Original', img)
cv.imshow('Canny', numpy_canny)
cv.imshow('Sobel', numpy_sobel)
k = cv.waitKey(0)

    
    