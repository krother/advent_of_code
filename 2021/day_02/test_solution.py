import pytest

from .solution import solve, solve2

COURSE = """forward 5
down 5
forward 8
up 3
down 8
forward 2
"""


def test_solve():
    assert solve(COURSE) == 150

def test_solve2():
    assert solve2(COURSE) == 900
