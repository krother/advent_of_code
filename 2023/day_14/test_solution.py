from solution import solve, solve2

INPUT = """
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""


def test_solve():
    assert solve(INPUT) == 136


def test_solve2():
    assert solve2(INPUT) == 64
