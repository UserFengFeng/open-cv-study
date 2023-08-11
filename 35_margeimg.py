import cv2
import numpy as np


def get_home(img1, img2):
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # 创建特征转换对象
    sift = cv2.SIFT_create()
    # 获得特征点、描述子
    kp1 = sift.detect(gray1, None)
    kp1, des1 = sift.compute(gray1, kp1)

    kp2 = sift.detect(gray2, None)
    kp2, des2 = sift.compute(gray2, kp2)

    # 创建特征匹配器
    flann = cv2.BFMatcher_create()
    # 特征匹配
    matches = flann.knnMatch(des1, des2, k=2)
    # 特征点过滤
    verify_ratio = 0.8
    verify_matches = []
    for m1, m2 in matches:
        if m1.distance < verify_ratio * m2.distance:
            verify_matches.append(m1)

    min_matches = 8
    # 单应性矩阵
    if len(verify_matches) > min_matches:
        img1_pts = []
        img2_pts = []
        for m in verify_matches:
            img1_pts.append(kp1[m.queryIdx].pt)
            img2_pts.append(kp2[m.trainIdx].pt)
        img1_pts = np.float32(img1_pts).reshape(-1, 1, 2)
        img2_pts = np.float32(img2_pts).reshape(-1, 1, 2)
        H, _ = cv2.findHomography(img1_pts, img2_pts, cv2.RANSAC, 0.5)
    return H


def stitch_image(H, img1, img2):
    # 获取每张图片的角点
    h1, w1 = img1.shape[:2]
    h2, w2 = img1.shape[:2]
    img1_dims = np.float32([[0, 0], [0, h1], [w1, h1], [w1, 0]]).reshape(-1, 1, 2)
    img2_dims = np.float32([[0, 0], [0, h2], [w2, h2], [w2, 0]]).reshape(-1, 1, 2)
    # 对图片进行变换
    img1_transform = cv2.perspectiveTransform(img1_dims, H)
    # 创建大图 合并
    result_dims = np.concatenate((img2_dims, img1_transform), axis=0)
    [minx, miny] = np.int32(result_dims.min(axis=0).ravel() - 0.5)
    [maxx, maxy] = np.int32(result_dims.max(axis=0).ravel() + 0.5)
    # 平移的距离
    transform_dist = [-minx, -miny]
    transfrom_array = np.array([[
        1, 0, transform_dist[0]],
        [0, 1, transform_dist[1]],
        [0, 0, 1]])
    result_img = cv2.warpPerspective(img1, transfrom_array.dot(H), (maxx - minx, maxy - miny))
    result_img[transform_dist[1]: transform_dist[1] + h2, transform_dist[0]: transform_dist[0] + w2] = img2
    return result_img


# 设置固定一样大小 800x700
img1 = cv2.imread("./split_left.png")
img2 = cv2.imread("./split_right.png")
img1 = cv2.resize(img1, (800, 700))
img2 = cv2.resize(img2, (800, 700))
# 找特征点、描述子、计算单应性矩阵
H = get_home(img1, img2)

# 拼接输出结果
result_img = stitch_image(H, img1, img2)
# marge_img = np.hstack((img1, img2))
cv2.imshow("result_img", result_img)
cv2.waitKey(0)
