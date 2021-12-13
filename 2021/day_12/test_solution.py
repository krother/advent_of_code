import pytest

from .solution import solve, solve2

INPUTS = [
    ("""start-A
start-b
A-c
A-b
b-d
A-end
b-end
""", 10, 36),
("""dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc""", 19, 103),
("""fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW""", 226, 3509)
]

@pytest.mark.parametrize('data,expected,_', INPUTS)
def test_solve(data,expected,_):
    assert solve(data) == expected

@pytest.mark.parametrize('data,_,expected', INPUTS)
def test_solve2(data,_,expected):
    assert solve2(data) == expected
