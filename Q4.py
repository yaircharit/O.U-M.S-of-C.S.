import numpy as np
import cv2 as cv
import sys

LVLS = 5

imgs = [cv.imread('Question4/Walnut.jpg'), cv.imread('Question4/brain.jpg')]

if imgs[0] is None or imgs[1] is None:
    sys.exit(f'Could not read img')

height, width, _ = imgs[0].shape
imgs[1] = cv.resize(imgs[1], (width, height))  # Fit second image to be same size as the first


# Calculate Gaussian and Lapcilian Pyramids for both images
gp_imgs = []
lp_imgs = []
for i in range(len(imgs)):
    # Gaussian Pyramid
    copy_img = imgs[i].copy()
    gp_imgs.append([copy_img])
    for j in range(LVLS):
        copy_img = cv.pyrDown(copy_img)
        gp_imgs[i].append(copy_img)
        # cv.imshow(f'gaussian-lvl#{i}', copy_img)

    # Laplacian Pyramid
    copy_img = gp_imgs[i][5]
    lp_imgs.append([copy_img])
    for j in range(LVLS, 0, -1):
        height, width, _ = gp_imgs[i][j-1].shape
        gaussian = cv.pyrUp(gp_imgs[i][j], dstsize=(width, height))
        laplacian_img = cv.subtract(gp_imgs[i][j-1], gaussian)
        lp_imgs[i].append(laplacian_img)
        cv.imshow(f'lapcilean-lvl#{i}', laplacian_img)


# Combine the 2 images in every level of the lapcilian pyramid
comb_pyramid = []  
for img1_lap, img2_lap in zip(lp_imgs[0], lp_imgs[1]):
    cols, rows, ch = img1_lap.shape
    laplacian = np.hstack((img2_lap[:, 0:int(rows/2)], img1_lap[:, int(rows/2):]))
    comb_pyramid.append(laplacian)
    
# Reconstruct final image from the comined lapcilean pyramid
comb_recon = comb_pyramid[0]
for i in range(1, LVLS+1):
    size = (comb_pyramid[i].shape[1], comb_pyramid[i].shape[0])
    comb_recon = cv.pyrUp(comb_recon, dstsize=size)
    comb_recon = cv.add(comb_pyramid[i], comb_recon)
    # Show every level
    cv.imshow(f'recon-lvl#{i}', comb_recon)

cv.imshow('image 1', imgs[0])
cv.imshow('image 2', imgs[1])
cv.imshow('Final Image', comb_recon)

k = cv.waitKey(0)

# Assignment B: It appears we get a decent result even after 3 levels



