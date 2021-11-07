

def solve(fn):
    """DP algorithm"""
    data = [int(x) for x in open(fn)]
    data.sort()
    # [1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19]

    paths = {0: 1}
    data.append(data[-1] + 3)
    for d in data:
        p = 0
        for offset in (1,2,3):
            if d-offset in paths:
                p += paths[d-offset]
        paths[d] = p

    return paths[d]


assert solve('input.txt') == 8

assert solve('input2.txt')  == 19208

result = solve('input_big.txt')
print(result)
assert result == 15790581481472
