import pytest
from can_sum import can_sum


def test_can_sum_empty():
    assert not can_sum(0, [])

def test_can_sum_one_of_elements():
    assert can_sum(7, [5, 3, 4, 7])

def test_can_sum_two_sum():
    assert can_sum(8, [5, 3, 4, 7])

def test_can_sum_three_sum():
    assert can_sum(12, [5, 3, 4, 7])

def test_can_sum_all_sum():
    assert can_sum(19, [5, 3, 4, 7])

def test_can_sum_skip_2():
    assert can_sum(9, [5, 3, 4, 7])

def test_can_sum_not_1():
    assert not can_sum(1, [5, 3, 4, 7])

def test_can_sum_not_10():
    assert not can_sum(10, [5, 3, 4, 7])

