import cv2
import numpy as np

img1 = cv2.imread("./match1.png")
img2 = cv2.imread("./match2.png")

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT_create()

kp1 = sift.detect(gray1, None)
kp1, des1 = sift.compute(gray1, kp1)

kp2 = sift.detect(gray2, None)
kp2, des2 = sift.compute(gray2, kp2)

# 创建匹配器
index_parasm = dict(algorithm=1, trees=5)
search_params = dict(checks=50)
# 近似最近邻搜索算法
flann = cv2.FlannBasedMatcher(index_parasm, search_params)
# 对描述子进行匹配计算
matchs = flann.knnMatch(des1, des2, k=2)

good = []
for i, (m, n) in enumerate(matchs):
    if m.distance < 0.7 * n.distance:
        good.append(m)

# 匹配点必须大于等于4
if len(good) >= 4:
    srcPts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
    dstPts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
    # 单应性矩阵
    H, _ = cv2.findHomography(srcPts, dstPts)
    # H, _ = cv2.findHomography(srcPts, dstPts, cv2.RANSAC, 5.0)
    h, w = img1.shape[:2]
    pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
    dst = cv2.perspectiveTransform(pts, H)

    cv2.polylines(img2, [np.int32(dst)], True, (0, 255, 255))
else:
    print("the number of good is less than 4.")
    exit()
ret = cv2.drawMatchesKnn(img1, kp1, img2, kp2, [good], None)

cv2.imshow("test", ret)
cv2.waitKey(0)
cv2.destroyAllWindows()
