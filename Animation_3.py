import opc
from time import *
import random
import numpy as np
import matplotlib.pyplot as plt

leds = [(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)

##theta = np.linspace(0, 6, 1000)
##
##x = 16*(np.sin(theta)**3)
##y = 13*np.cos(theta) - 5*np.cos(2*theta) - 2*np.cos(3*theta) - np.cos(4*theta)
##
##plt.scatter(x, y, c=y, cmap = plt.cm.Purples, s = 70)
##plt.plot(x,y)
##plt.show()

##def heart():
##    
##    
##    for i in range(plot_x):
##        leds[i] = (255,255,255)
##        client.put_pixels(leds)
##        sleep(0.1)
##        for t in range(plot_y):
##            leds[t] = (255,255,255)
##            client.put_pixels(leds)
##            sleep(0.1)
##
##        
##    plt.scatter(x, y, c=y, cmap = plt.cm.Purples, s = 70)
##    plt.plot(x,y)
##    plt.show()

    
