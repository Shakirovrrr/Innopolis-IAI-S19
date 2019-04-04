import cv2

from common import *

b = Canvas()
g = Canvas()
r = Canvas()
for i in range(48):
	b.add(random_rect())
	g.add(random_rect())
	r.add(random_rect())

canv = cv2.merge((b.render(), g.render(), r.render()))

cv2.imshow('Result', canv)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('glitch.png', canv)
