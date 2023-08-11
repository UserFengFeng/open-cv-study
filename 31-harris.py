import cv2
import numpy as np

# 特性 旋转不变的特性


img = cv2.imread("./sobel.png")
block_size = 2  # 检测窗口的大小
ksize = 3  # sobel卷积核
k = 0.04  # 权重系数，经验值 一般取0.02~0.04

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# harris角点检测
# dst = cv2.cornerHarris(gray, block_size, ksize, k)

# dst > 取dst中最大值的百分之一
# img[dst > 0.01 * dst.max()] = [0, 0, 255]


# shi-tomasi 角点检测 （基于harris的优化） useHarrisDetector是否用harris算法
corners = cv2.goodFeaturesToTrack(gray, 1000, 0.01, 10)
corners = np.int0(corners)
for conrner in corners:
    x, y = conrner.ravel()
    cv2.circle(img, (x, y), 2, (255, 255, 0), 1)

cv2.imshow("test", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
