import pytest

from .solution import solve, solve2

EXAMPLE = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""


def test_solve():
    assert solve(EXAMPLE) == 198


def test_solve2():
    assert solve2(EXAMPLE) == 230
