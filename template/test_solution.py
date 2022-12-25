import pytest

from solution import solve, solve2

INPUT = """
"""

EXAMPLES = [
    (0, 0)
]

#@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve():
    assert solve(INPUT) == ...

def test_solve2():
    assert solve2(INPUT) == INPUT
