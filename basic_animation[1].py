import opc
import time
import random

leds = [(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)

#SOLID STATE COLOUR
##led = 0
##while led < 60:
##    leds[59-led] = (255,255,50)
##    time.sleep(0.1)
##    client.put_pixels(leds)
##    led = led + 1

#SCROLL LEDS IN A ROW
led = 0
while led < 60: #scroll all rows at the same time
    for rows in range(3): #first three rows left to right
        leds[led + rows*60] =  (200,100,255) #pink led
    for rows in range(3,6):#last three rows reversed
        leds[59-led + rows*60] = (100,50,255) #purple led
    client.put_pixels(leds)
    time.sleep(0.1)
    led = led + 1


##led = 0
##while led < 30:
##    for rows in range(6):
##        leds[led + rows*60] = (200,100,100)
##        leds[59-led + rows*60] = (200,100,100)
##    client.put_pixels(leds)
##    led = led + 1

##led = 0
##while True:
####    for rows in range(6):
####        leds[led + rows*60] = (led*rows+50,0,100)
####        client.put_pixels(leds)
##    for column in range(6):
##        leds[led + column*60] = (led*column+100,0,100)
##        #leds[59-led + rows*60] = (led*rows+50,0,100)
##        client.put_pixels(leds)
##    time.sleep(0.1)
##    led = led - 1
###do a scroll from the middle to the outside - two pixels away from each other
###reverse the scroll from the middles
###do a snake, 5 pixels long, retuen to start when it hits the end

##led = 0
##while led < 
