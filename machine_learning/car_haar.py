import cv2
import numpy as np
from machine_learning.pytesseract import image_to_string
"""
Page segmentation modes:
  0    Orientation and script detection (OSD) only.
  1    Automatic page segmentation with OSD.
  2    Automatic page segmentation, but no OSD, or OCR.
  3    Fully automatic page segmentation, but no OSD. (Default)
  4    Assume a single column of text of variable sizes.
  5    Assume a single uniform block of vertically aligned text.
  6    Assume a single uniform block of text.
  7    Treat the image as a single text line.
  8    Treat the image as a single word.
  9    Treat the image as a single word in a circle.
 10    Treat the image as a single character.
 11    Sparse text. Find as much text as possible in no particular order.
 12    Sparse text with OSD.
 13    Raw line. Treat the image as a single text line,
                        bypassing hacks that are Tesseract-specific.
OCR Engine modes:
  0    Original Tesseract only.
  1    Neural nets LSTM only.
  2    Tesseract + LSTM.
  3    Default, based on what is available.
"""

# 创建haar级联器
haar = cv2.CascadeClassifier("../haarcascades/haarcascade_russian_plate_number.xml")

img = cv2.imread("../chinacar.jpeg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = haar.detectMultiScale(gray, 1.1, 5)
for index, (x, y, w, h) in enumerate(faces):
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)

# 对车牌预处理
# 提取roi
roi = gray[y: y+h, x: x+w]
# 二值化
ret, roi_bin = cv2.threshold(roi, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

car_result = image_to_string(roi_bin, lang="chi_sim+eng", config="--psm 11 --oem 3")
print(car_result)

cv2.imshow("roi_bin", roi_bin)
cv2.imshow("test", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
