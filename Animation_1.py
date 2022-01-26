import opc
from time import *
import random
from tkinter import *
from tkinter import messagebox

leds = [(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)


def confirm():
    answer = messagebox.askquestion(title = 'Confirmation', message  = 'Do you wish to continue the Snake Animation? ')
    if answer == 'yes':
        body = -5
        snake()
         
def food_item():
    food = []
    body = 0
    
    for i in range(0,360,60):
        food.append(random.randint(i,i+60))
    #print('list food = ',food)
    for x in food:
        leds[x] = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

    client.put_pixels(leds)
    client.put_pixels(leds)
    sleep(0.1)

        
##    while body < 355:
##        for position in range(len(food)):
##            #print('position', position)
##            if body == position:
##                body = x
##                print('colour = ', leds[x])
##        
##            body += 1
##        
##    client.put_pixels(leds)
##    client.put_pixels(leds)
##    client.put_pixels(leds)
##    sleep(0.1)
    


def snake():
    
    body = -5
    
    food_item()
    
    while body < 355: # when body is
        leds[body + 5] = (200,100,255) #5 led is created
        leds[body] = (0,0,0) #background back to default
        
        if body >= 354: #body is at the maximum led reset the value back to 0
            confirm()

        leds[body - 5] = (0,0,0) #change the led from the back to default    
            
        client.put_pixels(leds)
        sleep(0.1)
        body += 1
            

