import pytest

from .solution_notree import solve, solve2, reduce, magnitude, split, add, add_multiple, to_list, to_string


INPUT = """
[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"""

SPLITS = [
    (10, [5, 5]),
    (11, [5, 6]),
    (12, [6, 6])
]

REDUCES = [

    ('[[[[[9,8],1],2],3],4]', '[[[[0,9],2],3],4]'),
    ('[7,[6,[5,[4,[3,2]]]]]', '[7,[6,[5,[7,0]]]]'),
    ('[[6,[5,[4,[3,2]]]],1]', '[[6,[5,[7,0]]],3]'),
    ('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]', '[[3,[2,[8,0]]],[9,[5,[7,0]]]]'),
    ('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]', '[[3,[2,[8,0]]],[9,[5,[7,0]]]]'),
    ('[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]', '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]'),
    ('[[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]]', '[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]'),
]


ADD = [
    ('[[[[4,3],4],4],[7,[[8,4],9]]]', '[1,1]', '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]'),
    ('[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]', '[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]', '[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]'),
]

MULTI_ADD = [
    ('''[1,1]
[2,2]
[3,3]
[4,4]
''', '[[[[1,1],[2,2]],[3,3]],[4,4]]'),
    ('''[1,1]
[2,2]
[3,3]
[4,4]
[5,5]''', '[[[[3,0],[5,3]],[4,4]],[5,5]]'),

    ('''[1,1]
[2,2]
[3,3]
[4,4]
[5,5]
[6,6]''','[[[[5,0],[7,4]],[5,5]],[6,6]]'),

    ('''[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]
''', '[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]'),
]
@pytest.mark.parametrize('data,result', REDUCES)
def test_sanity(data, result):
    assert to_string(to_list(data)) == data

@pytest.mark.parametrize('data,result', SPLITS)
def test_split(data, result):
    assert split(data) == result

@pytest.mark.parametrize('data,result', REDUCES)
def test_explode(data, result):
    assert reduce(data) == result



MAGNITUDE = [
    ([[1,2],[[3,4],5]], 143),
    ([[[[0,7],4],[[7,8],[6,0]]],[8,1]], 1384),
    ([[[[1,1],[2,2]],[3,3]],[4,4]], 445),
    ([[[[3,0],[5,3]],[4,4]],[5,5]], 791),
    ([[[[5,0],[7,4]],[5,5]],[6,6]], 1137),
    ([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]], 3488)
]


@pytest.mark.parametrize('data,result', MAGNITUDE)
def test_magnitude(data, result):
    assert magnitude(data) == result, f"should have been {result}"


@pytest.mark.parametrize('a,b,result', ADD)
def test_add(a,b, result):
    assert add(a,b) == result

@pytest.mark.parametrize('data,result', MULTI_ADD)
def test_add_multiple(data, result):
    assert add_multiple(data) == result

def test_solve():
    assert solve(INPUT) == 4140

def test_solve2():
    assert solve2(INPUT) == 3993
