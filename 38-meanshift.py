import cv2
import numpy as np

img = cv2.imread("./flower.png")
# meanshift基于色彩图像分割
mean_img = cv2.pyrMeanShiftFiltering(img, 30, 40)
canny = cv2.Canny(mean_img, 150, 300)
contours, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0, 0, 255), 2)

cv2.imshow("img", img)
cv2.imshow("mean_img", mean_img)
cv2.imshow("canny", canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
