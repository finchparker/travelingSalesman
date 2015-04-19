from random import shuffle

def algorithm(cities):
	path = list( range( len( cities ) ) )
	shuffle( path )
	return path

def dist(c1, c2):
	return hypot(c2[0] - c1[0], c2[1] - c1[1])

def calcLength(cities, path):
	length = 0
	for i in range( len(path) ):
		length += dist( cities[ path[i-1] ], cities[ path[i] ] )

	return length