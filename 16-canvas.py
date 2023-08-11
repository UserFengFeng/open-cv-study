import cv2
import numpy as np

img = np.zeros((480, 640, 3), np.uint8)
# 坐标点（x, y） 线宽  平滑度 缩放系数
# cv2.line(img, (30, 20), (330, 400), (0, 0, 255), 5, 4)
# cv2.line(img, (10, 20), (300, 400), (0, 0, 255), 5, 16)

# 坐标  1不填充 -1填充
# cv2.rectangle(img, (10, 10), (100, 100), (0, 0, 255), -1)
# 坐标 半径
# cv2.circle(img, (200, 200), 100, (0, 255, 255), 1)

# 椭圆
# cv2.ellipse(img, (200, 200), (100, 50), 0, 0, 360, (0, 0, 255))
# cv2.ellipse(img, (200, 200), (100, 100), 90, 0, 90, (0, 255, 0))

# 多边形
# point = np.array([(300, 10), (150, 100), (450, 100)], np.int32)
# cv2.polylines(img, [point], True, (0, 0, 255))
# cv2.fillPoly(img, [point], (255, 0, 0))

# 文本
cv2.putText(img, "Hell World", (10, 200), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255,0))

cv2.imshow("img", img)
cv2.waitKey(0)
