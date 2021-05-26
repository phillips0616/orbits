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
        self.oribt_obj = None
        self.cur_x = None
        self.cur_y = None
        self.draw()

    def screen_coord(self, x, y):
        return self.origin_x + x, self.origin_y - y

    def draw(self):

        x, y = self.screen_coord(0,0)
        
        center_w = 50
        self.create_oval(x + center_w, y + center_w, x - center_w, y - center_w, fill="orange")


        x, y = self.screen_coord(0, 200)
        orbit_w = 8
        self.oribt_obj = self.create_oval(x + orbit_w, y + orbit_w, x - orbit_w, y - orbit_w, fill = "blue")

        self.cur_x = 0
        self.cur_y = 200

    def rotate(self, prev_degree):
        prev_x = self.cur_x
        prev_y = self.cur_y
        degree = prev_degree % 360
        rad = math.radians(degree)

        next_x = prev_x + prev_x*math.cos(rad)
        next_y = prev_y + prev_y*math.sin(rad)

        self.delete(self.oribt_obj)
        self.oribt_obj = self.create_oval(prev_x + next_x, prev_y + next_y, prev_x - next_x, prev_y - next_y, fill = "blue")

        self.cur_x = next_x
        self.cur_y = next_y