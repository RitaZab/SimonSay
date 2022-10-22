import pygame as py
from settings import *
from sprites import *
import random

class Game:
    def __init__(self):
        py.init()
        self.screen=py.display.set_mode((WIDTH,HEIGHT))
        py.display.set_caption(TITLE)
        self.clock=py.time.Clock()

        self.basic_colors=[
            RED,GREEN,BLUE,YELLOW
        ]
        self.bright_colors=[MRED,MGREEN,MBLUE,MYELLOW]

        self.buttons=[
        Button(80,120,RED),
        Button(80,300,GREEN),
        Button(260,120, BLUE),
        Button(260,300,YELLOW)
    ]




    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        py.display.update()
        for button in self.buttons:
            button.draw_rectangle(self.screen)
        py.display.update()

    def run(self):
        self.playing=True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.draw()
            self.update()

    def new(self):
        pass

    def update(self):
        pass

    def events(self):
        for event in py.event.get():
            if event.type==py.QUIT:
                py.quit()

game=Game()
while True:
    game.new()
    game.run()


