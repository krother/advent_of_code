import pytest

from .solution import solve, solve2, count_presents

EXAMPLES = [
    (1, 10),
    (2, 30),
    (3, 40),
    (4, 70),
    (5, 60),
    (6, 120),
    (7, 80),
    (8, 150),
    (9, 130),
    (100, 2170),
    ]

@pytest.mark.parametrize('house,presents', EXAMPLES)
def test_count_presents(house, presents):
    assert count_presents(house) == presents

@pytest.mark.parametrize('house,presents', EXAMPLES)
def test_solve(house, presents):
    assert solve(presents) == house

def test_solve_input():
    assert solve(29_000_000) == 665280


@pytest.mark.parametrize('house,presents', EXAMPLES)
def test_solve2(house, presents):
    assert solve2(presents) == house * 11 // 10

