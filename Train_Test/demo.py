import os
import numpy as np
import cv2 
from matplotlib import pyplot as plt
import scipy.io as sio
import sys
import numpy as np
import platform
import statistics
import time

input1 = "ch_15_013.PNG"
input2 = "ch_17_013.PNG"

def apply_FAST(source):
    #here fast is only used for detecting the keypoints but later on BRIEF will be used for the 
    img = cv2.imread(source,0)     
    # find the keypoints and descriptors with SIFT
    #kp1, des1 = orb.detectAndCompute(img1,None)
    #kp2, des2 = orb.detectAndCompute(img2,None)   
    
    # Initiate FAST extractor
    fast = cv2.FastFeatureDetector_create()
    kp = fast.detect(img,None)
    
    # Initiate BRIEF extractor
    brief = cv2.xfeatures2d.BriefDescriptorExtractor_create()
    kp1, des1 = brief.compute(img, kp)
    print(len(kp1))
    return kp1, des1






t = time.time()       
k1, d1 = apply_FAST(input1)
elapsed = time.time() - t
print("Time elapsed : " + str(elapsed))












            
            









       
