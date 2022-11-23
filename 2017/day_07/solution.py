"""
Recursive Circus

https://adventofcode.com/2017/day/7

"""
import re
from collections import Counter
from dataclasses import dataclass
from pprint import pprint


@dataclass
class Node:

    name : str
    number : int
    parent : object
    children : list

    def get_root(self):
        if self.parent:
            return self.parent.get_root()
        return self

    def sum(self):
        return self.number + sum([c.sum() for c in self.children])


def parse_tree(data):
    tree = {}
    for line in data.strip().split('\n'):
        name, num, *rest = line.split()
        num = int(num[1:-1])
        if rest:
            children = [c.rstrip(',') for c in rest[1:]]
        else:
            children = []
        tree[name] = Node(name=name, number=num, parent=None, children=children)
    
    # link children + parents
    for node in tree.values():
        new_childs = []
        for c in node.children:
            new_childs.append(tree[c])
            tree[c].parent = node
        node.children = new_childs

    return node.get_root()


def solve(data):
    root = parse_tree(data)
    return root.name


def fix_subtree(node, target=0):
    child_sums = [c.sum() for c in node.children]
    csums = Counter(child_sums)
    if len(csums) > 1:
        for child, s in zip(node.children, child_sums):
            if csums[s] == 1:
                return fix_subtree(child, csums.most_common(1)[0][0])
    return node.number - (node.sum() - target)    


def solve2(data):
    root = parse_tree(data)
    return fix_subtree(root)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')

    result = solve2(input_data)
    print(f'Example 2: {result}')
