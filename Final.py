#Tkinter GUI Interface
from tkinter import *
#Image Library
import PIL
#Snake Animation
import Animation_1
#Eye Animation
import Animation_2
#TicTacToe Animation
import Animation_3
#Heart Animation 
import Animation_4

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
img2 = PhotoImage(file = "Eye.gif")
canvas = Canvas(root,height = 200, width = 200)
canvas.create_image(130,100,image = img2)
canvas.grid(row = 5, column = 0)
img3 = PhotoImage(file = "Curtain.gif")
canvas = Canvas(root,height = 200, width = 200)
canvas.create_image(130,100,image = img3)
canvas.grid(row = 3, column = 1)
img4 = PhotoImage(file = "Heart.gif")
canvas = Canvas(root,height = 200, width = 200)
canvas.create_image(130,100,image = img4)
canvas.grid(row = 5, column = 1)

#Creates a button that indicates the name of the button as well as locates the position of the button
Snake = Button(root, text = 'Snake Animation', command = Animation_1.snake).grid(row = 2, column = 0)                                                                                       
Eye = Button(root, text = 'Eye Animation', command = Animation_2.build).grid(row = 4, column = 0)
TTT = Button(root, text = 'Curtain Animation', command = Animation_3.build).grid(row = 2, column = 1) 
Heart = Button(root, text = 'Heart Animation', command = Animation_4.heart).grid(row = 4, column = 1)

#closes the loop to run the Tkinter GUI 
root.mainloop()
