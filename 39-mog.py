import cv2
import numpy as np

video = cv2.VideoCapture("./person.mp4")

# mog去背景（history 默认500， detectshadows 是否检测阴影） 缺点 会产生很多噪点
# mog = cv2.createBackgroundSubtractorMOG2()

# gmg去背景 （初始化帧数）
# cv2.bgsegm.createBackgroundSubtractorGMG()
mog = cv2.createBackgroundSubtractorKNN()

while True:
    ret, frame = video.read()
    fgmask = mog.apply(frame)
    cv2.imshow("img", fgmask)

    k = cv2.waitKey(10)
    if k == 27:
        break

video.release()
cv2.destroyAllWindows()