import os
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import scipy.io as sio


#img = cv.imread(source,0)
#orb = cv.ORB_create(nfeatures=thrs, scoreType=cv.ORB_FAST_SCORE)
#kp = orb.detect(img,None)
#kp, des = orb.compute(img, kp)
#img1 = cv2.imread('box.png',0)          # queryImage
#img2 = cv2.imread('box_in_scene.png',0) # trainImage



# Initiate ORB detector
def apply_ORB(source):
    orb = cv.ORB_create()
    img1 = cv.imread(source,0)
    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    #kp2, des2 = orb.detectAndCompute(img2,None)
    return kp1, des1


def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file


#Threshold for limiting the number of features in the images.

#for file in files("."):
   # if "gen" in file:
    #    print (file)
     #   k, d = apply_ORB(file)
        #print (k)
        #print(d)

#main() starts from here
number_of_matches = 100;
k1, d1 = apply_ORB("input1.png")
k2, d2 = apply_ORB("input2.png")

# create BFMatcher object
bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
# Match descriptors.
matches = bf.match(d1,d2)
# Sort them in the order of their distance.
matches = sorted(matches, key = lambda x:x.distance)

img1 = cv.imread("input1.png",0)
img2 = cv.imread("input2.png",0)
img3 = cv.drawMatches(img1,k1,img2,k2, matches[:number_of_matches] ,None, flags=2)
plt.imshow(img3),plt.show()
