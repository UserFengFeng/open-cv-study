import cv2
import numpy
import numpy as np
import copy
import time

if __name__ == '__main__':
    # img = cv2.imread("./1.jpg")
    img = numpy.zeros((47104, 7930, 3), np.uint8)
    # 浅拷贝
    img2 = img
    # 深拷贝
    img3 = img.copy()

    # start_c = time.time()
    # count_c = 0
    # while count_c <= 1000:
    #     img3 = img.copy()
    #     count_c += 1
    # print(time.time() - start_c)
    #
    # start_b = time.time()
    # count_b = 0
    # while count_b <= 1000:
    #     img4 = copy.deepcopy(img)
    #     count_b+=1
    #
    # print(time.time() - start_b)

    img[10:100, 10: 100] = [0, 0, 255]

    cv2.imshow("img", img)
    cv2.imshow("img2", img2)
    cv2.imshow("img3", img3)
cv2.waitKey(0)