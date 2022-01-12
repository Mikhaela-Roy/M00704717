import opc
import time
import random

leds = [(255,0,0)]*360

client = opc.client('localhost:7890')
client.put_pixels(leds)


led = 0
while led < 60:
    leds[59-led] = (0,255,0)
    time.sleep(0.1)
    client.put_pixels(leds)
    led = led + 1

led = 0
while led < 60: #scroll all rows at the same time
    for rows in range(3): #first three rows left to right
        leds[led + rows*60] = (0,0,255)
    for rows in range(3,6):#last three rows reversed
        led[59-led + rows*60] = (50,50,255)
    client.put_pixels(leds)
    time.sleep(0.1)
    led = led + 1

led = 0
while led < 30:
    for rows in range(6):
        leds[led + rows*60] = (200,100,100)
        leds[59-led + rows*60] = (200,100,100)
    client,put_pixels(leds)
    led = led + 1

#do a scroll from the middle to the outside - two pixels away from each other
#reverse the scroll from the middles
#do a snake, 5 pixels long, retuen to start whenit hits the end

