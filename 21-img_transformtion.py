import cv2
import numpy as np
# 插值算法
img = cv2.imread("./1.jpg")

h, w, t = img.shape

# 邻近插值
new_img1 = cv2.resize(img, None, fx=0.3, fy=0.3, interpolation=cv2.INTER_NEAREST)
# 默认双线性差值 4个点
new_img2 = cv2.resize(img, None, fx=0.3, fy=0.3, interpolation=cv2.INTER_LINEAR)
# 三次插值16个点
new_img3 = cv2.resize(img, None, fx=0.3, fy=0.3, interpolation=cv2.INTER_CUBIC)
# 面积插值 效果最好
new_img4 = cv2.resize(img, None, fx=0.3, fy=0.3, interpolation=cv2.INTER_AREA)
cv2.imshow("img1", new_img1)
cv2.imshow("img2", new_img2)
cv2.imshow("img3", new_img3)
cv2.imshow("img4", new_img4)
cv2.waitKey(0)
