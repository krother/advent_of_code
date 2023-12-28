"""
Step Counter

https://adventofcode.com/2023/day/21
"""
import numpy as np
from aoc.parsers import parse_hash_grid
from pprint import pprint


FRONT = slice(None, -1)
BACK = slice(1, None)
ALL = slice(None, None)
SLICES = [
    (BACK, ALL, FRONT, ALL),
    (FRONT, ALL, BACK, ALL),
    (ALL, BACK, ALL, FRONT),
    (ALL, FRONT, ALL, BACK),
]


def parse(data):
    start = data.strip().index("S")
    row_len = len(data.strip().split("\n")[0])
    x, y = start % (row_len + 1), start // (row_len + 1)
    garden = parse_hash_grid(data.replace("S", "."))
    garden *= 2
    return garden, (x, y)


def flood_fill_step(garden, path):
    b = garden.copy()
    for k, l, m, n in SLICES:
        a = garden.copy()
        a[k, l] += path[m, n]
        b[np.where(a == 1)] = 1
    return b


def solve(data, steps):
    garden, start = parse(data)
    path = garden.copy()
    x, y = start
    path[y, x] = 1
    for _ in range(steps):
        path = flood_fill_step(garden, path)

    x = np.where(path == 1)
    return len(x[0])


def fill_garden(garden, start):
    """return long it takes to fill a garden"""
    reached = [1]
    path = garden.copy()
    x, y = start
    path[y, x] = 1
    while len(reached) < 3 or reached[-3] != n:
        path = flood_fill_step(garden, path)
        n = len(np.where(path == 1)[0])
        reached.append(n)

    reached.pop()
    return reached


def count_reached(steps, progression):
    if steps < 0:
        return 0
    if steps < len(progression):
        return progression[steps]
    if steps % 2 == len(progression) % 2:
        return progression[-2]
    return progression[-1]


def solve2(data, steps):
    print("-" * 60)
    print(f"steps                          : {steps:20}")

    garden, start = parse(data)
    size = garden.shape[0]
    max_xy = size - 1
    middle_xy = size // 2

    # calculate progression for all center tiles
    center = fill_garden(garden, start)

    # calculate progression for frontier tiles
    left = fill_garden(garden, (0, middle_xy))
    right = fill_garden(garden, (max_xy, middle_xy))
    top = fill_garden(garden, (middle_xy, 0))
    bottom = fill_garden(garden, (middle_xy, max_xy))

    topleft = fill_garden(garden, (0, 0))
    topright = fill_garden(garden, (max_xy, 0))
    bottomleft = fill_garden(garden, (0, max_xy))
    bottomright = fill_garden(garden, (max_xy, max_xy))

    time_to_outer_tip = size // 2 + 1
    time_to_inner_tip = time_to_outer_tip + size
    time_to_outer_rim = time_to_outer_tip * 2
    time_to_inner_rim = time_to_outer_rim + size
    time_to_corner = time_to_outer_rim - 1

    # center tile
    total = count_reached(steps, center)
    print(f"pos. in center tile            : {total:20}")

    # fully traversed tiles
    n_traversed = (steps + size - time_to_corner) // size
    print(f"completed tile layers          : {n_traversed:20}")
    traversed = 0
    for layer in range(n_traversed):
        n_tiles_in_layer = layer * 4
        if layer % 2 == 0:
            traversed += count_reached(steps, center) * n_tiles_in_layer
        else:
            # every second layer has the alternate setup
            traversed += count_reached(steps - 1, center) * n_tiles_in_layer

    total += traversed
    print(f"pos. in completed+center tiles : {traversed:20}")

    # frontier tip tiles
    if steps >= time_to_outer_tip:
        time_in_tip = steps - time_to_outer_tip
        if n_traversed > 0:
            time_in_tip -= (n_traversed - 1) * size
        frontier = count_reached(time_in_tip, left)
        frontier += count_reached(time_in_tip, right)
        frontier += count_reached(time_in_tip, top)
        frontier += count_reached(time_in_tip, bottom)
        print()
        print(f"time in outer tips             : {time_in_tip:20}")
        print(f"pos. in outer tip tiles        : {frontier:20}")
        total += frontier

    if steps >= time_to_inner_tip:
        time_in_tip = steps - time_to_inner_tip
        if n_traversed > 0:
            time_in_tip -= (n_traversed - 1) * size
        if time_in_tip >= 0:
            frontier = count_reached(time_in_tip, left)
            frontier += count_reached(time_in_tip, right)
            frontier += count_reached(time_in_tip, top)
            frontier += count_reached(time_in_tip, bottom)
            print()
            print(f"time in inner tips             : {time_in_tip:20}")
            print(f"pos. in inner tip tiles        : {frontier:20}")
            total += frontier

    # diagonal tiles
    if steps >= time_to_outer_rim:
        n_outer_rim_tiles = (steps + size - time_to_outer_rim) // size  # per corner
        time_in_outer_rim = steps - time_to_outer_rim
        if n_traversed > 1:
            time_in_outer_rim -= (n_traversed - 2) * size
        if time_in_outer_rim >= size:
            # add second layer
            time_in_inner_rim = time_in_outer_rim - size
            n_inner_rim_tiles = n_outer_rim_tiles

            irim = count_reached(time_in_inner_rim, topleft) * n_inner_rim_tiles
            irim += count_reached(time_in_inner_rim, topright) * n_inner_rim_tiles
            irim += count_reached(time_in_inner_rim, bottomleft) * n_inner_rim_tiles
            irim += count_reached(time_in_inner_rim, bottomright) * n_inner_rim_tiles
            total += irim
            print()
            print(f"inner rim tiles (*4)           : {n_inner_rim_tiles:20}")
            print(f"time in inner rim              : {time_in_inner_rim:20}")
            print(f"pos. in inner rim              : {irim:20}")

            n_outer_rim_tiles = (steps + size - time_to_inner_rim) // size  # per corner

        orim = count_reached(time_in_outer_rim, topleft) * n_outer_rim_tiles
        orim += count_reached(time_in_outer_rim, topright) * n_outer_rim_tiles
        orim += count_reached(time_in_outer_rim, bottomleft) * n_outer_rim_tiles
        orim += count_reached(time_in_outer_rim, bottomright) * n_outer_rim_tiles
        total += orim
        print()
        print(f"outer rim tiles (*4)           : {n_outer_rim_tiles:20}")
        print(f"time in outer rim              : {time_in_outer_rim:20}")
        print(f"pos. in outer rim              : {orim:20}")

    print(f"total                          : {total:20}")

    return total


if __name__ == "__main__":
    input_data = open("input_data.txt").read()
    result = solve(input_data, 64)
    print(f"Example 1: {result}")

    result = solve2(input_data, 26501365)
    print(f"Example 2: {result}")
