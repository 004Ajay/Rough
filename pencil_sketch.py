import cv2

image = cv2.imread('C:/Users/ASUS/Desktop/anj.jpg')
gray_im = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)
inverted = 255-gray_im
cv2.imshow("img", inverted)
blur = cv2.GaussianBlur(inverted, (21, 21), 0)
invertedBlur = 255-blur
sketch = cv2.divide(gray_im, invertedBlur, scale=240.0)
cv2.imwrite("sketch_im.jpg", sketch)