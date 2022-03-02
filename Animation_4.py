import opc
from time import *
import random
import colorsys

leds = [(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)

#list of the leds for the parts of the heart
hearts = [[20,21,22,23],[78,79,80,81,
         82,83,84,85],[139,140,141,142,143,144,145,146,
         147],[200,201,202,203,204,205,206,207],[264,265,
         266,267],[326,327]]

hearts_1 = [[32,33,34,35],[89,90,91,92,93,94,95,96,
         97],[148,149,150,151,152,153,154,155,
         156],[208,209,210,211,212,213,214],
            [268,269,270],[328]]

sort = sorted(hearts + hearts_1) #adds the two lists together and sorts the list from smallest to largest

s = 1.0 ##maximum colour
v = 1.0 ##maximum brightness



def heart():
        for rows in range(len(sort)):
                one = sort[rows]
                for i in one:
                    rgb_fractional = colorsys.hsv_to_rgb(random.randint(i-5, i+5)/360.0, s, v) #colorsys returns floats between 0 and 1
                    r_float = rgb_fractional[0] #extract said floating point numbers
                    g_float = rgb_fractional[1] 
                    b_float = rgb_fractional[2]

                    rgb = (r_float*255, g_float*255, b_float*255) #make new tuple with corrected values
                    leds[i]=rgb
                    client.put_pixels(leds) #send out

                sleep(0.1) #20ms
        
def colour_merge():
        
        led = 0
        
        for call in range(4):
                rand = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
                
                for rows in range(len(hearts)): #takes the length of the list
                        x = hearts[rows] #access the list of the list
                        for col in x: #col is the indes to acces the value of the lists of the list
                                leds[col] = (255,0,0) #colour of the led
                                #leds[col-1] = (200,50,0) #background back to default
                                
                        client.put_pixels(leds)
                        sleep(0.1)
                        
                for rows in range(len(hearts_1)):
                        y = hearts_1[rows]
                        for col1 in y:
                                leds[col1] = (255,255,255) #5 led is
                                #leds[col1] = (200,50,0) #background back to default
                                
                        client.put_pixels(leds)
                        sleep(0.1)

                for x in range(len(sort)):
                    row = sort[x]
                    for y in row:
                        leds[y] = (led+255,led+0,led+0) #increments the colour red to white
                        led += 1 #increases the led for increment of the colour red
                    client.put_pixels(leds)
                    sleep(0.1)

                heart()

colour_merge()
