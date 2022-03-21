import pytest

from .solution import solve

INPUT = """
.#.#.#
...##.
#....#
..#...
#.#..#
####..
"""


def test_solve():
    assert solve(INPUT, 4) == 4

def test_solve2():
    assert solve(INPUT,  5, True) == 17
