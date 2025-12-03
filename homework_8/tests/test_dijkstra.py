import pytest
from dijkstra import dijkstra

@pytest.mark.parametrize("graph, start, expected", [
    ({'A': {}}, 'A', {'A': 0}),

    ({'A': {'B': 1}, 'B': {'A': 1}}, 'A', {'A': 0, 'B': 1}),
    
    ({'A': {'B': 1}, 'B': {'C': 2}, 'C': {}}, 'A', 
     {'A': 0, 'B': 1, 'C': 3}),
     
    ({
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1, 'E': 3},
        'E': {'D': 3}
    }, 'A', 
    {'A': 0, 'B': 1, 'C': 3, 'D': 4, 'E': 7}),

    ({
        'A': {'B': 1}, 
        'B': {'A': 1}, 
        'X': {'Y': 1}, 
        'Y': {'X': 1}
    }, 'A',
    {'A': 0, 'B': 1, 'X': float('inf'), 'Y': float('inf')}),
    
    ({
        1: {2: 10, 3: 3},
        2: {3: 1, 4: 2},
        3: {2: 4, 4: 8},
        4: {5: 5},
        5: {}
    }, 1,
    {1: 0, 2: 7, 3: 3, 4: 9, 5: 14})
])
def test_dijkstra_shortest_paths(graph, start, expected):
    result_dists = dijkstra(graph, start)
    assert result_dists == expected