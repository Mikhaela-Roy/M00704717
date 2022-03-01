import opc
from time import *
import random
from tkinter import *
from tkinter import messagebox

leds = [(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)

def food_item():

    food = []
    l_colour = []

    for i in range(0,350,60): #access one row with a step of 60
        food.append(random.randint(i,i+60)) #appends the value to the food list
    for x in food: #access the food list
        leds[x] = (random.randint(0,255),random.randint(0,255),random.randint(0,255)) #assigns the colour of the led position at random colours
        colour = list(leds[x]) #convert tuple into list
        l_colour.append(colour) #append the values onto the empty list


    client.put_pixels(leds)
    client.put_pixels(leds)
    sleep(0.1)

    return food,l_colour
    
def snake():

    
    food,colour = food_item() #giving a variable to the return of the food_item() function
    
    body = 2 #the beginning of the body of the snake
    initial = (200,100,255) #initial colour of the snake
    
    for led in range (0,360): #this will run the whole of 360 leds
        for seg in range(body): #snake body
            leds[led+seg] = initial #1 - first iteration - snake at 0-5; 1-6 etc.
            if led > 0:
                leds[led-1] = (0,0,0) #background back to default
                
        client.put_pixels(leds)
        sleep(0.1)
        
        if led in food: #if snake hits food item:
            food.append(led) #appends the food from the list
            for i in colour: #runs through the list of colours
                change = tuple(i) #change list into tuples
                if initial != i: #not equal to i then make the initial to new colour
                    initial = change
                    client.put_pixels(leds)
                    
            body += 1 #increase body by 1
            client.put_pixels(leds)
            sleep(0.01)
            
        if led == 349: #if led is 358 the animation should stop
            break
        else:
            continue
