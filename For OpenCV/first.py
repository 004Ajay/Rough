import cv2

inp = cv2.imread('boss.jpg')

out = cv2.imshow('AJAY', inp)

cv2.waitKey()

cv2.destroyAllWindows()
