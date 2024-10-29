import pytest

from solution import get_fuel, get_more_fuel


EXAMPLES = [
    (12, 2),
    (14, 2),
    (1969, 654),
    (100756, 33583),
]

@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert get_fuel(data) == expected

def test_get_more_fuel():
    assert get_more_fuel(100756) == 50346
