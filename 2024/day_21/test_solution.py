import pytest

from solution import solve, calc_complexity, PathCalculator

INPUT = """
029A
980A
179A
456A
379A
"""

EXAMPLES = [
    ("0", "<vA<AA>>^AvAA<^A>A"),
    ("029A", "<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A"),
    ("980A", "<v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A"),
    ("179A", "<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A"),
    ("456A", "<v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A"),
    ("379A", "<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A"),
]


@pytest.mark.parametrize("data,path", EXAMPLES)
def test_find_path(data, path):
    pc = PathCalculator(robots=2)
    assert pc.find_path_length(data) == len(path)


def test_calc_complexity():
    assert (
        calc_complexity(
            "029A",
            len("<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A"),
        )
        == 68 * 29
    )


def test_solve():
    assert solve(INPUT, robots=2) == 126384
