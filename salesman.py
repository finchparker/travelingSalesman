__author__ = "Rohan Pandit"

from sorty import algorithm
import numpy as np
from numpy import hypot

def main():
	#loading data
	f = open("tsp0038.txt", 'r').read().splitlines()
	numCities = f.pop(0)
	cities = np.array([ tuple( map( float, coord.split() ) ) for coord in f ])
	#calculating path
	path = algorithm( cities )
	print(path)

	length = calcLength( cities, path )
	print( "Found path of length %s" % round(length,2) )

	#displaying path
	drawPath( path, cities )

def dist(c1, c2):
	return hypot(c2[0] - c1[0], c2[1] - c1[1])

def calcLength(cities, path):
	length = 0
	for i in range( len(path) ):
		length += dist( cities[ path[i-1] ], cities[ path[i] ] )

	return length

################################ DRAWING METHODS #################################
def drawPath(path, cities):
	cities = cities[ path ]
	statistics = dataStatistics(cities)
	displayPathOnScreen(cities, statistics)

def plot(city): # Plots 5x5 "points" on video screen
    x = city[0]+5; y = city[1]+5 # The +5 is to push away from the side bars.
    #if city[0] == -1:
    #    kolor = 'WHITE'
    kolor = 'YELLOW'
    canvas.create_rectangle(x-2, y-2, x+2, y+2, width = 1, fill = kolor)

def line(city1, city2, kolor = 'RED'):
    canvas.create_line(city1[0]+5, city1[1]+5, city2[0]+5, city2[1]+5, width = 1, fill = kolor)

def script(x, y, msg = '', kolor = 'WHITE'):
    canvas.create_text(x, y, text = msg, fill = kolor,  font = ('Helvetica', 10, 'bold'))

def pathLength(city):
    totalPath = 0
    for n in range(1, len(city)):
        totalPath += dist( city[n-1], city[n] )
    totalPath += dist( city[n], city[0] )
    return int(totalPath)

def dataStatistics(cities):
	xValues = []
	yValues = []
	size = len(cities)
	for x, y in cities:
		xValues.append( x )
		yValues.append( y )

	minX = min(xValues)
	maxX = max(xValues)
	minY = min(yValues)
	maxY = max(yValues)

	assert (minX >= 0 or maxX >= 0 or minY >= 0 or maxY >= 0)

	meanX = sum(xValues)/size
	meanY = sum(yValues)/size
	medianX = cities[len(cities)//2][0]
	medianY = cities[len(cities)//2][1]

#---Derive the line of best fit: y = mx+b
	xyDiff   = 0
	xDiffSqr = 0
	for (x,y) in cities:
		xyDiff  += (meanX - x)*(meanY - y)
		xDiffSqr+= (meanX - x)**2

	m = xyDiff/xDiffSqr
	b = meanY - m*meanX

	return minX, maxX, minY, maxY, meanX, meanY, medianX, medianY, size, m, b

def normalizeCityDataToFitScreen(cities, statistics):
	""" Coordinates are all assumed to be non-negative."""
	(minX, maxX, minY, maxY, meanX, meanY, medianX, medianY, size, m, b) = statistics
	newCity = []

#---Step 1a. Shift city points to the x- and y-axes.
	for (x,y) in cities:
		newCity.append ( (x-minX, y-minY))

#---Step 1b. Shift line-of-best-fit to the x- and y-axes.
	(x0,y0) = (maxX-minX, m*maxX+b - minY) # = x-intercept of line-of-best-fit.
	(x1,y1) = (minX-minX, m*minX+b - minY) # = y-intercept of line-of-best-fit.


#---Step 1c. Shift max-values to x- and y-axes.
	maxX = maxX-minX
	maxY = maxY-minY

#---Step 2a. # Re-scale city points to fit the screen.
	cityNorm = []
	for (x, y) in newCity:
		cityNorm.append ((x*SCREEN_WIDTH/maxX, y*SCREEN_HEIGHT/maxY))

#---Step 2b. # Re-scale the x-axis and y-axis intercepts for the line-of-best-fit.
	(x0,y0) = x0/maxX*SCREEN_WIDTH, y0/maxY*SCREEN_HEIGHT # a point on the x-axis
	(x1,y1) = x1/maxX*SCREEN_WIDTH, y1/maxY*SCREEN_HEIGHT # a point on the y-axis

	return cityNorm, (x1,y1,x0,y0)

def displayPathOnScreen(cities, statistics):
#=---Normalize data
	(minX, maxX, minY, maxY, meanX, meanY, medianX, medianY, size, m, b) = statistics
	canvas.delete('all')
	cityNorm, (p,q,r,s) = normalizeCityDataToFitScreen(cities[:], statistics)

#---Plot points and lines
	cityNorm.append(cityNorm[0])
	plot(cityNorm[0])
	for n in range(1, len(cityNorm)):
		plot(cityNorm[n])
		line(cityNorm[n], cityNorm[n-1])
	script(650,  20, 'path length = ' + str(pathLength(cities)))
	canvas.create_rectangle(530,10, 770, 30, width = 1, outline = 'WHITE')
	canvas.update()
	root.mainloop() # Required for graphics.

def setUpCanvas(root): # These are the REQUIRED magic lines to enter graphics mode.
	root.title("THE TRAVELING SALESMAN PROBLEM by Rohan.")
	canvas = Canvas(root, width  = root.winfo_screenwidth(), height = root.winfo_screenheight(), bg = 'black')
	canvas.pack(expand = YES, fill = BOTH)
	return canvas

from tkinter   import Tk, Canvas, YES, BOTH
from operator  import itemgetter
from itertools import permutations
from copy import deepcopy
from random    import shuffle
from time      import clock
root           = Tk()
canvas         = setUpCanvas(root)
START_TIME     = clock()
SCREEN_WIDTH   = root.winfo_screenwidth() //5*5 - 15 # adjusted to exclude task bars on my PC.
SCREEN_HEIGHT  = root.winfo_screenheight()//5*5 - 90 # adjusted to exclude task bars on my PC.

if __name__ == "__main__":
	main()