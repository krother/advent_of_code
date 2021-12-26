import pytest
from .solution import Room, Hallway, Amphipods, solve

INPUT = """#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########
"""

EXAMPLES = [
    # easy win in 3
    (Amphipods(
        (
        Room('A', 2, 'A'),
        Room('B', 2, 'BB'),
        Room('C', 2, 'CC'),
        Room('D', 2, 'DD')
        ),
        hallway='A------'
    ), 3),

    # fill empty room
    (Amphipods(
        (
        Room('A', 2, ''),
        Room('B', 2, 'BB'),
        Room('C', 2, 'CC'),
        Room('D', 2, 'DD')
        ),
        hallway='A-----A'
    ), 13),

    # fill room B (more expensive)
    (Amphipods(
        (
        Room('A', 2, 'AA'),
        Room('B', 2, ''),
        Room('C', 2, 'CC'),
        Room('D', 2, 'DD')
        ),
        hallway='B-----B'
    ), 130),

    # ( # swap positions
    (Amphipods(
        (
        Room('A', 2, 'BA'),
        Room('B', 2, 'AB'),
        Room('C', 2, 'CC'),
        Room('D', 2, 'DD')
        ),
    ), 46),

    # deep swap
    (Amphipods(
    (
    Room('A', 2, 'BB'),
    Room('B', 2, 'AA'),
    Room('C', 2, 'CC'),
    Room('D', 2, 'DD')
    ),
    ), 114),

    # fill deep room
    (Amphipods(
    (
    Room('A', 4, ''),
    Room('B', 4, 'BBBB'),
    Room('C', 4, 'CCCC'),
    Room('D', 4, 'DDDD')
    ),
    hallway='AAAA---'
    ), 17),

    # fill another deep room
    (Amphipods(
    (
    Room('A', 4, 'AAAA'),
    Room('B', 4, 'BBBB'),
    Room('C', 4, 'CCCC'),
    Room('D', 4, '')
    ),
    hallway='---DDDD'
    ), 17000),


    # example from challenge
    (Amphipods(
    (
    Room('A', 2, 'BA'),
    Room('B', 2, 'CD'),
    Room('C', 2, 'BC'),
    Room('D', 2, 'DA')
    ),
    ), 12521),
]

class TestRoom:

    @staticmethod
    def test_create_room():
        r = Room('A', 2, 'CD')
        assert r.name == 'A'

    @staticmethod
    def test_repr():
        r = Room('B', 4, 'CD')
        assert str(r) == '--CD'

    @staticmethod
    def test_repr_empty():
        r = Room('B', 2, '')
        assert str(r) == '--'

    @staticmethod
    def test_repr_full():
        r = Room('B', 2, 'BB')
        assert str(r) == 'BB'

    @staticmethod
    def test_complete():
        r = Room('B', 2, 'BB')
        assert r.complete

    @staticmethod
    def test_complete_not():
        r = Room('B', 4, 'BB')
        assert r.complete == False

    @staticmethod
    def test_create_big_room():
        r = Room('B', 4, 'CD')
        assert r.size == 4

    @staticmethod
    def test_pop():
        r = Room('B', 2, 'CD')
        assert r.pop() == ('C', 100)

    @staticmethod
    def test_pop_twice():
        r = Room('B', 2, 'CD')
        r.pop()
        assert r.pop() == ('D', 2000)

    @staticmethod
    def test_pop_multiple():
        r = Room('B', 4, 'AAAA')
        result = [r.pop() for i in range(4)]
        assert result == [('A', 1), ('A', 2), ('A', 3), ('A', 4)]

    @staticmethod
    def test_pop_empty():
        r = Room('B', 2, '')
        with pytest.raises(IndexError):
            r.pop()

    @staticmethod
    def test_pop_ready_item():
        r = Room('B', 2, 'B')
        with pytest.raises(IndexError):
            r.pop()

    @staticmethod
    def test_pop_multiple_ready_items():
        r = Room('B', 4, 'BBBB')
        with pytest.raises(IndexError):
            r.pop()

    @staticmethod
    def test_pop_fails_mixed_items():
        r = Room('B', 4, 'BAB')
        assert r.pop() == ('B', 20)

    @staticmethod
    def test_add():
        r = Room('B', 2, 'B')
        assert r.add('B') == 10

    @staticmethod
    def test_add_empty():
        r = Room('B', 4, '')
        assert r.add('B') == 40

    @staticmethod
    def test_add_multiple():
        r = Room('C', 4, '')
        result = [r.add('C') for _ in range(4)]
        assert result == [400, 300, 200, 100]

    @staticmethod
    def test_add_mismatch():
        r = Room('B', 2, 'B')
        with pytest.raises(ValueError):
            r.add('A')

    @staticmethod
    def test_add_full():
        r = Room('D', 2, 'DD')
        with pytest.raises(ValueError):
            r.add('D')

    @staticmethod
    def test_add_to_mixed():
        r = Room('B', 4, 'BAB')
        with pytest.raises(ValueError):
            r.add('B')

    @staticmethod
    def test_can_add():
        r = Room('B', 2, 'B')
        assert r.can_add('A') == False
        assert r.can_add('B') == True


class TestHallway:

    @staticmethod
    def test_create():
        h = Hallway()
        assert str(h) == '-------'

    @staticmethod
    def test_get_possible_positions():
        h = Hallway()
        assert h.get_possible_positions('A') == {0, 1, 2, 3, 4, 5, 6}

    @staticmethod
    def test_get_possible_positions_block():
        h = Hallway()
        h.add(fish='A', position=3, door='D')
        assert h.get_possible_positions('A') == {0, 1, 2}
        assert h.get_possible_positions('B') == {0, 1, 2}
        assert h.get_possible_positions('C') == {4, 5, 6}
        assert h.get_possible_positions('D') == {4, 5, 6}

    @staticmethod
    def test_add():
        h = Hallway()
        assert h.add(fish='A', position=3, door='D') == 3
        assert str(h) == '---A---'

    @staticmethod
    def test_add_expensive():
        h = Hallway()
        assert h.add(fish='D', position=6, door='A') == 8000
        assert str(h) == '------D'

    @staticmethod
    def test_add_fail():
        h = Hallway()
        h.add(fish='D', position=3, door='A')
        with pytest.raises(ValueError):
            h.add(fish='A', position=6, door='B')

    @staticmethod
    def test_remove():
        h = Hallway()
        h.add(fish='D', position=3, door='A')
        assert h.remove(3) == 3000
        assert str(h) == '-------'

    @staticmethod
    def test_remove_cheap():
        h = Hallway()
        h.add(fish='A', position=6, door='B')
        assert h.remove(6) == 8
        assert str(h) == '-------'

    @staticmethod
    def test_remove_empty():
        h = Hallway()
        with pytest.raises(KeyError):
            h.remove(6)

    @staticmethod
    def test_get_possible_removals_empty():
        h = Hallway()
        assert h.get_possible_removals() == set()

    @staticmethod
    def test_get_possible_removals():
        h = Hallway()
        h.add(fish='A', position=6, door='B')
        h.add(fish='C', position=5, door='D')
        h.add(fish='D', position=3, door='B')
        assert h.get_possible_removals() == {(3, 'D'), (5, 'C')}


@pytest.mark.parametrize('pods,cost', EXAMPLES)
def test_solve(pods, cost):
    assert solve(pods) == cost
