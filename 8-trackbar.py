import cv2
import numpy as np
def callback():
    pass

bar = cv2.namedWindow("bar", cv2.WINDOW_NORMAL)

cv2.createTrackbar("R", "bar", 0, 255, callback)
cv2.createTrackbar("G", "bar", 0, 255, callback)
cv2.createTrackbar("B", "bar", 0, 255, callback)

img = np.zeros((480, 460, 3), np.uint8)

while True:
    # 获取trackbar的值
    r = cv2.getTrackbarPos("R", "bar")
    g = cv2.getTrackbarPos("G", "bar")
    b = cv2.getTrackbarPos("B", "bar")

    img[:] = [b, g, r]
    cv2.imshow("bar", img)

    key = cv2.waitKey(10)

    if key & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()


