class Point:
	def __init__(self, x: int, y: int):
		self.x: int = x
		self.y: int = y

	def __add__(self, other):
		x_new = self.x + other.x
		y_new = self.y + other.y

		return Point(x_new, y_new)


class RectMono:
	from numpy import uint8, ndarray

	def __init__(self, begin: Point, end: Point, color: uint8):
		self.begin: Point = begin
		self.end: Point = end
		self.color: type(color) = color

	def draw(self, img: ndarray) -> ndarray:
		from cv2 import rectangle
		beg = self.begin.x, self.begin.y
		end = self.end.x, self.end.y
		return rectangle(img, beg, end, self.color, -1)


class Canvas:
	from numpy import ndarray

	def __init__(self, brightness: int = 255):
		from typing import List
		self.rects: List[RectMono] = []
		self.brightness = brightness

	def add(self, rect: RectMono):
		self.rects.append(rect)

	def __iadd__(self, other: RectMono):
		self.rects.append(other)
		return self

	def render(self) -> ndarray:
		from common import blank_channel
		canvas = blank_channel(self.brightness)
		for rect in self.rects:
			canvas = rect.draw(canvas)

		return canvas
