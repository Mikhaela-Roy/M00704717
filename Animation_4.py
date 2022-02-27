import opc
from time import *
import random
import colorsys

leds = [(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)

hearts = [20,21,22,23,32,33,34,35,78,79,80,81,
         82,83,84,85,89,90,91,92,93,94,95,96,
         97,139,140,141,142,143,144,145,146,
         147,148,149,150,151,152,153,154,155,
         156,200,201,202,203,204,205,206,207,
         208,209,210,211,212,213,214,264,265,
         266,267,268,269,270,326,327,328]
s = 1.0 ##maximum colour
v = 1.0 ##maximum brightness

def heart():
    
##        rands = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
##                                
##        for i in hearts:
##            rands = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
##            leds[i] = rands
##            
##        client.put_pixels(leds)            
##        sleep(1)
        
        for hue in range(360):
            rgb_fractional = colorsys.hsv_to_rgb(random.randint(hue-10, hue+10)/360.0, s, v) #colorsys returns floats between 0 and 1
            r_float = rgb_fractional[0] #extract said floating point numbers
            g_float = rgb_fractional[1]
            b_float = rgb_fractional[2]

            rgb = (r_float*255, g_float*255, b_float*255) #make new tuple with corrected values
            leds[hue]=rgb
            client.put_pixels(leds) #send out

            sleep(0.03) #20ms
heart()
