"""title

https://adventofcode.com/2021/day/12

"""
from collections import defaultdict

def parse(data):
    connections = defaultdict(list)
    for line in data.strip().split('\n'):
        a, b = line.split('-')
        connections[a].append(b)
        connections[b].append(a)
    return connections

def solve(data):
    connections = parse(data)
    candidates = [
        ('start', {'start'})
    ]
    npaths = 0

    while candidates:
        node, visited = candidates.pop(0)
        if node == 'end':
            npaths += 1
        
        for node2 in connections[node]:
            if node2 not in visited or node2.isupper():
                new_path = visited.copy()
                if node2.islower():
                    new_path.add(node2)
                candidates.append((node2, new_path))
        
    return npaths



def solve2(data):
    connections = parse(data)
    candidates = [
        ((['start'], False))
    ]
    npaths = 0
    while candidates:
        path, twice = candidates.pop()
        
        for node in connections[path[-1]]:
            if node == 'end':
                npaths += 1
                continue

            lower = node.islower() and node != 'start'
            second_visit = lower and not twice and path.count(node) == 1

            if (node.isupper() or node not in path or second_visit):
                new_path = path[:] + [node]
                new_twice = twice or second_visit
                candidates.append((new_path, new_twice))
    
    return npaths

if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')
    # 4912

    result = solve2(input_data)
    print(f'Example 2: {result}')
    # 150004
