import numpy as np
import cv2

def sketch(img):
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgGrayBlur = cv2.GaussianBlur(imgGray,(5,5),0)
    canny = cv2.Canny(imgGrayBlur,10,70)
    ret ,mask = cv2.threshold(canny,70,255,cv2.THRESH_BINARY_INV)
    return mask



cap = cv2.VideoCapture(0)

while True:
    ret ,frame = cap.read()
    cv2.imshow('Live Sketch', sketch(frame))
    if cv2.waitKey(1) == 13:
        break
    
cap.release()
cv2.destroyAllWindows()

