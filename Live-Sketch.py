import numpy as np
import cv2

def sketch(img):
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgGrayBlur = cv2.GaussianBlur(imgGray,(5,5),0)
    canny = cv2.Canny(imgGrayBlur,10,70)
    ret ,mask = cv2.threshold(canny,70,255,cv2.THRESH_BINARY_INV)
    return ret

image = cv2.imread('images/input.jpg')
mask = sketch(image)
cv2.imshow('Original', mask)
cv2.waitKey()
cv2.destroyAllWindows()

