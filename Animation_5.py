import opc
from time import *
import random

leds = [(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)

def colour_pick():
    
    led = 0

    colour_r = int(input("Please input a range from 0-255: ")) #input for the red
    colour_g = int(input("Please input a range from 0-255: ")) #input for the green
    colour_b = int(input("Please input a range from 0-255: ")) #input for the blue

    for x in range(2): #runs twice
        for rows in range(60): #access all led in one row
            for i in range(6): #runs through all columns
                #access the start of the row and adds value from 1 to 60 to run through all column
                leds[i*60 + rows] = (led+colour_r,led-colour_g,led-colour_b) #colour to be user input
                client.put_pixels(leds)
                led += 1
            sleep(0.0001)
            leds[rows] = (0,0,0) #first row to be off except for one
            sleep(0.1)
            client.put_pixels(leds)
            
