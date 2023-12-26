import pytest

from solution import solve, solve2, solve_line


EXAMPLES = [
    ("???.### 1,1,3", 1),
    (".??..??...?##. 1,1,3", 4),
    ("?#?#?#?#?#?#?#? 1,3,1,6", 1),
    ("????.#...#... 4,1,1", 1),
    ("????.######..#####. 1,6,5", 4),
    ("?###???????? 3,2,1", 10),
]
EXAMPLES2 = [
    ("?#?#??##?#? 2,5,1", 1),
    ("?????????? 1", 10),
    ("?????????? 10", 1),
]
EXAMPLES3 = [
    ("???.### 1,1,3", 1),
    (".??..??...?##. 1,1,3", 16384),
    ("?#?#?#?#?#?#?#? 1,3,1,6", 1),
    ("????.#...#... 4,1,1", 16),
    ("????.######..#####. 1,6,5", 2500),
    ("?###???????? 3,2,1", 506250),
]

INPUT = "\n".join(ex[0] for ex in EXAMPLES)


@pytest.mark.parametrize("data,expected", EXAMPLES + EXAMPLES2)
def test_solve_line(data, expected):
    assert solve_line(data) == expected


@pytest.mark.parametrize("data,expected", EXAMPLES3)
def test_solve_line_unfold(data, expected):
    assert solve_line(data, True) == expected


def test_solve():
    assert solve(INPUT) == 21


def test_solve2():
    assert solve2(INPUT) == 525152
