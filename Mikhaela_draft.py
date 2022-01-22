import opc # library
from time import * # import time if importing everything
import random

leds = [(0,0,0)]*360 #blank list of 360 leds

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

def snake(): 
    body = 5
    food = [] #food list
    colour = (200,100,255) #snake starting colour
    #pos =
    for i in range(0,360,60): #0,60,120,180,240,300 (beginning of each row)
        food.append(random.randint(i,i+60)) #food item, 1 per row
    for x in food: #every food item gets a colour:
        leds[i] = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

    client.put_pixels(leds) #display generated food
    client.put_pixels(leds)
    sleep(0.1)

##    for led in range(0,359-body): #(360 - length of snake)
##        for segment in range(body): # snake body
##            #print('colour',colour)
##            leds[led+segment] = colour #1 - first iteration - snake at 0-5; 1-6 etc.
##            if led > 0:
##                leds[led-1] = (0,0,0) #background back to default
##                
##            #if body == 11 and 
##            client.put_pixels(leds)
##            client.put_pixels(leds)
##            #print(food, body)
##            sleep(0.1)
##
##            # run thru all values in the food list and check if we're at one.
##            # remove that from that list, increase body by 1, draw new snake, remove old food item from screen.
##            
##        if led in food: #if snake hits food item:
##            food.append(led) #remove the food from the list !!!!!!!does the list change?
##            print('food',food)
##            colour = leds[led] #give snake the food item !!!!!!!!!not assigned properly
##            leds[led] = (0,0,0) #clear the food !!!!!!!!!happens late?
##            body += 1 #increase body by 1 !!!!!!! does not grow     

while True:
    client.put_pixels(leds)
    snake() #put a loop around this
    sleep(0.1)

    # does not grow after eating food
    # does not change color to the food item consumed.

#currently code is removing led and add in front
