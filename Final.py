from tkinter import *
import Animation_1
import Animation_2
import Animation_3
import Animation_4

root = Tk()
root.title('Animation')

User = Label(root, text = "Choose the animation you wish to see").grid(row = 1, column = 0)


Snake = Button(root, text = 'Snake Animation', command = Animation_1.snake).grid(row = 2, column = 0)
Eye = Button(root, text = 'Eye Animation', command = Animation_2.build).grid(row = 3, column = 0)
TTT = Button(root, text = 'TicTacToe Animation', command = Animation_3).grid(row = 4, column = 0)
Heart = Button(root, text = 'Heart Animation', command = Animation_4.heart_shape).grid(row = 5, column = 0)

root.mainloop()
