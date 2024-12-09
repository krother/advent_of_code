import pytest

from solution import solve, solve2

INPUT = """2333133121414131402
"""

EXAMPLES = [
    (0, 0)
]

#@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve():
    assert solve(INPUT) == 1928

def test_solve2():
    assert solve2(INPUT) == 2858
