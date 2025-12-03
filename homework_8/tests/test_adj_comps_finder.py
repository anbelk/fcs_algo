import pytest
from adj_comps_finder import find_adj_comps


@pytest.mark.parametrize("graph, expected", [
    ({}, []),

    ({1: []}, [[1]]),

    ({1: [2], 2: [1]}, [[1, 2]]),

    ({1: [], 2: [], 3: []}, [[1], [2], [3]]),

    ({1: [2], 2: [1], 3: [], 4: [5], 5: [4]}, [[1,2], [3], [4,5]]),

    ({
        1: [7, 3],
        7: [1, 3],
        3: [1, 7, 5],
        5: [3],
        6: [2],
        2: [6]
    },
    [[1, 3, 5, 7], [2, 6]])
])
def test_find_adj_comps(graph, expected):
    result = find_adj_comps(graph)

    for comp in result:
        comp.sort()
    result.sort()
    
    assert result == expected