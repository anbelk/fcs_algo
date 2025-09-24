import pytest

def find_max_even_sum(arr: list) -> int:
    max_even_sum = 0
    num_odd_elems = 0
    min_odd_elem = -1
    for idx in range(len(arr)):
        elem = arr[idx]
        if elem % 2:
            if elem < min_odd_elem or min_odd_elem == -1:
                min_odd_elem = elem
            num_odd_elems += 1
        max_even_sum += elem
    if num_odd_elems and num_odd_elems % 2:
        max_even_sum -= min_odd_elem
    return max_even_sum

def test_empty_arr():
    assert find_max_even_sum([]) == 0

def test_no_odd_nums():
    assert find_max_even_sum([4, 2]) == 6

def test_no_even_nums():
    assert find_max_even_sum([3, 7]) == 10

def test_odd_num_of_odd_nums():
    assert find_max_even_sum([5, 7, 13, 2, 14]) == 36

def test_even_num_of_odd_nums():
    assert find_max_even_sum([4, 7, 2, 11, 8]) == 32