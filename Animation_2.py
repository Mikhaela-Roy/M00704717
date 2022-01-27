import opc
from time import *
import random
import colorsys

leds = [(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)

#rand_colour = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

#references of position of LEDs

##row1 = [25, 28, 29, 30, 31, 34]
##row2 = [83, 87, 88, 89, 90, 91, 92, 97]
##row3 = [141, 147,148, 149, 150, 151, 152, 162]
##row4 = [197, 207,208, 209, 210, 211, 212, 226]
##row5 = [261, 267, 268, 269, 270, 271, 272, 282]
##row6 = [325, 328, 329, 330, 331, 338]

def eye():
    s = 1.0 ##maximum colour
    v = 1.0 ##maximum brightness
    
    for i in range(0,360): #Run from 0 to 359
        rgb_fractional = colorsys.hsv_to_rgb(i/360, s, v) #colorsys returns floats between 0 and 1
        r_float = rgb_fractional[0] #extract said floating point numbers
        g_float = rgb_fractional[1]
        b_float = rgb_fractional[2]

        rgb = (r_float*255, g_float*255, b_float*255) #make new tuple with corrected values
        
        if i == 360 or i == 0: #beginning random colour and when loop ends restart colour
            rand_colour = (random.randint(0,255),random.randint(0,255),random.randint(0,255)) #random colour 
    
        if i >= 25 and i <=34 or i >= 81 and i <= 98 or i >= 139 and i <= 160 or i >= 197 and i <= 222 or i >= 261 and i <= 278 or i >= 325 and i <= 334:
            leds[i] = (255,255,255) #when the range is between the values listed above change the colour to white
            client.put_pixels(leds)
            sleep(0.1)
       
        if i >= 28 and i <= 31 or i >= 87 and i <= 92 or i >= 147 and i <= 152 or i >= 207 and i <= 212 or i >= 267 and i <= 272 or i >= 328 and i <= 331:
            leds[i] = rand_colour #when the range is between the values listed above change colour to the initial random generated colour
            client.put_pixels(leds)
            sleep(0.01)
            client.put_pixels([rgb]*360) #sends out
            sleep(0.1)

eye()         
