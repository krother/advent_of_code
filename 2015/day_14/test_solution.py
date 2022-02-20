import pytest

from .solution import solve

INPUT = """
Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
"""


def test_solve():
    assert solve(INPUT, 1000) == (1120, 689)
