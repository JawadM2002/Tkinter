from tkinter import *

root = Tk()

# Creating Label Widget
myLabel = Label(root, text="Hello World!").grid(row=0, column=0)
myLabel2 = Label(root, text="My name is Jawad Mahmud").grid(row=1, column=5)
# Shoving it onto the screen

#myLabel.grid(row=0, column=0)
#myLabel2.grid(row=1, column=5)

root.mainloop()