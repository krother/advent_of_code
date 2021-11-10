
import pytest
from ip import has_tls, has_ssl

EXAMPLES = [
    ('abba[mnop]qrst', True),
    ('abcd[bddb]xyyx', False),
    ('ioxxoj[asdfgh]zxcvbn', True),
    ('aaaa[qwer]tyui', False),
    ('aaaa[qwer]xyyx', True),
    ('abba[aaaa]abc', True),
    ('ab[abcd]ba', False)
]

SSL_EXAMPLES = [
    ('aba[bab]xyz', True),
    ('xyx[xyx]xyx', False),
    ('aaa[kek]eke', True),
    ('zazbz[bzb]cdb', True),
    ('zzzabab[aba]xxx', True),
    ('zzzabab[aaa]xxx', False),
    ('zazbzaz[bzb]xxx', True)

]
@pytest.mark.parametrize('code,result', EXAMPLES)
def test_has_tls(code, result):
    assert has_tls(code) == result

@pytest.mark.parametrize('code,result', SSL_EXAMPLES)
def test_has_ssl(code, result):
    assert has_ssl(code) == result
