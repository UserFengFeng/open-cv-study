import cv2
import numpy as np

# 平移 and 变换矩阵
img = cv2.imread("./1.jpg")
h, w, ch = img.shape
# x平移
# M = np.float32([[1, 0, 100], [0, 1, 0]])
# x y都平移
# M = np.float32([[1, 0, 100], [0, 1, 300]])

# 中心点，度数（默认逆时针），缩放
# M = cv2.getRotationMatrix2D((w / 2, h / 2), 15, 1.0)


src = np.float32([[400, 300], [800, 300], [400, 1000]])
dst = np.float32([[200, 400], [600, 500], [150, 1100]])
# 仿射变换（旋转缩放平移）
M = cv2.getAffineTransform(src, dst)

img_new = cv2.warpAffine(img, M, (w, h))
cv2.imshow("tes1", img)
cv2.imshow("test", img_new)
cv2.waitKey(0)

