import opc
from time import *
import random
from tkinter import *
from tkinter import messagebox
import colorsys

leds = [(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)

#---------------------------------------------------------Tkinter Interface-----------------------------------------------------------------------------------------------
#opens the Tkinter GUI
root = Tk()
#Gives the Tkinter window a name
root.title('Animation')

User = Label(root, text = "Choose the animation you wish to see").grid(row = 1, column = 0)
###Identifies the Image that is to be shown in Tkinter
img = PhotoImage(file = "Snake.png") 
#Sets the canvas size of the interface
canvas = Canvas(root,height = 200, width = 200) 
#Sets the image height and width. Shows the Image on Tkinter
canvas.create_image(130,100,image = img) 
#Locates the position of the Image canvas
canvas.grid(row = 3, column = 0)
#Image for Eye
img2 = PhotoImage(file = "Eye.gif")
canvas = Canvas(root,height = 200, width = 200)
canvas.create_image(130,100,image = img2)
canvas.grid(row = 5, column = 0)
#Image for Curtains
img3 = PhotoImage(file = "Curtain.gif")
canvas = Canvas(root,height = 200, width = 200)
canvas.create_image(130,100,image = img3)
canvas.grid(row = 3, column = 1)
#Image for Heart 
img4 = PhotoImage(file = "Heart.gif")
canvas = Canvas(root,height = 200, width = 200)
canvas.create_image(130,100,image = img4)
canvas.grid(row = 5, column = 1)
#Image for Colour Wheel
img5 = PhotoImage(file = "colour_wheel.gif")
canvas = Canvas(root,height = 200, width = 200)
canvas.create_image(130,100,image = img5)
canvas.grid(row = 3, column = 2)
#Image for Rock Paper Scrissors
img6 = PhotoImage(file = "rpm.gif")
canvas = Canvas(root,height = 200, width = 200)
canvas.create_image(130,100,image = img6)
canvas.grid(row = 5, column = 2)


#---------------------------------------------------------Reset Animation-----------------------------------------------------------------------------------------------
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

#---------------------------------------------------------Snake Animation-----------------------------------------------------------------------------------------------
def food_item():

    food = []
    l_colour = []

    for i in range(0,350,60): #access one row with a step of 60
        food.append(random.randint(i,i+60)) #appends the value to the food list
    for x in food: #access the food list
        leds[x] = (random.randint(0,255),random.randint(0,255),random.randint(0,255)) #assigns the colour of the led position at random colours
        colour = list(leds[x]) #convert tuple into list
        l_colour.append(colour) #append the values onto the empty list


    client.put_pixels(leds)
    client.put_pixels(leds)
    sleep(0.1)

    return food,l_colour
    
def snake():

    reset()
    
    food,colour = food_item() #giving a variable to the return of the food_item() function
    
    body = 2 #the beginning of the body of the snake
    initial = (200,100,255) #initial colour of the snake
    
    for led in range (0,360): #this will run the whole of 360 leds
        for seg in range(body): #snake body
            leds[led+seg] = initial #1 - first iteration - snake at 0-5; 1-6 etc.
            if led > 0:
                leds[led-1] = (0,0,0) #background back to default
                
        client.put_pixels(leds)
        sleep(0.1)
        
        if led in food: #if snake hits food item:
            food.append(led) #appends the food from the list
            for i in colour: #runs through the list of colours
                change = tuple(i) #change list into tuples
                if initial != i: #not equal to i then make the initial to new colour
                    initial = change
                    client.put_pixels(leds)
                    
            body += 1 #increase body by 1
            client.put_pixels(leds)
            sleep(0.01)
            
        if led == 349: #if led is 358 the animation should stop
            break
        else:
            continue

#---------------------------------------------------------Eye Animation-----------------------------------------------------------------------------------------------
iris = [28,29,30,31,87,88,89,90,91,92,147,148,149,150,151,152,207,208,209,210,211,212,267,268,269,270,271,272,328,329,330,331]

def command(*args):
    print(var.get())

def option():
    
    opt = ['Blink','Flash']
    clicked = StringVar()
    clicked.set('Eye Animation')
    drop = OptionMenu(root, clicked, command = command).pack()
    
def eye():
    
    for loop in range(4): #runs the animation 4 times
        for i in range(0,360): #Run from 0 to 359
            
            if i == 360 or i == 0: #beginning random colour and when loop ends restart colour
                rand_colour = (random.randint(0,255),random.randint(0,255),random.randint(0,255)) #random colour
                 
            if i >= 25 and i <=34 or i >= 81 and i <= 98 or i >= 139 and i <= 160 or i >= 197 and i <= 222 or i >= 261 and i <= 278 or i >= 325 and i <= 334:
                leds[i] = (255,255,255) #when the range is between the values listed above change the colour to white
                client.put_pixels(leds)
                #sleep(0.1)
            
        for x in iris:
            leds[x] = rand_colour #when the range is between the values listed above change colour to the initial random generated colour
            client.put_pixels(leds)
            #sleep(0.02)

        for y in iris: #runs through the list 
            leds[i] = (0,0,0) #
            client.put_pixels(leds)
            sleep(0.02)
         
    blink() #calls the function blink() once finished
    
def build():

    reset()
    
    q = 3 #starts from the middle

    for i in range(4): #for q = 0
        for once in range(0,61): #access all leds i in rows
            if once == 60: #reaches 60 then decrement q
                q -= 1
                sleep(0.5)

            g = once + 60*q #access row from the top
            h = once + (300-60*q) #access row from the bottom

            #if the values from c and f is within the range, the led should be on
            if g >= 25 and g <=34 or g >= 81 and g <= 98 or g >= 139 and g <= 160 or h >= 197 and h <= 222 or h >= 261 and h <= 278 or h >= 325 and h <= 334:
                leds[g] = (255,255,255)
                client.put_pixels(leds)
                leds[h] = (255,255,255)
                client.put_pixels(leds)

    opt = str(input('Choose between F (Flash) or B (Blink): '))

    if opt == 'B':
        eye()
    elif opt == 'F':
        blinking()
    else:
        print('Invalid Answer')
        opt = str(input('Choose between F (Flash) or B (Blink): '))
            

def blinking():
    s = 1.0 ##maximum colour
    v = 1.0 ##maximum brightness
    rand_colour = (random.randint(0,255),random.randint(0,255),random.randint(0,255)) #random colour
    
    for i in range(0,360): #Run from 0 to 359

        rgb_fractional = colorsys.hsv_to_rgb(i/360, s, v) #colorsys returns floats between 0 and 1
        r_float = rgb_fractional[0] #extract said floating point numbers
        g_float = rgb_fractional[1]
        b_float = rgb_fractional[2]

        rgb = (r_float*255, g_float*255, b_float*255) #make new tuple with corrected values
        
##        if i == 360 or i == 0: #beginning random colour and when loop ends restart colour
##            rand_colour = (random.randint(0,255),random.randint(0,255),random.randint(0,255)) #random colour
        
    
        if i >= 25 and i <=34 or i >= 81 and i <= 98 or i >= 139 and i <= 160 or i >= 197 and i <= 222 or i >= 261 and i <= 278 or i >= 325 and i <= 334:
            leds[i] = (255,255,255) #when the range is between the values listed above change the colour to white
            client.put_pixels(leds)
            sleep(0.1)
       
        if i >= 28 and i <= 31 or i >= 87 and i <= 92 or i >= 147 and i <= 152 or i >= 207 and i <= 212 or i >= 267 and i <= 272 or i >= 328 and i <= 331:
            leds[i] = rand_colour #when the range is between the values listed above change colour to the initial random generated colour
            client.put_pixels(leds)
            sleep(0.01)
            client.put_pixels([rgb]*360) #sends out
            sleep(0.1)
            
    answer = messagebox.askquestion(title = 'Confirmation', message  = 'Do you wish to continue? ')
    #if yes start the building once again
    if answer == 'yes':
        build()       

def blink():

    inc = 0 #determines the row
    
    for i in range(4): #for inc = 3
        for once in range(0,61): #increment row by row
            if once == 60: #reaches 60 then increment inc
                sleep(0.5)
                inc += 1 #increment to access row
                
            c = once + 60*inc #access row from the top
            f = once + (300-60*inc) #access row from the bottom

            #if the values from c and f is within the range, the led should be off
            if c >= 25 and c <=34 or c >= 81 and c <= 98 or c >= 137 and c <= 162 or f >= 197 and f <= 222 or f >= 261 and f <= 278 or f >= 325 and f <= 334:
                leds[c] = (0,0,0) #close the rows above
                client.put_pixels(leds) #close the rows below
                leds[f] = (0,0,0)
                client.put_pixels(leds)
                leds[f-60] = (255,255,255) #leaves on row remaining 
                client.put_pixels(leds)
                
    #window would pop up, prompting the user to answer a question       
    answer = messagebox.askquestion(title = 'Confirmation', message  = 'Do you wish to continue? ')
    #if yes start the building once again
    if answer == 'yes':
        build()


#---------------------------------------------------------Curtain Animation-----------------------------------------------------------------------------------------------
def reverse():
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
        
def build1():
    led = 0

    reset()
    
    while led < 60: #scroll all rows at the same time
        for rows in range(2): #access the first two rows
            leds[led + rows*60] = (led+100,led+0,0) #row 1- 0-60
        for rows in range(2,4): #access the middle two rows
            leds[59-led + rows*60] = (led+100,led+0,0) #increment the red & green colour
        for rows in range(4,6): #access the last two rows
            leds[led + rows*60] = (led+100,led+0,0)
         
        led += 1 #increement the led to come together
        client.put_pixels(leds) #makes all the leds off at the same time
        sleep(0.1)
        
    reverse() #call the reverse function to set the simulator off
    
#---------------------------------------------------------Heart Animation-----------------------------------------------------------------------------------------------
#list of the leds for the parts of the heart
hearts = [[20,21,22,23],[78,79,80,81,
         82,83,84,85],[139,140,141,142,143,144,145,146,
         147],[200,201,202,203,204,205,206,207],[264,265,
         266,267],[326,327]]

hearts_1 = [[32,33,34,35],[89,90,91,92,93,94,95,96,
         97],[148,149,150,151,152,153,154,155,
         156],[208,209,210,211,212,213,214],
            [268,269,270],[328]]

sort = sorted(hearts + hearts_1) #adds the two lists together and sorts the list from smallest to largest

s = 1.0 ##maximum colour
v = 1.0 ##maximum brightness

def heart():
        for rows in range(len(sort)):
                one = sort[rows]
                for i in one:
                    rgb_fractional = colorsys.hsv_to_rgb(random.randint(i-5, i+5)/360.0, s, v) #colorsys returns floats between 0 and 1
                    r_float = rgb_fractional[0] #extract said floating point numbers
                    g_float = rgb_fractional[1] 
                    b_float = rgb_fractional[2]

                    rgb = (r_float*255, g_float*255, b_float*255) #make new tuple with corrected values
                    leds[i]=rgb
                    client.put_pixels(leds) #send out

                sleep(0.1) #20ms
        
def colour_merge():

    reset()
        
    led = 0
    
    for call in range(4): #runs the code four times
            rand = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            
            for rows in range(len(hearts)): #takes the length of the list
                    x = hearts[rows] #access the list of the list
                    for col in x: #col is the indes to acces the value of the lists of the list
                            leds[col] = (255,0,0) #colour of the led
                            #leds[col-1] = (200,50,0) #background back to default
                            
                    client.put_pixels(leds)
                    sleep(0.1)
                    
            for rows in range(len(hearts_1)):
                    y = hearts_1[rows]
                    for col1 in y:
                            leds[col1] = (255,255,255) #5 led is
                            #leds[col1] = (200,50,0) #background back to default
                            
                    client.put_pixels(leds)
                    sleep(0.1)

            for x in range(len(sort)):
                row = sort[x]
                for y in row:
                    leds[y] = (led+255,led+0,led+0) #increments the colour red to white
                    led += 1 #increases the led for increment of the colour red
                client.put_pixels(leds)
                sleep(0.1)

            heart() #after colour_merge function completes heart function is called

#---------------------------------------------------------Colour Wheel Animation-----------------------------------------------------------------------------------------------
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
    reset()

#---------------------------------------------------------Rock Paper Scissors Animation---------------------------------------------------------------------------------------------

def vs():
    
    led = 0
    
    for rows in range(6): #body of the leds
        leds[led+20 + rows*60] = (255,0,0) #allows for leds to be on each row. +20 
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

    for rows in range(2): #access the middle rows
        leds[led+32 + rows*60] = (255,0,0) #starts from 
        #leds[256-led + rows*60] = (112,128,144)
        client.put_pixels(leds)
        
    for rows in range(2):
        leds[217-led + rows*60] = (255,0,0)
        client.put_pixels(leds)

def decision():

    reset()
    
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

    #repeated code from above
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

        #creates a diagonal shape when led increments
        #starting point from right to left
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

        #creates a diagonal shape when led increments
        #repeated code from above with different starting points (left to right)
        for rows in range(3): #access three rows 
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

        #
        for rows in range(6): #body of led
            leds[11-rows] = (255,255,255)
            leds[311-rows] = (255,255,255)
            client.put_pixels(leds)
            sleep(0.1)
            
        for i in range(10): #body of led
            for rows in range(6): #access all rows
                #simultaneously run all six rows starting point to end point
                leds[i+4 + rows*60] = (255,255,255)
                leds[5-led + rows*60] = (255,255,255)
            client.put_pixels(leds)
            sleep(0.1)
            
    #Code below is to show the possibility of winning with different combinations
    #compares the input of the user and computer against each other
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
        reset() #this allows the screen to go back to default colour
        
#Creates a button that indicates the name of the button
#.grid() is to place the location of the button
#command calls upon the animation library and its function that I wish to run
Snake = Button(root, text = 'Snake Animation', command = snake).grid(row = 2, column = 0)
Eye = Button(root, text = 'Eye Animation', command = build).grid(row = 4, column = 0)
TTT = Button(root, text = 'Curtain Animation', command = build1).grid(row = 2, column = 1) 
Heart = Button(root, text = 'Heart Animation', command = colour_merge).grid(row = 4, column = 1)
Random = Button(root, text = 'Colour Picker Animation', command = colour_pick).grid(row = 2, column = 2)
RPM = Button(root, text = 'Rock Paper Scissors', command = decision).grid(row = 4, column = 2)

root.mainloop() #allows the window to run infinite to be able to see the window
