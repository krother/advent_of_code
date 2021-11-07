"""
Advent of Code - Day 3

Challenge: Graphical Output

comment:
I wanted to use my own library to solve the challenge.
It works nice for the example set but not for the real data
(ignored the endless playing field)
"""
import arcade
from tilegamelib import TiledMap
from tilegamelib import TileSprite
from tilegamelib import Vector
from tilegamelib import Game
from tilegamelib.config import config
from tilegamelib.vector import RIGHT, DOWN


PUZZLEMAP = open("input.txt").read().strip()

DEFAULT_PATH = [RIGHT, RIGHT, RIGHT, DOWN]

config.RESOLUTION = (1250, 550)
config.GAME_NAME = "Advent of Code - Day 3"


class Traversal(Game):

    def __init__(self):
        super().__init__()
        self.map = TiledMap(self.tiles, PUZZLEMAP, offset=Vector(50, 50))
        self.sprite = TileSprite(self.tiles['b.pac_right'], Vector(0, 0),
                                 speed=2, offset=Vector(50, 10*32 + 50))
        self.trees_counted = 0
        self.path = DEFAULT_PATH.copy()

    def next_move(self):
        if not self.path:
            self.path = DEFAULT_PATH.copy()
            if self.map.at(self.sprite.pos) == '#':
                self.trees_counted += 1
                self.map.set(self.sprite.pos, 'a')
                print('TREE!')

        vec = self.path.pop(0)
        self.sprite.add_move(vec)

    def check_complete(self):
        if self.sprite.pos.y == self.map.size.y - 1:
            print(self.trees_counted)
            self.exit()

    def on_draw(self):
        """automatically called to draw everything"""
        arcade.start_render()
        self.map.draw()
        self.sprite.draw()

    def update(self, delta_time):
        """automatically called every frame"""
        if self.sprite.is_moving:
            self.sprite.update()
        else:
            self.next_move()
            self.check_complete()


if __name__ == '__main__':
    window = Traversal()
    arcade.run()
