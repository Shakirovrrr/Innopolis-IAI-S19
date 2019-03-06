from math import sqrt, inf

a_map = []

with open('input.txt') as in_file:
	for i in in_file.readlines():
		a_map.append(i.split())

start, end = (0, 0), (3, 6)
open_nodes = [start]
closed_nodes = []
heuristic = lambda x, w: sqrt((x[0] - start[0]) ** 2 + (x[1] - start[1]) ** 2) * w


def best_step(current: (int, int)) -> (int, int):
	adjacent = [
		(current[0] - 1, current[1] - 1),
		(current[0] - 1, current[1]),
		(current[0] - 1, current[1] + 1),
		(current[0], current[1] - 1),
		(current[0], current[1] + 1),
		(current[0] + 1, current[1] - 1),
		(current[0] + 1, current[1]),
		(current[0] + 1, current[1] + 1)
	]

	h_vals = []
	h_min = inf
	for i in range(len(adjacent)):
		try:
			step = adjacent[i]

		except IndexError:
			continue


while len(open_nodes) > 0:
	pass