import cv2
import numpy as np
# 特征匹配
img1 = cv2.imread("./match1.png")
img2 = cv2.imread("./match2.png")

g1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
g2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# 特征描述子
sift = cv2.SIFT_create()
# orb = cv2.ORB_create()

kp1 = sift.detect(g1, None)
kp1, des1 = sift.compute(g1, kp1)

kp2 = sift.detect(g2, None)
kp2, des2 = sift.compute(g2, kp2)

# 暴力特征匹配
bf = cv2.BFMatcher_create(cv2.NORM_L1)
match = bf.match(des1, des2)

img3 = cv2.drawMatches(img1, kp1, img2, kp2, match, None)

cv2.imshow("test", img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
