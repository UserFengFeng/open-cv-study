import cv2
import numpy as np

img = cv2.imread("./contours.png")
# 转单通道
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 二值化
ret, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
# 查找轮廓
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# 绘制轮廓(目标图像， 轮廓， 绘制第几个轮廓， 颜色， 是否填充)
cv2.drawContours(img, contours, -1, (0, 0, 255), 1)


# 计算面积
# area = cv2.contourArea(contours[0])

# 计算周长
# length = cv2.arcLength(contours[0], False)

def drawShape(src, points):
    i = 0
    while i < len(points):
        if i == (len(points) - 1):
            x, y = points[i][0]
            x1, y1 = points[0][0]
        else:
            x, y = points[i][0]
            x1, y1 = points[i + 1][0]
        cv2.line(src, (x, y), (x1, y1), (0, 0, 255), 3)
        i += 1


img = cv2.imread("./shou.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
contours, hirearchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

"""多边形逼近"""
# 精度
e = 2
approx = cv2.approxPolyDP(contours[0], e, True)
drawShape(img, approx)

"""
    凸包
"""
hull = cv2.convexHull(contours[0])
drawShape(img, hull)

# 最小外接矩形 含有角度
rotatedrect = cv2.minAreaRect(contours[0])
box = cv2.boxPoints(rotatedrect)
box = np.int0(box)
cv2.drawContours(img, [box], 0, (0, 0, 255), 2)

# 最大外接矩形
x, y, w, h = cv2.boundingRect(contours[0])
cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow("test", img)
cv2.imshow("binary", binary)
cv2.waitKey(0)
