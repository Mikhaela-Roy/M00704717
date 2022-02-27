from tkinter import *
import opc
from time import *
import random

leds = [(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)

#opens the Tkinter GUI
root = Tk()
#Gives the Tkinter window a name
root.title('Animation')

User = Label(root, text = "Enter your choice: ").grid(row = 2, column = 0)
E1v = StringVar()
entry1 = Entry(root, textvariable = E1v).grid(row = 2, column = 1)
label1 = Label(root, text = "Choose between Rock, Paper, Scissors").grid(row = 1, column = 0)

def decision():
    leds = [(0,0,0)]*360
    option = ['Rock', 'Paper', 'Scissors']
    #print('These are your options: ', option)
    #choice = str(input('Choose you would like to play by typing either e.g Paper or paper: '))
    computer = random.choice(option)
    
    if E1v.get() == 'Rock' or E1v.get() == 'rock': #or computer == 'Rock' or computer == 'rock':
        Rock()
    elif E1v.get()== 'Paper' or E1v.get() == 'paper': #or computer == 'Paper' or computer == 'paper':
        Paper()
    elif E1v.get() == 'Scissors' or E1v.get() == 'scissors': #or computer == 'Scissors' or computer == 'scissors':
        Scissors()
    else:
        print('Invalid Choice. Try again')

def Rock():

    led = 0
    for rows in range(6):
        leds[53-rows] = (112,128,144)
        leds[353-rows] = (112,128,144)
        client.put_pixels(leds)
        sleep(0.1)

    for rows in range(1,5):
        leds[led+46 + rows*60] = (112,128,144)
        leds[55-led + rows*60] = (112,128,144)
        client.put_pixels(leds)
        sleep(0.1)
        
def Scissors():

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
        
    cont = str(input('Would you like to try again? '))
    if cont == 'yes' or cont == 'Yes':
        decision()
    else:
        root.destroy()
    pass
def Paper():
    print('paper')
    cont = str(input('Would you like to try again? '))
    if cont == 'yes' or cont == 'Yes':
        decision()
    else:
        root.destroy()

submit = Button(root, text = "Submit", command = decision).grid(row = 4, column = 1)

decision()

root.mainloop()
