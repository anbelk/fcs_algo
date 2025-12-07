import pytest
from knuth_morris_pratt import knuth_morris_pratt


@pytest.mark.parametrize("string, substring, expected", [
    ('', 'a', []),
    ('a', 'f', []),
    ('a', 'a', [0]),
    ('ab', 'a', [0]),
    ('ab', 'b', [1]),
    ('aa', 'a', [0, 1]),
    ('ababab', 'bab', [1, 3]),
    ('fergvrt', 'fer', [0]),
    ('dededgt', 'dedgt', [2]),
    ('cnoencoermvrot', 'oer', [6]),
    ('abbabababababbbaaba', 'baba', [2, 4, 6, 8])
])
def test_knuth_morris_pratt(string, substring, expected):
    assert knuth_morris_pratt(string, substring) == expected