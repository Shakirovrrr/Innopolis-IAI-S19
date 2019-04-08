import cv2

from common import *
from parameters import *


def fitness(canvas: Canvas, ideal: np.ndarray) -> float:
	img = canvas.render()
	if DIFF_SCALE <= 0:
		return image_diff(img, ideal)

	return image_diff(image_lower(img, DIFF_SCALE), image_lower(ideal, DIFF_SCALE))


def cross_over(mom: Canvas, dad: Canvas) -> (Canvas, Canvas):
	from copy import deepcopy
	child1 = deepcopy(mom)
	child2 = deepcopy(dad)

	for i in range(np.random.randint(N_RECTS // 8)):
		ix = np.random.randint(N_RECTS)
		child1.rects[ix], child2.rects[ix] = child2.rects[ix], child1.rects[ix]

	return child1, child2


def mutate(chromosome: Canvas) -> Canvas:
	from copy import deepcopy
	mutant = deepcopy(chromosome)
	for i in range(np.random.randint(N_RECTS // 4)):
		ix = np.random.randint(N_RECTS)
		mutant.rects[ix] = random_rect()

	return mutant


def genetic(src: np.ndarray) -> np.ndarray:
	gen = [Canvas(brightness=CANVAS_BRIGHTNESS) for i in range(8)]
	for i in range(len(gen)):
		for j in range(N_RECTS):
			gen[i] += random_rect()

	fit = 0
	it = 0
	while fit < MIN_FIT:
		gen.sort(key=lambda x: fitness(x, src), reverse=True)
		gen.pop()
		gen.pop()
		# print(gen)

		mom = gen[0]
		dad = gen[1]
		child1, child2 = cross_over(mom, dad)

		family = [mom, dad, child1, child2]
		for i in range(len(family)):
			family[i] = mutate(family[i])

		family.sort(key=lambda x: fitness(x, src), reverse=True)
		gen.append(family[0])
		gen.append(family[1])

		fit = fitness(gen[-2], src)
		it += 1

		if it % 100 == 0:
			print('Iteration {}, fitness={}'.format(it, fit))
			cv2.imwrite('progress.png', gen[0].render())

	return gen[0].render()


def compute_parallel(source: np.ndarray):
	from threading import Thread
	src_b, src_g, src_r = cv2.split(source)
	res = [None, None, None]

	def compute_channel(src: np.ndarray, ix: int):
		res[ix] = genetic(src)

	thread_blue = Thread(target=compute_channel, args=(src_b, 0))
	thread_green = Thread(target=compute_channel, args=(src_g, 1))
	thread_red = Thread(target=compute_channel, args=(src_r, 2))

	thread_blue.start()
	thread_green.start()
	thread_red.start()

	thread_blue.join()
	thread_green.join()
	thread_red.join()

	res_all = cv2.merge((res[0], res[1], res[2]))
	cv2.imwrite('result.png', res_all)


def compute(source: np.ndarray):
	src_b, src_g, src_r = cv2.split(source)

	res_b = genetic(src_b)
	res_g = genetic(src_g)
	res_r = genetic(src_r)

	res_all = cv2.merge((res_b, res_g, res_r))
	cv2.imwrite('result.png', res_all)


source = cv2.imread('source.png', cv2.IMREAD_COLOR)

CANVAS_BRIGHTNESS %= 255

compute_parallel(source)
