import opc
from time import *
import random

leds = [(255,255,255)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)

<<<<<<< Updated upstream
def snake():
    led = 0
    add = 0

    while led >= 0:
        for rows in range(3): #lights three led
            #leds[led + rows] = (200,100,255) #change three led colour
            #leds[led + rows*50] = (led*rows+0,0,0) #background back to default
            #leds[add] = (255,0,0)
            for column in range(rows):
                leds[led + column] = (200,100,255)
                #leds[add + column] = (50,5,0)
                #leds[add + column] = (add*column-0,0,0)
                leds[add + led + column + rows] = (255,0,0)
                
            add *= 5
            led += 10
            
                     
=======
##def eye():
##    led = 0
##    add = 0
##
##    while led >= 0:
##        for rows in range(3): #lights three led
##            for column in range(rows):
##                leds[led + column] = (200,100,255)
##                leds[add + led + column + rows] = (255,0,0)
##                
##            add *= 5
##            led += 10
##            
##                     
##        client.put_pixels(leds)
##        sleep(0.1)
##        led -= 1
##
##eye()

row1 = [25, 28, 29, 30, 31, 34]
row2 = [83, 87, 88, 89, 90, 91, 92, 97]
row3 = [141, 147,148, 149, 150, 151, 152, 162]
row4 = [197, 207,208, 209, 210, 211, 212, 226]
row5 = [261, 267, 268, 269, 270, 271, 272, 282]
row6 = [325, 328, 329, 330, 331, 338]

for one in row1:
    if one == 25 or one == 34:
        leds[one] = (255,255,52)
        client.put_pixels(leds)
    else:
        leds[one] = (200,100,255)
        client.put_pixels(leds)

sleep(0.1)

for two in row2:
    if two == 83 or two == 97:
        leds[two] = (255,255,52)
>>>>>>> Stashed changes
        client.put_pixels(leds)
    else:
        leds[two] = (200,100,255)
        client.put_pixels(leds)
        
sleep(0.1)
    

for third in row3:
    #print(third)
    if third == 141 or third == 162:
        leds[third] == (255,255,52)
        client.put_pixels(leds)
    else:
        leds[third] = (200,100,255)
        #print(leds[third])
        client.put_pixels(leds)

sleep(0.1)

<<<<<<< Updated upstream
snake()
=======
for fourth in row4:
    if fourth == 197 or fourth == 226:
        leds[fourth] = (255,255,52)
        client.put_pixels(leds)
    else:
        leds[fourth] = (200,100,255)
        client.put_pixels(leds)

sleep(0.1)

for fifth in row5:
    if fifth == 261 or fifth == 282:
        leds[fifth] = (255,255,52)
        client.put_pixels(leds)
    else:
        leds[fifth] = (200,100,255)
        client.put_pixels(leds)

sleep(0.1)

for sixth in row6:
    #325,338
    if sixth == 325 or sixth == 338:
        leds[sixth] = (255,255,52)
        client.put_pixels(leds)
    else:
        leds[sixth] = (200,100,255)
        client.put_pixels(leds)

sleep(0.1)
    
    #print(row1[one])
                 
##def eye():
##
##    food = [40,
##    for row in range(7):
##        leds[row] = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
##        for col in range(5):
##            #leds[row + col - body] = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
##            if ((col == 0 or col == 4) and (row != 0 and row != 6)) or ((row == 0 or row == 6) and (col > 0 and col < 4)):
##                print("*", end = "")
##            else:
##                print(end =" ")
##        print()
##    client.put_pixels(leds)
##eye()
                
        
>>>>>>> Stashed changes
