import cv2

# 实例化多媒体写入文件
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
# 分辨率大小要跟采集到的分辨率大小要一致
vw = cv2.VideoWriter("./out.mp4", fourcc, 25, (1920, 1080))

# 创建窗口
cv2.namedWindow("video", cv2.WINDOW_NORMAL)
cv2.resizeWindow("video", 500, 500)
# 创建视频帧对象
cap = cv2.VideoCapture("./video.mp4")

while cap.isOpened():
    # 读视频帧
    ret, frame = cap.read()
    vw.write(frame)
    if ret:
        # 显示帧
        cv2.imshow("video", frame)
        # cv2.resizeWindow("video", 500, 500)
        key = cv2.waitKey(40)
        if key & 0xFF == ord("q"):
            break
    else:
        break
        
cap.release()
vw.release()

cv2.destroyAllWindows()