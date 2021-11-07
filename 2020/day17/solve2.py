
import re
import numpy as np
from itertools import product

start = [[0,1,0], # active=#
         [0,0,1],
         [1,1,1]]

big = """..#..#..
.###..#.
#..##.#.
#.#.#.#.
.#..###.
.....#..
#...####
##....#.""".replace('#', '1').replace('.', '0')
big = np.array([[int(x) for x in line] for line in big.split('\n')], dtype=int)

VECTORS = list(product([0, -1, 1], [0, -1, 1], [0, -1, 1], [0, -1, 1]))
VECTORS.pop(0)

start = big
SIZE = len(start[0]) + 12

def count_neighbors(cubes,x,y,z,q):
    nb = 0
    for vx,vy,vz,vq in VECTORS:
        nx, ny, nz, nq = x+vx, y+vy, z+vz, q+vq
        if (0 <= nx < SIZE) and (0 <= ny < SIZE) \
            and (0 <= nz < SIZE) and (0 <= nq < SIZE):
            if cubes[nx,ny,nz, nq]:
                nb += 1
    return nb

cubes = np.zeros((SIZE, SIZE, SIZE, SIZE), int)
#cubes[5:8, 5:8, 6, 6] = start
cubes[6:14, 6:14, 6, 6] = start

for i in range(6):
    new = np.zeros((SIZE, SIZE, SIZE, SIZE), int)
    for x,y,z,q in product(range(SIZE), range(SIZE), range(SIZE), range(SIZE)):
        nb = count_neighbors(cubes,x,y,z,q)
        if cubes[x,y,z,q] and nb in (2,3):
            new[x,y,z,q] = 1
        elif not cubes[x,y,z,q] and nb == 3:
            new[x,y,z,q] = 1
           
    cubes = new
    print(cubes.sum())

#assert solve('input.txt')  ==

#print(solve('input_big.txt'))
