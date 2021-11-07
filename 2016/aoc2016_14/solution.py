"""Day 14: One-Time Pad

https://adventofcode.com/2016/day/9

"""
from hashlib import md5
from collections import deque
from functools import partial, reduce
import re

TRIPLE = re.compile(r'(\w)\1\1')

def get_hash(s):
    return md5(s.encode()).hexdigest()

def get_md5(salt, i):
    s = salt + str(i)
    return md5(s.encode()).hexdigest()


def get_stretch_hash(salt, i, iter):
    return reduce(
        lambda a,_: get_hash(a),
        range(iter),
        get_md5(salt, i))

def hash_generator(salt, hash_gen=get_md5):
    i = 1
    while True:
        yield hash_gen(salt, i)
        i += 1


def triplet_hash_generator(salt, hash_gen=get_md5):
    for i, md5 in enumerate(hash_generator(salt, hash_gen), 1):
        chars = TRIPLE.findall(md5)
        if chars:
            yield i, md5, chars[0]


def solve(salt, counter, hash_gen=get_md5):
    found = 0
    q = deque([])
    gen = triplet_hash_generator(salt, hash_gen)
    while found < counter:
        item = next(gen)
        q.append(item)
        if q[-1][0] - q[0][0] > 1000:
            count, _, char = q.popleft()
            query = char * 5
            for i, md5, _ in q:
                if query in md5 and count + 1000 >= i:
                    found += 1

    return count


if __name__ == '__main__':
    result = solve('ahsbgdzn', 64)
    print(f'Example 1: {result}')

    gen = partial(get_stretch_hash, iter=2016)
    result = solve('ahsbgdzn', 64, gen)
    print(f'Example 2: {result}')
    
