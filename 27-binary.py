import cv2
import numpy as np

# 二值化阈值

img = cv2.imread("./p.jpg")
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# THRESH_BINARY_INV 白色转黑色 黑色转白色
ret, dst = cv2.threshold(img, 180, 255, cv2.THRESH_BINARY)
cv2.imshow("img1", img1)
cv2.imshow("test", dst)
cv2.waitKey(0)