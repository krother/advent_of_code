import pytest

from .solution import solve, hash_generator, triplet_hash_generator, get_stretch_hash
from functools import partial

EXAMPLES = (
    ('abc', 1, 39),
    ('abc', 2, 92),
    ('abc', 64, 22728),
)

MD5_EXAMPLES = (
    ('abc', 1, '23734cd52ad4a4fb877d8a1e26e5df5f'),
    ('abc', 2, '63872b5565b2179bd72ea9c339192543'),
    ('abc', 10, '09c225f3c02c75d04627ae2e449891f0'),
    ('helloworld', 999, 'd5acb437b525e78a99c5a9a1c54d2c3f')
)

GEN3_EXAMPLES = (
    ('abc', 1, ('8', 18)),
    ('abc', 2, ('e', 39)),
    ('abc', 9, ('9', 92)),
)

STRETCH_MD5_EXAMPLES = (
    ('abc', 0, 0, '577571be4de9dcce85a041ba0410f29f'),
    ('abc', 0, 1, 'eec80a0c92dc8a0777c619d9bb51e910'),
    ('abc', 0, 2, '16062ce768787384c81fe17a7a60c7e3'),
    ('abc', 0, 2016, 'a107ff634856bb300138cac6568c0f24'),

)

STRETCH_EXAMPLES = (
    ('abc', 1, 10),
    ('abc', 64, 22551),
)


@pytest.mark.parametrize('salt,i,iterations,expected', STRETCH_MD5_EXAMPLES)
def test_get_stretch_hash(salt, i, iterations, expected):
    assert get_stretch_hash(salt, i,iterations) == expected

@pytest.mark.parametrize('salt,counter,expected', MD5_EXAMPLES)
def test_hash_generator(salt, counter, expected):
    g = hash_generator(salt)
    for _ in range(counter):
        md5 = next(g)
    assert md5 == expected


@pytest.mark.parametrize('salt,counter,expected', GEN3_EXAMPLES)
def test_triplet_hash_generator(salt, counter, expected):
    g = triplet_hash_generator(salt)
    for i in range(counter):
        count, md5, char = next(g)
    assert (char, count) == expected

@pytest.mark.parametrize('salt,counter,expected', EXAMPLES)
def test_solve(salt, counter, expected):
    assert solve(salt, counter) == expected

@pytest.mark.parametrize('salt,counter,expected', STRETCH_EXAMPLES)
def test_solve_stretch(salt,counter,expected):
    gen = partial(get_stretch_hash, iter=2016)
    assert solve(salt, counter, gen) == expected