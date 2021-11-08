import pytest

from .solution import solve, get_next_symbol, get_next_row

EXAMPLES = (
    ("..^^.", 3, 6),
    (".^^.^.^^^^", 10, 38),
)

NEXT_ROW_EXAMPLES = (
    ("..^^.", ".^^^^"),
    (".^^^^", "^^..^"),
    (".^^.^.^^^^", "^^^...^..^"),
)

TRIPLET_EXAMPLES = (
    ("...", "."),
    ("..^", "^"),
    (".^.", "."),
    (".^^", "^"),
    ("^..", "^"),
    ("^.^", "."),
    ("^^.", "^"),
    ("^^^", "."),
)

@pytest.mark.parametrize('data,expected', TRIPLET_EXAMPLES)
def test_is_triplet_safe(data,expected):
    assert get_next_symbol(data) == expected


@pytest.mark.parametrize('data,expected', NEXT_ROW_EXAMPLES)
def test_get_next_row(data,expected):
    assert get_next_row(data) == expected

@pytest.mark.parametrize('data,nrows,expected', EXAMPLES)
def test_solve(data, nrows, expected):
    assert solve(data, nrows) == expected
