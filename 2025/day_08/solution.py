"""


https://adventofcode.com/2025/day/8
"""
from pprint import pprint
from collections import Counter
from math import prod

def parse(data):
    d = []
    for line in data.strip().split("\n"):
        d.append(tuple([int(x) for x in line.split(",")]))
    return d

def euclidean(a, b):
    x1, y1, z1 = a
    x2, y2, z2 = b
    return (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2

def calc_distances(d):
    dist = []
    for i, a in enumerate(d):
        for b in d[i + 1:]:
            dist.append((euclidean(a, b), a, b))
    dist.sort()
    return dist

def get_clustering_steps(data):
    d = parse(data)
    clusters = dict(zip(d, range(len(d))))
    dist = calc_distances(d)
    for _, a, b in dist:
        old = clusters[a]
        new = clusters[b]
        for c in clusters:
            if clusters[c] == old:
                clusters[c] = new
        yield clusters, a, b

def solve(data, n):
    gen = get_clustering_steps(data)
    for _ in range(n):
        clusters, _, _ = next(gen)

    ct = Counter(clusters.values())
    top3 = [i for _, i in ct.most_common(3)]
    return prod(top3)


def solve2(data):
    for clusters, a, b in get_clustering_steps(data):
        nclusters = len(set(clusters.values()))
        if nclusters == 1:
            return a[0] * b[0]


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data, 1000)
    print(f'Example 1: {result}')
    assert result == 50760

    result = solve2(input_data)
    print(f'Example 2: {result}')
    assert result == 3206508875
