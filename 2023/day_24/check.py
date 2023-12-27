from util import parse

m_rock = [-110, -135, 299]
b_rock = [335849990884055, 362494628861890, 130073711567420]

data = open("input_data.txt").read()
stones = parse(data)

for i, s in enumerate(stones):
    for axis, label in enumerate("xyz"):
        bs = s[axis]
        ms = s[axis + 3]
        if (m_rock[axis] - ms) != 0:
            time = (bs - b_rock[axis]) / (m_rock[axis] - ms)
            print(f"stone {i:4d} collision time on axis {label}:", time)
        else:
            print(f"stone {i:4d} collision time on axis {label} = 0")
