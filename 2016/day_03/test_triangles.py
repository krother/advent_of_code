
import pytest
from triangles import check_triangle, count_correct_triangles, read_triangles_vertical

EXAMPLES = [
    ((1, 1, 1), True),
    ((1, 1, 2), False),
    ((1, 2, 1), False),
    ((2, 1, 1), False),
    ((5, 3, 7), True),
    ((2, 2, 1), True),
    ((5, 10, 25), False)
]

COUNT_EXAMPLES = [
    ([(1,1,1), (1,1,2)], 1),
    ([(1,1,2)], 0)

]


@pytest.mark.parametrize('sides, correct', EXAMPLES)
def test_check_triangle(sides, correct):
    assert check_triangle(*sides) == correct


@pytest.mark.parametrize('data, count', COUNT_EXAMPLES)
def test_count_correct_triangles(data, count):
    assert count_correct_triangles(data) == count


def test_read_triangles_vertical():
    data = """101 301 501
102 302 502
103 303 503""".split('\n')
    """201 401 601
202 402 602
203 403 603"""
    result = read_triangles_vertical(data)
    assert len(result) == 3
    assert (301, 302, 303) in result
