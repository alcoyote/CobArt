import cv2


def FindContours(image, thresh, area):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh_image = cv2.threshold(gray_image, thresh, 255, 0)
    contours, hierarchy = cv2.findContours(thresh_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_image = cv2.drawContours(image, contours, -1, (0, 0, 255), 2)
    clean_contours = []
    for i in range(len(contours)):
        if len(contours[i]) > 1 and cv2.contourArea(contours[i]) > area:
            clean_contours.append(contours[i])
    clean_contours = sorted(clean_contours, key=cv2.contourArea, reverse=True)
    clean_contours_image = cv2.drawContours(contours_image, clean_contours, -1, (0, 255, 0), 2)
    return contours, clean_contours, clean_contours_image
