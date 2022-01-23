import opc
from time import *
import random

leds = [(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)

def eye():
    led = 0
    add = 0

    while led >= 0:
        for rows in range(3): #lights three led
            for column in range(rows):
                leds[led + column] = (200,100,255)
                leds[add + led + column + rows] = (255,0,0)
                
            add *= 5
            led += 10
            
                     
        client.put_pixels(leds)
        sleep(0.1)
        led -= 1

eye()
