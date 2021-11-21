import pytest

from .solution import solve

EXAMPLES = (
    ("""cpy 41 a""", (41, 0, 0, 0)),
    ("""cpy -1 a""", (-1, 0, 0, 0)),
    ("""cpy 42 a""", (42, 0, 0, 0)),
    ("""cpy 1 b""", (0, 1, 0, 0)),
    ("""cpy 7 b
cpy 8 c
""", (0, 7, 8, 0)),
    ("""cpy 7 b
cpy b d
""", (0, 7, 0, 7)),

    ("""inc a""", (1, 0, 0, 0)),
    ("""inc c""", (0, 0, 1, 0)),
    ("""inc a
inc a""", (2, 0, 0, 0)),

    ("""dec a""", (-1, 0, 0, 0)),
    ("""dec c""", (0, 0, -1, 0)),
    ("""dec a
dec a""", (-2, 0, 0, 0)),

    ("""inc a
dec a""", (0, 0, 0, 0)),
    ("""inc a
cpy a b
dec c
cpy c d""", (1, 1, -1, -1)),

    ("""inc a
dec a""", (0, 0, 0, 0)),

    ("""inc a
jnz a 2
dec a""", (1, 0, 0, 0)),

    ("""jnz 1 2
inc a""", (0, 0, 0, 0)),

    # loop
    ("""cpy 5 a
dec a
inc b
inc b
jnz a -3
""", (0, 10, 0, 0)),

    # fibonacci
    ("""cpy 6 c
inc b
cpy b d
dec d
inc a
jnz d -2
dec c
cpy a d
cpy b a
cpy d b
jnz c -7
""", (8, 13, 0, 13)),

    ("""cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a""", (42, 0, 0, 0)),

    ("""cpy 5 a
tgl 1
inc a""", (4, 0, 0, 0)),

    ("""cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a""", (3, 0, 0, 0)),

)


@pytest.mark.parametrize('data,registers', EXAMPLES)
def test_solve(data, registers):
    assert solve(data) == registers
