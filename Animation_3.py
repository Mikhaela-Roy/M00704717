import opc
from time import *
import random

leds = [(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)

def reverse():
    led = 0
    
    while led < 60: #scroll all rows at the same time
        rand = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        for rows in range(2):
            leds[led-30 + rows*60] = (0,0,0) #row 1- 0-60
            leds[29-led +rows*60] = (0,0,0)
        for rows in range(2,4):
            leds[led-30 + rows*60] = (0,0,0)
            leds[29-led +rows*60] = (0,0,0)
        for rows in range(4,6):
            leds[led-30 + rows*60] = (0,0,0)
            leds[29-led +rows*60] = (0,0,0)
         
        led -= 1
        client.put_pixels(leds)
        sleep(0.1)

        if led == -60:
            break
        elif led == -31:
            break
        else:
            continue
        
def build():
    led = 0
    
    while led < 60: #scroll all rows at the same time
        for rows in range(2):
            leds[led + rows*60] = (led+100,0,0) #row 1- 0-60
        for rows in range(2,4):
            leds[59-led + rows*60] = (led+100,0,0)
        for rows in range(4,6):
            leds[led + rows*60] = (led+100,0,0)
         
        led += 1
        client.put_pixels(leds)
        sleep(0.1)
        
    reverse()
build()
