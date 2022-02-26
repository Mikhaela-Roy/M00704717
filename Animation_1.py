import opc
from time import *
import random
from tkinter import *
from tkinter import messagebox

leds = [(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)

def confirm():
    answer = messagebox.askquestion(title = 'Confirmation', message  = 'Do you wish to continue the Snake Animation? ')
    if answer == 'yes':
        body = 8
        leds[body] = (0,0,0)
        client.put_pixels(leds)
        snake()
        
        
def food_item():

    food = []
    l_colour = []

    for i in range(0,350,60):
        food.append(random.randint(i,i+60))
    for x in food:
        leds[x] = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        colour = list(leds[x])
        l_colour.append(colour)


    client.put_pixels(leds)
    client.put_pixels(leds)
    sleep(0.1)

    return food,l_colour

#food_item()
    
def snake():

    
    food,colour = food_item()
    
    body = 2
    initial = (200,100,255)
    
    for led in range (0,360):
        for seg in range(body):
            leds[led+seg] = initial
            if led > 0:
                leds[led-1] = (0,0,0)
                
        client.put_pixels(leds)
        sleep(0.1)
        
        if led in food:
            food.append(led)
            for i in colour:
                change = tuple(i)
                if initial != i:
                    initial = change
                    leds[led+seg] = initial
                    client.put_pixels(leds)
                    
            body += 1
            client.put_pixels(leds)
            sleep(0.01)
            
        leds[359-body] = (0,0,0)
        client.put_pixels(leds)
        
        if led == 349:
            confirm()
        elif led == 358:
            break
        else:
            continue
