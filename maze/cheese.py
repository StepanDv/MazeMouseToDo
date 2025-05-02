from ui import graphics
import settings
from ui import screen
import pygame

class Cheese:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = graphics.load_image('images/cheese.png')


    def draw(self):
        graphics.draw_image(self.image, self.x - 0.5, self.y - 0.5)