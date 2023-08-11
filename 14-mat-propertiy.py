import cv2
import numpy as np

if __name__ == '__main__':
    img = cv2.imread("./1.jpg")
    h, w, c = img.shape
    # 占用空间 h * w * chann
    size = img.size
    # 图像中每个元素的位深
    print(img.dtype)