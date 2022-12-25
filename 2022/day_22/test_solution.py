
from solution import solve
from aoc.directions import UP, DOWN, LEFT, RIGHT


INPUT = """        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5
"""
TEST_3D_EDGES = [

    (RIGHT, (16, 8), DOWN, 4, (11, 3), UP, LEFT),
    (RIGHT, (12, 3), UP, 4, (15, 8), DOWN, LEFT),

    (DOWN, (0, 8), RIGHT, 4, (11, 11), LEFT, UP),
    (DOWN, (11, 12), LEFT, 4, (0, 7), RIGHT, UP),

    (DOWN, (4, 8), RIGHT, 4, (8, 11), UP, RIGHT),
    (LEFT, (7, 11), UP, 4, (4, 7), RIGHT, UP),

    (UP, (0, 3), RIGHT, 4, (11, 0), LEFT, DOWN),
    (UP, (11, -1), LEFT, 4, (0, 4), RIGHT, DOWN),

    (UP, (12, 7), RIGHT, 4, (11, 7), UP, LEFT),
    (RIGHT, (12, 7), UP, 4, (12, 8), RIGHT, DOWN),

    (UP, (4, 3), RIGHT, 4, (8, 0), DOWN, RIGHT),
    (LEFT, (7, 0), DOWN, 4, (4, 4), RIGHT, DOWN),

    (LEFT, (-1, 4), DOWN, 4, (11, 15), LEFT, UP),
    (DOWN, (11, 16), LEFT, 4, (0, 4), DOWN, RIGHT),

]

TEST_2D_EDGES = [
    (UP, (0, 3), RIGHT, 8, (0, 7), RIGHT, UP),
    (DOWN, (0, 8), RIGHT, 8, (0, 4), RIGHT, DOWN),

    (UP, (8, -1), RIGHT, 4, (8, 11), RIGHT, UP),
    (DOWN, (8, 12), RIGHT, 4, (8, 0), RIGHT, DOWN),

    (UP, (12, 7), RIGHT, 4, (12, 11), RIGHT, UP),
    (DOWN, (12, 12), RIGHT, 4, (12, 8), RIGHT, DOWN),

    (LEFT, (7, 0), DOWN, 4, (11, 0), DOWN, LEFT),
    (RIGHT, (12, 0), DOWN, 4, (8, 0), DOWN, RIGHT),

    (LEFT, (-1, 4), DOWN, 4, (11, 4), DOWN, LEFT),
    (RIGHT, (12, 4), DOWN, 4, (0, 4), DOWN, RIGHT),

    (LEFT, (7, 8), DOWN, 4, (15, 8), DOWN, LEFT),
    (RIGHT, (16, 8), DOWN, 4, (8, 8), DOWN, RIGHT),
]


def test_solve():
    assert solve(INPUT, TEST_2D_EDGES) == 6032

def test_solve2():
    assert solve(INPUT, TEST_3D_EDGES) == 5031
