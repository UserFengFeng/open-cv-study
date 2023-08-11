import cv2
import numpy as np

img = cv2.imread("./1.jpg")
# 图的加法运算就是矩阵的加法运算 两张图大小一致
h, w, c = img.shape

oimg = np.ones((h, w, c), np.uint8) * 100
# result = cv2.add(img, oimg)
# cv2.imshow("result", result)

# 减法
# oimg = cv2.subtract(result, oimg)
# cv2.imshow("sub", oimg)

# 乘除
result = cv2.multiply(img, oimg)
# result = cv2.divide(img, oimg)
cv2.imshow("result", result)
cv2.imwrite("./add.jpg", result)

cv2.waitKey(0)
