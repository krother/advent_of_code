import pytest

from .solution import next_valid_password, next_candidate

EXAMPLES = [
    ('aaaaaaaa', 'aaaaaaab'),
    ('aaaaaaaz', 'aaaaaaba'),
    ('aaaaaazz', 'aaaaabaa'),
    ('azzzzzzz', 'baaaaaaa'),
]


@pytest.mark.parametrize('psw, expected', EXAMPLES)
def test_next_candidate(psw, expected):
    assert next_candidate(psw) == expected


def test_next_valid_password():
    assert next_valid_password('abcdefgh') == 'abcdffaa'
    assert next_valid_password('ghijklmn') == 'ghjaabcc'
