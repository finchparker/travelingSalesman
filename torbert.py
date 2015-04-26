#
# Torbert, 21 April 2015
#
from random  import random
from Tkinter import Tk,Canvas
#
n = 600
r = 3
#
x = [ 0.5 , 0.9 , 0.1 ]
y = [ 0.1 , 0.9 , 0.9 ]
#
tkid = []
#
############################################################
#
def ib( x , y ) :
   #
   return 0.0 <= x <= 1.0 and 0.0 <= y <= 1.0
   #
#
def init() :
   #
   j = 0
   #
   while j < 3 :
      #
      x[ j ] = random()
      y[ j ] = random()
      #
      xp = x[ j ] # value is from 0.0 to 1.0
      yp = y[ j ]
      #
      xp *= n   # scale to window dimensions
      yp *= n
      #
      id = cnvs . create_oval( xp - r , yp - r , xp + r , yp + r , fill = 'black' , outline = 'black' )
      #
      tkid . append( id )
      #
      j += 1
      #
   #
   #
   #
   oldx = x[ -1 ]
   oldy = y[ -1 ]
   #
   j = 0
   #
   while j < 3 :
      #
      xp = x[ j ]
      yp = y[ j ]
      #
      id = cnvs . create_line( oldx * n , oldy * n , xp * n , yp * n , fill = 'black' )
      #
      tkid . append( id )
      #
      oldx = xp
      oldy = yp
      #
      j += 1
      #
   #
#
def walk() :
   #
   j = 0
   #
   while j < 3 :
      #
      x[ j ] = random()
      y[ j ] = random()
      #
      xp = x[ j ] # value is from 0.0 to 1.0
      yp = y[ j ]
      #
      xp *= n   # scale to window dimensions
      yp *= n
      #
      id = tkid[ j ]
      #
      cnvs . coords( id , xp - r , yp - r , xp + r , yp + r )
      #
      j += 1
      #
   #
   oldx = x[ -1 ]
   oldy = y[ -1 ]
   #
   j = 0
   #
   while j < 3 :
      #
      xp = x[ j ]
      yp = y[ j ]
      #
      id = tkid[ 3 + j ]
      #
      cnvs . coords( id , oldx * n , oldy * n , xp * n , yp * n )
      #
      oldx = xp
      oldy = yp
      #
      j += 1
      #
   #
#
def tick() :
   #
   walk()
   #
   cnvs . after( 500 , tick )
   #
#
############################################################
#
root = Tk()
cnvs = Canvas( root , width = n , height = n , bg = 'white' )
cnvs . pack()
#
init()
#
cnvs . after( 1 , tick )
root . mainloop()
#
# end of file
#