import pytest
from makeheap import sift_up, makeheap_n_log_n, sift_down, makeheap


@pytest.mark.parametrize("arr, i, expected", [
    ([], 0, []),
    ([1], 0, [1]),
    ([1, 2], 1, [1, 2]),
    ([2, 1], 1, [1, 2]),
    ([2, 4, 3, 3, 1, 1, 6], 3, [2, 3, 3, 4, 1, 1, 6]),
    ([2, 4, 3, 3, 1, 1, 6], 5, [1, 4, 2, 3, 1, 3, 6])
])
def test_sift_up(arr, i, expected):
    assert sift_up(arr, i) == expected


@pytest.mark.parametrize("arr, expected", [
    ([], []),
    ([1], [1]),
    ([2, 1], [1, 2]),
    ([2, 4, 3, 3, 1, 1, 6], [1, 2, 1, 4, 3, 3, 6])
])
def test_makeheap_n_log_n(arr, expected):
    assert makeheap_n_log_n(arr) == expected


@pytest.mark.parametrize("arr, i, expected", [
    ([], 0, []),
    ([1], 0, [1]),
    ([2, 1], 0, [1, 2]),
    ([2, 1], 1, [2, 1]),
    ([2, 4, 3, 3, 1, 1, 6], 1, [2, 1, 3, 3, 4, 1, 6]),
    ([9, 4, 3, 3, 1, 1, 6], 0, [3, 4, 1, 3, 1, 9, 6])
])
def test_sift_down(arr, i, expected):
    assert sift_down(arr, i) == expected


@pytest.mark.parametrize("arr, expected", [
    ([], []),
    ([1], [1]),
    ([2, 1], [1, 2]),
    ([2, 4, 3, 3, 1, 0, 6], [0, 1, 2, 3, 4, 3, 6])
])
def test_makeheap(arr, expected):
    assert makeheap(arr) == expected