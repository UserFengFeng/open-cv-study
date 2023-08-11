import cv2
import numpy as np

bgsubmog = cv2.createBackgroundSubtractorMOG2(history=200, varThreshold=30)
# kernel
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (6, 6))

minw = 90
minh = 90

line_h = 480
# 有效范围
offset = 2
carno = 0
cars = []


def center(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx, cy


if __name__ == '__main__':
    video = cv2.VideoCapture("./video.mp4")

    while True:
        ret, frame = video.read()
        if ret:
            # 灰度
            cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # 去噪 高斯
            blur = cv2.GaussianBlur(frame, (3, 3), 5)

            # 去背景
            mask = bgsubmog.apply(blur)

            # 开运算
            erode = cv2.erode(mask, kernel)
            # 去噪后还原
            dilate = cv2.dilate(erode, kernel, iterations=4)
            cv2.imshow("dil3ate", dilate)

            # 闭运算 去掉物体内部的小块
            close = cv2.morphologyEx(dilate, cv2.MORPH_CLOSE, kernel)
            close = cv2.morphologyEx(close, cv2.MORPH_CLOSE, kernel)

            cnts, h = cv2.findContours(close, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            #  有效线
            cv2.line(frame, (10, line_h), (1200, line_h), (255, 255, 0), 3)

            for (i, c) in enumerate(cnts):
                x, y, w, h = cv2.boundingRect(c)
                is_valid = (w >= minw) and (h >= minh)
                if not is_valid:
                    continue
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

                # 求中心点
                center_point = center(x, y, w, h)
                cars.append(center_point)
                cv2.circle(frame, center_point, 2, (0, 0, 255), -1)

                for (x, y) in cars:
                    # 不能识别车辆的唯一性 需要深度学习
                    if (y > line_h - offset) and (y < line_h + offset):
                        carno += 1
                        cars.remove((x, y))
            cv2.putText(frame, f"cars count:{str(carno)}", (450, 86), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)
            cv2.imshow("video", frame)
            cv2.imshow("dilate", close)

        key = cv2.waitKey(1)

        if key == 27:
            break

    video.release()
    cv2.destroyAllWindows()
