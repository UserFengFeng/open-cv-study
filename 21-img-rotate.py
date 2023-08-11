import cv2
import numpy as np
# 旋转
img = cv2.imread("./1.jpg")
new = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
new1 = cv2.rotate(img, cv2.ROTATE_180)
cv2.imshow("new", new)
cv2.imshow("new2", new1)

cv2.waitKey(0)