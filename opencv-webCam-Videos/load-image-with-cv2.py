# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 19:04:39 2020

@author: Benai
"""

import cv2
import matplotlib.pyplot as plt

# 0 gray scale image, 1 color image, -1 original image
img = cv2.imread('data/lena.jpg', 0)

# read an image
cv2.imshow('image', img)

k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    # of we press s then save then save the image
    cv2.imwrite('lala.png', img)
    cv2.destroyAllWindows()
    