import opc
from time import *
import random

leds = [(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)

heart = [20,21,22,23,32,33,34,35,78,79,80,81,
         82,83,84,85,89,90,91,92,93,94,95,96,
         97,139,140,141,142,143,144,145,146,
         147,148,149,150,151,152,153,154,155,
         156,200,201,202,203,204,205,206,207,
         208,209,210,211,212,213,214,264,265,
         266,267,268,269,270,326,327,328]

def heart_shape():
    
        rands = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
                                
        for i in heart:
            rands = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            leds[i] = rands
            
        client.put_pixels(leds)            
        sleep(1)
