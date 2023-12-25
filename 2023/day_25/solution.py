"""
Snowverload

https://adventofcode.com/2023/day/25
"""
from collections import defaultdict
from sklearn.cluster import SpectralClustering
import numpy as np
from pprint import pprint


def parse(data):
    """parses graph into a connectivity matrix"""
    graph = defaultdict(set)
    for line in data.strip().split("\n"):
        left, r = line.split(": ")
        graph[left].add(left)
        r = r.split()
        for right in r:
            graph[left].add(right)
            graph[right].add(left)
    return graph


def is_connected(graph):
    visited = set()
    stack = [next(iter(graph.keys()))]
    while stack:
        node = stack.pop()
        visited.add(node)
        for e in graph[node]:
            if e not in visited:
                stack.append(e)
    return len(graph) == len(visited)


def cut(graph, node1, node2):
    graph[node1].remove(node2)
    graph[node2].remove(node1)


def get_affinity_matrix(graph):
    mtx = []
    for node1 in graph:
        row = []
        for node2 in graph:
            row.append(1 if node2 in graph[node1] else 0)
        mtx.append(row)
    return np.array(mtx)


def find_connections(graph, clusters):
    c1, c2 = clusters
    connections = []
    for n1 in c1:
        for n2 in graph[n1]:
            if n2 in c2:
                print("connection:", n1, n2)
                connections.append((n1, n2))
    return connections


def solve(data):
    graph = parse(data)
    pprint(f"parsed graph with {len(graph)} nodes")

    # spectral clustering
    mtx = get_affinity_matrix(graph)
    clustering = SpectralClustering(
        n_clusters=2, affinity="precomputed", assign_labels="discretize", random_state=0
    ).fit(mtx)

    # extract cluster labels
    clusters = [set(), set()]
    for c, label in zip(clustering.labels_, graph):
        clusters[c].add(label)
    print("final clusters of size", len(clusters[0]), len(clusters[1]))

    # cut to double check
    connections = find_connections(graph, clusters)
    for n1, n2 in connections:
        cut(graph, n1, n2)
    print("graph still connected: ", is_connected(graph))

    return len(clusters[0]) * len(clusters[1])


if __name__ == "__main__":
    input_data = open("input_data.txt").read()
    result = solve(input_data)
    print(f"Example 1: {result}")  # 571753
