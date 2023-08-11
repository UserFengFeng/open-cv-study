import cv2
import numpy as np

curshape = 1
startpos = (0, 0)

def mouse_callback(event, x, y, falgs, userdata):
    global curshape, startpos
    print(event, x, y, falgs, userdata)
    if event & cv2.EVENT_LBUTTONDOWN == cv2.EVENT_LBUTTONDOWN:
        startpos = (x, y)
    elif event & cv2.EVENT_LBUTTONUP == cv2.EVENT_LBUTTONUP:
        endpos = (x, y)
        if curshape == 1:
            cv2.line(img, startpos, endpos, (0, 0, 255))
        elif curshape == 2:
            cv2.rectangle(img, startpos, endpos, (0, 0, 255))
        elif curshape == 3:
            a = (x - startpos[0])
            b = (y - startpos[1])
            r = int((a ** 2 + b ** 2) ** 0.5)

            cv2.circle(img, startpos, r, (0, 0, 255))
        else:
            print("error no shape")

cv2.namedWindow("drawshape", cv2.WINDOW_NORMAL)
cv2.setMouseCallback("drawshape", mouse_callback, "123")

img = np.zeros((480, 640, 3), np.uint8)
while True:
    cv2.imshow("drawshape", img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    elif key == ord('l'):
        curshape = 1
    elif key == ord('r'):
        curshape = 2
    elif key == ord('c'):
        curshape = 3

cv2.destroyAllWindows()
