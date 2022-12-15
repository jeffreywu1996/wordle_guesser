import pytest
from grid_traveler import grid_traveler


def test_0_0():
    assert grid_traveler(0, 0) == 0


def test_1_0():
    assert grid_traveler(1, 0) == 0


def test_0_1():
    assert grid_traveler(0, 1) == 0


def test_1_1():
    assert grid_traveler(1, 1) == 1


def test_2_3():
    assert grid_traveler(2, 3) == 3


def test_3_2():
    assert grid_traveler(3, 2) == 3


def test_3_3():
    assert grid_traveler(3, 3) == 6


def test_18_18():
    assert grid_traveler(18, 18) == 2333606220
