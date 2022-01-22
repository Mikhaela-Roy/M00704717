##value = input('''Welcome to the menu. Options below:
##\n\t 1. Roll
##\n\t 2. Sweep
##\n\t 3. Scroll
##
##Type the number of your choice and Enter. ''')
##
##def roll(val):
##    return val**1
##def sweep(val):
##    return val**2
##def scroll(val):
##    return val**3
##
##print("The value you input is: ", value)
##print(f'it is of type {type(value)}.')
##
##while True:
##    if value.isdigit() == True:
##        value = int(value)
##        if value > 3 or value < 1:
##            value = input("Please input a smaller number between 1 and 2")
##            continue
##        else: break
##        '''print("The value you input is converted: ", value)
##        print(f'it is of type {type(value)}.')
##        break'''
##    else:
##        input("Invalid. Input: ")
##
##if value == 1:
##    print(roll(value))
##elif value == 2:
##    print(sweep(value))
##else:
##    print(scroll(value))

import opc # library
from time import * # import time if importing everything
import random

leds = [(0,0,0)]*360 #blank list of 360 leds

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

food = []

for i in range(0,360,60): #0,60,120,180,240,300 (beginning of each row)
        food.append(random.randint(i,i+60)) #food item, 1 per row
for x in food: #every food item gets a colour:
    leds[x] = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

print('i = ',i)
print('x = ',x)
print('food = ',food)

client.put_pixels(leds) #display generated food
client.put_pixels(leds)
sleep(0.1)
