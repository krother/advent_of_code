import pytest

from .solution import solve, solve2

INPUT = """
e => H
e => O
H => HO
H => OH
O => HH

HOHOHO
"""

TRANSITIONS = open('input_data.txt').read().split('\n\n')[0] + '\n\n'

EXAMPLES = [
    ('SiRnBPTiMgAr', (4, 'Ca')),
    ('CRnFYFAr', (1, 'O')),
    ('CRnMgAr', (1, 'O')),
    ('CRnTiMgAr', (2, 'O')),
    ('CaCaCaCaCaCaCaCaCaCaCaCaCa', (12, 'Ca')),
    ('TiRnPBSiThRnFArAr', (5, 'B')),
    ('TiRnPBSiThRnCaFArAr', (6, 'B')),
    ('CRnCaFYCaFAr', (3, 'O')),
]


def test_solve():
    assert solve(INPUT) == 7

def test_solve2():
    assert solve2(INPUT) == (5, 'H')

@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve2_examples(data, expected):
    assert solve2(TRANSITIONS + data) == expected
