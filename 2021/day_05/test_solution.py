import pytest

from .solution import solve, Vent

INPUT = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""

POINTS = [
    (1, 1, 3, 3, [(1,1), (2, 2), (3, 3)]),
    (3, 3, 1, 1, [(1,1), (2, 2), (3, 3)]),
    (5, 5, 8, 2, [(5,5), (6, 4), (7, 3), (8, 2)]),
]

@pytest.mark.parametrize('x1, y1, x2, y2, points', POINTS)
def test_points(x1, y1, x2, y2, points):
    v = Vent(x1, y1, x2, y2)
    assert list(sorted(v.get_points())) == points

def test_solve():
    assert solve(INPUT, diag=False) == 5

def test_solve2():
    assert solve(INPUT, diag=True) == 12
