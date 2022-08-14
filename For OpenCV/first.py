import cv2
import numpy as np

inp = cv2.imread('image.jpg')

out = cv2.imshow('AJAY', inp)

print(inp.shape)