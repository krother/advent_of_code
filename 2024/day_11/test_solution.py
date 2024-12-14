import pytest

from solution import solve, solve2

INPUT = """125 17
"""

EXAMPLES = [(0, 0)]

# @pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve():
    assert solve(INPUT) == 55312
