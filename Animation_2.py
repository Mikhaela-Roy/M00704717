import opc
from time import *
import random

leds = [(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)

rand_colour = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

##row1 = [25, 28, 29, 30, 31, 34]
##row2 = [83, 87, 88, 89, 90, 91, 92, 97]
##row3 = [141, 147,148, 149, 150, 151, 152, 162]
##row4 = [197, 207,208, 209, 210, 211, 212, 226]
##row5 = [261, 267, 268, 269, 270, 271, 272, 282]
##row6 = [325, 328, 329, 330, 331, 338]

def eye():
    for i in range(0,360):
        if i == 360 or i == 0:
            rand_colour = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        #row1
        if i >= 25 and i <=34:
            leds[i] = (255,255,255)
            client.put_pixels(leds)
        if i >= 28 and i <= 31:
            leds[i] = rand_colour
            client.put_pixels(leds)
        #row2
        if i >= 81 and i <= 98:
            leds[i] = (255,255,255)
            client.put_pixels(leds)
        if i >= 87 and i <= 92:
            leds[i] = rand_colour
            client.put_pixels(leds)
            sleep(0.1)
        #row3
        if i >= 139 and i <= 160:
            leds[i] = (255,255,255)
            client.put_pixels(leds)
        if i >= 147 and i <= 152:
            leds[i] = rand_colour
            client.put_pixels(leds)
            sleep(0.1)
        #row4
        if i >= 197 and i <= 222:
            leds[i] = (255,255,255)
            client.put_pixels(leds)
        if i >= 207 and i <= 212:
            leds[i] = rand_colour
            client.put_pixels(leds)
            sleep(0.1)
        #row5
        if i >= 261 and i <= 278:
            leds[i] = (255,255,255)
            client.put_pixels(leds)
        if i >= 267 and i <= 272:
            leds[i] = rand_colour
            client.put_pixels(leds)
            sleep(0.1)
        #row6
        if i >= 325 and i <= 334:
            leds[i] = (255,255,255)
            client.put_pixels(leds)
        if i >= 328 and i <= 331:
            leds[i] = rand_colour
            client.put_pixels(leds)
            sleep(0.1)
            continue


for i in range(2):
    eye()
