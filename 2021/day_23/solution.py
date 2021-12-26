"""title

https://adventofcode.com/2021/day/23

"""

from advent_of_code.aoc.priority_queue import PriorityQueue
from copy import deepcopy


COST = dict(zip('ABCD', [1, 10, 100, 1000]))

EMPTY = '-'

DISTANCE = {
    'A': [2, 1, 1, 3, 5, 7, 8],
    'B': [4, 3, 1, 1, 3, 5, 6],
    'C': [6, 5, 3, 1, 1, 3, 4],
    'D': [8, 7, 5, 3, 1, 1, 2],
}
DOORS = {
    'A': 1.5,
    'B': 2.5,
    'C': 3.5,
    'D': 4.5
}


class Room:
    
    def __init__(self, name, size, items=''):
        self.name = name
        self.size = size
        self.items = list(items)
        assert self.size >= len(self.items)

    def __repr__(self):
        s = '-' * self.size + ''.join(self.items)
        return s[-self.size:]

    def __len__(self):
        return len(self.items)

    def copy(self):
        return Room(self.name, self.size, ''.join(self.items))

    @property
    def complete(self):
        return self.is_ready and len(self.items) == self.size

    @property
    def is_ready(self):
        return len(set(self.items)) == 1 and self.items[0] == self.name

    def pop(self):
        if self.is_ready:
            raise IndexError(f"all amphipods in {self.name} are happy")
        char = self.items.pop(0)
        return char, COST[char] * (self.size - len(self))

    def can_add(self, item):
        if (
            len(self.items) == self.size or
            item != self.name or
            (len(self) > 0 and not self.is_ready)
        ):
            return False
        return True

    def add(self, item):
        if not self.can_add(item):
            raise ValueError(f"room {self.name} does not accept {item}")
        self.items.insert(0, item)
        return COST[item] * (self.size - len(self) + 1)


class Hallway:

    def __init__(self, items=''):
        self.slots = [EMPTY] * 7
        if items:
            for pos, fish in enumerate(items):
                self.slots[pos] = fish

    def __repr__(self):
        return ''.join(self.slots)

    def copy(self):
        h = Hallway()
        h.slots = self.slots[:]
        return h

    def is_path_free(self, door, pos):
        target = DOORS[door]
        p = pos
        if p > target:
            p -= 1
            while p > target:
                if self.slots[p] != EMPTY:
                    return False
                p -= 1
            return True
        
        p += 1
        while p < target:
            if self.slots[p] != EMPTY:
                return False
            p += 1
        return True

    def get_possible_positions(self, door):
        result = set()
        for pos in range(7):
            if self.slots[pos] == EMPTY and self.is_path_free(door, pos):
                result.add(pos)
        return result

    def add(self, fish, position, door):
        if position not in self.get_possible_positions(door): # DISABLE FOR SPEEDUP
            raise ValueError(f"move to {door} not possible")
        self.slots[position] = fish
        return COST[fish] * DISTANCE[door][position]

    def get_possible_removals(self):
        result = set()
        for pos in range(7):
            fish = self.slots[pos]
            if fish != EMPTY and self.is_path_free(fish, pos):
                result.add((pos, self.slots[pos]))
        return result

    def remove(self, position):
        fish = self.slots[position]
        self.slots[position] = EMPTY
        return COST[fish] * DISTANCE[fish][position]


class Amphipods:

    def __init__(self, rooms, cost=0, hallway=''):
        self.cost = cost
        self.hallway = Hallway(hallway)
        self.rooms = {r.name: r for r in rooms}

    def __repr__(self):
        return ''.join([str(self.rooms[r]) for r in 'ABCD']) + str(self.hallway)

    def get_str_hash(self):
        return str(self)

    def wins(self):
        return all([r.complete for r in self.rooms.values()])

    def copy(self):
        rooms = (self.rooms[r].copy() for r in 'ABCD')
        return Amphipods(rooms, cost=self.cost, hallway=str(self.hallway))

    def get_possible_moves(self):
        # from hallway to room
        for pos, fish in self.hallway.get_possible_removals():
            if self.rooms[fish].can_add(fish):
                new = self.copy()
                new.cost += new.hallway.remove(pos)
                new.cost += new.rooms[fish].add(fish)                
                yield new

        # from room to hallway
        for r in self.rooms.values():
            if r.items and not r.is_ready:
                for pos in self.hallway.get_possible_positions(r.name):
                    new = self.copy()
                    fish, cost = new.rooms[r.name].pop()
                    new.cost += cost
                    new.cost += new.hallway.add(fish=fish, position=pos, door=r.name)
                    yield new


def solve(start):
    pq = PriorityQueue()
    pq.add_task(start, 0)
    visited = set()
    i = 0
    while pq:
        i += 1
        cand = pq.pop_task()
        if cand.wins():
            return cand.cost

        h = cand.get_str_hash()
        if h in visited:
            continue
        visited.add(h)
        for move in cand.get_possible_moves():
            pq.add_task(move, move.cost)
        if i % 10000 == 0:
            print(f"queued candidates: {len(pq.pq):8d}    cost: {cand.cost:6d}")



if __name__ == '__main__':
 
    input1 = Amphipods((
        Room('A', 2, 'DC'),
        Room('B', 2, 'BA'),
        Room('C', 2, 'CD'),
        Room('D', 2, 'AB')
        ))
    result = solve(input1)
    print(f'Example 1: {result}')
    # 15338

    # test big
    input2 = Amphipods((
        Room('A', 4, 'BDDA'),
        Room('B', 4, 'CCBD'),
        Room('C', 4, 'BBAC'),
        Room('D', 4, 'DACA')
        ))
    result = solve(input2)
    print(f'Example 2: {result}')
    # 44169

    input2 = Amphipods((
        Room('A', 4, 'DDDC'),
        Room('B', 4, 'BCBA'),
        Room('C', 4, 'CBAD'),
        Room('D', 4, 'AACB')
        ))
    result = solve(input2)
    print(f'Example 2: {result}')
    #  45164 < x < 47164

