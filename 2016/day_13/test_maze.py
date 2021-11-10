"""
1. Do not write production code without writing a test first.
2. Write a minimal test that fails
3. Only write enough code so that the test passes.
"""
import pytest

from maze import Maze, MazeException, find_path_length, count_positions_visited


@pytest.mark.parametrize(
            'base,pos,expected',
            (
                (0, (0, 0), True),
                (1, (0, 0), False),
                (3, (0, 0), True),
                (3, (-1, 0), False),
                (3, (0, -1), False),
                (10, (1, 1), True),
                (10, (2, 1), False),
                (10, (4, 4), True),
                (10, (8, 2), True),
                (10, (9, 6), False),
                (15, (0, 0), True),
            ))        
def test_is_maze_position_open(base,pos,expected):
    m = Maze(base)
    assert m.is_position_open(*pos) == expected


@pytest.mark.parametrize(
        'base,pos,expected',
        [
            (10, (1, 1), {(0, 1), (1, 2)}),
            (10, (2, 2), {(1, 2), (3, 2)}),
            (10, (6, 5), {(5, 5), (7, 5), (6, 4), (6, 6)}),
            (10, (1, 2), {(1, 1), (2, 2)}),
            (10, (6, 1), {(7, 1)}),
            (10, (5, 3), set()),
        ])
def test_find_moves(base, pos, expected):
    maze = Maze(base)
    assert maze.find_moves(pos) == expected


@pytest.mark.parametrize(
        'base,stop,expected',
        (
            (10, (3,1), 4),
            (10, (7,4), 11),
        ))
def test_find_path_length(base, stop, expected):
    assert find_path_length(base, stop) == expected


@pytest.mark.parametrize(
        'base,steps,expected',
        (
            (10, 1, 3),
            (10, 2, 5),
            (10, 3, 6),
            (10, 4, 9),
            (10, 5, 11),
        ))
def test_count_positions_visited(base, steps, expected):
    assert count_positions_visited(base, steps) == expected


def test_find_path_length_fails_when_max_iter_exceeded():
    with pytest.raises(MazeException):
        find_path_length(10, (7,4), max_iter=3)
