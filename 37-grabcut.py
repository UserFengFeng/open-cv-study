import cv2
import numpy as np


class App:
    startx = 0
    starty = 0
    flag_left = False
    rect = (0, 0, 0, 0)
    img = None
    img2 = None

    def onmouse(self, event, x, y, flag, param):
        print(x, y, event)
        if event == cv2.EVENT_LBUTTONDOWN:
            self.flag_left = True
            print("down")
            self.startx = x
            self.starty = y
        elif event == cv2.EVENT_LBUTTONUP:
            print("up")
            self.flag_left = False
            cv2.rectangle(self.img, (self.startx, self.starty), (x, y), (0, 0, 255), 3)
            self.rect = (min(self.startx, x), min(self.starty, y), abs(self.startx - x), abs(self.starty - y))
        elif event == cv2.EVENT_MOUSEMOVE:
            print("mousemove")
            if self.flag_left:
                self.img = self.img2.copy()
                cv2.rectangle(self.img, (self.startx, self.starty), (x, y), (255, 0, 255), 3)

    def run(self):
        print("run....")
        cv2.namedWindow("test")
        cv2.setMouseCallback("test", self.onmouse)
        self.img = cv2.imread("./p.jpg")
        self.img2 = self.img.copy()
        self.mask = np.zeros(self.img.shape[:2], dtype=np.uint8)
        self.output = np.zeros(self.img.shape[:2], np.uint8)

        while True:
            cv2.imshow("test", self.img)
            k = cv2.waitKey(100)
            if k == 27:
                break
            elif k == ord('g'):
                bgdmodel = np.zeros((1, 65), np.float64)
                fgdmodel = np.zeros((1, 65), np.float64)
                cv2.grabCut(self.img2, self.mask, self.rect, bgdmodel, fgdmodel, 1, cv2.GC_INIT_WITH_RECT)
                mask2 = np.where((self.mask == 1) | (self.mask == 3), 255, 0).astype('uint8')
                self.output = cv2.bitwise_and(self.img2, self.img2, mask=mask2)
                cv2.imshow("output", self.output)
        cv2.destroyAllWindows()


App().run()
