import cv2, numpy
import numpy as np

# 控制鼠标

# 鼠标回调方法
def mouse_callback(event, x, y, flags, userdata):
    print(event, x, y, flags, userdata)

cv2.namedWindow("mouse", cv2.WINDOW_NORMAL)
cv2.resizeWindow("mouse", 600, 600)
# 绑定鼠标回调
cv2.setMouseCallback("mouse", mouse_callback, "123")

img = np.zeros((600, 600, 3), np.uint8)
while True:
    cv2.imshow("mouse", img)
    key = cv2.waitKey(1)
    if key & 0xFF == ord("q"):
        break
cv2.destroyAllWindows()

