import numpy as np
from numba import jit

from drawing import *


def blank_image(brightness: int) -> np.ndarray:
	return np.ones((512, 512, 3), np.uint8) * brightness


def blank_channel(brightness: int) -> np.ndarray:
	return np.ones((512, 512), np.uint8) * brightness


def random_rect() -> RectMono:
	color = np.random.randint(256)
	beg = Point(np.random.randint(500), np.random.randint(500))
	size = Point(np.random.randint(192), np.random.randint(192))

	rect = RectMono(beg, beg + size, color)

	return rect


def image_lower(img: np.ndarray, scale: int = 1) -> np.ndarray:
	from cv2 import pyrDown
	lower = img
	for i in range(scale):
		lower = pyrDown(lower)

	return lower


@jit(nopython=True, parallel=True)
def image_diff(img1: np.ndarray, img2: np.ndarray) -> float:
	diff = np.abs(img1.astype(np.int16) - img2.astype(np.int16))
	fit = np.sum(diff) / (diff.shape[0] * diff.shape[1] * 255)
	return fit * 100
