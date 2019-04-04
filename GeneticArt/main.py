import cv2

from common import *

N_RECTS = 32


def fitness(canvas: Canvas, ideal: np.ndarray) -> float:
	img = canvas.render()
	return image_diff(img, ideal)


def cross_over(mom: Canvas, dad: Canvas) -> (Canvas, Canvas):
	from copy import copy
	child1 = copy(mom)
	child2 = copy(dad)

	for i in range(np.random.randint(12)):
		ix = np.random.randint(N_RECTS)
		child1.rects[ix], child2.rects[ix] = child2.rects[ix], child1.rects[ix]

	return child1, child2


def mutate(chromosome: Canvas) -> Canvas:
	from copy import copy
	mutant = copy(chromosome)
	for i in range(np.random.randint(8)):
		ix = np.random.randint(N_RECTS)
		mutant.rects[ix] = random_rect()

	return mutant


def genetic(source: np.ndarray):
	src_b, src_g, src_r = cv2.split(source)

	gen_b = [Canvas() for i in range(6)]
	for i in range(len(gen_b)):
		for j in range(N_RECTS):
			gen_b[i] += random_rect()

	for it in range(1000):
		gen_b.sort(key=lambda x: fitness(x, src_b), reverse=True)

		mom = gen_b[0]
		dad = gen_b[1]
		c1, c2 = cross_over(mom, dad)

		family = [mom, dad, c1, c2]
		for i in range(len(family)):
			family[i] = mutate(family[i])

		family.sort(key=lambda x: fitness(x, src_b), reverse=True)
		gen_b.append(family[0])
		gen_b.append(family[1])

		print('Iteration {}, fitness={}'.format(it, fitness(gen_b[-2], src_b)))

		if it % 10 == 0:
			cv2.imwrite('progress.png', gen_b[-2].render())


source = cv2.imread('source.png', cv2.IMREAD_COLOR)

genetic(source)
