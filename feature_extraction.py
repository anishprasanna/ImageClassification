import cv2
import numpy as np

features = []

#Import relative path to image (must be as string)
#Format of list - [corners value, orb value, edge value]
def extractFeatures(imgString):
    #FEATURE EXTRACTION - CORNERS
    img = cv2.imread(imgString)
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
    img[dst>0.1*dst.max()]=[0,0,255]
    #add number of corners to list
    features.append(len(corners))

    #FEATURE EXTRACTION - ORB KEYPOINTS
    img = cv2.imread('photos/cats/cat.4001.jpg', 0)
    # Initiate detector and find ORB keypoints
    orb = cv2.ORB_create()
    kp = orb.detect(img,None)
    # compute the descriptors with ORB
    kp, des = orb.compute(img, kp)
    #add number of keypoints to list
    features.append(len(kp))

    #FEATURE EXTRACTION - CANNY EDGE DETECTION
    img = cv2.imread('photos/cats/cat.4001.jpg', 0)
    edges = cv2.Canny(img,100,200)
    features.append(len(edges))
    print(features)