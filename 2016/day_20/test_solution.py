import pytest

from .solution import solve, merge_boundaries, count_ips

EXAMPLES = (
    ("""0-5""", 6),
    ("""0-3""", 4),
    ("""1-5""", 0),
    ("""2-5""", 0),
    ("""0-5
2-7""", 8),
    ("""0-5
7-8""", 6),
    
    ("""5-8
 0-2
 4-7""", 3),
)

COUNT_EXAMPLES = (
    ("""0-5""", 9, 4),
    ("""0-5""", 19, 14),
    ("""1-5""", 9, 5),
    ("""0-3""", 9, 6),
    ("""1-8""", 9, 2),
    ("""0-5
2-7""", 9, 2),
    ("""0-5
7-8""", 9, 2),
    ("""2-3
7-8""", 9, 6),    
    ("""5-8
0-2
4-7""", 9, 2),
)


MERGE_EXAMPLES = (
    ([(0, 5), (2, 7)], [(0, 7)]),
    ([(0, 5), (7, 8)], [(0, 5), (7, 8)]),
    ([(1, 2), (2, 5)], [(1, 5)]),
    ([(1, 2), (2, 5), (4, 7)], [(1, 7)]),
    ([(1, 2), (3, 5)], [(1, 5)]),
    ([(1, 8), (2, 4)], [(1, 8)]),
    ([(1, 3), (2, 5), (6, 8)], [(1, 8)]),
    ([(6, 8), (1, 3), (2, 5)], [(1, 8)]),
    ([(6, 8), (1, 3), (2, 5), (12, 15), (14, 20)], [(1, 8), (12, 20)]),
)


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected

@pytest.mark.parametrize('data,maxip,expected', COUNT_EXAMPLES)
def test_count_ips(data, maxip, expected):
    assert count_ips(data,maxip) == expected

@pytest.mark.parametrize('data,expected', MERGE_EXAMPLES)
def test_merge_boundaries(data, expected):
    assert merge_boundaries(data) == expected
