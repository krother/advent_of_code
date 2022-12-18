import pytest

from solution import solve, solve2

INPUT = """
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
"""

EXTRAS = """
[2,3,4]
[4]

[[2,3], 9]
[[5,1]]

[[5,3], 9]
[[5,3], 1]

[[1,2,3]]
[[1,2]]

[[1,2], 9]
[[1,2,3], 1]
"""

EXAMPLES = zip((INPUT + EXTRAS).split('\n\n'), [1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1])

@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_pair(data, expected):
    assert solve(data) == expected


def test_solve():
    assert solve(INPUT) == 13

def test_solve2():
    assert solve2(INPUT) == 140
