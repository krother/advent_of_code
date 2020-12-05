
def binary_search(s, step, right):
    result = 0
    for char in s:
        if char == right:
            result += step
        step = step // 2
    return result


def check(s):
    row = binary_search(s[:7], 64, 'B')
    seat = binary_search(s[7:], 4, 'R')
    sid = row * 8 + seat
    return sid

# tests
assert check("FBFBBFFRLR") == 357
assert check("BFFFBBFRRR") == 567
assert check("FFFBBBFRRR") == 119
assert check("BBFFBBFRLL") == 820

# process input file
data = []
for line in open('input.txt'):
    data.append(check(line.strip()))
print("part 1:", max(data))

# part 2
# missing number with both adjacent numbers present
for v in range(max(data)):
    if v not in data and v-1 in data and v+1 in data:
        print("part 2:", v)
