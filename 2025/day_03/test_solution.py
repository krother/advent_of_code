from hypothesis import assume, given, strategies as st

from solution import solve, solve2, find_best_joltage


INPUT = """
987654321111111
811111111111119
234234234234278
818181911112111
"""

def test_solve():
    assert solve(INPUT) == 357

def test_solve2():
    assert solve2(INPUT) == 3121910778619

@given(st.lists(st.integers(min_value=1, max_value=9), 
                min_size=1, max_size=12,), 
       st.integers(min_value=1, max_value=10))
def test_one(bank, n):
    assume(n <= len(bank))
    j = find_best_joltage(tuple(bank), n)
    assert j > 0
