import opc
import time
import random

leds = [(255,0,0)]*360 #[(255,255,255)]*360 White

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

#for led in leds: # pick out an element: led = (255,255,255)
for led in range(60): #pick out indeces: led = 0,1,2,3...
    leds[led] = (255,0,0)
    time.sleep(0.1)
    client.put_pixels(leds)

led = 0
while led < 60:
    leds[59-led] = (0,255,0)
    time.sleep(0.1)
    client.put_pixels(leds)
    led = led + 1 #or reverse if you want

led = 0
while led < 60: #scroll all rows at the same time
    leds[led] = (0,0,255) #row 1- 0-60
    leds[led+60] = (0,0,255) # row 2 - 0+60 - 59+60 (60-119)
    leds[led+120] = (0,0,255)
    leds[led+180] = (0,0,255) # this can be done in 2 lines intead of 6
    leds[led+240] = (0,0,255)
    leds[led+300] = (0,0,255)
    client.put_pixels(leds)
    time.sleep(0.1)
    led = led + 1 
    
#refractor the last example to use less code
#reverse the last example
#do a scroll from the middle to the outside - two pixels moving away from each other.
