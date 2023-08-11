import cv2
import numpy as np
'''
    形态学
'''

# 腐蚀
img = cv2.imread("erode-bilater.png")

# kernel = np.ones((3, 3), np.uint8)
# 矩形腐蚀
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
# 椭圆腐蚀
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
# 十字架腐蚀
# kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))


# 先腐蚀后膨胀 -- 开运算
# dst = cv2.erode(img, kernel, iterations=1)
# # 膨胀
# dst = cv2.dilate(dst, kernel, iterations=1)

# 开运算 先腐蚀再膨胀 去除大图性外的小图形
dst = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

img = cv2.imread("close-dilate.png")
# 闭运算   先膨胀再腐蚀   去除大图形内的小图形
dst = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
#
# # 梯度 = 原图 - 腐蚀  求图形的边缘
dst = cv2.morphologyEx(dst, cv2.MORPH_GRADIENT, kernel)
#
# # 顶帽 = 原图 - 开运算  得到大图形外的小图形
img = cv2.imread("morph.png")
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (6, 6))
dst = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

# # 黑帽 = 原图 - 闭运算 (留下噪点)  得到大图形内的小图形
img = cv2.imread("close-dilate.png")
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (6, 6))
dst = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow("test", dst)
cv2.imshow("test1", img)
cv2.waitKey(0)
