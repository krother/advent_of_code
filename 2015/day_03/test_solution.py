import pytest

from .solution import solve, solve2

EXAMPLES = [
    ('>', 2),
    ('^>v<', 4),
    ('^v^v^v^v^v', 2),
    (open('input_data.txt').read(), 2592)
]

ROBO_EXAMPLES = [
    ('>', 2),
    ('^v', 3),
    ('^>v<', 3),
    ('^v^v^v^v^v', 11),
    (open('input_data.txt').read(), 2360)
]


@pytest.mark.parametrize('data,houses', EXAMPLES)
def test_solve(data, houses):
    assert solve(data) == houses

@pytest.mark.parametrize('data,houses', ROBO_EXAMPLES)
def test_solve2(data, houses):
    assert solve2(data) == houses
