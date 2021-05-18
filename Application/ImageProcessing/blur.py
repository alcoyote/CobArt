import cv2


class Blur:
    def Average(self, image, ksize):
        return cv2.blur(image, (ksize, ksize))

    def Gaussian(self, image, ksize):
        return cv2.GaussianBlur(image, (ksize, ksize), sigmaX=0, sigmaY=0)

    def Median(self, image, ksize):
        return cv2.medianBlur(image, ksize)

    def Bilateral(self, image, fsize, sigmaColor, sigmaSpace):
        return cv2.bilateralFilter(image, d=fsize, sigmaColor=sigmaColor, sigmaSpace=sigmaSpace)
