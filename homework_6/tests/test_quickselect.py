import pytest
from quicksort import quickselect

def test_basic():
    array = [3, 2, 1, 5, 6, 4]
    assert quickselect(array.copy(), 1) == 6
    assert quickselect(array.copy(), 2) == 5
    assert quickselect(array.copy(), 6) == 1

def test_with_duplicates():
    array = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    assert quickselect(array.copy(), 1) == 6
    assert quickselect(array.copy(), 2) == 5
    assert quickselect(array.copy(), 3) == 5
    assert quickselect(array.copy(), 4) == 4
    assert quickselect(array.copy(), 9) == 1

def test_equal_array():
    array = [7, 7, 7, 7, 7]
    assert quickselect(array.copy(), 1) == 7
    assert quickselect(array.copy(), 5) == 7