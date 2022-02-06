from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look, I made a button!")
    myLabel.pack()

myButton = Button(root, text="Click Me", command=myClick, fg="blue") # padx and pady manages overall size
myButton.pack()


root.mainloop()

