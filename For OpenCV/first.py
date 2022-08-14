import cv2
import numpy as np

inp = cv2.imread('img.jpg')

out = cv2.imshow('AJAY', inp)

cv2.waitKey()

print(f"Height: {inp.shape[0]}\nWidth: {inp.shape[1]}\nChannels: {inp.shape[2]}\n") # Image informations

cv2.destroyAllWindows()