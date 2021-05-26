from tkinter import *
import math

class Sketchpad(Canvas):
    def __init__(self, parent, screen_w, screen_h, objs):
        super().__init__(parent, bg="white")
        self.objs = objs
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.origin_x = screen_w / 2
        self.origin_y = screen_h / 2
        self.orbit_obj = None
        self.degree = 90
        self.obj_len = 200
        self.draw()
        self.rotate()

    def screen_coord(self, x, y):
        return self.origin_x + x, self.origin_y - y

    def draw(self):

        x, y = self.screen_coord(0,0)
        
        center_w = 50
        self.create_oval(x + center_w, y + center_w, x - center_w, y - center_w, fill="orange")


        x, y = self.screen_coord(0, self.obj_len)
        orbit_w = 8
        self.orbit_obj = self.create_oval(x + orbit_w, y + orbit_w, x - orbit_w, y - orbit_w, fill = "blue")


    def rotate(self):
        print("rotating..." + str(self.degree))

        self.degree = self.degree % 360
        rad = math.radians(self.degree)

        x = self.obj_len*math.cos(rad)
        y = self.obj_len*math.sin(rad)

        x, y = self.screen_coord(x,y)

        print("next location (" + str(x) + "," + str(y) + ")")

        self.delete(self.orbit_obj)
        self.orbit_obj = self.create_oval(x + 8, y + 8, x - 8, y - 8, fill = "blue")

        self.degree += 1
        self.after(100, self.rotate)