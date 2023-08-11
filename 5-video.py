import cv2

# 创建窗口
cv2.namedWindow("video", cv2.WINDOW_NORMAL)
cv2.resizeWindow("video", 500, 500)
# 创建视频帧对象
cap = cv2.VideoCapture("./video.mp4")
while True:
    # 读视频帧
    ret, frame = cap.read()
    if ret:
        # 显示帧
        cv2.imshow("video", frame)
        key = cv2.waitKey(40)
        if key & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()