from tkinter import *
import opc
from time import *
import random

leds = [(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)

def decision():
    
    option = ['R', 'P', 'S'] #list with the options for rock, paper, scissors
    print('These are your options: ', option) #display option to the user
    #choice is the user input that allows only string
    choice = str(input('Choose you would like to play by typing either e.g R, P, S : '))
    #using random library to choose in the option list
    computer = random.choice(option)
    print('Computer chooses: ',computer) #display computer play

    #if the user input is R as well as the computer 
    if choice == 'R' or computer == 'R':
        led = 0
        
        for rows in range(6): #body of the first row
            leds[53-rows] = (112,128,144) #first row 
            leds[353-rows] = (112,128,144) #last row
            client.put_pixels(leds)
            sleep(0.1)
            
        for i in range(10): #body for the middle rows
            for rows in range(1,5): #acces the middle rows
                leds[i+46 + rows*60] = (112,128,144) #starts from 
                leds[55-led + rows*60] = (112,128,144)
            client.put_pixels(leds)
            sleep(0.1)

        if computer == 'Rock' or computer == 'rock':
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
    elif choice== 'P' or computer == 'P':
        #Paper
        led = 0

        for rows in range(3):
            leds[led+10 + rows*60] = (255,255,255)
            led += 1
            client.put_pixels(leds)
        for rows in range(3):
            leds[led+11 + rows*60] = (255,255,255)
            led -= 1
            client.put_pixels(leds)
        for rows in range(1,6):
            leds[led+7 + rows*60] = (255,255,255)
            led += 1
            client.put_pixels(leds)
        for rows in range(1,6):
            leds[led+12 + rows*60] = (255,255,255)
            led -= 1
            client.put_pixels(leds)
            
    elif choice == 'S' or computer == 'S':
        Scissors()
        
    else:
        print('Invalid Choice. Try again')

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
        decision()

decision()
