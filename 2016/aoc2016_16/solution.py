"""Day 16: Dragon Checksum

https://adventofcode.com/2016/day/16

"""

def dragon_step(a):
    """
    Call the data you have at this point "a".
    Make a copy of "a"; call this copy "b".
    Reverse the order of the characters in "b".
    In "b", replace all instances of 0 with 1 and all 1s with 0.
    The resulting data is "a", then a single 0, then "b".
    """
    b = a[::-1]
    b = ''.join(['0' if c == '1' else '1' for c in b])
    return a + '0' + b

def get_checksum(data):
    result = ''
    for start in range(0, len(data), 2):
        pair = data[start:start+2]
        if pair[0] == pair[1]:
            result += '1'
        else:
            result += '0'
    if len(result) % 2 == 1:
        return result
    else:
        return get_checksum(result)

def solve(state, disk_size):
    while len(state) < disk_size:
        state = dragon_step(state)
    
    state = state[:disk_size]
    return get_checksum(state)


if __name__ == '__main__':
    result = solve('11101000110010100', 272)
    print(f'Example1: {result}')

    result = solve('11101000110010100', 35651584)
    print(f'Example2: {result}')
