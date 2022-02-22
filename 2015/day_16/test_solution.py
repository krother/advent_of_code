import pytest

from .solution import solve, solve2

INPUT = """
Sue 1: goldfish: 6, trees: 9, akitas: 0
Sue 2: goldfish: 7, trees: 1, akitas: 0
Sue 3: samoyeds: 2, trees: 3, akitas: 0
Sue 4: cars: 10, akitas: 6, perfumes: 7
Sue 5: goldfish: 4, trees: 4, cars: 2
"""


def test_solve():
    assert solve(INPUT) == 3

def test_solve2():
    assert solve2(INPUT) == 5
