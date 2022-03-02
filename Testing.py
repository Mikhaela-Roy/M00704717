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
         266,267,326,327]

hearts_1 = [[32,33,34,35],[89,90,91,92,93,94,95,96,
         97],[148,149,150,151,152,153,154,155,
         156],[208,209,210,211,212,213,214],
            [268,269,270],[328]]

#puzzle = hearts + hearts_1
#sort = sorted(hearts+hearts_1)


inc = 0

##while inc < 360:
##    for x in range(len(sort)):
##        row = sort[x]
##        for y in row:
##            print(y)
##            if inc == y:
##                leds[inc] = (led+255,led+0,led+0)
##                led += 1
##        
##        client.put_pixels(leds)
##        #sleep(0.1)
##        inc += 1
##        print('inc',inc)

inc = 0

##for rows in range(6): #body of the first row
##    leds[53-rows] = (112,128,144) #first row 
##    leds[353-rows] = (112,128,144) #last row
##    client.put_pixels(leds)
##    sleep(0.1)
##    
##for i in range(10): #body for the middle rows
##    for rows in range(1,5): #access the middle rows
##        leds[i+46 + rows*60] = (112,128,144) #starts from 
##        leds[55-led + rows*60] = (112,128,144)
##    client.put_pixels(leds)
##    sleep(0.1)

        
def half():
    for rows in range(len(hearts_1)):
         y = hearts_1[rows]
         for col1 in y:
            leds[col1] = (255,255,255) #5 led is
         client.put_pixels(leds)
         sleep(0.1)
         
def other():
    
    inc = 0
    i = 4
    
    for led in range(360):
        for rows in hearts:
            if inc == rows:
                leds[rows+4] = (255,0,0)
                leds[rows] = (0,0,0)
                client.put_pixels(leds)
                sleep(0.1)
        i += 1
        inc += 1
        
##    for led in range(78,85):
##        leds[inc + 8] = (255,0,0)
##        leds[inc] = (0,0,0)
##        client.put_pixels(leds)
##        sleep(0.1)
##        inc += 1
    

    #half()
other()
inc = 0

##while inc < 360:
##    for rows in hearts:
##        if inc == rows:
##            print('Alright')
##    inc += 1
