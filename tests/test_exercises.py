# tests/test_lists.py

import exercises


def test_first_item():
    assert exercises.first_item([10, 20, 30]) == 10


def test_last_item():
    assert exercises.last_item([10, 20, 30]) == 30


def test_add_to_end():
    assert exercises.add_to_end([1, 2], 3) == [1, 2, 3]


def test_add_to_start():
    assert exercises.add_to_start([2, 3], 1) == [1, 2, 3]


def test_list_length():
    assert exercises.list_length([5, 6, 7, 8]) == 4


def test_middle_slice():
    assert exercises.middle_slice([10, 20, 30, 40, 50]) == [20, 30, 40]


def test_combine_lists():
    assert exercises.combine_lists([1, 2], [3, 4]) == [1, 2, 3, 4]


def test_contains_value():
    assert exercises.contains_value([1, 2, 3], 2) is True
    assert exercises.contains_value([1, 2, 3], 5) is False


def test_count_value():
    assert exercises.count_value([1, 2, 2, 3, 2], 2) == 3


def test_double_items():
    assert exercises.double_items([1, 2, 3]) == [2, 4, 6]