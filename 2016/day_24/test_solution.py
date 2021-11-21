import pytest

from .solution import solve, find_shortest_path, get_all_paths
from .solution import Maze, MazeException

MAZE1 = """
##1##
#...#
##0##
#####
"""

MAZE2 = """
###
#0#
#.#
#1#
###
"""

MAZE3 = """
######
#....#
#0...#
#...1#
######
"""

MAZE4 = """
###
#0#
#1#
###
"""

MAZE5 = """
######
#....#
#1...#
#...0#
######
"""

MAZE_NO_EXIT = """
###
#0#
#.#
###
"""

MAZE_NO_ENTRANCE = """
###
#.#
#1#
###
"""

SMALL_MAZE = """
###########
#0.1.....2#
#.#######.#
#4.......3#
###########"""

TINY_MAZE = """
######
#0.12#
#.##.#
#..3.#
###########"""

PATH_EXAMPLES = (
    (SMALL_MAZE, 0, 1, 2),
    (SMALL_MAZE, 0, 2, 8),
    (SMALL_MAZE, 1, 2, 6),
    (TINY_MAZE, 0, 3, 4),
    (TINY_MAZE, 1, 2, 1),
    (TINY_MAZE, 2, 3, 3),
)

ALL_TINY_PATHS = {
    (0, 1): 2,
    (0, 2): 3,
    (0, 3): 4,
    (1, 2): 1,
    (1, 3): 4,
    (1, 2): 1,
    (2, 3): 3,
}

SOLVE_EXAMPLES = (
    (TINY_MAZE, 6),
    (SMALL_MAZE, 14)
)

class TestMaze:

    def test_init_maze(self):
        assert Maze(MAZE1)

    def test_maze_attribute(self):
        maze = Maze(MAZE1)
        assert isinstance(maze.maze, list)

    @pytest.mark.parametrize(
        'data,output',
        [
            (MAZE1, 4),
            (MAZE2, 5)
        ])
    def test_n_rows(self, data, output):
        maze = Maze(data)
        assert len(maze.maze) == output

    @pytest.mark.parametrize(
        'data,output',
        [
            (MAZE1, 5),
            (MAZE2, 3)
        ])
    def test_n_first_col(self, data, output):
        maze = Maze(data)
        assert len(maze.maze[0]) == output

    @pytest.mark.parametrize(
        'data,elem,output',
        [
            (MAZE1, '0', (2, 2)),
            (MAZE2, '0', (1, 1)),
            (MAZE3, '0', (1, 2)),
            (MAZE1, '1', (2, 0)),
        ])
    def test_find_position(self, data, elem, output):
        maze = Maze(data)
        assert maze.find_position(elem) == output

    @pytest.mark.parametrize(
        'data',
        [
            MAZE_NO_EXIT,
            MAZE_NO_ENTRANCE
        ])
    def test_find_path_fails_with_incomplete_maze(self, data):
        with pytest.raises(MazeException):
            find_shortest_path(data)

    @pytest.mark.parametrize(
        'data,pos,output',
        [
            (MAZE1, (1, 1), {(2, 1)}),
            (MAZE1, (2, 2), {(2, 1)}),
            (MAZE2, (1, 1), {(1, 2)}),
            (MAZE2, (1, 2), {(1, 1), (1, 3)}),
            (MAZE3, (4, 1), {(3, 1), (4, 2)}),
        ])
    def test_find_adjacent_positions(self, data, pos, output):
        maze = Maze(data)
        assert maze.find_adjacent_positions(pos) == output

    @pytest.mark.parametrize(
        'maze,output',
        [
            (MAZE1, 2),
            (MAZE2, 2),
            (MAZE3, 4),
            (MAZE4, 1),
            (MAZE5, 4),
        ])
    def test_find_shortest_path(self, maze, output):
        assert find_shortest_path(maze, 0, 1) == output


    def test_find_shortest_path_fails_when_max_iter_exceeded(self):
        with pytest.raises(MazeException):
            find_shortest_path(MAZE3, max_iter=3)


@pytest.mark.parametrize('data,wp1,wp2,expected', PATH_EXAMPLES)
def test_find_shortest_path(data, wp1, wp2, expected):
    assert find_shortest_path(data, wp1, wp2) == expected

def test_get_all_paths():
    assert get_all_paths(TINY_MAZE) == ALL_TINY_PATHS

@pytest.mark.parametrize('maze,expected', SOLVE_EXAMPLES)
def test_solve(maze, expected):
    assert solve(maze) == expected