import pytest
from mergesort import mergesort_rec, mergesort_iterative

@pytest.mark.parametrize("array", [
    [],
    [1],
    [5, 2, 9, 1, 5, 6],
    [10, 9, 8, 7, 6, 5, 4],
    [3, 3, 3, 3],
    list(range(100, 0, -1))
])
def test_mergesort_rec(array):
    assert mergesort_rec(array) == sorted(array)

@pytest.mark.parametrize("array", [
    [],
    [1],
    [5, 2, 9, 1, 5, 6],
    [10, 9, 8, 7, 6, 5, 4],
    [3, 3, 3, 3],
    list(range(100, 0, -1))
])
def test_mergesort_iterative(array):
    assert mergesort_iterative(array) == sorted(array)
