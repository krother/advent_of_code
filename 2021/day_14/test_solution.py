
from .solution import solve, parse

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
    assert solve(INPUT, 10) == 1588

def test_solve2():
    assert solve(INPUT, 40) == 2188189693529

def test_parse():
    """test for helper function"""
    mol, rules = parse(INPUT)
    assert mol == 'NNCB'
    assert rules['CN'] == 'C'
