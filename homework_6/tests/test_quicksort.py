import pytest
from quicksort import quicksort_rec, quicksort_iterative

@pytest.mark.parametrize("array", [
    [],
    [1],
    [5, 2, 9, 1, 5, 6],
    [10, 9, 8, 7, 6, 5, 4],
    [3, 3, 3, 3],
    list(range(100, 0, -1))
])
def test_quicksort_rec(array):
    assert quicksort_rec(array) == sorted(array)

@pytest.mark.parametrize("array", [
    [],
    [1],
    [5, 2, 9, 1, 5, 6],
    [10, 9, 8, 7, 6, 5, 4],
    [3, 3, 3, 3],
    list(range(100, 0, -1))
])
def test_quicksort_iterative(array):
    assert quicksort_iterative(array) == sorted(array)
