import opc
from time import *
import random

leds = [(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)

def reverse():
    led = 0
    
    while led < 60: #scroll all rows at the same time
        for rows in range(2): #access the first two rows
            leds[led-30 + rows*60] = (0,0,0) #row 1- 0-60
            leds[29-led +rows*60] = (0,0,0) #leds off on all two rows
        for rows in range(2,4): #access the middle two rows
            leds[led-30 + rows*60] = (0,0,0) #leds off on all two rows
            leds[29-led +rows*60] = (0,0,0)
        for rows in range(4,6): #access the last two rows
            leds[led-30 + rows*60] = (0,0,0)
            leds[29-led +rows*60] = (0,0,0) #leds off on all two rows
         
        led -= 1 #decrement led to remove backwards
        client.put_pixels(leds)#makes all the leds off at the same time
        sleep(0.1)

        if led == -60: #-60 as led strats from 0
            break
        elif led == -31: 
            break
        else:
            continue
        
def build():
    led = 0
    
    while led < 60: #scroll all rows at the same time
        for rows in range(2): #access the first two rows
            leds[led + rows*60] = (led+100,led+0,0) #row 1- 0-60
        for rows in range(2,4): #access the middle two rows
            leds[59-led + rows*60] = (led+100,led+0,0) #increment the red & green colour
        for rows in range(4,6): #access the last two rows
            leds[led + rows*60] = (led+100,led+0,0)
         
        led += 1 #increement the led to come together
        client.put_pixels(leds) #makes all the leds off at the same time
        sleep(0.1)
        
    reverse() #call the reverse function to set the simulator off
