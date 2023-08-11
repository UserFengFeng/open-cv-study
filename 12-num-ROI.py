import numpy as np
import cv2

# 获取子矩阵
if __name__ == '__main__':
    img = np.zeros((800, 800, 3), np.uint8)
    # 取圖中的一塊區域進行改變
    roi = img[100: 200, 100: 200]
    roi[:] = [0, 0, 255]
    roi[5: 20, 1:20] = [0, 255, 0]

    cv2.imshow("img", roi)
    key = cv2.waitKey(0)
    if key & 0xFF == ord("q"):
        cv2.destroyAllWindows()
