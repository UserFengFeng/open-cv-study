import cv2
import numpy as np

img = np.zeros((200, 200), np.uint8)
img2 = np.zeros((200, 200), np.uint8)
img[20:120, 20:120] = 255
img2[80:180, 80:180] = 255


# 非运算 也就是ps中的反选
# img[50:150, 50:150] = 255
# new_img = cv2.bitwise_not(img)

# 与运算 取交集
# new_img = cv2.bitwise_and(img, img2)

# 或 两个都合起来
# new_img = cv2.bitwise_or(img, img2)

# 异或 取差集
new_img = cv2.bitwise_xor(img, img2)

cv2.imshow("b_and", new_img)
cv2.waitKey(0)
