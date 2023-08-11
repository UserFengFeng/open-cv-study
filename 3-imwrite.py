import cv2

cv2.namedWindow("img", cv2.WINDOW_NORMAL)
img = cv2.imread("./1.jpg")

cv2.imshow('img', img)
while True:
    key = cv2.waitKey(0)
    if key & 0xFF == ord("q"):
        exit()
    elif key & 0xFF == ord("s"):
        try:
            print(key, '---2-')
            cv2.imwrite("./xxx/xx.jpg", img)
        except Exception as e:
            print(e)
    else:
        print("other")
cv2.destroyAllWindows()

