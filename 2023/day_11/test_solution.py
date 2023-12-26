from solution import solve

INPUT = """
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""

INPUT2 = """
...#
....
#...
"""


def test_solve():
    assert solve(INPUT) == 374


def test_solve2():
    assert solve(INPUT, 9) == 1030
    assert solve(INPUT, 99) == 8410