
UP = 0, -1
DOWN = 0, 1
LEFT = -1, 0
RIGHT = 1, 0
UPLEFT = -1, -1
UPRIGHT = 1, -1
DOWNLEFT = -1, 1
DOWNRIGHT = 1, 1
MOVES8 = UP, DOWN, LEFT, RIGHT, UPLEFT, UPRIGHT, DOWNLEFT, DOWNRIGHT


DIRECTIONS4 = UP, RIGHT, DOWN, LEFT

def is_on_grid(x, y, grid):
    """should work for both np arrays and nested lists"""
    return (x >= 0 and y >= 0 and x < len(grid[0]) and y < len(grid))
