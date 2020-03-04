import cv2
import argparse
import numpy as np
ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="path to input image")
args=vars(ap.parse_args())
img=cv2.imread(args["image"])
gray=img[:,:,0]*0.0722 + img[:,:,1]*0.7152 + img[:,:,2]*0.2126
cv2.imwrite("grayscaled.png",gray)
