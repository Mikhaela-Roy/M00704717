import opc
from time import *
import random

leds = [(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)

rand_colour = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

led = 0
while led < 5:
    for i in range(0,360):
        if i == 360 or i == 0:
            rand_colour = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        if i >= 28 and i <= 31:
            leds[i] = rand_colour
            client.put_pixels(leds)
            sleep(0.1)
        if i >= 87 and i <= 92:
            leds[i] = rand_colour
            client.put_pixels(leds)
        if i >= 147 and i <= 152:
            leds[i] = rand_colour
            client.put_pixels(leds)
            sleep(0.1)
        if i >= 207 and i <= 212:
            leds[i] = rand_colour
            client.put_pixels(leds)
        if i >= 267 and i <= 272:
            leds[i] = rand_colour
            client.put_pixels(leds)
        if i >= 328 and i <= 331:
            leds[i] = rand_colour
            client.put_pixels(leds)
            sleep(0.1)
            #continue
    led += 1   
