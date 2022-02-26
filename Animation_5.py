import opc
from time import *
import random

leds = [(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)

led = 0
fade_amount = 5

while led < 360:
    for led_s in enumerate(leds): # enumerate creates a list of tuples that contain index and contents of each element
                                    # in our case: led = (led_num, (R,G,B))
        r,g,b = led_s[1]              # this points to the second element in led - the (R,G,B) tuple.
        r = r+fade_amount
        g = g+fade_amount
        b = b+fade_amount

        new_colour = (r,g,b)            # create new tuple containing the updated values
        leds[led_s[0]] = new_colour   # place it in the original list at index led_num.

        if r >=255 or r <= 0:           # check if the fade has hit its' limit;
            fade_amount = -fade_amount  # if it has - change directions from the next iteration.
        led += 1
    client.put_pixels(leds)         # send the entire new list to the lights.
    sleep(.02)                          # 20ms delay
    
for col in range(10):
    leds[col] = (255,0,0)
    leds[col+300] = (255,0,0)
    sleep(0.1)

for rows in range(7):
    leds[rows+60] = (255,0,0)
    leds[rows+240] = (255,0,0)
    client.put_pixels(leds)  
    sleep(0.1)

for rows in range(4):
    leds[rows+120] = (255,0,0)
    leds[rows+180] = (255,0,0)
    client.put_pixels(leds)
    sleep(0.1)



