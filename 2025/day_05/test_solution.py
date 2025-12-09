
#from hypothesis import assume, given, strategies as st
from solution import solve, solve2

INPUT = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""

def test_solve():
    assert solve(INPUT) == 3

def test_solve2():
    assert solve2(INPUT) == 14


"""
@given(st.lists(st.integers(min_value=1, max_value=100), 
                min_size=10, max_size=70,),
       st.lists(st.integers(min_value=1, max_value=100), 
                min_size=0, max_size=40),
)
def _test_one(numbers, points):
    numbers = set(numbers)
    data = ""
    for i in range(0, len(points) - 1, 2):
        start, end = points[i: i + 2]
        while start not in numbers and start < 101:
            start += 1
        e = start
        while e in numbers and e < end:
            e += 1
        if start < 101:
            data += f"{start}-{e}\n"
    data += "\n123"

    assert solve2(data) == len(numbers)

"""