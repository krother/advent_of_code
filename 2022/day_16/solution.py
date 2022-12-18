"""


https://adventofcode.com/2022/day/16
"""
import re
from pprint import pprint
from aoc.priority_queue import PriorityQueue
from functools import lru_cache


cave = {}

def parse(data):
    to_open = 0
    for valve, rate, connections in re.findall(r'Valve (..) has flow rate=(\d+); tunnel.? lead.? to valve.? (.+)', data):
        rate = int(rate)
        connections = connections.split(', ')
        cave[valve] = (rate, connections)
        if rate > 0:
            to_open += 1


def get_possible_moves(node, prev, opened):
    # open a valve
    if node not in opened and cave[node][0] > 0:
        op2 = frozenset(opened.union(frozenset([node])))
        yield node, op2, cave[node][0]

    # move
    for con in cave[node][1]:
        if con != prev:
            yield con, opened, 0

@lru_cache
def cost_per_minute(opened):
    """cost goes up for all valves not opened"""
    return sum([cave[key][0] for key in cave if key not in opened])


def get_moves(node, opened, pressure, minutes, cost):
    cost += cost_per_minute(opened)
    node, prev = node
    for newnode, opened, rate in get_possible_moves(node, prev, opened):
        pr = pressure + rate * (29 - minutes)
        yield (newnode, node), opened, pr, cost - rate



def walk_cave(data, move_func, time, start_node):
    parse(data)
    pq = PriorityQueue()
    pq.add_task((start_node, frozenset(), 0, 0, 0), priority=0)
    while pq:
        node, opened, minutes, pressure, cost = pq.pop_task()
        #print(f"min={minutes} node={node} open={opened} pressure={pressure} cost={cost} queue={len(pq.pq)}")
        for no, op, pr, newcost in move_func(node, opened, pressure, minutes, cost):
            if minutes == time - 1:
                print(op)
                return pr
            else:
                pq.add_task((no, op, minutes + 1, pr, newcost), priority=newcost)


def solve(data):
    return walk_cave(data, get_moves, 30, ('AA', None))



if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')
    assert result == 2056
