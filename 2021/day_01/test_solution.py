import pytest

from .solution import solve, triple_window

NUMBERS = """199
200
208
210
200
207
240
269
260
263"""


def test_solve():
    assert solve(NUMBERS) == 7


def test_solve_triple():
    assert triple_window(NUMBERS) == 5
