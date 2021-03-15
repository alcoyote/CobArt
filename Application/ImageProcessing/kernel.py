import cv2


class Kernel:
    def Sharpen(self, image, kernel):
        return cv2.filter2D(image, cv2.CV_64F, kernel)

    def MyVariant(self, image, kernel):
        return cv2.filter2D(image, cv2.CV_64F, kernel)
