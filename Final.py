from tkinter import *
import Animation_1
import Animation_2

root = Tk()
root.title('Animation')

User = Label(root, text = "Choose the animation you wish to see").grid(row = 1, column = 0)


Snake = Button(root, text = 'Snake Animation', command = Animation_1.snake).grid(row = 2, column = 0)
Eye = Button(root, text = 'Eye Animation', command = Animation_2.eye).grid(row = 3, column = 0)

root.mainloop()
