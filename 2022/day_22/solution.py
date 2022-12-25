"""
Monkey Map

https://adventofcode.com/2022/day/22
"""
import re
from aoc.directions import UP, DOWN, LEFT, RIGHT


TURNS = {
    RIGHT: {'L': UP, 'R': DOWN},
    LEFT: {'L': DOWN, 'R': UP},
    UP: {'L': LEFT, 'R': RIGHT},
    DOWN: {'L': RIGHT, 'R': LEFT}
}
DIR_VAL = dict(zip([RIGHT, DOWN, LEFT, UP], range(4)))

MAIN_2D_EDGES = [
    (UP, (50, -1), RIGHT, 50, (50, 149), RIGHT, UP),
    (DOWN, (50, 150), RIGHT, 50, (50, 0), RIGHT, DOWN),

    (UP, (100, -1), RIGHT, 50, (100, 49), RIGHT, UP),
    (DOWN, (100, 50), RIGHT, 50, (100, 0), RIGHT, DOWN),

    (UP, (0, 99), RIGHT, 50, (0, 199), RIGHT, UP),
    (DOWN, (0, 200), RIGHT, 50, (0, 100), RIGHT, DOWN),

    (LEFT, (-1, 100), DOWN, 50, (99, 100), DOWN, LEFT),
    (RIGHT, (100, 100), DOWN, 50, (0, 100), DOWN, RIGHT),

    (LEFT, (-1, 150), DOWN, 50, (49, 150), DOWN, LEFT),
    (RIGHT, (50, 150), DOWN, 50, (0, 150), DOWN, RIGHT),

    (LEFT, (49, 0), DOWN, 50, (149, 0), DOWN, LEFT),
    (RIGHT, (150, 0), DOWN, 50, (50, 0), DOWN, RIGHT),

    (LEFT, (49, 50), DOWN, 50, (99, 50), DOWN, LEFT),
    (RIGHT, (100, 50), DOWN, 50, (50, 50), DOWN, RIGHT),
]

MAIN_3D_EDGES = [

    # A
    (UP, (0, 99), RIGHT, 50, (50, 50), DOWN, RIGHT),
    (LEFT, (49, 50), DOWN, 50, (0, 100), RIGHT, DOWN),

    # B
    (RIGHT, (100, 50), DOWN, 50, (100, 49), RIGHT, UP),
    (DOWN, (100, 50), RIGHT, 50, (99, 50), DOWN, LEFT),

    # C
    (RIGHT, (50, 150), DOWN, 50, (50, 149), RIGHT, UP),
    (DOWN, (50, 150), RIGHT, 50, (49, 150), DOWN, LEFT),

    # D
    (RIGHT, (100, 100), DOWN, 50, (149, 49), UP, LEFT),
    (RIGHT, (150, 0), DOWN, 50, (99, 149), UP, LEFT),

    # E
    (DOWN, (0, 200), RIGHT, 50, (100, 0), RIGHT, DOWN),
    (UP, (100, -1), RIGHT, 50, (0, 199), RIGHT, UP),

    # F
    (UP, (50, -1), RIGHT, 50, (0, 150), DOWN, RIGHT),
    (LEFT, (-1, 150), DOWN, 50, (50, 0), RIGHT, DOWN),

    # G
    (LEFT, (49, 0), DOWN, 50, (0, 149), UP, RIGHT),
    (LEFT, (-1, 100), DOWN, 50, (50, 49), UP, RIGHT),
]


class Maze:

    def __init__(self, maze, edges):
        maze = maze.split('\n')
        maxrow = max(len(row) for row in maze)
        self.maze = [(row + ' ' * maxrow)[:maxrow] for row in maze]

        self.edges = self.create_edges(edges)

        startx = maze[0].index('.')
        starty = 0
        self.start_pos = startx, starty
        self.validate()

    def validate(self):
        # not empty
        assert len(self.maze[-1]) > 0

        # validate content
        for row in self.maze:
            for char in row:
                assert char in '#. '

        # validate row dimensions
        for row in self.maze:
            assert len(row) == self.xsize

        # start position on maze
        startx, starty = self.start_pos
        assert self.maze[starty][startx] == '.'

    def __repr__(self):
        return f"maze with {self.ysize} rows and {self.xsize} columns. Start at {self.start_pos}"

    @property
    def xsize(self):
        return len(self.maze[0])

    @property
    def ysize(self):
        return len(self.maze)

    def create_edges(self, edges):
        result = {}
        for enter, (x1, y1), (dx1, dy1), steps, (x2, y2), (dx2, dy2), leave in edges:
            for _ in range(steps):
                key = ((x1, y1), enter)
                assert key not in result
                result[key] = (x2, y2), leave
                x1, y1 = x1 + dx1, y1 + dy1
                x2, y2 = x2 + dx2, y2 + dy2
        return result

    def draw(self, pos):
        print()
        for y, row in enumerate(self.maze):
            for x, c in enumerate(row):
                if (x, y) == pos:
                    print('*', end="")
                else:
                    print(c, end='')
            print()
        print()
    
    def is_wall(self, pos):
        x, y = pos
        assert self.maze[y][x] in '#.'        
        return self.maze[y][x] == '#'

    def step(self, pos, bearing):
        x, y = pos
        dx, dy = bearing
        newpos = x + dx, y + dy
        return self.edges.get((newpos, bearing), (newpos, bearing))
        

    def next_pos(self, pos, bearing):
        newpos, newbearing = self.step(pos, bearing)
        if self.is_wall(newpos):
            return pos, bearing
        return newpos, newbearing


def parse(data, cube_size=None):
    maze, instructions = data.split('\n\n')
    maze = Maze(maze, cube_size)
    instructions = instructions.strip() + "L0R"  # dummy move at the end
    instructions = re.findall(r'(\d+)([RL])', instructions)
    instructions = [(int(a), b) for a, b in instructions]
    return maze, instructions, maze.start_pos


def solve(data, edges):
    maze, instructions, pos = parse(data, edges)
    bearing = RIGHT
    print(maze)
    #pprint(maze.edges)
    for steps, turn in instructions:
        # print(pos, bearing, steps, turn)
        #maze.draw(pos)
        for _ in range(steps):
            pos, bearing = maze.next_pos(pos, bearing)
        bearing = TURNS[bearing][turn]
        

    print('final', pos, bearing)
    x, y = pos
    return (y + 1) * 1000 + (x + 1) * 4 + DIR_VAL[bearing]



if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data, MAIN_2D_EDGES)
    print(f'Example 1: {result}')
    assert result == 122082

    result = solve(input_data, MAIN_3D_EDGES)
    print(f'Example 2: {result}')
