import pytest

from solution import solve, solve2, is_valid, no_anagram

INPUT = """
aa bb cc dd ee
aa bb cc dd aa
aa bb cc dd aaa
"""

EXAMPLES = [

    ('aa bb cc dd ee', True),
    ('aa bb cc dd aa', False),
    ('aa bb cc dd aaa', True),
]

NO_ANAGRAMS = [
    ('abcde fghij', True),
    ('abcde xyz ecdab', False),
    ('a ab abc abd abf abj', True),
    ('iiii oiii ooii oooi oooo', True),
    ('oiii ioii iioi iiio', False),
]


@pytest.mark.parametrize('data,valid', EXAMPLES)
def test_is_valid(data, valid):
    assert is_valid(data) is valid


@pytest.mark.parametrize('data,valid', NO_ANAGRAMS)
def test_no_anagram(data, valid):
    assert no_anagram(data) is valid


def test_solve():
    assert solve(INPUT) == 2


def test_solve2():
    assert solve2(INPUT) == 2
