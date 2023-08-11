import cv2
import numpy as np

img = cv2.imread("./ori.png")
paint_img = cv2.imread("./org_paint.png", 0)
# 图像修复
result_img = cv2.inpaint(img, paint_img, 5, cv2.INPAINT_TELEA)
cv2.imshow("test", result_img)
cv2.waitKey(0)
cv2.destroyAllWindows()