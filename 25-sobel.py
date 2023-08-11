import cv2
import numpy as np

img = cv2.imread("./sobel.png")


# 索贝尔算子y方向边缘
d1 = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
# 索贝尔算子x方向边缘
d2 = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
# d2 = cv2.Sobel(img, cv2.CV_64F, 1, 1, ksize=5)


# 沙尔算子y方向边缘 (不可以直接求xy方向边缘)
s1 = cv2.Scharr(img, cv2.CV_64F, 0, 1)
# 沙尔算子x方向边缘
s2 = cv2.Scharr(img, cv2.CV_64F, 1, 0)

# 拉普拉斯算子
lap = cv2.Laplacian(img, cv2.CV_64F)

dst1 = cv2.add(d1, d2)
dst2 = cv2.add(s1, s2)

# cv2.imshow("img", img)
# cv2.imshow("d1", d1)
# cv2.imshow("d2", d2)
cv2.imshow("dst", dst1)
cv2.imshow("lap", lap)
cv2.imshow("dst2", dst2)
cv2.waitKey(0)