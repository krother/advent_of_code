"""
Pulse Propagation

https://adventofcode.com/2023/day/20
"""

from dataclasses import dataclass


@dataclass
class Broadcaster:

    name: str
    targets: list[str]

    def receive(self, source, pulse):
        return [(self.name, t, pulse) for t in self.targets]


@dataclass
class FlipFlop:

    name: str
    state: int
    targets: list[str]

    def receive(self, source, pulse):
        if pulse:
            return []
        self.state = 1 - self.state
        return [(self.name, t, self.state) for t in self.targets]


@dataclass
class Conjunction:

    name: str
    targets: list[str]
    sources: dict[str, int]

    def receive(self, source, pulse):
        self.sources[source] = pulse
        pulse = 1 - int(all(p == 1 for p in self.sources.values()))
        return [(self.name, t, pulse) for t in self.targets]


def parse(data):
    modules = {}
    for line in data.strip().split("\n"):
        first, second = line.split("->")
        targets = [t.strip() for t in second.split(",")]
        if line.startswith("%"):
            name = first[1:].strip()
            modules[name] = FlipFlop(name, targets=targets, state=0)

        if line.startswith("&"):
            name = first[1:].strip()
            modules[name] = Conjunction(name, targets, sources={})

        if line.startswith("broadcaster"):
            modules["broadcaster"] = Broadcaster("broadcaster", targets=targets)

    for name, m in modules.items():
        for t in m.targets:
            if isinstance(modules.get(t), Conjunction):
                modules[t].sources[name] = 0
    return modules


def push_button(modules, total_sent, stop_rx=False):
    pulses = [("button", "broadcaster", 0)]
    total_sent[0] += 1
    while pulses:
        new_pulses = []
        for source, target, pulse in pulses:
            if stop_rx and target == "rx" and pulse == 0:
                return True
            if target in modules:
                result = modules[target].receive(source, pulse)
                for _, _, p in result:
                    total_sent[p] += 1
                new_pulses += result
        pulses = new_pulses


def solve(data):
    modules = parse(data)
    total_sent = {0: 0, 1: 0}
    for _ in range(1000):
        push_button(modules, total_sent)
    return total_sent[0] * total_sent[1]


def solve2(data):
    modules = parse(data)
    total_sent = {0: 0, 1: 0}
    i = 1
    while not push_button(modules, total_sent, True):
        i += 1
    return i


if __name__ == "__main__":
    input_data = open("input_data.txt").read()
    result = solve(input_data)
    print(f"Example 1: {result}")  # 949764474

    total = 1
    for i in range(1, 5):
        data = open(f"alu{i}.txt").read()
        result = solve2(data)
        print(f"ALU {i}: {result}")
        total *= result

    print(f"Example 2: {total}")  # 243221023462303
