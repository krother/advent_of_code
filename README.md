
# Advent of Code Cheat Sheet

*by Kristian Rother*

----

## What is Advent of Code?

[Advent of Code](https://adventofcode.com/) is an advanced coding challenge.

* one challenge released at 5:00 a.m. UTC per day December 1st - 25th
* every challenge has two parts
* there are >100k participants globally
* collect up to 50 stars (two per day) 
* the challenges come with [great santa stories](https://adventofcode.com/2021/day/1)

----

## What can you learn?

* rehearse your coding fundamentals
* understand requirements
* decompose problems into smaller parts
* estimate computational complexity
* programming practices (OOP, functional programming)
* code cleanup, refactoring

----

## Data Structures

The biggest step towards the solution is choosing a good data structure.
All problems can be solved with standard Python data types: `list`, `dict`, `set`

Data structures that you will need for some of the challenges are:

* stack
* queue
* chained list
* tree
* graph
* 2D array

----

## Algorithms

Identifying a good algorithm is essential. 
For many challenges a brute-force solution is computationally infeasible!

Here are some algorithms that I have used in AoC with links to according challenges:

* [Move along a 2D grid](https://adventofcode.com/2020/day/3)
* [Crypto mining](https://adventofcode.com/2015/day/4)
* [Graph traversal](https://adventofcode.com/2021/day/12)
* [Interpreting an assembly-like language](https://adventofcode.com/2016/day/12)
* [Conways Game of Life](https://adventofcode.com/2020/day/17)
* [Josephus Problem](https://adventofcode.com/2016/day/19)
* [Dynamic Programming (backpack)](https://adventofcode.com/2015/day/19)
* [2D Convolutional Kernel](https://adventofcode.com/2021/day/20)
* [kd-Tree](https://adventofcode.com/2021/day/22)
* [Dijkstra](https://adventofcode.com/2021/day/23)

Most challenges use strings and integer numbers only. 
You do not have to worry about floating-point precision, probabilities and heuristic algorithms.

To learn more about algorithmics, I recommend [Algorithms by Robert Sedgewick and Kevin Wayne](https://algs4.cs.princeton.edu/home/).

----

## Useful Python libraries

Some Python libraries I have used over and over in AoC:

* re – essential to parse most inputs
* numpy – fast arrays help with many challenges
* deque – fast queue implementation (much faster than `list`)
* heapq – for priority queues
* itertools – iterable helpers like permutations, products etc.

Careful with deepcopy (slow)

----

## Testing

I made heavy use of automated tests using `pytest`:

* test a minimal input first
* copy-paste the small examples from the AoC page, write tests for them
* test your toplevel functions only unless it gets really difficult
* add more examples to cover boarder cases (use `@pytest.mark.parametrize`)
* great opportunity to exercise TDD (see live TDD in [Uncle Bobs "Clean Code" lecture](https://www.youtube.com/watch?v=58jGpV2Cg50)

----

## Team Up

AoC works great in teams with:

* pair programming
* people using different programming languages
* beginners who spend their time researching stuff
* solving challenges of a previous year at a slower pace

----

## My daily routine in December

| time | what I do |
|------|-----------|
|  5:50 | get up |
|  5.59 | power-click refresh button |
|  6:00 | start coding |
|  9:00 | call with AoC team (30' timebox) | 
|  9:05 | review solutions of previous day |
|  9:20 | exchange ideas for current day |
|  ? | solve the challenge after 10 minutes to five days | 

----

## Energy management

* Coding 25 days in a row is exhausting. 
* Do not try to go as fast as possible.
* Go slow and steady.
* It is OK to stop at any point.
* If you solve **one problem**, be proud of yourself already.

----

## Further Reading

You can find my solutions on [www.github.com/krother/advent_of_code](https://github.com/krother/advent_of_code). 

----

## License

(c) 2022 Dr. Kristian Rother

This Cheat Sheet is available under the conditions of the [Creative Commons Attribution International License 4.0](https://creativecommons.org/licenses/by/4.0/)

The code on [www.github.com/krother/advent_of_code](https://github.com/krother/advent_of_code) is available under the conditions of the MIT License. See LICENSE.TXT for details.
