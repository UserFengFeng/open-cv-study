import cv2
import numpy as np

img = cv2.imread("./sobel.png")
# SIFT特征描述子
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# sift = cv2.SIFT_create()
# surf = cv2.SURF_create()
orb = cv2.ORB_create()

# 获取关键点列表
# kp = sift.detect(gray, None)

# 已废弃如下方法代替
# kp, dest = sift.defectAndCompute(gray, None)
kp = orb.detect(gray, None)
# 创建一个空的图像，用于绘制关键点
keypoints_img = np.zeros_like(img)

cv2.drawKeypoints(gray, kp, keypoints_img)
cv2.imshow("test", keypoints_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
