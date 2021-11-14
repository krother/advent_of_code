import pytest

from .solution import count_pairs, parse_row, parse_grid, solve

COUNT_PAIR_EXAMPLES = (
    ("""root@ebhq-gridcenter# df -h
Filesystem              Size  Used  Avail  Use%
/dev/grid/node-x0-y0     10T    1T     9T   10%
/dev/grid/node-x0-y1     10T    2T     8T   20%""", 2),

    ("""root@ebhq-gridcenter# df -h
Filesystem              Size  Used  Avail  Use%
/dev/grid/node-x0-y0     10T    9T     1T   90%
/dev/grid/node-x0-y1     10T    8T     2T   80%""", 0),

    ("""root@ebhq-gridcenter# df -h
Filesystem              Size  Used  Avail  Use%
/dev/grid/node-x0-y0     10T    1T     9T   10%
/dev/grid/node-x0-y1     20T   16T     4T   80%""", 1),

    ("""root@ebhq-gridcenter# df -h
Filesystem              Size  Used  Avail  Use%
/dev/grid/node-x0-y0     10T    0T    10T    0%
/dev/grid/node-x0-y1     20T   16T     4T   80%""", 0),

    ("""root@ebhq-gridcenter# df -h
Filesystem              Size  Used  Avail  Use%
/dev/grid/node-x0-y0     10T    1T     9T   10%
/dev/grid/node-x0-y1     10T    8T     2T   80%
/dev/grid/node-x0-y1     20T    3T    17T   15%""", 5),
)

# Node A is not empty (its Used is not zero).
# Nodes A and B are not the same node.
# The data on node A (its Used) would fit on node B (its Avail).

PARSE_EXAMPLES = (
    ("/dev/grid/node-x0-y0     10T    9T     1T   90%", (0, 0, 9, 1)),
    ("/dev/grid/node-x0-y1     10T    8T     2T   80%", (0, 1, 8, 2)),
    ("/dev/grid/node-x4-y5     10T    7T     3T   70%", (4, 5, 7, 3)),
    ("/dev/grid/node-x2-y3     16T    8T     8T   50%", (2, 3, 8, 8)),
)

PARSE_GRID_EXAMPLES = (
    ("""Filesystem            Size  Used  Avail  Use%
/dev/grid/node-x0-y0   10T    8T     2T   80%
/dev/grid/node-x0-y1   11T    6T     5T   54%
/dev/grid/node-x0-y2   32T   28T     4T   87%
/dev/grid/node-x1-y0    9T    7T     2T   77%
/dev/grid/node-x1-y1    8T    0T     8T    0%
/dev/grid/node-x1-y2   11T    7T     4T   63%
/dev/grid/node-x2-y0   10T    6T     4T   60%
/dev/grid/node-x2-y1    9T    8T     1T   88%
/dev/grid/node-x2-y2    9T    6T     3T   66%""", """
..G
._.
#..
"""),

    ("""Filesystem            Size  Used  Avail  Use%
/dev/grid/node-x0-y0   10T    6T     4T   40%
/dev/grid/node-x0-y1   11T    6T     5T   54%
/dev/grid/node-x0-y2   32T   28T     4T   87%
/dev/grid/node-x1-y0   10T    0T    10T  100%
/dev/grid/node-x1-y1    8T    8T     0T    0%
/dev/grid/node-x1-y2   11T    7T     4T   63%
/dev/grid/node-x2-y0   10T    6T     4T   60%
/dev/grid/node-x2-y1    9T    8T     1T   88%
/dev/grid/node-x2-y2    9T    6T     3T   66%""", """
._G
...
#..
"""),

)

SOLVE_EXAMPLES = (
    ("""Filesystem            Size  Used  Avail  Use%
/dev/grid/node-x0-y0   10T    8T     2T   80%
/dev/grid/node-x0-y1   11T    6T     5T   54%
/dev/grid/node-x0-y2   32T   28T     4T   87%
/dev/grid/node-x1-y0    9T    7T     2T   77%
/dev/grid/node-x1-y1    8T    0T     8T    0%
/dev/grid/node-x1-y2   11T    7T     4T   63%
/dev/grid/node-x2-y0   10T    6T     4T   60%
/dev/grid/node-x2-y1    9T    8T     1T   88%
/dev/grid/node-x2-y2    9T    6T     3T   66%""", 7),

    ("""Filesystem            Size  Used  Avail  Use%
/dev/grid/node-x0-y0   10T    6T     4T   40%
/dev/grid/node-x0-y1   11T    6T     5T   54%
/dev/grid/node-x0-y2   32T   28T     4T   87%
/dev/grid/node-x1-y0   10T    0T    10T  100%
/dev/grid/node-x1-y1    8T    8T     0T    0%
/dev/grid/node-x1-y2   11T    7T     4T   63%
/dev/grid/node-x2-y0   10T    6T     4T   60%
/dev/grid/node-x2-y1    9T    8T     1T   88%
/dev/grid/node-x2-y2    9T    6T     3T   66%""", 6),

)

@pytest.mark.parametrize('data,expected', PARSE_EXAMPLES)
def test_parse_row(data, expected):
    assert parse_row(data) == expected

@pytest.mark.parametrize('data,expected', COUNT_PAIR_EXAMPLES)
def test_count_pairs(data, expected):
    assert count_pairs(data) == expected

@pytest.mark.parametrize('data,expected', PARSE_GRID_EXAMPLES)
def test_parse_grid(data, expected):
    assert str(parse_grid(data)) == expected.strip()


@pytest.mark.parametrize('data,expected', SOLVE_EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected