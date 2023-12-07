import pytest

from solution import solve, solve2, Hand

INPUT = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

EXAMPLES = [
    ("JJJJJ", 7),
    ("JJJJA", 7),
    ("JJJAA", 7),
    ("JJAAA", 7),
    ("JAAAA", 7),
    ("AAAAA", 7),
    ("AAAAK", 6),
    ("JAAAK", 6),
    ("JJAAK", 6),
    ("JJJAK", 6),
    ("AAAKK", 5),
    ("JAAKK", 5),
    ("AAA12", 4),
    ("JAA12", 4),
    ("JJA12", 4),
    ("AAKK1", 3),
    ("AA123", 2),
    ("JA123", 2),
    ("AK123", 1),
]
@pytest.mark.parametrize("cards,quality", EXAMPLES)
def test_examples(cards, quality):
    assert Hand(cards, 0, jokers=True).quality == quality

def test_solve():
    assert solve(INPUT) == 6440

def test_solve2():
    assert solve2(INPUT) == 5905
