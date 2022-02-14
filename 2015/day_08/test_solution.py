import pytest

from .solution import solve, solve2, size, encode

EXAMPLES = [
    ('""', 2, 0, 6),
    ('"ABC"', 5, 3, 9),
    (r'"aaa\"aaa"', 10, 7, 16),
    (r'"\x27"', 6, 1, 11)
]

INPUT = open('input_data.txt').read()

@pytest.mark.parametrize('s,total,chars,encoded', EXAMPLES)
def test_size(s, total, chars, encoded):
    assert size(s) == (total, chars)
    assert encode(s) == encoded

def test_solve():
    assert solve(INPUT) == 1371

def test_solve2():
    assert solve2(INPUT) == 2117
