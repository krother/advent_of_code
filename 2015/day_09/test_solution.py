import pytest

from .solution import solve, solve2

INPUT = """
London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
"""


def test_solve():
    assert solve(INPUT) == 605

def test_solve_big():
    assert solve(open('input_data.txt').read()) == 251

def test_solve2():
    assert solve2(INPUT) == 982

def test_solve2_big():
    assert solve2(open('input_data.txt').read()) == 898
