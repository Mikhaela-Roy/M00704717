from tkinter import *
import opc
from time import *
import random

leds = [(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)

def reset():
    
    led = 0
    
    while led < 60: #scroll all rows at the same time
        for rows in range(2): #access the first two rows
            leds[led-30 + rows*60] = (0,0,0) #row 1- 0-60
            leds[29-led +rows*60] = (0,0,0) #leds off on all two rows
        for rows in range(2,4): #access the middle two rows
            leds[led-30 + rows*60] = (0,0,0) #leds off on all two rows
            leds[29-led +rows*60] = (0,0,0)
        for rows in range(4,6): #access the last two rows
            leds[led-30 + rows*60] = (0,0,0)
            leds[29-led +rows*60] = (0,0,0) #leds off on all two rows
         
        led -= 1 #decrement led to remove backwards
        client.put_pixels(leds)#makes all the leds off at the same time
        sleep(0.1)

        if led == -60: #-60 as led strats from 0
            break
        elif led == -31: 
            break
        else:
            continue
def vs():
    led = 0
    
    for rows in range(6):
        leds[led+20 + rows*60] = (255,0,0)
        led += 1
        client.put_pixels(leds)
        
    for rows in range(6):
        leds[led+24 + rows*60] = (255,0,0)
        led -= 1
        client.put_pixels(leds)
        
    for rows in range(6): #body of the first row
        leds[37-rows] = (255,0,0) #first row
        leds[157-rows] = (255,0,0) #middle row
        leds[337-rows] = (255,0,0) #last row
        client.put_pixels(leds)

    for rows in range(2): #acces the middle rows
        leds[led+32 + rows*60] = (255,0,0) #starts from 
        #leds[256-led + rows*60] = (112,128,144)
        client.put_pixels(leds)
        
    for rows in range(2):
        leds[217-led + rows*60] = (255,0,0)
        client.put_pixels(leds)

def decision():
    
    option = ["R", "P", "S"] #list with the options for rock, paper, scissors
    print('These are your options: ', option) #display option to the user
    #choice is the user input that allows only string
    choice = str(input('Choose you would like to play by typing either e.g R, P, S : '))
    #using random library to choose in the option list
    computer = random.choice(option)

    vs()
    
    #if the user input is R as well as the computer 
    if choice == 'R':
        led = 0
        
        for rows in range(6): #body of the first row
            leds[53-rows] = (112,128,144) #first row 
            leds[353-rows] = (112,128,144) #last row
            client.put_pixels(leds)
            sleep(0.1)
            
        for i in range(10): #body for the middle rows
            for rows in range(1,5): #access the middle rows
                leds[i+46 + rows*60] = (112,128,144) #starts from 
                leds[55-led + rows*60] = (112,128,144)
            client.put_pixels(leds)
            sleep(0.1)

    if computer == 'R':
        
        led = 0

        for rows in range(6):
            leds[11-rows] = (112,128,144)
            leds[311-rows] = (112,128,144)
            client.put_pixels(leds)
            sleep(0.1)
            
        for i in range(10):
            for rows in range(1,5):
                leds[i+4 + rows*60] = (112,128,144)
                leds[5-led + rows*60] = (112,128,144)
            client.put_pixels(leds)
            sleep(0.1)

    #if the user input is P as well as the computer   
    if choice == 'S':
        
        led = 0
        
        for rows in range(3):
            leds[led+48 + rows*60] = (0,255,255)
            led += 1
            client.put_pixels(leds)
            sleep(0.1)
        for rows in range(3):
            leds[led+49 + rows*60] = (0,255,255)
            led -= 1
            client.put_pixels(leds)
            sleep(0.1)
        for rows in range(1,6):
            leds[led+46 + rows*60] = (0,255,255)
            led += 1
            client.put_pixels(leds)
            sleep(0.1)
        for rows in range(1,6):
            leds[led+49 + rows*60] = (0,255,255)
            led -= 1
            client.put_pixels(leds)
            sleep(0.1)

    if computer == 'S':
        led = 0
        
        for rows in range(3):
            leds[led+10 + rows*60] = (0,255,255)
            led += 1
            client.put_pixels(leds)
        for rows in range(3):
            leds[led+11 + rows*60] = (0,255,255)
            led -= 1
            client.put_pixels(leds)
        for rows in range(1,6):
            leds[led+8 + rows*60] = (0,255,255)
            led += 1
            client.put_pixels(leds)
        for rows in range(1,6):
            leds[led+11 + rows*60] = (0,255,255)
            led -= 1
            client.put_pixels(leds)
                       
    if choice == 'P':

        led = 0
        
        for rows in range(6): #body of the first row
            leds[rows] = (0,0,0)
            client.put_pixels(leds)
            leds[53-rows] = (255,255,255) #first row 
            leds[353-rows] = (255,255,255) #last row
            client.put_pixels(leds)
            sleep(0.1)
            
        for i in range(10): #body for the middle rows
            for rows in range(6): #acces the middle rows
                leds[i+46 + rows*60] = (255,255,255) #starts from 
                leds[55-led + rows*60] = (255,255,255)
            client.put_pixels(leds)
            sleep(0.1)
            
    if computer == 'P':
        
        led = 0

        for rows in range(6):
            leds[11-rows] = (255,255,255)
            leds[311-rows] = (255,255,255)
            client.put_pixels(leds)
            sleep(0.1)
            
        for i in range(10):
            for rows in range(6):
                leds[i+4 + rows*60] = (255,255,255)
                leds[5-led + rows*60] = (255,255,255)
            client.put_pixels(leds)
            sleep(0.1)
            
    #Code below is to show the possibility of winning with different combinations
    if computer == choice:
        print("DRAW!")
        
    elif computer == 'R' and choice == 'S':
        print("COMPUTER WINS!")

    elif computer == 'S' and choice == 'R':
        print("YOU WIN!")
        
    elif computer == 'P' and choice == 'R':
        print("COMPUTER WINS!")
        
    elif computer == 'R' and choice == 'P':
        print("YOU WIN!")
        
    elif computer == 'S' and choice == 'P':
        print("COMPUTER WINS!")
        
    elif computer =='P' and choice == 'S':
        print("YOU WIN!")
        
    else:
        print("????")

    #asks user if they want to continue to play and if yes run the function again
    cont = str(input('Would you like to try again? '))
    if cont == 'yes' or cont == 'Yes':
        reset()
        decision()
    else:
        reset()
