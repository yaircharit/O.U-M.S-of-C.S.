import numpy as np
import cv2 as cv
import sys

LVLS = 5
scaler = .5
def reduce(imgs):
    height, width, _ = imgs[0].shape
    
    width *= scaler
    height *= scaler
    print(height, width)
    return [cv.resize(img, (int(width), int(height))) for img in imgs]

    
imgs = [cv.imread('lion-face.jpg'), cv.imread('tiger-face.jpg')]

if imgs[0] is None or imgs[1] is None:
    sys.exit(f'Could not read img')

height, width, _ = imgs[0].shape
imgs[1] = cv.resize(imgs[1], (width, height))

imgs = reduce(imgs)

mid = imgs[0].shape[1]//2
img3 = np.hstack((imgs[0][:,:mid], imgs[1][:,mid:]))
img1 = imgs[0]
img2 = imgs[1]

copy_img1=img1.copy()
gp_img1=[copy_img1] #making a list for image 1 and its first element is image itself
#gaussian pyramid for img1 image
for i in range(LVLS):
    copy_img1=cv.pyrDown(copy_img1)
    gp_img1.append(copy_img1) #appending the pyr down image to the list of first image
#copy image2 in a new variable
copy_img2=img2.copy()
gp_img2=[copy_img2] #making a list for image 2 and its first element is image itself
#gaussian pyramid for img2 image
for i in range(LVLS):
    copy_img2=cv.pyrDown(copy_img2)
    gp_img2.append(copy_img2) #appending the pyr down image to the list of second image
copy_img1=gp_img1[5]#assigning the first image list last element to copied variable
lp_img1=[copy_img1]#again making alist for image one whose first element is the last element of previous list
#laplacian pyramid for img1 image
for i in range(5,0,-1):
    size=(gp_img1[i-1].shape[1],gp_img1[i-1].shape[0])
    gaussian=cv.pyrUp(gp_img1[i],dstsize=size)
    laplacian_img1=cv.subtract(gp_img1[i-1],gaussian)
    lp_img1.append(laplacian_img1)
#same process with img2 image
copy_img2=gp_img2[5]#assigning the first image list last element to copied variable
lp_img2=[copy_img2]#again making alist for image one whose first element is the last element of previous list
#laplacian pyramid for img1 image
for i in range(5,0,-1):
    size=(gp_img2[i-1].shape[1],gp_img2[i-1].shape[0])
    gaussian=cv.pyrUp(gp_img2[i],dstsize=size)
    laplacian_img2=cv.subtract(gp_img2[i-1],gaussian)
    lp_img2.append(laplacian_img2)
#now add left and right halves of the images in each level of pyramid
img1_img2_pyramid=[] #an empty list
for img1_lap,img2_lap in zip(lp_img1,lp_img2):
    cols,rows,ch=img1_lap.shape
    laplacian=np.hstack((img2_lap[:,0:int(rows/2)],img1_lap[:,int(rows/2):]))
    img1_img2_pyramid.append(laplacian)
    # cv.imshow(f'reduce-lvl#{i}', laplacian)
#now reconstruct
img1_img2_reconstruct=img1_img2_pyramid[0]
for i in range(1,LVLS+1):
    size=(img1_img2_pyramid[i].shape[1],img1_img2_pyramid[i].shape[0])
    img1_img2_reconstruct=cv.pyrUp(img1_img2_reconstruct,dstsize=size)
    img1_img2_reconstruct=cv.add(img1_img2_pyramid[i],img1_img2_reconstruct)
    # cv.imshow(f'recon-lvl#{i}', img1_img2_reconstruct)

cv.imshow('img1', imgs[0])
cv.imshow('img2', imgs[1])
cv.imshow('img3',img1_img2_reconstruct)

k = cv.waitKey(0)
