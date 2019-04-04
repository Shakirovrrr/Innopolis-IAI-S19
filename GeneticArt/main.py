import cv2

from common import *


def fitness(img: np.ndarray, ideal: np.ndarray) -> int:
	diff = np.abs(img - ideal)
	fit = np.mean(diff) / 255 * 100
	return int(fit)


def genetic(source: np.ndarray):
	src_b, src_g, src_r = cv2.split(source)

	gen_b = [blank_channel() for i in range(20)]
	gen_b.sort(key=lambda x: fitness(x, src_b))

	for i in gen_b:
		i = random_rect().draw(i)


source = cv2.imread('source.png', cv2.IMREAD_COLOR)
genetic(source)
