from tkinter import *

root = Tk()
root.title('Animation')

User = Label(root, text = "Choose the animation you wish to see").grid(row = 1, column = 0)


def snake():
    import Animation_1

def eye():
    import Animation_2
    


Snake = Button(root, text = 'Snake Animation', command = snake).grid(row = 2, column = 0)
Eye = Button(root, text = 'Eye Animation', command = eye).grid(row = 3, column = 0)

root.mainloop()
