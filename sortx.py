import numpy as np

def algorithm(cities):
	path = np.argsort(cities, axis=0)
	return path[:,0]