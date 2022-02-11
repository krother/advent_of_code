import pytest

from .solution import solve, solve2, is_nice, is_nice2

EXAMPLES = [
    ('ugknbfddgicrmopn', True),
    ('aaa', True),
    ('haegwjzuvuyypxyu', False),
    ('jchzalrnumimnmhp', False),
    ('dvszwmarrgswjxmb', False),
]

EXAMPLES2 = [
    ('qjhvhtzxzqqjkmpb', True),
    ('xxyxx', True),
    ('uurcxstgmygtbstg', False),
    ('ieodomkazucvgmuy', False),
]

INPUT = '\n'.join([a for a, _ in EXAMPLES])

@pytest.mark.parametrize('data,nice', EXAMPLES)
def test_is_nice(data, nice):
    assert is_nice(data) == nice


@pytest.mark.parametrize('data,nice', EXAMPLES2)
def test_is_nice2(data, nice):
    assert is_nice2(data) == nice

def test_solve():
    assert solve(INPUT) == 2

def test_solve_long():
    assert solve(open('input_data.txt').read()) == 255

def test_solve2():
    assert solve2(open('input_data.txt').read()) == 55
