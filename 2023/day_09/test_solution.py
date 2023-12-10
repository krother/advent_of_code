import pytest

from solution import solve, solve2, solve_diff

INPUT = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""

EXAMPLES = [
    ([0, 3, 6, 9, 12, 15], 18),
    ([10, 13, 16, 21, 30, 45], 68),
    ([9, 4, -1, -6, -11, -16, -21], -26),
    #([-7, -7, -85, -7936, -9894, -12195], 0),
]

@pytest.mark.parametrize('row,expected', EXAMPLES)
def test_solve_diff(row,expected):
    assert solve_diff(row) == expected

def test_solve2():
    assert solve2(INPUT) == 2
