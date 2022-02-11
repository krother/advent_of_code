import pytest

from .solution import solve, solve2

EXAMPLE = """
turn on 0,0 through 9, 9
turn off 5,5 through 9,9
toggle 5,0 through 9,9
"""

INPUT = open('input_data.txt').read()

def test_small():
    assert solve(EXAMPLE) == 75

def test_solve():
    assert solve(INPUT) == 400410

def test_solve2():
    assert solve2(INPUT) == 15343601
