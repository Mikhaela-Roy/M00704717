import opc
from time import *
import random
from matplotlib import pyplot as plt
import numpy as ass
import pylab
import scipy

x = ass.linspace(2,6,1000)
y1 = ass.sqrt(1+(abs(x)+1)**2)
y2 = 3*ass.sqrt(1+(abs(x)/2)**0.5)
pylab.fill_between(x, y1, color='red')
pylab.fill_between(x, y2, color='red')
#pylab.xlim([-2.5, 2.5])
#pylab.text(0, -0.4, 'Stack Overflow', fontsize=24, fontweight='bold#color='white', horizontalalignment='center')
pylab.savefig('heart.png')

##leds = [(0,0,0)]*360
##
##client = opc.Client('localhost:7890')
##client.put_pixels(leds)
##
###Creating equally spaced 100 data in range 0 to 2*pi
##theta = ass.linspace(0,2*ass.pi,100) 
##
###Generating x and y data
##x = 6*(ass.sin(theta)**2) 
##y = 3 * ass.cos(theta) - 5* ass.cos(2*theta) - 2 * ass.cos(3*theta) - ass.cos(4*theta)
##
###Plotting
##plt.plot(x,y)
##plt.title('Heart Shape')
##plt.show()
