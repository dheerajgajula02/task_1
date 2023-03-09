from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()


def testing():
    return "testing this"
    


button = Button(root, text="show", command=testing)
button.pack()
print(button.invoke())
root.mainloop()