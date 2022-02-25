from tkinter import *
import PIL
import Animation_1
import Animation_2
import Animation_3
import Animation_4

root = Tk()
root.title('Animation')

User = Label(root, text = "Choose the animation you wish to see").grid(row = 1, column = 0)
img = PhotoImage(file = "Snake.gif")
canvas = Canvas(root,height = 500, width = 500)
canvas.create_image(200,150,image = img)
canvas.grid(row = 3, column = 0)
img2 = PhotoImage(file = "Black.gif")
canvas = Canvas(root,height = 200, width = 100)
canvas.create_image(15,15,image = img2)
canvas.grid(row = 5, column = 0)
img3 = PhotoImage(file = "Black.gif")
canvas = Canvas(root,height = 200, width = 100)
canvas.create_image(15,15,image = img3)
canvas.grid(row = 7, column = 0)
img4 = PhotoImage(file = "Heart.gif")
canvas = Canvas(root,height = 200, width = 100)
canvas.create_image(200,250,image = img4)
canvas.grid(row = 9, column = 0)

Snake = Button(root, text = 'Snake Animation', command = Animation_1.snake).grid(row = 2, column = 0)
Eye = Button(root, text = 'Eye Animation', command = Animation_2.build).grid(row = 4, column = 0)
TTT = Button(root, text = 'TicTacToe Animation', command = Animation_3).grid(row = 6, column = 0)
Heart = Button(root, text = 'Heart Animation', command = Animation_4.heart_shape).grid(row = 8, column = 0)

root.mainloop()
