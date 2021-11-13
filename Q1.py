import cv2 as cv
import sys
import numpy as np

img = cv.imread('lighthouse.jpg')


if img is None:
    sys.exit("Could not read the image.")
img = cv.resize(img, (0, 0), None, .65, .65)
gray = cv.GaussianBlur(img ,(3,3),0)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# Canny edge detection
edges1 = cv.Canny(gray,100,200)
edges2 = cv.Canny(gray,0,200)
edges3 = cv.Canny(gray,200,500)

#Sobel edge detection
sobelx = cv.Sobel(gray,cv.CV_16S,1,0,ksize=7)  # x
sobely = cv.Sobel(gray,cv.CV_16S,0,1,ksize=7) # y
sobelxy = cv.Sobel(gray,cv.CV_16S,1,1,ksize=7) # xy


# Show results
numpy_canny = np.vstack((edges1,edges2,edges3))
numpy_sobel = np.vstack((sobelx,sobely,sobelxy))
cv.imshow('Original', img)
cv.imshow('Canny', numpy_canny)
cv.imshow('Sobel', numpy_sobel)

# gray = np.float32(gray)
dst1 = cv.cornerHarris(gray,2,3,0.04)
dst2 = cv.cornerHarris(gray,2,5,0.07)
#result is dilated for marking the corners, not important
dst1 = cv.dilate(dst1,None)
dst2 = cv.dilate(dst1,None)
# Threshold for an optimal value, it may vary depending on the image.
img1 = img.copy()
img2 = img.copy()
img1[dst1>0.01*dst1.max()]= 0
img2[dst2>0.01*dst2.max()]= 0

sift = cv.SIFT_create()
kp = sift.detect(gray,None)
img_sift =cv.drawKeypoints(gray,kp,img)

numpy_harris = np.vstack((img1,img2,img_sift))
cv.imshow('dst',numpy_harris)

k = cv.waitKey(0)
if k & 0xff == 27:
    cv.destroyAllWindows()
    
    