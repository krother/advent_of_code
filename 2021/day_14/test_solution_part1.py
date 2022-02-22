import pytest

from .solution_part1 import solve, parse, step

INPUT = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""


def test_solve():
    """example copied from AoC site"""
    assert solve(INPUT, 10) == 1588


def test_parse():
    """test for helper function"""
    mol, rules = parse(INPUT)
    assert mol == 'NNCB'
    assert rules['CN'] == 'C'


EXAMPLES = [
    ('NNCB', 'NCNBCHB'),
    ('NCNBCHB', 'NBCCNBBBCBHCB'),
    ('NBCCNBBBCBHCB', 'NBBBCNCCNBBNBNBBCHBHHBCHB'),
    ('NBBBCNCCNBBNBNBBCHBHHBCHB', 'NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB')
]
@pytest.mark.parametrize('molecule,expected', EXAMPLES)
def test_step(molecule, expected):
    """more examples copied from AoC page"""
    _, rules = parse(INPUT)
    assert step('NNCB', rules) == 'NCNBCHB'

