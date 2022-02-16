import re

import pytest

from .solution import solve, propagate

EXAMPLES = [
    ('1', '11'),
    ('11', '21'),
    ('21', '1211'),
    ('1211', '111221'),
    ('111221', '312211'),
]

INPUT = '1113122113'

@pytest.mark.parametrize('before,after', EXAMPLES)
def test_propagate(before, after):
    assert propagate(before) == after

def test_solve():
    assert solve(INPUT, 40) == 360154

def test_solve2():
    assert solve(INPUT, 50) == 5103798
