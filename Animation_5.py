import opc
from time import *
import random

leds = [(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)

led = 0

for col in range(10):
    leds[col] = (255,0,0)
    leds[col+300] = (255,0,0)
    sleep(0.1)

for rows in range(60):
    leds[rows+60] = (led+50,led+50,led+20)
    leds[rows+240] = (led+50,led+80,led+0)
    client.put_pixels(leds)  
    sleep(0.1)
    led += 1
    
for rows in range(60):
    for i in range(6):
        leds[i*60 + rows] = (0,150,0)
        #leds[led + rows] = (255,0,0)
        
        client.put_pixels(leds)
        sleep(0.1)
