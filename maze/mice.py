from maze import Maze
from maze.directions import directions
from maze.tiles import Wall_tile, Room_tile
from ui import graphics
import random


class Mouse:
    def __init__(self, x, y, dir = 0):
        self.x, self.y = x, y
        self.speed = 1 # тайлов в секунду
        self.dir = dir

    def draw(self):
        self.image = graphics.load_image('images/mouse.png', (0.5, 0.5))
        graphics.draw_image(self.image, self.x, self.y)

    def update(self, delta_time):
        # Ничего не умеет вообще
        pass


# немного интеллекта
class Mouse2(Mouse):
    def __init__(self, x, y, dir=0):
        super().__init__(x, y, dir)
        self.x, self.y = x, y
        self.size = 1 / 20  # доля тайла, тайлы 1x1
        self.speed = 1  # тайлов в секунду
        self.dir = dir

    def update(self, delta_time):
        cur_tile = Maze.get_tile(self.x, self.y)
        dx, dy = directions[self.dir]
        self.x += dx * self.speed * delta_time
        self.y += dy * self.speed * delta_time
        next_tile = cur_tile.get_neighb_tile(self.dir)
        if cur_tile.dist_to_border(self.x, self.y, self.dir) < 0.2 and (
                next_tile is None or isinstance(next_tile, Wall_tile)):
            self.dir = (self.dir - 1) % 4

class SmartMouse(Mouse):
    def __init__(self, x, y, dir=0):
        super().__init__(x, y, dir)
        self.x, self.y = x, y
        self.size = 1 / 20  # доля тайла, тайлы 1x1
        self.speed = 1  # тайлов в секунду
        self.dir = dir

    def check(self):
        if Maze.cheese and int(self.x) == int(Maze.cheese.x) and int(self.y) == int(Maze.cheese.y):
            return True
        return False

    def update(self, delta_time):
        if self.check():
            return
        cur_tile = Maze.get_tile(self.x, self.y)
        dx, dy = directions[self.dir]
        self.x += dx * self.speed * delta_time
        self.y += dy * self.speed * delta_time
        next_tile = cur_tile.get_neighb_tile(self.dir)
        if cur_tile.dist_to_border(self.x, self.y, self.dir) < 0.4 and (
                next_tile is None or isinstance(next_tile, Wall_tile)):
            self.dir = (self.dir - random.choice([-1, 1])) % 4






