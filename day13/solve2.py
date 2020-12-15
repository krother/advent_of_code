import numpy as np

def solve_slow(buses):
    """
    slow, brute-force.
    Used this to test
    - whether i understood the problem
    - whether my faster solution works
    """
    buses = [int(x.replace('x', '0')) for x in buses.split(',')]
    depart = -1
    found = False
    highest = max(buses)
    while not found:
        depart += 1
        found = True
        for i, b in enumerate(buses):
            if b > 0:
                if not (depart+i) % b == 0:
                    found = False
                    break
    return depart


def solve_pair(p1, p2, ofs1, ofs2):
    """correct but slow"""
    for t in range(p1*p2):
        if (t+ofs1) % p1 == 0 and (t+ofs2) % p2 == 0:
            return t

def solve_pair(p1, p2, ofs1, ofs2):
    """way faster"""
    for n in range(p2):
        t = p1 * n - ofs1
        if (t + ofs2) % p2 == 0:
            return t

assert solve_pair(3, 5, 0, 1) == 9
assert solve_pair(15, 7, 6, 2) == 54

def solve_recursive(buses):
    print(buses)
    # TODO: try reduce()
    if len(buses) == 2:
        (p1, ofs1), (p2, ofs2) = buses
        return solve_pair(p1, p2, ofs1, ofs2)
    else:
        (p1, ofs1), (p2, ofs2) = buses[:2]
        p = p1 * p2
        ofs = solve_pair(p1, p2, ofs1, ofs2)
        buses = [(p, p-ofs)] + buses[2:]
        return solve_recursive(buses)

assert solve_recursive([(3,0), (5,1)]) == 9
assert solve_recursive([(3,0), (5,1), (7, 2)]) == 54

def solve(buses):
    buses = [(int(x), i) for i,x in enumerate(buses.split(',')) if x != 'x']
    return solve_recursive(buses)

assert solve("3,5") == 9
assert solve("3,5,7") == 54
assert solve("17,x,13,19") == 3417
assert solve("67,7,59,61") == 754018
assert solve("67,x,7,59,61") == 779210
assert solve("67,7,x,59,61") == 1261476
assert solve("7,13,x,x,59,x,31,19") == 1068781

assert solve("1789,37,47,1889") == 1202161486

big = "37,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,587,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,13,19,x,x,x,23,x,x,x,x,x,29,x,733,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,17"
print(solve(big))
