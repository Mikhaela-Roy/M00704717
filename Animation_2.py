import opc
from time import *
import random

leds = [(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)

<<<<<<< Updated upstream
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
=======
row1 = [25, 28, 29, 30, 31, 34]
row2 = [83, 87, 88, 89, 90, 91, 92, 97]
row3 = [121, 147,148, 149, 150, 151, 152, 162]
row4 = [197, 207,208, 209, 210, 211, 212, 222]
row5 = [261, 267, 268, 269, 270, 271, 272, 278]
row6 = [325, 328, 329, 330, 331, 334]

for one in row1:
    if one == 25 or one == 34:
        leds[one] = (255,255,52)
        client.put_pixels(leds)
    else:
        leds[one] = (200,100,255)
        client.put_pixels(leds)

for two in row2:
    if two == 83 or two == 97:
        leds[two] = (255,255,52)
        client.put_pixels(leds)
    else:
        leds[two] = (200,100,255)
        client.put_pixels(leds)

for third in row3:
    if third == 121 or third == 162:
        leds[third] == (255,255,52)
        client.put_pixels(leds)
    else:
        leds[third] = (200,100,255)
        client.put_pixels(leds)

for fourth in row4:
    if fourth == 197 or fourth == 222:
        leds[fourth] = (255,255,52)
        client.put_pixels(leds)
    else:
        leds[fourth] = (200,100,255)
        client.put_pixels(leds)

for fifth in row5:
    if fifth == 261 or fifth == 278:
        leds[fifth] = (255,255,52)
        client.put_pixels(leds)
    else:
        leds[fifth] = (200,100,255)
        client.put_pixels(leds)

for sixth in row6:
    #325,338
    if sixth == 325 or sixth == 334:
        leds[sixth] = (255,255,52)
        client.put_pixels(leds)
    else:
        leds[sixth] = (200,100,255)
        client.put_pixels(leds)
    
        
>>>>>>> Stashed changes
