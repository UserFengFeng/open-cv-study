import numpy as np
import cv2

if __name__ == '__main__':
    # img = cv2.imread("./shou.png")
    # cv2.imshow("img", img)
    # # 将图片矩阵向下偏移50像素
    # shifted_matrix = np.roll(img, 50, axis=0)
    #
    # # 将图片矩阵向右偏移50像素
    # shifted_matrix2 = np.roll(shifted_matrix, 50, axis=1)
    # cv2.imshow("shifted_matrix2", shifted_matrix2)
    # cv2.waitKey(0)
    port_data = {
        "1": [
            16661,
            16662,
            16663,
            16664
        ],
        "2": [
            16665,
            16666,
            16667,
            16668
        ],
        "3": [
            16669,
            16670,
            16671,
            16672
        ],
        "4": [
            16673,
            16674,
            16675,
            16676
        ]
    }
    port_dict = {}
    for _, ports in port_data.items():

        for index, port in enumerate(ports):
            if index not in port_dict:
                port_dict[index] = []
            port_dict[index].append(port)

    for p_id, ports in port_dict.items():
        print(p_id)