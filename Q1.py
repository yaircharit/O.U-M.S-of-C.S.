import cv2 as cv
import sys
import numpy as np

__IMG_SIZE_FACTOR__ = 0.25


# Welcome screen setup
welcome = cv.resize(cv.imread('Question1/welcome.png'), (0, 0), None, 0.4, 0.4)
cv.putText(welcome, 'Enter assignment letter (a, b, c...); ESC to close',
           (0, 550), cv.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 1, 2)


# initialize
imgs = ['img0.jpeg', 'img1.jpeg', 'img2.jpeg']
org = []
gray = []
r2w = []
for img in imgs:
    temp = cv.imread(f'Question1/{img}')

    if temp is None:
        sys.exit(f'Could not read {img}')

    temp = cv.resize(temp, (0, 0), None, __IMG_SIZE_FACTOR__,
                     __IMG_SIZE_FACTOR__)
    gray.append(cv.cvtColor(cv.cvtColor(
        temp, cv.COLOR_RGB2GRAY), cv.COLOR_GRAY2BGR))
    r2w.append(cv.GaussianBlur(gray[-1], (3, 3), 0))
    org.append(temp)

# Shows specific image
def show(img_index):
    cv.imshow(imgs[img_index], np.hstack((org[img_index], gray[img_index])))


canny_thresholds = [(100, 200), (0, 300), (200, 500)]
# Shows Canny Edge detection for the thresholds listed above for specific image
def canny(img_index):
    cv.imshow(f'{imgs[img_index]} canny', np.hstack(
        [cv.Canny(r2w[img_index], l, h) for (l, h) in canny_thresholds]))

# Shows sobel edge detection (x and y) for a specific image
def sobel(img_index):
    sobelx = cv.Sobel(r2w[img_index], cv.CV_16S, 1, 0, ksize=7)  # x
    sobely = cv.Sobel(r2w[img_index], cv.CV_16S, 0, 1, ksize=7)  # y
    cv.imshow(f'{imgs[img_index]} sobel', np.hstack((sobelx, sobely)))

# returns image with harris corners highlighted
def get_harris(img, block_size, k_size, k):
    dst = cv.cornerHarris(img, block_size, k_size, k)
    dst = cv.dilate(dst, None)
    temp = img.copy()
    temp[dst > 0.01*dst.max()] = 0
    return temp


harris_thresholds = [(2, 3, 0.04), (2, 5, 0.07)]
# Shows harris corners of specific image
def harris(img_index):
    temp = cv.cvtColor(org[img_index], cv.COLOR_BGR2GRAY)
    cv.imshow(f'{imgs[img_index]} sift', np.hstack(
        [get_harris(temp, *th) for th in harris_thresholds]))


# Shows SIFT points for specific image
def sift(img_index):
    temp = cv.cvtColor(org[img_index], cv.COLOR_BGR2GRAY)

    img_sifts = []
    s = cv.SIFT_create()
    for th in harris_thresholds:
        harr = get_harris(temp, *th)
        kp = s.detect(harr, None)
        img_sifts.append(cv.drawKeypoints(temp, kp, org[img_index]))

    cv.imshow(f'{imgs[img_index]} SIFT', np.hstack(img_sifts))

# Shows matches of 2 different images
def match(img1_index, img2_index):
    orb = cv.ORB_create()
    bf = cv.BFMatcher_create(cv.NORM_HAMMING, crossCheck=True)

    kp1, des1 = orb.detectAndCompute(gray[img1_index], None)
    kp2, des2 = orb.detectAndCompute(gray[img2_index], None)

    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda x: x.distance)
    img = cv.drawMatches(org[img1_index], kp1,
                         org[img2_index], kp2, matches[:25], None, flags=2)  # Draws first 25 matches

    cv.imshow(f'{imgs[img1_index]} & {imgs[img2_index]} matching?', img)


# Shows Hough lines for specific image
def houghLines(img_index):
    temp = cv.imread('Question1/lighthouse.jpg', 0)
    temp = cv.resize(temp, (0, 0), None, .5, .5)
    edges = cv.Canny(temp, 50, 150, apertureSize=3)
    lines = cv.HoughLines(edges, 1, np.pi/180, 200)

    if lines is None:
        lines = []

    for line in lines:
        for rho, theta in line:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000*(a))
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 - 1000*(a))

            cv.line(temp, (x1, y1), (x2, y2), (0, 0, 255), 2)

    cv.imshow(f'{imgs[img_index]} houghlines', temp)


# Show Welcome screen
cv.imshow('Welcome Screen', welcome)
work_on_img = 0
while True:
    k = cv.waitKey(0)
    num = k - ord('0')
    if k & 0xff == 27 or k == ord('q'):
        cv.destroyAllWindows()
        break
    elif k == ord('a'):             # Assignment A
        show(work_on_img)
    elif k == ord('b'):             # Assignment B
        canny(work_on_img)
        sobel(work_on_img)
    elif k == ord('c'):             # Assignment C
        harris(work_on_img)
    elif k == ord('d'):             # Assignment D
        sift(work_on_img)
    elif k == ord('e'):             # Assignment E
        match(work_on_img, (work_on_img+1) % len(imgs))
    elif k == ord('f'):             # Assignment F
        houghLines(work_on_img)
    # Switch to an image by typing its serial number
    elif num in range(10) and num < len(imgs):
        work_on_img = num
