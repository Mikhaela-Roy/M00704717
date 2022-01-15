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

    while led < 57:
        for rows in range(4): #lights three led
            leds[led + rows*1] = (200,100,255) #change three led colour
            leds[led + rows*2] = (0,0,0) #background back to default
            leds[add] = (255,0,0)
        if led > 40 and led < 60:
            for column in range(4):
                #leds[led + rows*2] = (200,100,50)
                leds[add + column*1] = (255,0,0)
                #leds[add + column*4] = (255,255,0)
                leds[add + column*5] = (0,0,0)
                
            add += 1
            leds[led + rows] = (255,0,0)
                
                
                
        client.put_pixels(leds)
        sleep(0.1)
        led += 1

snake()
