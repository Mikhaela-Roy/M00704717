import opc
from time import *
import random

leds = [(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)

vs = [146,150,207,209,268,152,153,154,155,212,215,272,273,274]
    
def fist():
    for i in vs:
        leds[i] = (255,0,0)
        client.put_pixels(leds)

    




fist()
