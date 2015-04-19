from itertools import permutations
from math import hypot

def algorithm(cities):
	min_length = calcLength( cities, range( len( cities ) ) )
	min_path = range( len( cities ) )

	for path in permutations( range( len( cities ) ) ):
		length = calcLength(cities, path)
		if length < min_length:
			min_length = length
			min_path = path

	return min_path

def dist(c1, c2):
	return hypot(c2[0] - c1[0], c2[1] - c1[1])

def calcLength(cities, path):
	length = 0
	for i in range( len(path) ):
		length += dist( cities[ path[i-1] ], cities[ path[i] ] )

	return length
