import numpy as np
from random import shuffle, randrange
from time import time
from numba import jit
from scipy import weave

@jit
def algorithm(cities):

	order =  range( cities.shape[0] )
	shuffle(order)
	length = calcLength(cities, order)
	start = time()

	changed = True
	while changed:

		changed = False

		for a in range(-1, cities.shape[0]):

			for b in range(a+1, cities.shape[0]):

				new_order = order[:a] + order[a:b][::-1] + order[b:]
				new_length = calcLength(cities, new_order)

				if new_length < length:
					length = new_length
					order = new_order
					changed = True

	return order

@jit
def calcLength(cities, path):
	length = 0
	for i in range( len(path) ):
		length += dist( cities[ path[i-1] ], cities[ path[i] ] )

	return length
	
@jit
def dist(c1, c2):
	return np.hypot(c2[0] - c1[0], c2[1] - c1[1])

def calcLength_C(cities, path):

	seq = [1,2,3,4,5,6,10] 
	t = 5
	cities = list(cities)

	code = """
			float length = 0;

			for(int i=0; i < path.length(); i++){
				float c1x = cities[ (int) path[i-1] ][0];
				float c1y = cities[ (int) path[i-1] ][1];
				float c2x = cities[ (int) path[i] ][0];
				float c2y = cities[ (int) path[i] ][1];
				length += sqrt( (c2x - c1x)*(c2x - c1x) - (c2y - c1y)*(c2y - c1y) );
			}

			return_val = length;
		"""
	return weave.inline(code, ['cities', 'path'])