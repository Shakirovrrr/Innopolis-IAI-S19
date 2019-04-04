import numpy as np
from numba import jit

from drawing import *


def blank_image() -> np.ndarray:
	return np.ones((512, 512, 3), np.uint8) * 255


def blank_channel() -> np.ndarray:
	return np.ones((512, 512, 1), np.uint8) * 255


def random_rect() -> RectMono:
	color = np.random.randint(256)
	beg = Point(np.random.randint(500), np.random.randint(500))
	size = Point(np.random.randint(192), np.random.randint(192))

	rect = RectMono(beg, beg + size, color)

	return rect


@jit(nopython=True)
def image_diff(img1: np.ndarray, img2: np.ndarray) -> float:
	diff = np.abs(img1 - img2)
	fit = np.mean(diff) / 255 * 100
	return 100 - fit
