from tkinter import *

root = Tk()
root.title('Frame')

frame = LabelFrame(root, text="This is a frame.", padx=50, pady=50)
frame.pack(padx=10, pady=10)

b = Button(frame, text="I can't read.")
b2 = Button(frame, text="... or write.")
b.grid()
b2.grid()

root.mainloop()