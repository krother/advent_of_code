
from hash import get_password, get_password2, get_next_index

def test_get_password():
    assert get_password('abc') == '18f47a30'

def test_get_password():
    assert get_password2('abc') == '05ace8e3'

def test_get_next_index():
    assert get_next_index('abc', 0) == (3231929, '1')
    assert get_next_index('abc', 3231929) == (5017308, '8')
