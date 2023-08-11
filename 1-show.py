import cv2
# 显示窗口
cv2.namedWindow("new", cv2.WINDOW_NORMAL)
cv2.resizeWindow("new", 1920, 1080)
cv2.imshow("new", 0)
key = cv2.waitKey(delay=0)
if key == "q":
    exit()
cv2.destroyAllWindows()