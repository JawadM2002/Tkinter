from tkinter import *


root = Tk()
root.title('Checkbox')
root.geometry("400x400")

def show():
	myLabel = Label(root, text=var.get()).pack()

var = StringVar()

c = Checkbutton(root, text="Checkbox, lads", variable=var, onvalue="On", offvalue="Off")
c.deselect()
c.pack()

myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()