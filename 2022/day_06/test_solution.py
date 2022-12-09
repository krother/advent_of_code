import pytest

from solution import solve, solve2

EXAMPLES = [
    ('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 7, 19),
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5, 23),
    ("nppdvjthqldpwncqszvftbrmjlhg", 6, 23),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10, 29),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11, 26),
]


@pytest.mark.parametrize('data,expected,_', EXAMPLES)
def test_solve(data, expected,_):
    assert solve(data) == expected

@pytest.mark.parametrize('data,_,expected', EXAMPLES)
def test_solve2(data, _, expected):
    assert solve2(data) == expected
