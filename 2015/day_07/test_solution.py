import pytest

from .solution import solve, solve2, run

INPUT = """
123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
"""


def test_run():
    assert run(INPUT) == {
        'd': 72,
        'e': 507,
        'f': 492,
        'g': 114,
        'h': 65412,
        'i': 65079,
        'x': 123,
        'y': 456
    }

def test_solve():
    assert solve(open('input_data.txt').read()) == 3176

def test_solve2():
    assert solve2(open('input_data.txt').read()) == 14710
