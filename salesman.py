__author__ = "Rohan Pandit" 

from swap3 import algorithm
import numpy as np
from time import time
from Tkinter   import Tk, Canvas
from random import randint

size = 700

def main():
	#loading data
	f = open("tsp0734.txt", 'r').read().splitlines()
	numCities = f.pop(0)
	cities = np.array([ tuple( map( float, coord.split() ) ) for coord in f ])
	
	#calculating path
	start = time()
	path, length = algorithm( cities )
	print(path)

	tottime = time() - start
	print( "Found path of length %s in %s seconds" % ( round(length,2), round(tottime, 2) ) )

	#displaying path
	drawPath( path, cities, length )

################################ DRAWING METHODS #################################

def randColor():
	return "#%06x" % randint(0,0xFFFFFF)

def drawPath(path, cities, length):
	cities = cities[ path ]

	msg = "Length = " + str( round(length, 2) )
	canvas.create_text(size/2, size+50, text = msg, fill = 'black',  font = ('Helvetica', 20, 'bold'))
	
	addToCanvas(cities)
	canvas.update()
	root.mainloop()

def addToCanvas(cities):
	min_x = np.min( cities[:,0] )
	min_y = np.min( cities[:,1] )

	max_x = np.max( cities[:,0] )
	max_y = np.max( cities[:,1] )

	for i in range( len( cities ) ):
		c = cities[i-1]
		c_next = cities[i]

		scaled_x = (c[0] - min_x) / (max_x - min_x) * size + 20
		scaled_y = (c[1] - min_y) / (max_y - min_y) * size + 20

		scaled_x_next = (c_next[0] - min_x) / (max_x - min_x) * size + 20
		scaled_y_next = (c_next[1] - min_y) / (max_y - min_y) * size + 20

		canvas.create_oval( scaled_x - 4 , scaled_y - 4 , scaled_x + 4  , scaled_y + 4 , fill = randColor() , outline = 'black' )
		canvas.create_oval( scaled_x_next - 4 , scaled_y_next - 4 , scaled_x_next + 4  , scaled_y_next + 4 , fill = randColor() , outline = 'black' )

		canvas.create_line( scaled_x, scaled_y , scaled_x_next, scaled_y_next , fill = 'black' )


root = Tk()
canvas = Canvas( root , width = size + 40, height = size + 100 , bg = 'white' )
canvas.pack()

if __name__ == "__main__":
	main()