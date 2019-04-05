import cv2
import numpy as np

print(cv2.useOptimized())

empty = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread('source.png', cv2.IMREAD_COLOR)
ch_blue, ch_green, ch_red = cv2.split(img)

img = cv2.rectangle(img, (384, 0), (511, 128), (0, 255, 0), -1)
ch_blue = cv2.rectangle(ch_blue, (0, 0), (192, 192), 200, -1)

cv2.imshow('Image - Original', img)
cv2.imshow('Image - Red Channel', ch_red)
cv2.imshow('Image - Green Channel', ch_green)
cv2.imshow('Image - Blue Channel', ch_blue)

lower = cv2.pyrDown(img)
lower = cv2.pyrDown(lower)
lower = cv2.pyrDown(lower)
cv2.imshow('Image - Lowered', lower)

key = cv2.waitKey(0) & 0xFF
if key == 27:  # wait for ESC key to exit
	cv2.destroyAllWindows()
elif key == ord('s'):  # wait for 's' key to save and exit
	cv2.imwrite('result.png', img)
	cv2.destroyAllWindows()
