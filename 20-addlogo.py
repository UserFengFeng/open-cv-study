import cv2
import numpy as np

img = cv2.imread("./1.jpg")

logo = np.zeros((200, 200, 3), np.uint8)
mask = np.zeros((200, 200), np.uint8)

logo[20: 120, 20:120] = [0, 0, 255]
logo[80:180, 80:180] = [0, 255, 0]


mask[20: 120, 20:120] = 255
mask[80:180, 80:180] = 255

m = cv2.bitwise_not(mask)
cv2.imshow("m", m)

# roi = img[0:200, 0:200]
#
# tmp = cv2.bitwise_and(roi, roi, mask=m)
# dst = cv2.add(tmp, logo)
#
# img[0:200, 0:200] = dst

# cv2.imshow("img", img)
cv2.waitKey(0)
