import pytest

def two_sum(arr: list, k: int) -> list:
    res_map = {}
    for i in range(len(arr)):
        res = k - arr[i]
        if res in res_map:
            return res_map[res], i
        res_map[arr[i]] = i

def test_two_nums():
    assert two_sum([1, 3], 4) == (0, 1)

def test_one():
    assert two_sum([1, 3, 4, 10], 7) == (1, 2)

def test_two():
    assert two_sum([5, 5, 1, 4], 10) == (0, 1)