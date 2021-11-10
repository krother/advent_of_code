
from decoy import decrypt, parse, check

EXAMPLE = "aaaaa-bbb-z-y-x-123[abxyz]"
BAD_EXAMPLE = "totally-real-room-200[decoy]"
DECRYPT_EXAMPLE = "qzmt-zixmtkozy-ivhz-343[xxxx]"
DERYPCT_HELLO = 'gdkkn-1[xxx]'
DERYPCT_HELLO2 = 'fcjjm-2[xxx]'
DERYPCT_WORLD = 'vnqkc-1[xxx]'


def test_parse():
    assert parse(EXAMPLE) == (["aaaaa", "bbb", "z", "y", "x"], 123, "abxyz")

def test_check():
    assert check(EXAMPLE) == 123
    assert check(BAD_EXAMPLE) == 0
    assert check("not-a-real-room-404[oarel]") == 404

def test_decrypt():
    assert decrypt(DERYPCT_HELLO) == 'hello'
    assert decrypt(DERYPCT_HELLO2) == 'hello'
    assert decrypt(DERYPCT_WORLD) == 'world'
    assert decrypt(DECRYPT_EXAMPLE) == 'very encrypted name'
