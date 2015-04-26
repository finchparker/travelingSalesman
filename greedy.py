import numpy as np

def algorithm(cities):
	best_order = []
	best_length = float('inf')

	for i_start, start in enumerate(cities):
		order = [i_start]
		length = 0

		i_next, next, dist = getClosest(start, cities, order)
		length += dist
		order.append(i_next)

		while len(order) < cities.shape[0]:
			i_next, next, dist = getClosest(next, cities, order)
			length += dist
			order.append(i_next)

		print(order)

		if length < best_length:
			best_length = length
			best_order = order
			
	return best_order

def getClosest(city, cities, visited):
	best_distance = float('inf')

	for i, c in enumerate(cities):

		if i not in visited:
			distance = dist(city, c)

			if distance < best_distance:
				closest_city = c
				i_closest_city = i
				best_distance = distance

	return i_closest_city, closest_city, best_distance

def dist(c1, c2):
	return np.hypot(c2[0] - c1[0], c2[1] - c1[1])