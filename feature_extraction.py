import cv2
import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt

#FEATURE EXTRACTION - CORNERS
#Replace with whatever file name is needed
img = cv2.imread('photos/cats/cat.4001.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv2.cornerHarris(gray,5,3,0.04)

#threshold for determining whether a corner exists
ret, dst = cv2.threshold(dst,0.1*dst.max(),255,0)
dst = np.uint8(dst)
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)

#corners are created here
corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)

for i in range(1, len(corners)):
    print(corners[i])
print(len(corners))
img[dst>0.1*dst.max()]=[0,0,255]
#cv2.imshow('image', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows

#FEATURE EXTRACTION - ORB KEYPOINTS
img = cv2.imread('photos/cats/cat.4001.jpg', 0)

# Initiate STAR detector
orb = cv2.ORB_create()

# find the keypoints with ORB
kp = orb.detect(img,None)

# compute the descriptors with ORB
kp, des = orb.compute(img, kp)
print('Number of keypoints found is: ', len(kp))

# draw only keypoints location,not size and orientation
#img2 = cv2.drawKeypoints(img,kp,'cat.png', color=(0,255,0), flags=0)
#plt.imshow(img2),plt.show()

#FEATURE EXTRACTION - CANNY EDGE DETECTION
img = cv2.imread('photos/cats/cat.4001.jpg', 0)
edges = cv2.Canny(img,100,200)
print('Amount of edges we have are: ' , len(edges))

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()