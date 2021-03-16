import cv2


class EdgeDetection:
    def Canny(self, image, thresh1, thresh2):
        return cv2.Canny(image, thresh1, thresh2)

    def Laplacian(self, image):
        # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return cv2.Laplacian(image, cv2.CV_64F)

    def SobelX(self, image, ksize):
        # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=ksize)

    def SobelY(self, image, ksize):
        # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=ksize)

    def Sobel(self, image, ksize):
        # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gradient_x = self.SobelX(image.copy(), ksize)
        gradient_y = self.ScharrY(image.copy(), ksize)
        gradient_x = cv2.convertScaleAbs(gradient_x)
        gradient_y = cv2.convertScaleAbs(gradient_y)
        return cv2.addWeighted(gradient_x, 0.5, gradient_y, 0.5, 0)

    def ScharrX(self, image):
        # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return cv2.Scharr(image, cv2.CV_64F, 1, 0)

    def ScharrY(self, image):
        # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return cv2.Scharr(image, cv2.CV_64F, 0, 1)

    def SimpleThresholding(self, image, thresh):
        # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(image, thresh, 255, cv2.THRESH_BINARY)
        return thresh

    def AdaptiveThresholding(self, image, area, const):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, area, const)
