import numpy as np
import cv2
import time

if __name__ == '__main__':
    img = np.zeros((100, 200, 3), np.uint8)
    print(img[10, 10])
    count = 0
    while count < 50:
        # 通道蓝
        img[count, 100, 0] = 255

        # 通道绿
        # img[count, 100, 1] = 255
        # 通道红
        # img[count, 100, 2] = 255
        # 白色
        # img[count, 100] = [255, 255, 255]


        count+=1

    cv2.imshow("img", img)
    key = cv2.waitKey(0)
    if key & 0xFF == ord("q"):
        cv2.destroyAllWindows()
