import cv2
import numpy as np

# 创建haar级联器
haar = cv2.CascadeClassifier("../haarcascades/haarcascade_frontalface_default.xml")
eye = cv2.CascadeClassifier("../haarcascades/haarcascade_eye.xml")
mouth = cv2.CascadeClassifier("../haarcascades/haarcascade_mcs_mouth.xml")
nose = cv2.CascadeClassifier("../haarcascades/haarcascade_mcs_nose.xml")

# 导入人脸识别图片并将其灰度化
img = cv2.imread("../p3.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 人脸识别
# [[x,y, w,h]]
faces = haar.detectMultiScale(gray, 1.1, 5)
for index, (x, y, w, h) in enumerate(faces):
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)

    face_img = img[y: y+h, x: x+w]
    face_img_gray = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)

    eyes = eye.detectMultiScale(face_img_gray, 1.1, 5)
    for (x, y, w, h) in eyes:
        cv2.rectangle(face_img, (x, y), (x + w, y + h), (0, 255, 255), 3)
    cv2.imshow(str(index), face_img)


# mouths = mouth.detectMultiScale(gray, 1.1, 5)
# for (x, y, w, h) in mouths:
#     cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 3)
#
# noses = nose.detectMultiScale(gray, 1.1, 5)
# for (x, y, w, h) in noses:
#     cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 3)

cv2.imshow("test", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
