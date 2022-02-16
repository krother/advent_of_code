import pytest

from .solution import solve

EXAMPLES = [
    ('abcdef', 609043),
    ('pqrstuv', 1048970),
    ('bgvyzdsv', 254575)
]

@pytest.mark.parametrize('key,adv', EXAMPLES)
def test_solve(key, adv):
    assert solve(key) == adv

def test_solve2():
    assert solve('bgvyzdsv', '000000') == 1038736
