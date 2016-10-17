from itertools import permutations
from math import hypot

def algorithm(cities):
	min_length = calcLength( cities, range( len( cities ) ) )
	min_path = range( len( cities ) )

	for path in permutations( range( len( cities ) ) ):
		length = calc_length(cities, path)
		if length < min_length:
			min_length = length
			min_path = path

	return min_path

def dist_squared(c1, c2):
	t1 = c2[0] - c1[0]
	t2 = c2[1] - c1[1]

	return t1**2 + t2**2

def calc_length(cities, path):
	length = 0
	for i in range( len(path) ):
		length += dist_squared( cities[ path[i-1] ], cities[ path[i] ] )

	return length
