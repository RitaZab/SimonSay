import pygame as py
from settings import *

class Button:
    def __init__(self, x,y,color):
        self.x=x
        self.y=y
        self.color=color

    def draw_rectangle(self,screen):
        py.draw.rect(screen, self.color,(self.x,self.y,BUTTON_SIZE,BUTTON_SIZE))

    def isClicked(self,mouse_x, mouse_y):
        return self.x<=mouse_x<=(self.x+BUTTON_SIZE) and self.y<=mouse_y<=(self.y+BUTTON_SIZE)
        #its determinates if we clicked on the coordinates inside the rectangle