"""


https://adventofcode.com/2022/day/16
"""
from pprint import pprint
from aoc.priority_queue import PriorityQueue
from functools import lru_cache
from copy import deepcopy
import itertools


TIME_LIMIT = 30


big_cave = {
    'AA': (0,[('DD', 2), ('IR', 2), ('NJ', 3), ('LL', 2), ('VH', 2)]),
    'IR': (9,[('AA', 2), ('LY', 2), ('SS', 2), ('NJ', 3), ('LL', 2)]),
    'LY': (21,[('WL', 2), ('CP', 3), ('QD', 2), ('IR', 2)]),
    'DD': (8,[('AA', 2), ('EU', 2), ('LL', 2), ('SS', 3)]),
    'CP': (24,[('LY', 3), ('UC', 3), ('WL', 2)]),
    'SS': (17,[('NJ', 2), ('UC', 3), ('DD', 3), ('IR', 2)]),
    'KH': (13,[('PC', 2), ('WL', 3)]),
    'NJ': (6,[('VH', 2), ('LL', 3), ('AA', 3), ('SS', 2), ('IR', 3)]),
    'LL': (5,[('NJ', 3), ('VH', 3), ('DD', 2), ('AA', 2), ('IR', 2)]),
    'QD': (14,[('WL', 2), ('LY', 2)]),
    'WL': (12,[('LY', 2), ('KH', 3), ('CP', 2), ('QD', 2)]),
    'VH': (10,[('AA', 2), ('LL', 3), ('NJ', 2), ('OC', 3)]),
    'UC': (25,[('SS', 3), ('CP', 3)]),
    'PC': (22,[('KH', 2)]),
    'EU': (19,[('DD', 2)]),
    'OC': (18,[('VH', 3)]),
}

class CaveSolver:

    def __init__(self, cave):
        self.cave = cave

    def get_possible_moves(self, node, opened):
        # wait
        node, wait = node
        if wait > 0:
            yield (node, wait - 1), opened, 0
            return

        # open a valve
        if node not in opened:
            if self.cave[node][0] > 0:
                op2 = frozenset(opened.union(frozenset([node])))
                yield (node, 0), op2, self.cave[node][0]

        # move
        for connection, steps in self.cave[node][1]:
            yield (connection, steps - 1), opened, 0

    @lru_cache
    def cost_per_minute(self, opened):
        """cost goes up for all valves not opened"""
        return sum([self.cave[key][0] for key in self.cave if key not in opened])


    def get_moves(self, node, opened, pressure, minutes, cost):
        cost += self.cost_per_minute(opened)
        for newnode, opened, rate in self.get_possible_moves(node, opened):
            pr = pressure + rate * (29 - minutes)
            yield newnode, opened, pr, cost - rate


    def get_moves_with_elephant(self, node, opened, pressure, minutes, cost):
        cost += self.cost_per_minute(opened)
        player, elephant = node
        for plr, op2, plr_rate in self.get_possible_moves(player, opened):
            for ele, op3, ele_rate in self.get_possible_moves(elephant, opened):
                if player == elephant and plr < ele: continue
                pr = pressure + (plr_rate + ele_rate) * (29 - minutes)
                yield (
                    (plr, ele),
                    op2.union(op3),
                    pr,
                    cost - plr_rate - ele_rate
                )


    def walk(self, move_func, start_time, start_node):
        pq = PriorityQueue()
        open_valves = frozenset()
        pq.add_task((start_node, open_valves, start_time, 0, 0), priority=0)
        while pq:
            node, opened, minutes, pressure, cost = pq.pop_task()
            # print(f"min={minutes} node={node} open={opened} pressure={pressure} cost={cost} queue={len(pq.pq)}")
            for no, op, pr, newcost in move_func(node, opened, pressure, minutes, cost):
                if minutes == TIME_LIMIT - 1:
                    #print(op)
                    return pr
                else:
                    pq.add_task((no, op, minutes + 1, pr, newcost), priority=newcost)


def solve(cave):
    solver = CaveSolver(cave)
    return solver.walk(
        solver.get_moves,
        start_time=0,
        start_node=('AA', 0)
    )


def solve2(cave):
    solver = CaveSolver(cave)
    return solver.walk(
        solver.get_moves_with_elephant, 26, 
        (('AA', 0), ('AA', 0))
    )


def solve_partition(cave, node_mask):
    """solve partition with some nodes set to zero"""
    cave = deepcopy(cave)
    for n in node_mask:
        cave[n] = 0, cave[n][1]
    # pprint(node_mask)
    # pprint(cave)
    solver = CaveSolver(cave)
    result = solver.walk(
        solver.get_moves,
        start_time=4,
        start_node=('AA', 0)
        )
    return result


def solve2(cave):
    node_groups = [
        ('IR',), ('LY',), ('CP',), ('SS',),  ('NJ',), 
        ('LL',), ('QD',), ('UC',),
        ('VH', 'OC'), 
        ('DD', 'EU'), 
        ('KH', 'PC', 'WL'),
    ]
    rstart, rstop = 3, 5

    flat_nodes = set(cave.keys())
    flat_nodes.remove('AA')

    # for testing
    if 'IR' not in cave:
        node_groups = [(n,) for n in flat_nodes]
        rstart, rstop = 1, 5
    print(f'total nodes: {len(flat_nodes)}     node groups: {len(node_groups)}')
    
    best = 0
    for r in range(rstart, rstop + 1):
        print(f'node pairs with r={r}')
        for combo in itertools.combinations(node_groups, r):
            nodes1 = set(itertools.chain(*combo))
            nodes2 = flat_nodes.difference(nodes1)

            part1 = solve_partition(cave, nodes1)
            part2 = solve_partition(cave, nodes2)
            total = part1 + part2
            if total > best:
                best = total
                print(f'\nnew best: {best}')
                print(part1, nodes2)
                print(part2, nodes1)

    return best

if __name__ == '__main__':
    # result = solve(big_cave)
    # print(f'Example 1: {result}')
    # assert result == 2056

    result = solve2(big_cave)
    print(f'Example 2: {result}')
