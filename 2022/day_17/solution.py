"""
Pyroclastic Flow

https://adventofcode.com/2022/day/17
"""
import itertools
import numpy as np
from aoc.parsers import parse_hash_grid


ROCKS = [parse_hash_grid(b) for b in [
    """####""",
""".#.
###
.#.""",

"""..#
..#
###""",

"""#
#
#
#""",
"""
##
##"""]
]

def create_box(nrocks):
    a = np.zeros((nrocks*3, 9), dtype=np.uint8)
    a[-1,:] = 1
    a[:, 0] = 1
    a[:, -1] = 1
    return a

def create_jets(jets):
    for j in itertools.cycle(jets.strip()):
        yield -1 if j == '<' else +1


def create_blocks():
    for b in itertools.cycle(ROCKS):
        yield b


def draw_box(box):
    print()
    for row in box: # [-10:]:
        print(''.join(['#' if char else '.' for char in row]))


def check_free(box, rock, x, y):
    height, width = rock.shape
    area = box[y:y+height, x:x+width]
    return 2 not in (rock + area)


def add_rock(box, rocks, jets, top):
    rock = next(rocks)
    x, y = 3, top - rock.shape[0] - 3
    while True:
        # apply jet
        j = next(jets)
        if check_free(box, rock, x + j, y):
            x += j

        # drop rock
        if check_free(box, rock, x, y + 1):
            y += 1
        else:
            # stop moving
            box[y:y+rock.shape[0], x:x+rock.shape[1]] += rock
            top = min(top, y)
            return top


def drop_blocks(jets, nrocks):
    box = create_box(nrocks)
    jets = create_jets(jets)
    rocks = create_blocks()
    top = box.shape[0] - 1
    for i in range(nrocks):
        top = add_rock(box, rocks, jets, top)    
    return box, box.shape[0] - top - 1


def solve(jets, nrocks=2022):
    box, pile_size = drop_blocks(jets, nrocks)
    return pile_size


def solve2(jetstr, target):
    box = create_box(30000)
    jets = create_jets(jetstr)
    rocks = create_blocks()
    top = box.shape[0] - 1

    # create baseline:
    n_base_rocks = 200
    for i in range(n_base_rocks):
        top = add_rock(box, rocks, jets, top)
    
    memory = []
    dropped = n_base_rocks
    while True:
        # add a rock
        top = add_rock(box, rocks, jets, top)
        dropped += 1
        pile_size = box.shape[0] - top - 1

        # check for repeats
        sample = box[top:top+200].copy()
        for d, psize, mem in memory:
            if (mem - sample).sum() == 0:
                # repeat found
                repeat_rocks = dropped - d
                pile_inc = pile_size - psize
                print(f'repeat after adding {repeat_rocks} rocks')
                print(f'height gained: {pile_inc}')

                nrepeats = target // repeat_rocks
                offset_rocks = target % repeat_rocks
                b = solve(jetstr, offset_rocks)

                return nrepeats * pile_inc + b

        # memorize last state
        memory.append((dropped, pile_size, sample))
        


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')

    result = solve2(input_data, 1_000_000_000_000)
    print(f'Example 2: {result}')
