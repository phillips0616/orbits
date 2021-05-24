from tkinter import *

class Sketchpad(Canvas):
    def __init__(self, parent, objs):
        super().__init__(parent, bg="white")
        self.objs = objs


