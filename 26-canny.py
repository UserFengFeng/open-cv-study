import cv2
import numpy as np
'''
 它使用5x5高斯滤波消除噪音
'''

img = cv2.imread("./p.jpg")
dst = cv2.Canny(img, 50, 300)
cv2.imshow("img", img)
cv2.imshow("dst", dst)
cv2.waitKey(0)