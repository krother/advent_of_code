"""title

https://adventofcode.com/2021/day/19

"""
import numpy as np
import pandas as pd
import itertools
import re

SMALL_INPUT = open('small_input.txt').read()

ORIENTATIONS = """
 x, y, z
 x, z,-y
 x,-y,-z
 x,-z, y
 y,-x, z
 y, z, x
 y, x,-z
 y,-z,-x
 z, y,-x
 z,-x,-y
 z,-y, x
 z, x, y
-x, y,-z
-x, z, y
-x,-y, z
-x,-z,-y
-y,-x,-z
-y, z,-x
-y, x, z
-y,-z, x
-z, y, x
-z,-x, y
-z,-y,-x
-z, x,-y
"""

ORIENTATIONS = re.findall(r'(.)(.),(.)(.),(.)(.)', ORIENTATIONS)

def parse(data):
    result = {}
    scanners = data.strip().split('\n\n')
    for i, s in enumerate(scanners):
        coords = []
        for row in re.findall(r'(-?\d+),(-?\d+),(-?\d+)', s):
            coords.append(list(map(int, row)))
        coords.sort()
        a = np.array(coords)
        result[i] = a
    return result

def get_axis(a, sign, axis):
    axis_index = 'xyz'.find(axis)
    sign = -1 if sign == '-' else 1
    return sign * a[:, axis_index]

def get_orientations(scanner):
    for xsig, xax, ysig, yax, zsig, zax in ORIENTATIONS:
        b = np.zeros(scanner.shape, scanner.dtype)
        b[:, 0] = get_axis(scanner, xsig, xax)
        b[:, 1] = get_axis(scanner, ysig, yax)
        b[:, 2] = get_axis(scanner, zsig, zax)
        yield b

def match(s1, s2):
    for origin1 in s1[-10:]: # one of these has to match because they are sorted
        for origin2 in s2:
            translation = origin2 - origin1
            s2_trans = s2 - translation
            merged = np.vstack([s1, s2_trans])
            uni = np.unique(merged, axis=0)
            overlap = merged.shape[0] - uni.shape[0]
            if overlap >= 12:
                s2_trans = pd.DataFrame(s2_trans).sort_values(by=0).values
                return translation, s2_trans
    return None, None

def match_pair(s1, s2):
    for s2 in get_orientations(s2):
        r, s = match(s1, s2)
        if r is not None:
            return r, s
    return None, None

def solve(data):
    scanners = parse(data)
    aligned = [0]
    vectors = [(0, 0, 0)]
    checked = set()

    while len(aligned) < len(scanners):
        print(f'{len(aligned)} / {len(scanners)} scanners matched')
        merge_found = False
        for s1, s2 in itertools.product(aligned, scanners):
            if (s1, s2) in checked or s2 in aligned:
                continue
            checked.add((s1, s2))
            print(f'comparing {s1} vs {s2}')
            vec, s2_trans = match_pair(scanners[s1], scanners[s2])
            if vec is not None:
                aligned.append(s2)
                vectors.append(vec)
                scanners[s2] = s2_trans
                print('match found!\n')
                merge_found = True
                break
        if not merge_found:
            raise Exception("something went wrong")

    df = pd.DataFrame(scanners[0])
    a = np.vstack(list(scanners.values()))
    a = np.unique(a, axis=0)
    df = pd.DataFrame(a)
    df.sort_values(by=0, ascending=True).to_csv('out.csv', index=False)

    v = pd.DataFrame(vectors)
    v.to_csv('vectors.csv', index=False)
    return df.shape[0]

def solve2(fn):
    df = pd.read_csv(fn)
    largest = 0
    for _, r1 in df.iterrows():
        for _, r2 in df.iterrows():
            manhattan = np.abs(r1.values - r2.values).sum()
            if manhattan > largest:
                largest = manhattan

    return largest

if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    
    #result = solve(SMALL_INPUT)
    result = solve(input_data)
    print(f'Example 1: {result}')
    # 355

    result = solve2('vectors_small.csv')
    result = solve2('vectors.csv')
    print(f'Example 2: {result}')
    # 10842
