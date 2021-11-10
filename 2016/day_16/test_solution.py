import pytest

from .solution import solve, dragon_step, get_checksum

DRAGON_EXAMPLES = (
    ('1', '100'),
    ('0', '001'),
    ('11', '11000'),
    ('00', '00011'),
    ('10', '10010'),
    ('11111', '11111000000')
)
CHECKSUM_EXAMPLES = (
    ('11', '1'),
    ('10', '0'),
    ('111111', '111'),
    ('1111', '1'),
    ('110010110100', '100'),
)

@pytest.mark.parametrize('data,expected', DRAGON_EXAMPLES)
def test_dragon_step(data, expected):
    assert dragon_step(data) == expected

@pytest.mark.parametrize('data,expected', CHECKSUM_EXAMPLES)
def test_checksum(data, expected):
    assert get_checksum(data) == expected

def test_solve():
    assert solve('10000', 20) == '01100'
