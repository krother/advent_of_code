"""
Day 23: LAN Party

https://adventofcode.com/2024/day/23
"""
from collections import defaultdict
from itertools import combinations


def parse(data):
    network = defaultdict(set)
    for line in data.strip().split("\n"):
        c1, c2 = line.split("-")
        network[c1].add(c2)
        network[c2].add(c1)
    return network


def solve(data):
    network = parse(data)
    result = set()
    for n1 in network:
        if n1.startswith("t"):
            for n2, n3 in combinations(network[n1], 2):
                if n3 in network[n2]:
                    x = ",".join(sorted([n1, n2, n3]))
                    result.add(x)
    return len(result)


def find_maximum_clique(network):
    """naive brute-force algorithm"""
    nodes = sorted(network)
    candidates = set(frozenset([n]) for n in nodes)
    best = set()
    while candidates:
        print(f"best size {len(best)}  candidates: {len(candidates)}")
        new = set()
        for c in candidates:
            for n1 in nodes:  # node to add
                if n1 not in c:
                    if all(n2 in network[n1] for n2 in c):
                        x = frozenset(list(c) + [n1])
                        new.add(x)
                        if len(x) > len(best):
                            best = x

        candidates = new


bk_result = set()


def bron_kerbosch(R, P, X, network):
    """wikipedia solution: faster!"""
    # R, P, X are disjoint sets
    # R: current maximum clique
    # P: nodes left to try
    # X: nodes already excluded
    global bk_result
    if not P and not X:
        # found a candidate
        if len(R) > len(bk_result):
            bk_result = R
        return
    for v in list(P):
        bron_kerbosch(
            R=R.union(set([v])),
            P=P.intersection(network[v]),
            X=X.intersection(network[v]),
            network=network,
        )
        P.remove(v)
        X.add(v)


def solve2(data):
    network = parse(data)
    # best = find_maximum_clique(network)
    bron_kerbosch(set(), set(network), set(), network)
    best = bk_result
    return ",".join(sorted(best))


if __name__ == "__main__":
    input_data = open("input_data.txt").read()
    result = solve(input_data)
    print(f"Example 1: {result}")
    assert result == 1366

    result = solve2(input_data)
    print(f"Example 2: {result}")
    assert result == "bs,cf,cn,gb,gk,jf,mp,qk,qo,st,ti,uc,xw"
