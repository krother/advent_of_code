import pytest

from solution import solve, solve2

INPUT = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

EXAMPLES = [
    (INPUT, 3)
]

@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert solve(INPUT) == 3

def test_solve2():
    assert solve2(INPUT) == 6
