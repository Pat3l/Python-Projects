import pywhatkit as kit
import cv2

kit.text_to_handwriting("Hey! wassup.", save_to = 'handwritten.png')
img = cv2.imread('handwritten.png')
cv2.imshow('text_to_handwritinn', img)
cv2.waitKey(0)
cv2.destroyAllWindows()