import cv2
import numpy as np
from matplotlib import pyplot as plt

# 分水岭法
img = cv2.imread("./qian.png")
# 获取背景
# 1.通过二值法获取黑白图片
# 2.通过形态学获取背景

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ret, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
# 反转 自适应阈值THRESH_OTSU（会将目标体中的黑色部分填充白色）
ret, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# 开运算
kernel = np.ones((3, 3), np.int8)
open1 = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
# 膨胀
bg = cv2.dilate(open1, kernel, iterations=1)

# 获取前景物体
dist = cv2.distanceTransform(open1, cv2.DIST_L2, 5)
ret, fg = cv2.threshold(dist, 0.7 * dist.max(), 255, cv2.THRESH_BINARY)

# 获取未知区域
fg = np.uint8(fg)
unknow = cv2.subtract(bg, fg)

# 创建连通域
ret, marker = cv2.connectedComponents(fg)
marker = marker + 1
marker[unknow == 255] = 0

# 图像分割
result = cv2.watershed(img, marker)
img[result == -1] = [0, 0, 255]

# plt.imshow(dist, cmap="gray")
# plt.show()
# exit()

cv2.imshow("xxxx", img)
cv2.imshow("unknow", unknow)
cv2.imshow("fg", fg)
cv2.imshow("bg", bg)
cv2.imshow("test", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
