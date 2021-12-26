"""title

https://adventofcode.com/2021/day/23

"""
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


COST = dict(zip('abcd', [1, 10, 100, 1000]))

HOME = ['a1', 'a2', 'b1', 'b2', 'c1', 'c2', 'd1', 'd2']
EMPTY = '-'


MAP = {
    'a2': [('a1', 1, '')],
    'a1': [('a2', 1, ''), ('h1', 3, '2'), ('h2', 2, ''), ('h3', 2, ''), ('h4', 4, '3'), 
                          ('h5', 6, '34'), ('h6', 8, '345'), ('h7', 9, '3456')],
    'b2': [('b1', 1, '')],
    'b1': [('b2', 1, ''), ('h1', 5, '23'), ('h2', 4, '3'), ('h3', 2, ''), ('h4', 2, ''), 
                          ('h5', 4, '4'), ('h6', 6, '45'), ('h7', 7, '456')],
    'c2': [('c1', 1, '')],
    'c1': [('c2', 1, ''), ('h1', 7, '234'), ('h2', 6, '34'), ('h3', 4, '4'), ('h4', 2, ''), 
                          ('h5', 2, ''), ('h6', 4, '5'), ('h7', 5, '56')],
    'd2': [('d1', 1, '')],
    'd1': [('d2', 1, ''), ('h1', 9, '2345'), ('h2', 8, '345'), ('h3', 6, '45'), ('h4', 4, '5'), 
                          ('h5', 2, ''), ('h6', 2, ''), ('h7', 3, '6')],

    'h1': [('a1', 3, '2'), ('b1', 5, '23'), ('c1', 7, '234'), ('d1', 9, '2345')],
    'h2': [('a1', 2, ''), ('b1', 4, '3'), ('c1', 6, '34'), ('d1', 8, '345')],
    'h3': [('a1', 2, ''), ('b1', 2, ''), ('c1', 4, '4'), ('d1', 6, '45')],
    'h4': [('a1', 4, '3'), ('b1', 2, ''), ('c1', 2, ''), ('d1', 4, '5')],
    'h5': [('a1', 6, '34'), ('b1', 4, '4'), ('c1', 2, ''), ('d1', 2, '')],
    'h6': [('a1', 8, '345'), ('b1', 6, '45'), ('c1', 4, '5'), ('d1', 2, '')],
    'h7': [('a1', 9, '3456'), ('b1', 7, '456'), ('c1', 5, '56'), ('d1', 3, '6')],
}
MAP = {
    'a2': [('a1', 1)],
    'a1': [('a2', 1), ('h2', 2), ('h3', 2)],
    'b2': [('b1', 1)],
    'b1': [('b2', 1), ('h3', 2), ('h4', 2)],
    'c2': [('c1', 1)],
    'c1': [('c2', 1), ('h4', 2), ('h5', 2)],
    'd2': [('d1', 1)],
    'd1': [('d2', 1), ('h5', 2), ('h6', 2)],

    'h1': [('h2', 1)],
    'h2': [('h1', 1), ('a1', 2), ('h3', 2)],
    'h3': [('a1', 2), ('b1', 2), ('h2', 2), ('h4', 2)],
    'h4': [('b1', 2), ('c1', 2), ('h3', 2), ('h5', 2)],
    'h5': [('c1', 2), ('d1', 2), ('h4', 2), ('h6', 2)],
    'h6': [('d1', 2), ('h5', 2), ('h7', 1)],
    'h7': [('h6', 1)],
}
POSITIONS = list(sorted(MAP))

class Amphipods:

    def __init__(self, positions):
        # {location: occupant}
        self.cost = 0
        self.pods = positions

    def __repr__(self):
        return '  '.join([pos + ':' + self.pods[pos] for pos in POSITIONS]).upper()

    def get_str_hash(self):
        return ''.join([self.pods[pos] for pos in POSITIONS])

    def wins(self):
        return self.get_str_hash()[:8] == 'aabbccdd'

    def is_blocked(self, blocked):
        return any([True for b in blocked if self.pods['h' + b] != EMPTY])

    def is_move_valid(self, pos, target, char):
        to_hallway = target[0] == 'h'
        up_pocket = pos[1] == '2' and target[1] == '1'
        into_right_pocket = target[0] == char and pos[0] == 'h'
        deeper = pos[1] == '1' and target[1] == '2'
        make_space = pos[0] == char and self.pods[pos[0] + '2'][0] != char
        leave_good_position = char == pos[0] and (up_pocket or (to_hallway and not make_space)) 
        return (into_right_pocket or deeper or to_hallway or up_pocket) and not leave_good_position

    def get_possible_moves(self):
        for pos in self.pods:
            if self.pods[pos] != EMPTY:
                for target, nsteps in MAP[pos]:
                    char = self.pods[pos]
                    if (
                        self.pods[target] == EMPTY and
                        self.is_move_valid(pos, target, char)
                        # and not self.is_blocked(blocked)
                    ):
                        new = self.pods.copy()
                        new[pos] = EMPTY
                        new[target] = char
                        a = Amphipods(new)
                        a.cost = self.cost + nsteps * COST[char]
                        yield a


def solve(data):
    start = Amphipods(data)
    candidates = [] # pq
    add_task(candidates, start, 0)
    visited = set()
    i = 0
    while candidates:
        i += 1
        cand = pop_task(candidates)
        if cand.wins():
            return cand.cost

        h = cand.get_str_hash()
        if h in visited:
            continue
        visited.add(h)
        for move in cand.get_possible_moves():
            add_task(candidates, move, move.cost)
        if i % 10000 == 0:
            print(len(candidates), cand.cost)


def solve2(data):
    return data

if __name__ == '__main__':
 
    INPUT = {
        'a1': 'd',
        'a2': 'c',
        'b1': 'b',
        'b2': 'a',
        'c1': 'c',
        'c2': 'd',
        'd1': 'a',
        'd2': 'b',
        'h1': '-',
        'h2': '-',
        'h3': '-',
        'h4': '-',
        'h5': '-',
        'h6': '-',
        'h7': '-',
    }

    result = solve(INPUT)
    print(f'Example 1: {result}')
    # 15338

    # result = solve2(input_data)
    # print(f'Example 2: {result}')
