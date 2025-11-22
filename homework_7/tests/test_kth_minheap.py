import pytest
from kth_minheap import kth_minheap, kth_minheap_hq


@pytest.mark.parametrize("nums, k, expected", [
    ([1], 1, 1),
    ([5, 4, 3, 2, 1], 1, 5),
    ([5, 4, 3, 2, 1], 5, 1),
    ([3, 2, 1, 5, 6, 4], 2, 5),
    ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
])
def test_kth_meanheap(nums, k, expected):
    assert kth_minheap(nums.copy(), k) == expected


@pytest.mark.parametrize("nums, k, expected", [
    ([1], 1, 1),
    ([5, 4, 3, 2, 1], 1, 5),
    ([5, 4, 3, 2, 1], 5, 1),
    ([3, 2, 1, 5, 6, 4], 2, 5),
    ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
])
def test_kth_meanheap_hq(nums, k, expected):
    assert kth_minheap_hq(nums.copy(), k) == expected
