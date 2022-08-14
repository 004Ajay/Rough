import cv2
import numpy as np

inp = cv2.imread('img.jpg', 1) # opening image, num 1 indicates 'Color Image', 0 means 'B&W Image'

out = cv2.imshow('Test Image', inp) # showing image with title as 1st argument

cv2.waitKey() # wait time in ms, until a key-press detected

print("\nshape: ", inp.shape)

try:
    print(f"Height: {inp.shape[0]}\nWidth: {inp.shape[1]}\nChannels: {inp.shape[2]}\n") # Image informations
except IndexError:
    print("\nIndex out of range error for displaying image information.\n")

cv2.destroyAllWindows()