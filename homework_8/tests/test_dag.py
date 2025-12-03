import pytest
from dag import DagExplorer

@pytest.mark.parametrize("dag, expected_key", [
    ({}, "sorted_result"),

    ({1: []}, "sorted_result"),

    ({'A': ['B'], 'B': ['C'], 'C': []}, "sorted_result"),

    ({1: [], 2: []}, "sorted_result"),
    
    ({
        1: [7, 3],
        7: [1, 3],
        3: [1, 7, 5],
        5: [3],
        6: [2],
        2: [6]
    }, "loop_path"),

    ({1: [2], 2: [3], 3: [1]}, "loop_path"),

    ({
        'X': ['Y'],
        'Y': ['Z'],
        'Z': ['X'],
        'A': ['B'],
        'B': []
    }, "loop_path"),
    
    ({
        'U': ['V', 'W'],
        'V': ['X'],
        'W': ['X'],
        'X': []
    }, "sorted_result")
])
def test_graph_analysis_outcomes(dag, expected_key):
    explorer_instance = DagExplorer(dag)
    result = explorer_instance.process_graph()

    assert expected_key in result
    
    if expected_key == "sorted_result":
        assert "loop_path" not in result
        assert result["has_loop"] is False
    elif expected_key == "loop_path":
        assert "sorted_result" not in result
        assert result["has_loop"] is True
        assert len(result["loop_path"]) >= 2
