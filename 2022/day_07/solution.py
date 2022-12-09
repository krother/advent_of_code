"""
No Space Left On Device

https://adventofcode.com/2022/day/7
"""
import re


class Directory:

    def __init__(self, parent):
        self.subdirs = {}
        self.files = []
        self.parent = parent

    def __repr__(self):
        return '[' + str(self.subdirs) + ';' + str(self.files) + ']'

    def get_subdir(self, name):
        if name == "":
            return self
        if name not in self.subdirs:
            self.subdirs[name] = Directory(parent=self)
        return self.subdirs[name]

    @property
    def size(self):
        return sum(
            self.files + 
            [subdir.size for subdir in self.subdirs.values()]
        )

    def traverse_subdirectories(self):
        """recursively travel through all subdirectories"""
        for subdir in self.subdirs.values():
            for subsubdir in subdir.traverse_subdirectories():
                yield subsubdir
        yield self


def parse_tree(data):
    root = Directory(parent=None)
    current = root
    for line in data.strip().split('\n'):
        if line.startswith('$ cd /'):
            current = root
        elif line.startswith('$ cd ..'):
            current = current.parent
        elif line.startswith('$ cd'):
            current = current.get_subdir(line[4:].strip())
        else:
            num = re.findall(r'^\d+', line)
            if num:
                current.files.append(int(num[0]))
    return root


def solve(data):
    tree = parse_tree(data)
    return sum(subdir.size for subdir in tree.traverse_subdirectories() if subdir.size <= 100_000)


def solve2(data):
    tree = parse_tree(data)
    required = tree.size - 40000000
    return min(subdir.size for subdir in tree.traverse_subdirectories() if subdir.size >= required)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')
    assert result == 1792222

    result = solve2(input_data)
    print(f'Example 2: {result}')
    assert result == 1112963
