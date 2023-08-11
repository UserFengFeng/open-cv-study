import cv2

# 自适应阈值
p = cv2.imread("./p.jpg")
p = cv2.cvtColor(p, cv2.COLOR_BGR2GRAY)
dst = cv2.adaptiveThreshold(p, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 0)
cv2.imshow("test", dst)
cv2.waitKey(0)
