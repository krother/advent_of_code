
from collections import defaultdict

MAXZ = [
    1, 26, 26**2, 26**3, 26**2, 26**3, 26**2,
    26**3, 26**2, 26**3, 26**4, 26**3, 26**2, 26
]

STEPS = [
    (1, 10, 10),   # z0 = w0 + 10              z < 26
    (1, 13, 5),    # z1 = z0 * 26 + w1 + 5     z < 26 ** 2
    (1, 15, 12),   # z2 = z1 * 26 + w2 + 12    z < 26 ** 3
    (26, -12, 12), #                           z < 26 ** 2
    (1, 14, 6),    #                           z < 26 ** 3
    (26, -2, 4),   #                           z < 26 ** 2
    (1, 13, 15),   #                           z < 26 ** 3
    (26, -12, 3),  #                           z < 26 ** 2
    (1, 15, 7),    #                           z < 26 ** 3
    (1, 11, 11),   #                           z < 26 ** 4
    (26, -3, 2),   #                           z < 26 ** 3
    (26, -13, 12), #                           z < 26 ** 2
    (26, -12, 4),  #                           z = 13 + w13
    (26, -13, 11)  # z13 = z12 - 13
]

def calc_step(w, z, div, add1, add2):
    x = z % 26 + add1  # last char
    z = z // div
    if x != w:
        z = z * 26 + w + add2
    return z

def solve_step(zmax, step, zoutput):
    validz = defaultdict(list)
    for zstart in range(zmax):
        for w in range(0, 10):
            z = calc_step(w, zstart, *step)
            if z in zoutput:
                validz[zstart] += [str(w) + num for num in zoutput[z]]
    return validz

def solve():
    validz = {0: ['']}
    for i in range(13, -1, -1):
        print(i, len(validz))
        validz = solve_step(MAXZ[i], STEPS[i], validz)
    print(len(validz))
    numbers = [int(s) for s in validz[0] if '0' not in s]
    print(min(numbers))


if __name__ == '__main__':
    result = solve()
    print(f'Example 1: {result}')

