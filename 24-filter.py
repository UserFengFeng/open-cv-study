import cv2
import numpy as np

# 图像滤波

img = cv2.imread("./p.jpg")
# 卷积核
# kernal = np.ones((5, 5), np.float32) / 25
# # 目标图像、位深、卷积核
# dst = cv2.filter2D(img, -1, kernal)

# 均值滤波
# dst = cv2.blur(img, (5, 5))
# 方盒滤波
# dst = cv2.boxFilter(img, -1, (5, 5))

# 高斯滤波 处理噪点
# dst = cv2.GaussianBlur(img, (5, 5), sigmaX=50)

img = cv2.imread("./median.png")

# 中值滤波 # 消除胡椒噪音
# dst = cv2.medianBlur(img, 5)

img = cv2.imread("./bilater.png")
# 双边滤波
dst = cv2.bilateralFilter(img, 8, 20, 50)


cv2.imshow("xx", img)
cv2.imshow("test", dst)
cv2.waitKey(0)
