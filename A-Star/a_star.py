from math import sqrt, inf

a_map = []


def dist(pos1: (int, int), pos2: (int, int)) -> float:
	xpos1, ypos1 = pos1
	xpos2, ypos2 = pos2
	return sqrt((xpos2 - xpos1) ** 2 + (ypos2 - ypos1) ** 2)


def heur(pos1: (int, int), pos2: (int, int)) -> int:
	xpos1, ypos1 = pos1
	xpos2, ypos2 = pos2
	return abs(xpos2 - xpos1) + abs(ypos2 - ypos1)


def cost(pos1, pos2):
	return dist(pos1, pos2) + heur(pos1, pos2)


def get_adjacent(pos: (int, int)):
	xpos, ypos = pos
	move_queue = []
	if ypos < len(a_map) - 1:
		move_queue.append((xpos, ypos + 1))
	if xpos > 0:
		move_queue.append((xpos - 1, ypos))
	if xpos < len(a_map) - 1:
		move_queue.append((xpos + 1, ypos))
	if ypos > 0:
		move_queue.append((xpos, ypos - 1))

	return move_queue


with open('input.txt') as in_file:
	for i in in_file.readlines():
		a_map.append(i.split())

start, end = (0, 0), (3, 6)
open_nodes = [start]
closed_nodes = []


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
