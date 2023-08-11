import cv2
import numpy as np

img = cv2.imread("./1.jpg")
h, w, ch = img.shape
# src要不断尝试，或者要知道目标不规则四边形的四个点
src = np.float32([[100, 800], [1000, 800], [0, 800], [1000, 800]])
dst = np.float32([[0, 0], [1161, 0], [0, 992], [1161, 992]])
M = cv2.getPerspectiveTransform(src, dst)

new_img = cv2.warpPerspective(img, M, (2300, 3000))

cv2.imshow("test", new_img)
cv2.waitKey(0)