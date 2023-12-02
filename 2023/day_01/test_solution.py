import pytest

from solution import solve, solve2

EXAMPLES = [
    ("1abc2", 12),
    ("pqr3stu8vwx", 38),
    ("a1b2c3d4e5f", 15),
    ("treb7uchet", 77),
]
EXAMPLES2 = [
    ("two1nine", 29),
    ("eightwothree", 83),
    ("abcone2threexyz", 13),
    ("xtwone3four", 24),
    ("4nineeightseven2", 42),
    ("zoneight234", 14),
    ("7pqrstsixteen", 76),
]
EXAMPLES3 = [
    ("eight3eight", 88),
]

INPUT = "\n".join(word for word, _ in EXAMPLES)
INPUT2 = "\n".join(word for word, _ in EXAMPLES2)


@pytest.mark.parametrize("data,expected", EXAMPLES)
def test_solve_line(data, expected):
    assert solve(data) == expected


@pytest.mark.parametrize("data,expected", EXAMPLES2 + EXAMPLES3)
def test_solve_line2(data, expected):
    assert solve2(data) == expected


def test_solve():
    assert solve(INPUT) == 142


def test_solve2():
    assert solve2(INPUT2) == 281
