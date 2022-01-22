import tkinter as tk
from tkinter.messagebox import askquestion

root = tk.Tk()
root.title('Animation')

User = tk.Label(root, text = "Choose the animation you wish to see").grid(row = 1, column = 0)


def snake():
    import Animation_1    
##    answer = askquestion(title = 'Confirmation', message  = 'Do you wish to continue? ')
##    if answer == 'yes':
##        snake()
        
def eye():
    import Animation_2

    




Snake = tk.Button(root, text = 'Snake Animation', command = snake).grid(row = 2, column = 0)
#Question = tk.Button(root, text = 'Ask Yes/No', command = snake)
Eye = tk.Button(root, text = 'Eye Animation', command = eye).grid(row = 3, column = 0)



root.mainloop()
