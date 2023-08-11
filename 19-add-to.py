import cv2
import numpy as np
# 溶合
img1 = cv2.imread("./1.jpg")
img2 = cv2.imread("./add.jpg")

result = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)
cv2.imshow("add", result)
cv2.waitKey(0)


