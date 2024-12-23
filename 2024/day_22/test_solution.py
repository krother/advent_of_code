from solution import solve, solve2, get_secret

INPUT = """
1
10
100
2024
"""

INPUT2 = """
1
2
3
2024"""

SECRETS = [
    15887950,
    16495136,
    527345,
    704524,
    1553684,
    12683156,
    11100544,
    12249484,
    7753432,
    5908254,
]


def test_get_secret():
    sec = 123
    for s in SECRETS:
        sec = get_secret(sec)
        assert sec == s


def test_solve():
    assert solve(INPUT) == 37327623


def test_solve2():
    assert solve2(INPUT2) == 23
