from tkinter import *
from Sketchpad import Sketchpad

objs = [
    {}
]

root = Tk()
root.geometry("1000x1000")
root.update_idletasks()

sketchpad = Sketchpad(root,1000, 1000, objs)
sketchpad.pack(expand=True, fill='both')

root.mainloop()