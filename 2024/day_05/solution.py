"""


https://adventofcode.com/2024/day/5
"""


class Number:
    """sortable number container"""

    def __init__(self, num, rules):
        self.num = num
        self.rules = rules

    def __eq__(self, other):
        return self.num == other.num

    def __lt__(self, other):
        return (self.num, other.num) in self.rules


class Update(list):
    @property
    def sorted(self):
        return Update(sorted(self))

    @property
    def correct(self):
        return self == self.sorted

    @property
    def middle(self):
        middle = len(self) // 2
        return self[middle].num


def parse(data):
    rules = set()
    r, seq = data.strip().split("\n\n")
    for rr in r.split("\n"):
        rules.add(tuple(map(int, rr.split("|"))))

    updates = []
    for line in seq.split("\n"):
        updates.append(Update([Number(int(x), rules) for x in line.split(",")]))
    return updates


def solve(data):
    updates = parse(data)
    return sum(u.middle for u in updates if u.correct)


def solve2(data):
    updates = parse(data)
    return sum(u.sorted.middle for u in updates if not u.correct)


if __name__ == "__main__":
    input_data = open("input_data.txt").read()
    result = solve(input_data)
    print(f"Example 1: {result}")  # 5948

    result = solve2(input_data)
    print(f"Example 2: {result}")  # 3062
