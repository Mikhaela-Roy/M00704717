import opc
from time import *
import random

leds = [(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)

def snake():
    led = 0
    add = 40
    body = []
    
    while led < 55:
        for rows in range(6): #lights three led
            leds[led + rows*1] = (200,100,255) #change three led colour
            leds[led + rows*2] = (0,0,0) #background back to default
            leds[add] = (255,0,0)
            if led > 40 and led < 55:
                for column in range(6):
                    #leds[add] = (0,0,0)
                    #leds[led + rows*1] = (200,100,255)
                    leds[add + column*1] = (255,0,0) #orange 
                    #leds[led + rows*1] = (255,255,255) #white
                    leds[add + column*2] = (0,0,0) #
                    #leds[led + rows*2] = (0,0,0)
                    
                leds[led + column] = (255,0,0)
                add += 1
                
        client.put_pixels(leds)
        sleep(0.1)
        led += 1

snake()
