
import re
import numpy as np
from itertools import product

def parse(fn):
    data = {}
    r = open(fn).read()
    for tile in r.split('Tile')[1:]:
        number, t = tile.split(':')
        number = int(number.strip())
        t = t.strip().replace('#', '1').replace('.','0')
        t = [[int(c) for c in row.strip()] for row in t.split('\n')]
        data[number] = np.array(t, np.uint8)
    return data
        
    
def solve(fn):

    p = parse(fn)
    
    # collect borders
    bord = {}
    for num, tile in p.items():
        borders = [
            tile[0, :], tile[-1, :], tile[:, 0], tile[:, -1],
            tile[0, :][::-1], tile[-1, :][::-1], tile[:, 0][::-1], tile[:, -1][::-1],
        ]
        bord[num] = borders
    
    # compare borders
    matches = {k: 0 for k in p}
    for (num, borders), (num2, borders2) in product(bord.items(), bord.items()):
        if num == num2: continue # no matches with itself
        for b1, b2 in product(borders, borders2[:4]):
            assert b1.shape == (10,)
            if (b1 - b2).sum() == 0:
                matches[num] += 1
    
    corners = 1
    for k, i in matches.items():
        if i == 2:
            print(k)
            corners *= k
            
    return corners


#1951    2311    3079
#2729    1427    2473
#2971    1489    1171

#corners = 

assert solve('input.txt') == 20899048083289

print(solve('input_big.txt'))
