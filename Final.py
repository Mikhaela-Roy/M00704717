from tkinter import * #Use of GUI
import PIL #Use of Image library
import Animation_1 #Snake
import Animation_2 #Eye
import Animation_3 #Curtain
import Animation_4 #Heart
import Animation_5 #Colour Wheel
import Animation_6 #Rock Papaer Scissors

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

#Creates a button that indicates the name of the button
#.grid() is to place the location of the button
#command calls upon the animation library and its function that I wish to run
Snake = Button(root, text = 'Snake Animation', command = Animation_1.snake).grid(row = 2, column = 0)
Eye = Button(root, text = 'Eye Animation', command = Animation_2.build).grid(row = 4, column = 0)
TTT = Button(root, text = 'Curtain Animation', command = Animation_3.build).grid(row = 2, column = 1) 
Heart = Button(root, text = 'Heart Animation', command = Animation_4.heart).grid(row = 4, column = 1)
Random = Button(root, text = 'Colour Picker Animation', command = Animation_5.colour_pick).grid(row = 2, column = 2)
RPM = Button(root, text = 'Rock Paper Scissors Animation', command = Animation_6.decision).grid(row = 4, column = 2)

#closes the loop to run the code within the mainloop
root.mainloop()
