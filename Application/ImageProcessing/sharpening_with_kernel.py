import cv2


class SharpeningWithKernel:
    def Sharpen(self, image, kernel):
        return cv2.filter2D(image, -1, kernel)

    def YourVariant(self, image, kernel):
        return cv2.filter2D(image, -1, kernel)
