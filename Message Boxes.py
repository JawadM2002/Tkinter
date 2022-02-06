from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Message Box')

def popup():
   response = messagebox.askyesno("This is a message!", "Hello world!")
   Label(root, text=response).pack()
 #  if response == 1:
 #      Label(root, text="You Clicked yes!").pack()
  # else:
   #    Label(root, text="NOOOO!!!!!").pack()

Button(root, text="Popup", command=popup).pack()

root.mainloop()