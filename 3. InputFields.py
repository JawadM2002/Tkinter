from tkinter import *

root = Tk()

e = Entry(root, width=50, borderwidth=50)
e.pack()
e.insert(0, "Enter Name: ")

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text="Enter Name", command=myClick, fg="blue") # padx and pady manages overall size
myButton.pack()


root.mainloop()