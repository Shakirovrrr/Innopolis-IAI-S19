from cv2 import imread, merge, imwrite

b = imread('blue.png', 0)
g = imread('green.png', 0)
r = imread('red.png', 0)

res = merge((b, g, r))
imwrite('res.png', res)
