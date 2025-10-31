# Для запуска тестов: pytest -s test_permutations.py

import pytest
from permutations import permutations

@pytest.mark.parametrize("nums, expected", [
    ([], [[]]),
    ([1], [[1]]),
    ([0, 1], [[0, 1], [1, 0]]),
    ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
])
def test_permutations(nums, expected):
    sorted_output = sorted([tuple(p) for p in permutations(nums)])
    sorted_expected = sorted([tuple(p) for p in expected])
    assert sorted_output == sorted_expected