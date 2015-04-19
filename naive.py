import numpy as np

def algorithm(cities):
	start = cities[0]
	cities = np.array(cities)
	print(cities)
	markov = np.hypot( cities[:,0] - np.roll( cities, 1 )[:,0], cities[:,1] - cities[1:-1, 1] )

	print(markov)