import pytest
from longest_common_subsequence import longest_common_subsequence

@pytest.mark.parametrize("string1, string2, expected", [
    ('', '', ''),
    ('A', '', ''),
    ('', 'A', ''),
    ('A', 'B', ''),
    ('A', 'A', 'A'),
    ('AB', 'A', 'A'),
    ('B', 'AB', 'B'),
    ('AB', 'AC', 'A'),
    ('AB', 'CA', 'A'),
    ('AB', 'CB', 'B'),
    ('ABC', 'AC', 'AC'),
    ('ABCDABCDE', 'ABDECE', 'ABDCE'),
    ('AGGTAB', 'GXTXAYB', 'GTAB')
])
def test_longest_common_subsequence(string1, string2, expected):
    assert longest_common_subsequence(string1, string2) == expected