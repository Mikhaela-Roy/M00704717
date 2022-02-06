import opc
from time import *
import random

leds = [(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)

heart = [20,21,22,23,32,33,34,35,78,79,80,81,
         82,83,84,85,89,90,91,92,93,94,95,96,
         97,139,140,141,142,143,144,145,146,
         147,148,149,150,151,152,153,154,155,
         156,200,201,202,203,204,205,206,207,
         208,209,210,211,212,213,214,264,265,
         266,267,268,269,270,326,327,328]

def heart_shape():
    
        fade_amount = 5

        rands = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
                                
        for led in enumerate(leds):     # enumerate creates a list of tuples that contain index and contents of each element
                                        # in our case: led = (led_num, (R,G,B))
            r,g,b = led[1]              # this points to the second element in led - the (R,G,B) tuple.
            r = r+fade_amount
            g = g+fade_amount
            b = b+fade_amount

            new_colour = (r,g,b)        # create new tuple containing the updated values
            leds[led[0]] = new_colour   # place it in the original list at index led_num.

            #print(led[0])

            for i in heart:
                leds[i] = rands
          # check if the fade has hit its' limit;
                if r == 0 and g == 0 and b == 0:
                    fade_amount = -fade_amount # if it has - change directions from the next iteration.
                    
                    
        client.put_pixels(leds)            # send the entire new list to the lights.
        sleep(1)
 
while True:
    heart_shape()
