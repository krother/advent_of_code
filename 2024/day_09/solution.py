"""
Day 9: Disk Fragmenter

https://adventofcode.com/2024/day/9
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import count


@dataclass
class ChainedBlock:
    file_id: int
    size: int
    prev: ChainedBlock = None
    next: ChainedBlock = None

    def __str__(self):
        return f"({self.file_id}, {self.size})"
    
    @property
    def is_file(self):
        return self.file_id is not None

    @property
    def is_gap(self):
        return not self.is_file
    
    def insert_after(self, new):
        new.prev = self
        new.next = self.next
        if self.next:
            self.next.prev = new
        self.next = new

    def shrink(self, amount):
        self.size -= amount
        assert self.size >= 0
        if self.size == 0:
            self.remove()

    def remove(self):
        self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


def parse_chained_list(data: str) -> tuple[ChainedBlock, ChainedBlock]:
    first, last = None, None
    file = True
    file_id = count()
    for c in data.strip():
        new = ChainedBlock(
            file_id=next(file_id) if file else None,
            size=int(c)
            )
        if not first:
            first = new
            last = new
        elif new.size > 0:
            last.insert_after(new)
            last = last.next
        file = not file
    return first, last


def calc_checksum(first: ChainedBlock) -> int:
    checksum = 0
    position = 0
    cursor = first
    while cursor is not None:
        if cursor.is_file:
            for p in range(position, position + cursor.size):
                checksum += p * cursor.file_id
        position += cursor.size
        cursor = cursor.next
    return checksum


def print_chain(first):
    c = first
    while c is not None:
        print(c, end=", ")
        c = c.next
    print()


def solve(data):
    first, last = parse_chained_list(data)
    head, tail = first, last
    while tail and head and tail is not head:
        if head.is_file or head.size == 0:
            head = head.next
        elif tail.is_gap or tail.size == 0:
            tail = tail.prev
        else:
            # move blocks
            m = min(head.size, tail.size)
            new = ChainedBlock(file_id=tail.file_id, size=m)
            head.prev.insert_after(new)
            head.shrink(m)
            tail.shrink(m)
    return calc_checksum(first)


def solve2(data):
    first, last = parse_chained_list(data)
    tail = last
    while tail is not None:
        if tail.is_file:
            # find a gap that fits from beginning
            head = first
            while head is not tail and not (head.is_gap and head.size >= tail.size):
                head = head.next

            if head is not tail:
                # move block
                new = ChainedBlock(file_id=tail.file_id, size=tail.size)
                head.prev.insert_after(new)
                tail.file_id = None  # free old block
                head.shrink(new.size)
            
        tail = tail.prev
    return calc_checksum(first)

 

if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')
    assert result == 6607511583593

    result = solve2(input_data)
    print(f'Example 2: {result}')
    assert result == 6636608781232
