import numpy as np
from random import shuffle, randrange
from time import time
from numba import jit
from scipy import weave

N_ITER = 10

@jit
def algorithm(cities):
	best_order = []
	best_length = float('inf')

	for i in range(N_ITER):
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
					new_length = calc_length(cities, new_order)

					if new_length < length:
						length = new_length
						order = new_order
						changed = True

		if length < best_length:
			best_length = length
			best_order = order

	return best_order, best_length

@jit
def calc_length(cities, path):
	length = 0
	for i in range( len(path) ):
		length += dist_squared( cities[ path[i-1] ], cities[ path[i] ] )

	return length

@jit
def dist_squared(c1, c2):
	t1 = c2[0] - c1[0]
	t2 = c2[1] - c1[1]

	return t1**2 + t2**2

def calc_length_C(cities, path):

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
				length += (c2x - c1x)*(c2x - c1x) - (c2y - c1y)*(c2y - c1y);
			}

			return_val = length;
		"""
	return weave.inline(code, ['cities', 'path'])