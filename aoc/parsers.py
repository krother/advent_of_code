
import re
import numpy as np


def parse_numbers(data) -> [int]:
    """Grabs all integers from a string"""
    n = re.findall(r"-?\d+", data)
    return [int(i) for i in n]

    
def parse_2d_numbers(data):
    lines = data.strip().split('\n')
    bits = [list(map(int, row)) for row in lines]
    a = np.array(bits)
    return a

