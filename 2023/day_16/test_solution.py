from solution import solve, solve2

INPUT = r"""
.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
"""


def test_solve():
    assert solve(INPUT) == 46


def test_solve2():
    assert solve2(INPUT) == 51
