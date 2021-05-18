import cv2
import numpy as np


class Morphology:
    def Dilate(self, image, ksize, iterations):
        kernel = np.ones((ksize, ksize), np.uint8)
        return cv2.dilate(image, kernel, iterations=iterations)

    def Erode(self, image, ksize, iterations):
        kernel = np.ones((ksize, ksize), np.uint8)
        return cv2.erode(image, kernel, iterations=iterations)

    def Gradient(self, image, ksize):
        kernel = np.ones((ksize, ksize), np.uint8)
        return cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)

    def Close(self, image, ksize):
        kernel = np.ones((ksize, ksize), np.uint8)
        return cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

    def Open(self, image, ksize):
        kernel = np.ones((ksize, ksize), np.uint8)
        return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
