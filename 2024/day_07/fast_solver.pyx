"""
fast equation solver using Cython
NOT REALLY FASTER

compile with
python setup.py build_ext --inplace
"""
from itertools import product
import cython
from cython.cimports.libc.math import log10


def add(a: cython.int, b: cython.int) -> cython.int:
    return a + b


def mul(a: cython.int, b: cython.int) -> cython.int:
    return a * b


def concat(a: cython.int, b: cython.int) -> cython.int:
    # return int(str(a) + str(b))
    ndigits = 1 if b == 0 else int(log10(b)) + 1;
    return a * pow(10, ndigits) + b;

def check_equation(out, numbers, operators):
    start, *tail = numbers
    for oplist in product(operators, repeat=len(numbers) - 1):
        a = start
        for op, b in zip(oplist, tail):
            a = op(a, b)
        if a == out:
            return True
    