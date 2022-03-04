import opc
from time import *
from tkinter import messagebox
import random
import colorsys

leds = [(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)

#list of the leds for the heart 
##hearts = [20,21,22,23,78,79,80,81,
##         82,83,84,85,139,140,141,142,143,144,145,146,
##         147,200,201,202,203,204,205,206,207,264,265,
##         266,267,326,327]

##hearts_1 = [32,33,34,35,89,90,91,92,93,94,95,96,
##         97,148,149,150,151,152,153,154,155,
##         156,208,209,210,211,212,213,214,
##            268,269,270,328]

##hearts_1 = [328,270,269,268,214,213,212,211,210,209,208,
##            156,155,154,153,152,151,150,149,148,97,96,95,
##            94,93,92,91,90,89,35,34,33,32]


#puzzle = hearts + hearts_1
#sort = sorted(hearts+hearts_1)

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

        
##def half():
##    for rows in range(len(hearts_1)):
##         y = hearts_1[rows]
##         for col1 in y:
##            leds[col1] = (255,255,255) #5 led is
##         client.put_pixels(leds)
##         sleep(0.1)
         

    
##for rows in range(360):
##    for j in hearts_1:
##        if rows == j:
##            leds[4-j] = (255,0,0)
##            leds[j-1] = (0,0,0)
##            client.put_pixels(leds)
##            sleep(0.1)
        
##    for i in hearts:
##        if i == rows:
##            leds[1-i] = (255,0,0)
##            leds[i+4] = (0,0,0)
##            client.put_pixels(leds)
##            sleep(0.1)


    #half()

##while inc < 360:
##    for rows in hearts:
##        if inc == rows:
##            print('Alright')
##    inc += 1

#-----------------------------------------------------------------------------#
hearts = [[20,21,22,23],[78,79,80,81,
         82,83,84,85],[139,140,141,142,143,144,145,146,
         147],[200,201,202,203,204,205,206,207],[264,265,
         266,267],[326,327]]

hearts_1 = [[32,33,34,35],[89,90,91,92,93,94,95,96,
         97],[148,149,150,151,152,153,154,155,
         156],[208,209,210,211,212,213,214],
            [268,269,270],[328]]
##
##for i in range(len(hearts)):
##    x = hearts[i]
##    for rows in x:

iris = [28,29,30,31,87,88,89,90,91,92,147,148,149,150,151,152,207,208,209,210,211,212,267,268,269,270,271,272,328,329,330,331]

def eye():

    messagebox.showwarning(title = '', message  = 'FLASH WARNING')
    for i in range(360):
        if i >= 25 and i <=34 or i >= 81 and i <= 98 or i >= 139 and i <= 160 or i >= 197 and i <= 222 or i >= 261 and i <= 278 or i >= 325 and i <= 334:
            leds[i] = (255,255,255) #when the range is between the values listed above change the colour to white
            client.put_pixels(leds)
            #sleep(0.1)

    for x in iris:
        leds[x] = (255,0,0)
        #sleep(0.1)
        client.put_pixels(leds)
                

        client.put_pixels(leds)
        sleep(0.1)
        i+=1
        
eye()
