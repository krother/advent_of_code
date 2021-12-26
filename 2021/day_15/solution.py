"""Chiton

https://adventofcode.com/2021/day/15

"""
from aoc import PriorityQueue
import numpy as np


BOTTOM_OR_RIGHT = [(0, 1), (1,0)]
MOVES = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def parse(data):
    return np.array([[int(x) for x in row] for row in data.strip().split('\n')])


def make_big_map(a):
    """Expand the array for part II"""
    ys, xs = a.shape
    b = np.zeros((ys * 5, xs * 5), dtype=int)
    for i in range(5):
        for j in range(5):
            part = a + i + j
            part[part >= 10] -= 9
            b[i*xs: (i+1)*ys, j*xs:(j+1)*xs] = part

    return b


def find_adjacent_positions(a, position, directions=MOVES):
    y, x = position
    for dx, dy in directions:
        xc, yc = x + dx, y + dy
        if xc >= 0 and yc >= 0 and xc < a.shape[1] and yc < a.shape[0]:
            yield yc, xc


def traversal(a):
    """exhaustive graph search, correct but takes too long"""
    start = (0, 0)
    target = (a.shape[0] - 1, a.shape[1] - 1)
    candidates = [
        (start, 0, set())
    ]
    best = 9999999999999999999

    while candidates:
        pos, cost, visited = candidates.pop(0)
        for p in find_adjacent_positions(a, pos):
            if p == target:
                if cost + a[y, x] < best:
                    best = cost + a[y, x]
            elif p not in visited:
                y, x = p
                new_vis = visited.copy()
                new_vis.add(p)
                new_cost = cost + a[y, x]
                candidates.append((p, new_cost, new_vis))
    
    return best


def get_max_cost_matrix(a, bottom_right=True, top_left=False):
    """Return matrix with maximum cost for paths from all nodes"""
    maxcost = 9 * a.shape[0] * a.shape[1]
    cost = np.zeros(a.shape, int) + maxcost
    if bottom_right:
        cost[-1, -1] = 0
    if top_left:
        cost[0, 0] = 0
    return cost


def find_path(a, start, best_paths):
    """Helper function for the DP algorithm"""
    return min([
        best_paths[pos] + a[pos] 
        for pos in find_adjacent_positions(a, start, BOTTOM_OR_RIGHT)
        if pos in best_paths])


def dp(a):
    target = a.shape[0] - 1, a.shape[1] - 1
    best_paths = {target: 0}

    for x in range(a.shape[1]-1, -1, -1):
        for y in range(a.shape[1]-1, -1, -1):
            start = y, x
            if start != target:
                best_paths[start] = find_path(a, start, best_paths)

    cost_matrix = np.zeros(a.shape, int)
    for pos in best_paths:
        cost_matrix[pos] = best_paths[pos]
    return cost_matrix


def iterative(a, cost=None):
    if cost is None:
        cost = get_max_cost_matrix(a)
    
    changed = True
    while changed:
        changed = False
        for x in range(a.shape[0]):
            for y in range(a.shape[1]):
                start = y, x
                for pos in find_adjacent_positions(a, start):
                    move_cost = cost[pos] + a[pos]
                    if move_cost < cost[start]:
                        cost[start] = move_cost
                        changed = True

    return cost



def dijkstra(a):
    cost = get_max_cost_matrix(a)
    maxcost = cost[0, 0]

    q = list(np.ndindex(a.shape))

    while q:
        cheapest_cost = maxcost
        cheapest = None
        for pos in q:
            if cost[pos] < cheapest_cost:
                cheapest_cost = cost[pos]
                cheapest = pos
        q.remove(cheapest)

        for pos in find_adjacent_positions(a, cheapest):
            if pos in q:
                dist = cost[cheapest] + a[cheapest]
                if dist < cost[pos]:
                    cost[pos] = dist

        if cheapest == (0, 0):
            q = []

    return cost

#-----------------------------------------------------

from heapq import heappush, heappop
import itertools


entry_finder = {}               # mapping of tasks to entries
REMOVED = '<removed-task>'      # placeholder for a removed task
counter = itertools.count()     # unique sequence count

def add_task(pq, task, priority=0):
    'Add a new task or update the priority of an existing task'
    if task in entry_finder:
        remove_task(task)
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heappush(pq, entry)

def remove_task(task):
    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED

def pop_task(pq):
    'Remove and return the lowest priority task. Raise KeyError if empty.'
    while pq:
        priority, count, task = heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task
    raise KeyError('pop from an empty priority queue')



def dijkstra_heap(a):
    cost = get_max_cost_matrix(a)

    pq = PriorityQueue()
    for pos in np.ndindex(a.shape):
        pq.add_task(pos, cost[pos])

    while pq:
        cheapest = pq.pop_task()
        for pos in find_adjacent_positions(a, cheapest):
            dist = cost[cheapest] + a[cheapest]
            if dist < cost[pos]:
                cost[pos] = dist
                pq.add_task(pos, dist)

        if cheapest == (0, 0):
            break

    return cost

#-----------------------------------------

def dp_by_cost(a):
    target = (a.shape[0]-1, a.shape[1]-1)
    cost = get_max_cost_matrix(a, bottom_right=False, top_left=True)
    threshold = 1
    heads = {(0, 0)}

    while heads:
        new_heads = set()
        for h in heads:
            connections_left = False
            for pos in find_adjacent_positions(a, h):
                dist = cost[h] + a[pos]
                if dist == threshold and cost[pos] > threshold:
                    cost[pos] = threshold
                    new_heads.add(pos)
                elif dist > threshold:
                    connections_left = True
            if connections_left:
                new_heads.add(h)
        heads = new_heads
        threshold += 1

    return cost[target]

def shortest_path(a):
    # variant A: works, very crude but not efficient
    #cost = dp(a)
    #iterative(a, cost)

    # variant B: works, nicer but still too slow
    #cost = dijkstra(a)

    # variant C: great!
    cost = dijkstra_heap(a)
    return cost[0, 0]

    # variant D: DP by cost
    return dp_by_cost(a)


def solve(data):
    a = parse(data)
    return shortest_path(a)


def solve2(data):
    a = parse(data)
    a = make_big_map(a)
    return shortest_path(a)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')
    # 363

    result = solve2(input_data)
    print(f'Example 2: {result}')
    # 2835
