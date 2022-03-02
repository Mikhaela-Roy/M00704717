import opc
from time import *
import random
import colorsys

leds = [(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)

#list of the leds for the heart 
hearts = [20,21,22,23,78,79,80,81,
         82,83,84,85,139,140,141,142,143,144,145,146,
         147,200,201,202,203,204,205,206,207,264,265,
         266,267,326,327,328]

hearts_1 = [32,33,34,35,89,90,91,92,93,94,95,96,
         97,148,149,150,151,152,153,154,155,
         156,208,209,210,211,212,213,214,
            268,269,270,326]

s = 1.0 ##maximum colour
v = 1.0 ##maximum brightness

def second():
        for i in hearts_1:
            rgb_fractional = colorsys.hsv_to_rgb(random.randint(i-5, i+5)/360.0, s, v) #colorsys returns floats between 0 and 1
            r_float = rgb_fractional[0] #extract said floating point numbers
            g_float = rgb_fractional[1]
            b_float = rgb_fractional[2]

            rgb = (r_float*255, g_float*255, b_float*255) #make new tuple with corrected values
            leds[i]=rgb
            client.put_pixels(leds) #send out

            sleep(0.1) #20ms

def heart():
        
        for hue in hearts: #runs through the list, leds are changed to the colour spectrum
            rgb_fractional = colorsys.hsv_to_rgb(random.randint(hue-5, hue+5)/360.0, s, v) #colorsys returns floats between 0 and 1
            r_float = rgb_fractional[2] #extract said floating point numbers
            g_float = rgb_fractional[1]
            b_float = rgb_fractional[0]

            rgb = (r_float*255, g_float*255, b_float*255) #make new tuple with corrected values
            leds[hue]=rgb
            client.put_pixels(leds) #send out

            sleep(0.1) #20ms

        second()

heart()
