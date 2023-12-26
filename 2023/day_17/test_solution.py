import pytest

from solution import solve, solve2

EXAMPLES = [
    (
        """
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
""",
        102,
    ),
    (
        """
11111
22221
11111
11111
""",
        8,
    ),
    (
        """
2413
3215
3255
""",
        16,
    ),
]


@pytest.mark.parametrize("data,expected", EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected


def test_solve2():
    assert solve2(EXAMPLES[0][0]) == 94
