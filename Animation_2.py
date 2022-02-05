import opc
import Animation_1
from time import *
import random
import colorsys
from tkinter import messagebox

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

iris = [[28,29,30,31],[87,88,89,90,91,92],[147,148,149,150,151,152],[207,208,209,210,211,212],[267,268,269,270,271,272],[328,329,330,331]]

def white():

    rand_colour = (random.randint(0,255),random.randint(0,255),random.randint(0,255)) #random colour

    inc = 0
    q = 0
    
    for i in range(3):
        print('i',i)
        for loop in range(0,61):
            print('loop',loop)
            q += 1
            if loop == 60:
                inc += 1
                sleep(1)
                
            c = loop + 60*inc
            f = loop + (300-60*inc)
            
            print('f',f)
            print('c',c)
            print('inc',inc)
            
            if c >= 25 and c <=34 or c >= 81 and c <= 98 or c >= 139 and c <= 160 or f >= 197 and f <= 222 or f >= 261 and f <= 278 or f >= 325 and f <= 334:
                leds[c-60] = (0,0,0)
                client.put_pixels(leds)
                leds[c] = (255,255,255)
                client.put_pixels(leds)
                leds[f] = (255,255,255)
                client.put_pixels(leds)
                #sleep(0.1)
                leds[f+60] = (0,0,0)
                client.put_pixels(leds)
            
white()

def eye():
    
    messagebox.showwarning(title = '', message  = 'FLASH WARNING')
    
    for loop in range(5):    
        s = 1.0 ##maximum colour
        v = 1.0 ##maximum brightness

        for i in range(0,360): #Run from 0 to 359
            rgb_fractional = colorsys.hsv_to_rgb(i/360.0, s, v) #colorsys returns floats between 0 and 1
            r_float = rgb_fractional[0] #extract said floating point numbers
            g_float = rgb_fractional[1]
            b_float = rgb_fractional[2]

            rgb = (r_float*255, g_float*255, b_float*255) #make new tuple with corrected values
            
            if i == 360 or i == 0: #beginning random colour and when loop ends restart colour
                rand_colour = (random.randint(0,255),random.randint(0,255),random.randint(0,255)) #random colour
                
            if i >= 25 and i <=34 or i >= 81 and i <= 98 or i >= 139 and i <= 160 or i >= 197 and i <= 222 or i >= 261 and i <= 278 or i >= 325 and i <= 334:
                leds[i] = (255,255,255) #when the range is between the values listed above change the colour to white
                client.put_pixels(leds)
                #sleep(0.1)
            
        for x in iris:
            for y in x:
                leds[y] = rand_colour #when the range is between the values listed above change colour to the initial random generated colour
                client.put_pixels([rgb]*1) #send out
                sleep(0.01)
            
        client.put_pixels(leds)
        sleep(0.1)
    
        
    #Animation_1.snake()

#eye()
