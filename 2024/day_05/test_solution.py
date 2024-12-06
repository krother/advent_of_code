import pytest

from solution import solve, solve2

INPUT = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

EXAMPLES = [
    (0, 0)
]

#@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve():
    assert solve(INPUT) == 143

def test_solve2():
    assert solve2(INPUT) == 123
