
import re

INPUT = "R2, L1, R2, R1, R1, L3, R3, L5, L5, L2, L1, R4, R1, R3, L5, L5, R3, L4, L4, R5, R4, R3, L1, L2, R5, R4, L2, R1, R4, R4, L2, L1, L1, R190, R3, L4, R52, R5, R3, L5, R3, R2, R1, L5, L5, L4, R2, L3, R3, L1, L3, R5, L3, L4, R3, R77, R3, L2, R189, R4, R2, L2, R2, L1, R5, R4, R4, R2, L2, L2, L5, L1, R1, R2, L3, L4, L5, R1, L1, L2, L2, R2, L3, R3, L4, L1, L5, L4, L4, R3, R5, L2, R4, R5, R3, L2, L2, L4, L2, R2, L5, L4, R3, R1, L2, R2, R4, L1, L4, L4, L2, R2, L4, L1, L1, R4, L1, L3, L2, L2, L5, R5, R2, R5, L1, L5, R2, R4, R4, L2, R5, L5, R5, R5, L4, R2, R1, R1, R3, L3, L3, L4, L3, L2, L2, L2, R2, L1, L3, R2, R5, R5, L4, R3, L3, L4, R2, L5, R5"

x, y = 0, 0
bearing = "N"

locs = set()
p2solved = False

for direction, steps in re.findall("(\w)(\d+)", INPUT):
    if direction == 'R':
        bearing = dict(zip("NOSW", "OSWN"))[bearing]
    else:
        bearing = dict(zip("NOSW", "WNOS"))[bearing]
    dx, dy = dict(zip("NOSW", ((0, 1), (1, 0), (0, -1), (-1, 0))))[bearing]
    x += dx * int(steps)
    y += dy * int(steps)
    if not p2solved and (x, y) in locs:
        print('part 2:', abs(x) + abs(y))
        p2solved = True
    locs.add((x, y))
    
print('part 1:', abs(x) + abs(y))
