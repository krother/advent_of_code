
from math import sin, cos, radians
import numpy as np

DIRS = {
        'N': np.array([0, 1], np.int32),
        'S': np.array([0, -1], np.int32),
        'E': np.array([1, 0], np.int32),
        'W': np.array([-1, 0], np.int32),
}

ROT = np.array([
          [0, -1],
          [1,  0],
        ], np.int32)

def solve(fn):
    p = np.zeros(2, np.int32)
    w = np.array([10, 1], np.int32)
    
    for line in open(fn):
        char = line[0]
        m = int(line.strip()[1:])
        if char == 'L':
            for i in range(m // 90):
                w = np.dot(w, -ROT)
        elif char == 'R':
            for i in range(m // 90):
                w = np.dot(w, ROT)
            
        elif char in 'NSEW':
            w += DIRS[char] * m
        elif char == 'F':
            p += w * m
            
    return np.abs(p).sum()
        

assert solve('input.txt')  == 286
solve('input2.txt')
result = solve('input_big.txt')
assert result == 145117
