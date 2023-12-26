import pytest

from solution import solve, solve2

EXAMPLES = [
    (
        """
broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a
""",
        32000000,
    ),
    (
        """
broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> rx
""",
        11687500,
    ),
]


@pytest.mark.parametrize("data,expected", EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected


def test_solve2():
    assert solve2(EXAMPLES[1][0]) == 1
