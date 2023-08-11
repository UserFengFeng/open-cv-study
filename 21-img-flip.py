import cv2

img = cv2.imread("./1.jpg")
new_img1 = cv2.flip(img, 0)
new_img2 = cv2.flip(img, -1)
new_img3 = cv2.flip(img, 1)
cv2.imshow("img", img)
# 上下翻转
cv2.imshow("img1", new_img1)
# 上下+左右
cv2.imshow("img2", new_img2)
# 左右
cv2.imshow("img3", new_img3)
cv2.waitKey(0)
