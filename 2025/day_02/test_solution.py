import pytest

from solution import solve, solve2

INPUT = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124
"""

EXAMPLES = [
    (0, 0)
]

#@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve():
    assert solve(INPUT) == 1227775554

def test_solve2():
    assert solve2(INPUT) == 4174379265
